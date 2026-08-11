#!/usr/bin/env python
"""Mechanical translation verification for the multilingual manuals tree.

Checks per target language against the base (en):
  structure  FAIL  headings (count+levels), component sequence, numbered steps,
                   table rows, img/video srcs, frontmatter icon
  numbers    FAIL  numeric-token multiset (base decimals normalized . -> ,)
  dnt        FAIL  do-not-translate terms present in base but absent in target
  stub       FAIL  leftover STUB-TRANSLATION-PENDING marker
  dedupe     FAIL  dedupe-group bodies not byte-identical within a language
  register   WARN  wrong-register pronouns (de: Sie..., fr: tu..., it: Lei...)
  negation   WARN  safety-file negation-marker count suspiciously low vs base

Usage: python scripts/verify_translation.py --base en --targets de fr it [--include-nl]
Exit 1 if any FAIL. WARNs are printed for human review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.S)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.M)
COMPONENT_RE = re.compile(
    r"<(/?)(Note|Warning|Info|Tip|Card|CardGroup|Steps|Step|Tabs|Tab|"
    r"Accordion|AccordionGroup|Frame|Check)\b"
)
SRC_RE = re.compile(r'src="([^"]+)"')
NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")
STEP_RE = re.compile(r"^\s*\d+\.\s", re.M)
TABLEROW_RE = re.compile(r"^\|.*\|\s*$", re.M)
ICON_RE = re.compile(r'^icon:\s*"?([^"\r\n]+)"?\s*$', re.M)
STUB_MARKER = "STUB-TRANSLATION-PENDING"

REGISTER_RE = {
    "de": re.compile(r"\b(Sie|Ihnen|Ihr|Ihre[mnrs]?)\b"),
    "fr": re.compile(r"\b([Tt]u|[Tt]oi|[Tt]on|[Tt]a|[Tt]es)\b"),
    "it": re.compile(r"\b(Lei|Suo|Sua|Sue|Suoi)\b"),
}
NEGATION_RE = {
    "en": re.compile(r"\b(do not|don't|never|avoid|must not)\b", re.I),
    "de": re.compile(r"\b(nicht|kein\w*|niemals|vermeide\w*)\b", re.I),
    "fr": re.compile(r"\b(ne|n['’]|pas|jamais|aucun\w*|évit\w*)\b", re.I),
    "it": re.compile(r"\b(non|mai|nessun\w*|evita\w*)\b", re.I),
}
DEDUPE_GROUPS = {
    "safety.mdx": [["onecable", "lite", "lite-144hz", "flip", "expand", "one-4k", "one-4k-oled"]],
    "display-settings.mdx": [["onecable", "dual-flip", "flip", "expand"]],
}

# Spelled-out counts in "### N. ..." connection-option headings (e.g.
# "### 2. One USB-C cable, one HDMI cable and one USB-A cable"). Observed in
# the known-good nl corpus, different files translate these two different but
# equally valid ways: some keep the spelled word ("Twee", "Eén" -- a faithful
# translation, no digit ever appears), others switch to the digit+"x"
# shorthand used elsewhere in the same doc ("1x USB-C-kabel, ..."). A digit in
# the target that corresponds 1:1 to a spelled count in the base heading is
# therefore *tolerated*, never *required*.
#
# This is deliberately a PAIRWISE, per-heading-POSITION comparison, not a
# document-wide value-keyed credit bucket (that was tried twice and leaked
# both times: a same-valued credit generated at one heading could forgive an
# unrelated defect anywhere else with the same digit -- once via prose
# anywhere in the body, once via another heading's own ordinal number). It
# also does NOT try to strip a "### N." ordinal prefix off the heading text
# before scanning for digits -- an earlier attempt at that broke on the real
# corpus pattern "### 3.5mm Headphone Jack" (not a numbered step at all, but
# `\d+\.` still matches the "3." inside "3.5mm", tearing the decimal in two
# and minting a phantom '5'). Instead: NUM_RE runs over the FULL heading text
# unmodified for both base and target at the SAME position; a real "N."
# ordinal then naturally cancels itself out (both sides contribute the same
# ordinal digit), and a decimal like "3.5mm"/"3,5 mm" survives intact as one
# token on both sides -- no special-casing needed for either.
NUMWORDS = {
    "One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5", "Six": "6",
    "Seven": "7", "Eight": "8", "Nine": "9", "Ten": "10", "Eleven": "11", "Twelve": "12",
}
NUMWORD_RE = re.compile(r"\b(" + "|".join(NUMWORDS) + r")\b", re.I)

# French (and other European) convention groups large numbers with a space
# instead of en's comma: "100,000:1" (en) vs "100 000:1" (fr), where the
# space may be a plain space, the literal HTML entity "&nbsp;", or a real
# non-breaking/narrow-no-break-space character (U+00A0, U+202F). NUM_RE alone
# tokenizes the fr form as two separate numbers ('100', '000') since it only
# recognizes '.'/',' as an internal separator -- a guaranteed false
# "numbers" FAIL. Canonicalize to en's own native comma-grouped form (rather
# than stripping to bare digits) so both land on the exact same token via the
# existing NUM_RE + dot->comma pipeline, with no change to how en or the
# already-working de dot-grouped convention ("100.000" -> "100,000" via the
# pre-existing normalization) are handled.
#
# Guarded to only the shape of a genuine thousands grouping: a standalone
# 1-3 digit group immediately followed by a space/nbsp variant and EXACTLY 3
# digits. Decimal fractions in this corpus are always single-digit precision
# ("15,6", "3,5"), never 3 digits, so this can't collide with a real decimal.
# The 3-digit requirement is a shape guard, not a semantic one: a string like
# "10 000" is mechanically indistinguishable from a genuine "ten thousand"
# grouping and will be merged -- there is no way to tell without meaning. The
# lookaround boundaries (no digit immediately before the left group or after
# the right group) at least prevent eating into a longer, unrelated digit run
# (e.g. a 4-digit code right after the space is never touched).
THOUSANDS_SEP_RE = re.compile(
    r"(?<!\d)(\d{1,3})(?:[   ]|&nbsp;)(\d{3})(?!\d)"
)


def _normalize_spaced_thousands(text: str) -> str:
    """Canonicalize a space/nbsp-grouped thousands figure to en's own native
    comma-grouped form, before NUM_RE tokenization."""
    return THOUSANDS_SEP_RE.sub(r"\1,\2", text)


def _pairwise_numword_forgiveness(base_headings: list[tuple[int, str]],
                                  tgt_headings: list[tuple[int, str]]) -> Counter:
    """Per-heading-position credit: a spelled-out count in base heading i may
    be claimed ONLY by excess digit tokens within target heading i itself --
    never pooled across headings or the whole document.

    Guarded behind positional parity: the structure check elsewhere already
    FAILs if heading counts/levels differ, so pairing by index is safe here;
    if counts differ (e.g. this is called before that check runs, or on data
    that will already FAIL structure), no forgiveness is computed at all --
    better to under-forgive than to mis-pair headings.
    """
    forgiven: Counter = Counter()
    if len(base_headings) != len(tgt_headings):
        return forgiven
    for (_, base_text), (_, tgt_text) in zip(base_headings, tgt_headings):
        credits = Counter(
            NUMWORDS[w.capitalize()] for w in NUMWORD_RE.findall(base_text)
        )
        if not credits:
            continue
        base_line_nums = Counter(
            n.replace(".", ",") for n in NUM_RE.findall(_normalize_spaced_thousands(base_text)))
        tgt_line_nums = Counter(
            n.replace(".", ",") for n in NUM_RE.findall(_normalize_spaced_thousands(tgt_text)))
        for v, c in credits.items():
            excess_local = max(0, tgt_line_nums.get(v, 0) - base_line_nums.get(v, 0))
            forgiven[v] += min(excess_local, c)
    return forgiven


_DNT_PATTERN_CACHE: dict[str, re.Pattern] = {}


def _dnt_pattern(term: str) -> re.Pattern:
    """Word-boundary match for a DNT term so it doesn't hit inside an unrelated
    word (e.g. the DNT product name "Flip" must not match the English word
    "Flipped" used for screen orientation)."""
    pat = _DNT_PATTERN_CACHE.get(term)
    if pat is None:
        pat = re.compile(r"\b" + re.escape(term) + r"\b")
        _DNT_PATTERN_CACHE[term] = pat
    return pat


@dataclass
class Issue:
    severity: str  # FAIL | WARN
    check: str
    path: str
    detail: str

    def __str__(self) -> str:
        return f"{self.severity} {self.check:<9} {self.path}: {self.detail}"


def parse_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    fm = m.group(1) if m else ""
    body = text[m.end():] if m else text
    icon = ICON_RE.search(fm)
    return {
        "headings": [(len(h), t.strip()) for h, t in HEADING_RE.findall(body)],
        "components": ["".join(c) for c in COMPONENT_RE.findall(body)],
        "srcs": SRC_RE.findall(body),
        "numbers": sorted(NUM_RE.findall(_normalize_spaced_thousands(body))),
        "steps": len(STEP_RE.findall(body)),
        "table_rows": len(TABLEROW_RE.findall(body)),
        "icon": icon.group(1).strip() if icon else None,
        "body": body,
        "stub": STUB_MARKER in text,
    }


def body_hash(path: Path) -> str:
    # Trailing blank lines/newlines are not meaningful content divergence
    # (observed in the known-good nl/en corpus: a stray trailing newline on
    # one file in a dedupe group with otherwise byte-identical content).
    return hashlib.md5(parse_page(path)["body"].rstrip().encode("utf-8")).hexdigest()


def compare_page(base: dict, tgt: dict, lang: str, rel: str, dnt: list[str],
                 base_body: str) -> list[Issue]:
    issues: list[Issue] = []
    p = f"{lang}/{rel}"

    if tgt["stub"]:
        issues.append(Issue("FAIL", "stub", p, "stub marker still present"))
        return issues  # everything else would be noise

    if [l for l, _ in base["headings"]] != [l for l, _ in tgt["headings"]]:
        issues.append(Issue("FAIL", "structure", p,
                            f"heading levels {[l for l, _ in base['headings']]} != "
                            f"{[l for l, _ in tgt['headings']]}"))
    if base["components"] != tgt["components"]:
        issues.append(Issue("FAIL", "structure", p, "component sequence differs"))
    if base["srcs"] != tgt["srcs"]:
        issues.append(Issue("FAIL", "structure", p, "img/video src paths differ"))
    if base["steps"] != tgt["steps"]:
        issues.append(Issue("FAIL", "structure", p,
                            f"numbered steps {base['steps']} != {tgt['steps']}"))
    if base["table_rows"] != tgt["table_rows"]:
        issues.append(Issue("FAIL", "structure", p,
                            f"table rows {base['table_rows']} != {tgt['table_rows']}"))
    if base["icon"] != tgt["icon"]:
        issues.append(Issue("FAIL", "structure", p,
                            f"icon {base['icon']!r} != {tgt['icon']!r}"))

    base_counts = Counter(n.replace(".", ",") for n in base["numbers"])
    tgt_counts = Counter(n.replace(".", ",") for n in tgt["numbers"])
    if base_counts != tgt_counts:
        forgiven_credits = _pairwise_numword_forgiveness(base["headings"], tgt["headings"])
        missing: list[str] = []
        extra: list[str] = []
        for v in sorted(set(base_counts) | set(tgt_counts)):
            b, t = base_counts[v], tgt_counts[v]
            if t < b:
                missing.extend([v] * (b - t))
            elif t > b:
                forgiven = min(t - b, forgiven_credits.get(v, 0))
                remaining = (t - b) - forgiven
                if remaining > 0:
                    extra.extend([v] * remaining)
        if missing or extra:
            issues.append(Issue("FAIL", "numbers", p,
                                f"missing {missing[:8]} extra {extra[:8]}"))

    for term in dnt:
        pat = _dnt_pattern(term)
        if pat.search(base_body) and not pat.search(tgt["body"]):
            issues.append(Issue("FAIL", "dnt", p, f"term {term!r} lost"))

    reg = REGISTER_RE.get(lang)
    if reg:
        hits = sorted(set(reg.findall(tgt["body"])))
        if hits:
            issues.append(Issue("WARN", "register", p, f"wrong-register hits {hits[:6]}"))

    if rel.endswith("safety.mdx") and lang in NEGATION_RE:
        nb = len(NEGATION_RE["en"].findall(base_body))
        nt = len(NEGATION_RE[lang].findall(tgt["body"]))
        if nb and (nt == 0 or nt < nb * 0.5):
            issues.append(Issue("WARN", "negation", p,
                                f"negation markers en={nb} {lang}={nt} — review"))
    return issues


def verify_tree(root: Path, base: str = "en", targets: list[str] | None = None,
                include_nl: bool = False) -> list[Issue]:
    targets = list(targets or [])
    dnt_path = root / "translations" / "dnt.json"
    dnt = json.loads(dnt_path.read_text(encoding="utf-8")) if dnt_path.is_file() else []
    issues: list[Issue] = []

    base_pages: dict[str, Path] = {}
    base_root = root / base
    if (base_root / "manuals-index.mdx").is_file():
        base_pages["manuals-index.mdx"] = base_root / "manuals-index.mdx"
    for f in sorted(base_root.rglob("manuals/**/*.mdx")):
        base_pages[str(f.relative_to(base_root)).replace("\\", "/")] = f

    for lang in targets:
        for rel, bpath in base_pages.items():
            tpath = root / lang / rel
            if not tpath.is_file():
                issues.append(Issue("FAIL", "structure", f"{lang}/{rel}", "file missing"))
                continue
            bparsed = parse_page(bpath)
            issues.extend(compare_page(bparsed, parse_page(tpath), lang, rel, dnt,
                                       bparsed["body"]))

    langs_for_dedupe = targets + ([ "nl", base] if include_nl else [base])
    for fname, groups in DEDUPE_GROUPS.items():
        for group in groups:
            for lang in langs_for_dedupe:
                hashes = {}
                for slug in group:
                    f = root / lang / "manuals" / slug / fname
                    if f.is_file():
                        hashes.setdefault(body_hash(f), []).append(slug)
                if len(hashes) > 1:
                    issues.append(Issue("FAIL", "dedupe", f"{lang}/*/{fname}",
                                        f"bodies diverge: { {h[:8]: s for h, s in hashes.items()} }"))
    return issues


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="en")
    ap.add_argument("--targets", nargs="+", default=["de", "fr", "it"])
    ap.add_argument("--include-nl", action="store_true",
                    help="also enforce dedupe byte-identity for nl and the base language")
    args = ap.parse_args()

    issues = verify_tree(Path.cwd(), base=args.base, targets=args.targets,
                         include_nl=args.include_nl)
    fails = [i for i in issues if i.severity == "FAIL"]
    warns = [i for i in issues if i.severity == "WARN"]
    for i in issues:
        print(i)
    print(f"\n{len(fails)} FAIL, {len(warns)} WARN")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
