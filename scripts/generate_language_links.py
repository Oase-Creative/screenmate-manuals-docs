#!/usr/bin/env python
"""Generate/repair the cross-language `<lang>_link` frontmatter keys on manual pages.

Every product tab in docs.json is `hidden: true`, so Mintlify's language switcher
cannot infer a page's counterpart in another language. Each page must therefore
carry an explicit link to its twin in every OTHER language:

    ---
    title: "Display Settings"
    nl_link: "/nl/manuals/onecable/display-settings"
    ---

With N languages that is N-1 keys per page, i.e. quadratic hand-maintenance.
This script derives them from the file tree instead.

Usage (run from the repo root):
    python scripts/generate_language_links.py            # write mode (default)
    python scripts/generate_language_links.py --check    # exit 1 if anything would change
    python scripts/generate_language_links.py --verbose  # per-file detail

Scope: `<lang>/manuals-index.mdx` and `<lang>/manuals/**/*.mdx` only. Files
outside a language directory are never touched. Edits are targeted line edits --
the YAML is never parsed-and-redumped, so key order, formatting, comments and
each file's line-ending style survive byte-for-byte.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# A language directory: "en", "nl", "de" ... or "pt-BR", "zh-CN".
LANG_DIR_RE = re.compile(r"^[a-z]{2}(?:-[A-Z]{2})?$")

# A top-level `<lang>_link:` frontmatter key (column 0 only -- never a nested key).
LINK_KEY_RE = re.compile(r"^([a-z]{2}(?:-[A-Z]{2})?)_link[ \t]*:(.*)$")

FM_DELIM = "---"
INDEX_PAGE = "manuals-index.mdx"
MANUALS_DIR = "manuals"

BOM = "﻿"


# --------------------------------------------------------------------------- #
# discovery
# --------------------------------------------------------------------------- #

def discover_languages(root: Path) -> list[str]:
    """A language = top-level dir named like a language code that holds manuals."""
    langs = []
    for child in sorted(root.iterdir()):
        if not child.is_dir() or not LANG_DIR_RE.match(child.name):
            continue
        if (child / INDEX_PAGE).is_file() or (child / MANUALS_DIR).is_dir():
            langs.append(child.name)
    return langs


def collect_pages(root: Path, lang: str) -> dict[str, Path]:
    """Map language-stripped page key -> file path.

    "manuals-index"                        <- <lang>/manuals-index.mdx
    "manuals/onecable/display-settings"    <- <lang>/manuals/onecable/display-settings.mdx
    """
    base = root / lang
    pages: dict[str, Path] = {}

    index = base / INDEX_PAGE
    if index.is_file():
        pages["manuals-index"] = index

    manuals = base / MANUALS_DIR
    if manuals.is_dir():
        for path in sorted(manuals.rglob("*.mdx")):
            rel = path.relative_to(base).with_suffix("")
            pages["/".join(rel.parts)] = path

    return pages


def link_target(lang: str, page_key: str) -> str:
    return f"/{lang}/{page_key}"


# --------------------------------------------------------------------------- #
# line-level file surgery
# --------------------------------------------------------------------------- #

def split_lines(text: str) -> list[str]:
    """Split keeping each line's own terminator (CRLF or LF) attached."""
    return re.findall(r"[^\n]*\n|[^\n]+$", text)


def line_body(line: str) -> str:
    """The line without its terminator."""
    if line.endswith("\r\n"):
        return line[:-2]
    if line.endswith("\n"):
        return line[:-1]
    return line


def line_eol(line: str) -> str:
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n"):
        return "\n"
    return ""


def dominant_eol(lines: list[str]) -> str:
    """The line-ending style to use for newly inserted lines."""
    crlf = sum(1 for ln in lines if ln.endswith("\r\n"))
    lf = sum(1 for ln in lines if ln.endswith("\n")) - crlf
    return "\r\n" if crlf >= lf and crlf > 0 else "\n"


def find_frontmatter(lines: list[str]) -> tuple[int, int] | None:
    """Return (open_idx, close_idx) of the `---` delimiters, or None."""
    if not lines or line_body(lines[0]).strip() != FM_DELIM:
        return None
    for i in range(1, len(lines)):
        if line_body(lines[i]).strip() == FM_DELIM:
            return 0, i
    return None


def canonical_line(lang: str, target: str, eol: str) -> str:
    return f'{lang}_link: "{target}"{eol}'


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


class Change:
    __slots__ = ("action", "key", "detail")

    def __init__(self, action: str, key: str, detail: str = ""):
        self.action = action  # added | fixed | removed
        self.key = key
        self.detail = detail

    def __str__(self) -> str:
        return f"{self.action:<7} {self.key}{(' ' + self.detail) if self.detail else ''}"


def process_page(path: Path, wanted: dict[str, str]) -> tuple[bool, list[Change], str | None]:
    """Reconcile one page's `<lang>_link` keys against `wanted` {lang: target}.

    Returns (has_frontmatter, changes, new_text); new_text is None when nothing
    changes. Anything matching `<lang>_link` that is not in `wanted` is stale
    and gets removed.
    """
    raw = path.read_bytes().decode("utf-8")
    prefix = ""
    if raw.startswith(BOM):
        prefix, raw = BOM, raw[len(BOM):]

    lines = split_lines(raw)
    span = find_frontmatter(lines)
    if span is None:
        return False, [], None
    open_idx, close_idx = span
    fm_eol = dominant_eol(lines[open_idx:close_idx + 1])

    changes: list[Change] = []
    out = list(lines)
    seen: set[str] = set()
    drop: list[int] = []

    for i in range(open_idx + 1, close_idx):
        m = LINK_KEY_RE.match(line_body(lines[i]))
        if not m:
            continue
        lang, rawval = m.group(1), m.group(2)

        if lang not in wanted:
            drop.append(i)
            changes.append(Change("removed", f"{lang}_link", f'(stale: "{unquote(rawval)}")'))
            continue

        if lang in seen:
            drop.append(i)
            changes.append(Change("removed", f"{lang}_link", "(duplicate key)"))
            continue
        seen.add(lang)

        want = canonical_line(lang, wanted[lang], line_eol(lines[i]))
        if lines[i] != want:
            was = unquote(rawval)
            out[i] = want
            detail = (
                f'("{was}" -> "{wanted[lang]}")' if was != wanted[lang] else "(reformatted)"
            )
            changes.append(Change("fixed", f"{lang}_link", detail))

    for i in reversed(drop):
        del out[i]
    close_idx -= len(drop)

    missing = sorted(set(wanted) - seen)
    if missing:
        eol = fm_eol
        # Insert after the last non-blank frontmatter line (before any trailing
        # blanks and before the closing delimiter).
        insert_at = close_idx
        while insert_at - 1 > open_idx and not line_body(out[insert_at - 1]).strip():
            insert_at -= 1
        # The line we append after must itself be newline-terminated.
        if insert_at - 1 >= 0 and not out[insert_at - 1].endswith("\n"):
            out[insert_at - 1] += eol
        for offset, lang in enumerate(missing):
            out.insert(insert_at + offset, canonical_line(lang, wanted[lang], eol))
            changes.append(Change("added", f"{lang}_link", f'("{wanted[lang]}")'))

    if not changes:
        return True, [], None
    return True, changes, prefix + "".join(out)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate cross-language <lang>_link frontmatter keys for manual pages.",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="report only; exit 1 if any file would change or parity is broken",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="per-file detail")
    args = parser.parse_args(argv)

    root = Path.cwd()
    if not (root / "docs.json").is_file():
        print(f"error: docs.json not found in {root}", file=sys.stderr)
        print("       run this script from the repo root:", file=sys.stderr)
        print("       python scripts/generate_language_links.py", file=sys.stderr)
        return 2

    langs = discover_languages(root)
    if len(langs) < 2:
        print(f"Languages found: {', '.join(langs) if langs else '(none)'}")
        print("Nothing to do: cross-language links need at least 2 languages.")
        return 0

    pages_by_lang = {lang: collect_pages(root, lang) for lang in langs}
    all_keys = sorted({k for pages in pages_by_lang.values() for k in pages})

    # -- parity -----------------------------------------------------------
    parity_gaps: list[tuple[str, list[str], list[str]]] = []
    for key in all_keys:
        have = [l for l in langs if key in pages_by_lang[l]]
        missing = [l for l in langs if key not in pages_by_lang[l]]
        if missing:
            parity_gaps.append((key, have, missing))

    # -- links ------------------------------------------------------------
    no_frontmatter: list[Path] = []
    changed: list[tuple[Path, list[Change]]] = []
    totals = {"added": 0, "fixed": 0, "removed": 0}

    for lang in langs:
        for key, path in sorted(pages_by_lang[lang].items()):
            wanted = {
                other: link_target(other, key)
                for other in langs
                if other != lang and key in pages_by_lang[other]
            }
            has_fm, changes, new_text = process_page(path, wanted)
            if not has_fm:
                no_frontmatter.append(path)
                continue
            if new_text is None:
                continue
            for c in changes:
                totals[c.action] += 1
            changed.append((path, changes))
            if not args.check:
                path.write_bytes(new_text.encode("utf-8"))

    # -- report -----------------------------------------------------------
    total_pages = sum(len(p) for p in pages_by_lang.values())
    print(f"Languages: {', '.join(langs)}")
    print(
        "Pages:     "
        + f"{total_pages} ("
        + ", ".join(f"{l}={len(pages_by_lang[l])}" for l in langs)
        + ")"
    )

    if parity_gaps:
        print(f"\nPARITY: {len(parity_gaps)} page(s) missing a counterpart:")
        for key, have, missing in parity_gaps:
            print(f"  {key}: present in [{', '.join(have)}] -- MISSING in [{', '.join(missing)}]")
        print("  (links to missing counterparts are skipped, not written)")
    else:
        print("Parity:    OK -- every page exists in every language")

    if no_frontmatter:
        print(f"\nSKIPPED: {len(no_frontmatter)} file(s) with no frontmatter block:")
        for path in no_frontmatter:
            print(f"  {path.relative_to(root).as_posix()}")

    verb = "would change" if args.check else "changed"
    if changed:
        print(
            f"\n{len(changed)} file(s) {verb}: "
            f"{totals['added']} added, {totals['fixed']} fixed, {totals['removed']} removed"
        )
        for path, changes in changed:
            print(f"  {path.relative_to(root).as_posix()}")
            if args.verbose:
                for c in changes:
                    print(f"      {c}")
    else:
        print(f"\nAll cross-language links are correct -- no files {verb}.")

    if args.verbose and not changed:
        for lang in langs:
            for key in sorted(pages_by_lang[lang]):
                others = [o for o in langs if o != lang and key in pages_by_lang[o]]
                print(f"  ok  {lang}/{key} -> {', '.join(others) or '(none)'}")

    if args.check and (changed or parity_gaps):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
