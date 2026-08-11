# IT/DE/FR Language Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Italian, German, and French as full languages (62 pages each) to the Screenmate Mintlify manuals site, with machine-verified fidelity and a client delivery doc.

**Architecture:** Stub-first scaffold on a feature branch so the Mintlify build stays green throughout; dual-source translation (EN = structure, NL = meaning/register/formatting) executed by Opus subagents against locked per-language glossaries; a mechanical verification script plus blind back-translation and adversarial review before merge.

**Tech Stack:** Mintlify (`mint` CLI 4.2.776, on PATH), MDX, Python 3 (verification script, pytest), Node (docs.json manipulation), Git Bash on Windows.

**Spec:** `docs/superpowers/specs/2026-08-11-it-de-fr-language-expansion-design.md`

## Global Constraints

- **Branch:** all work on `lang-expansion-de-fr-it`. NEVER push to `main` — it deploys on push. Merge only at Task 12 with explicit user approval.
- **Delegation:** Fable main session orchestrates and gates only. Translation/review/glossary tasks → **Opus** subagents. Mechanical tasks (scaffold, docs.json, CSS, verify script) → **Sonnet** subagents. Never Fable subagents.
- **Registers (locked):** German informal **du** (never Sie). French formal **vous** (never tu). Italian informal **tu** (never Lei).
- **Number format (all three languages):** comma decimal (`15,6"`, `2,5 cm`, `3,5 mm`), no thousands separator (`1820 gram` pattern). Follow NL conventions.
- **Do-not-translate:** product names (`Screenmate OneCable`, `One 4K OLED`, …); OSD caps labels (`LANGUAGE`, `OSD TIMER`, `TRANSPARENCY`, …); keep-EN glossary terms (`Drivers`, `Power Delivery`, `Backlight`, `FAQ`); image/video `src` paths (byte-identical; alt text IS translated); frontmatter `icon` values.
- **Never hand-write or edit `<lang>_link` frontmatter keys** — `scripts/generate_language_links.py` owns them (run in Task 11).
- **English OS screenshots are reused as-is** on all language pages (client decision `c9e6d1f`). Never flag, never request localized screenshots.
- **Existing EN/NL copy is frozen** except: (a) the Task 1 whitespace fix, (b) edits explicitly approved during flag disposition (Task 10).
- **Safety text style:** literal fidelity over idiomatic polish. When EN and NL disagree in meaning, halt and flag (write to `translations/flags/`), never silently pick one.
- **Stub marker:** `STUB-TRANSLATION-PENDING`. Any occurrence remaining at Task 11 is a hard failure.

## Dedupe groups (verified by body checksum 2026-08-11)

| File | Group (bodies byte-identical per language) |
|---|---|
| `safety.mdx` | **A:** onecable, lite, lite-144hz, flip, expand, one-4k, one-4k-oled · **B:** dual-flip · **C:** infinity · **D:** infinity-lite · **E:** panorama |
| `display-settings.mdx` | **S:** onecable, dual-flip, flip, expand · infinity · infinity-lite |

Safety frontmatter is identical across group A (only generated `_link` keys differ). display-settings frontmatter: flip's differs slightly from onecable/dual-flip/expand — translate frontmatter per file, body once.

## Page inventory (en, mirrored per language)

| Slug | Pages |
|---|---|
| onecable | index, installation, installation-windows, installation-mac, display-settings, controls, troubleshooting, safety (8) |
| lite / lite-144hz / one-4k / one-4k-oled / panorama | index, installation, controls, osd, safety (5) |
| dual-flip / flip / expand | index, installation, controls, display-settings, osd, safety (6) |
| infinity / infinity-lite | index, installation, controls, display-settings, safety (5) |
| — | `manuals-index.mdx` (1 per language) |

---

### Task 1: Whitespace fix + stub scaffold (Sonnet)

**Files:**
- Modify: `nl/manuals/onecable/display-settings.mdx` (remove one trailing blank line)
- Create: `de/**/*.mdx`, `fr/**/*.mdx`, `it/**/*.mdx` (62 stubs each, mirroring `en/` tree)

**Interfaces:**
- Produces: complete `de/ fr/ it/` file trees at final paths; every file contains marker `STUB-TRANSLATION-PENDING`. Later tasks overwrite these files in place.

- [ ] **Step 1: Fix the NL whitespace divergence**

Remove the single trailing blank line at the end of `nl/manuals/onecable/display-settings.mdx` so its body checksum matches dual-flip/flip/expand.

- [ ] **Step 2: Verify the checksum now matches**

```bash
for p in onecable dual-flip flip expand; do printf "%-12s " "$p"; awk 'BEGIN{fm=0} /^---$/{fm++; next} fm>=2{print}' "nl/manuals/$p/display-settings.mdx" | md5sum | cut -c1-12; done
```
Expected: all four hashes identical.

- [ ] **Step 3: Commit the fix separately**

```bash
git add nl/manuals/onecable/display-settings.mdx
git commit -m "fix(nl): restore display-settings frozen-chapter byte-identity (trailing blank line)"
```

- [ ] **Step 4: Generate stub trees**

```bash
python - <<'EOF'
from pathlib import Path
STUB = '---\ntitle: "STUB"\n---\n\n{/* STUB-TRANSLATION-PENDING */}\n'
for lang in ["de", "fr", "it"]:
    for src in Path("en").rglob("*.mdx"):
        dst = Path(lang) / src.relative_to("en")
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(STUB, encoding="utf-8")
    print(lang, len(list(Path(lang).rglob("*.mdx"))))
EOF
```
Expected output: `de 62`, `fr 62`, `it 62`.

- [ ] **Step 5: Commit**

```bash
git add de fr it
git commit -m "chore(i18n): scaffold de/fr/it stub trees (62 pages each)"
```

---

### Task 2: docs.json language blocks + style.css flags + DNT list (Sonnet)

**Files:**
- Modify: `docs.json` (3 new language blocks), `style.css` (3 flags)
- Create: `translations/dnt.json`

**Interfaces:**
- Consumes: stub trees from Task 1 (docs.json references must resolve).
- Produces: `translations/dnt.json` — a JSON array of strings; Task 8 (verify script) reads it.

- [ ] **Step 1: Add the three language blocks to docs.json**

```bash
node - <<'EOF'
const fs = require('fs');
const d = JSON.parse(fs.readFileSync('docs.json', 'utf8'));
const langs = [
  ["de", "Handbücher", "Installationsanleitungen"],
  ["fr", "Manuels", "Instructions d'installation"],
  ["it", "Manuali", "Istruzioni di installazione"],
];
const en = d.navigation.languages.find(l => l.language === "en");
for (const [code, tabLabel, groupLabel] of langs) {
  const b = JSON.parse(JSON.stringify(en).replaceAll('"en/', '"' + code + '/'));
  b.language = code;
  b.tabs[0].tab = tabLabel;
  const oc = b.tabs.find(t => t.tab === "OneCable");
  for (const p of oc.pages) if (typeof p === "object" && p.group) p.group = groupLabel;
  d.navigation.languages.push(b);
}
const order = ["nl", "en", "de", "fr", "it"];
d.navigation.languages.sort((a, b) => order.indexOf(a.language) - order.indexOf(b.language));
fs.writeFileSync('docs.json', JSON.stringify(d, null, 2) + "\n");
console.log("languages:", d.navigation.languages.map(l => l.language).join(","));
EOF
```
Expected: `languages: nl,en,de,fr,it`.

- [ ] **Step 2: Verify every referenced page exists**

```bash
node - <<'EOF'
const fs = require('fs');
const d = JSON.parse(fs.readFileSync('docs.json', 'utf8'));
const pages = [];
const walk = x => { if (typeof x === "string") pages.push(x); else if (Array.isArray(x)) x.forEach(walk); else if (x && x.pages) walk(x.pages); };
d.navigation.languages.forEach(l => l.tabs.forEach(t => walk(t.pages)));
const missing = pages.filter(p => !fs.existsSync(p + ".mdx"));
console.log("pages:", pages.length, "missing:", missing.length);
missing.forEach(m => console.log("  MISSING", m));
process.exit(missing.length ? 1 : 0);
EOF
```
Expected: `pages: 310 missing: 0` (62 × 5).

- [ ] **Step 3: Add flags to style.css**

Build data URIs from these exact SVGs (same cropped-square geometry as the existing NL/EN flags):

```bash
DE_SVG='<svg xmlns="http://www.w3.org/2000/svg" viewBox="85.5 0 342 342"><path fill="#000" d="M0 0h513v114H0z"/><path fill="#D00" d="M0 114h513v114H0z"/><path fill="#FFCE00" d="M0 228h513v114H0z"/></svg>'
FR_SVG='<svg xmlns="http://www.w3.org/2000/svg" viewBox="85.5 0 342 342"><path fill="#0055A4" d="M0 0h171v342H0z"/><path fill="#FFF" d="M171 0h171v342H171z"/><path fill="#EF4135" d="M342 0h171v342H342z"/></svg>'
IT_SVG='<svg xmlns="http://www.w3.org/2000/svg" viewBox="85.5 0 342 342"><path fill="#009246" d="M0 0h171v342H0z"/><path fill="#FFF" d="M171 0h171v342H171z"/><path fill="#CE2B37" d="M342 0h171v342H342z"/></svg>'
printf '%s' "$DE_SVG" | base64 -w0   # → use as DE_B64 below, likewise FR/IT
```

Append to `style.css`, following the file's documented fail-safe pattern **exactly** (trigger `::before` rules ONLY inside `html[lang="…"]`-scoped selectors, never unscoped — see the comment block at the top of the file):

```css
#localization-select-item-de > p::before,
#localization-select-item-fr > p::before,
#localization-select-item-it > p::before,
html[lang="de"] #localization-select-trigger > span::before,
html[lang="fr"] #localization-select-trigger > span::before,
html[lang="it"] #localization-select-trigger > span::before {
  content: ""; display: inline-block;
  width: 1rem; height: 1rem; margin-right: .4rem; vertical-align: -2px;
  background-size: cover; background-position: center;
  border-radius: 9999px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.1);
}
#localization-select-item-de > p::before { background-image: url("data:image/svg+xml;base64,DE_B64"); }
#localization-select-item-fr > p::before { background-image: url("data:image/svg+xml;base64,FR_B64"); }
#localization-select-item-it > p::before { background-image: url("data:image/svg+xml;base64,IT_B64"); }
html[lang="de"] #localization-select-trigger > span::before { background-image: url("data:image/svg+xml;base64,DE_B64"); }
html[lang="fr"] #localization-select-trigger > span::before { background-image: url("data:image/svg+xml;base64,FR_B64"); }
html[lang="it"] #localization-select-trigger > span::before { background-image: url("data:image/svg+xml;base64,IT_B64"); }
```

(Replace `DE_B64`/`FR_B64`/`IT_B64` with the actual base64 output. Note the unscoped shared rule lists only `-item-` selectors plus `html[lang]`-scoped trigger selectors — this preserves the fail-safe.)

- [ ] **Step 4: Create the DNT list**

Write `translations/dnt.json`:

```json
[
  "Screenmate", "OneCable", "Lite 144", "Dual Flip", "Flip", "Expand",
  "Infinity Lite", "Infinity", "One 4K OLED", "One 4K", "Panorama",
  "USB-C", "USB-A", "HDMI", "Mini-HDMI", "Power Delivery", "Backlight",
  "Drivers", "FAQ", "OSD",
  "LANGUAGE", "OSD TIMER", "TRANSPARENCY", "BRIGHTNESS", "CONTRAST",
  "SHARPNESS", "COLOR TEMP", "ECO", "RESET", "HDR", "FREESYNC", "VOLUME"
]
```

Then cross-check the OSD caps labels against what actually appears in `en/manuals/*/osd.mdx` (`grep -ohE '\(([A-Z][A-Z0-9 /]+)\)' en/manuals/*/osd.mdx | sort -u`) and adjust the list to match reality — the list above is the starting set, the grep output is authoritative.

- [ ] **Step 5: Run the build check**

```bash
mint broken-links
```
Expected: passes (stubs contain no links; existing nl/en unaffected). If the command errors on environment grounds, record the error verbatim in the task report — do not paper over it.

- [ ] **Step 6: Commit**

```bash
git add docs.json style.css translations/dnt.json
git commit -m "feat(i18n): docs.json language blocks, switcher flags, DNT list for de/fr/it"
```

**ORCHESTRATOR GATE:** review the docs.json diff (language order, tab labels, hidden flags preserved), the CSS fail-safe pattern, and the final DNT list before Phase 1 dispatch.

---

### Task 3–5: Locked glossaries — de, fr, it (Opus ×3, parallel)

**Files (one task per language):**
- Create: `translations/glossary-de.md` (Task 3), `translations/glossary-fr.md` (Task 4), `translations/glossary-it.md` (Task 5)

**Interfaces:**
- Consumes: `.claude/skills/screenmate-dutch-fidelity/references/glossary.md` (structure model), `translations/dnt.json`, the EN corpus.
- Produces: a locked glossary file per language. Every Phase 2 translator prompt references it as binding.

- [ ] **Step 1: Dispatch one Opus agent per language with this brief**

> Create `translations/glossary-{LANG}.md` for the Screenmate manuals translation ({LANGUAGE_NAME}). Model its structure on `.claude/skills/screenmate-dutch-fidelity/references/glossary.md` (read it first). Requirements:
> 1. **Term table:** every technical term in the EN corpus (`en/manuals/**/*.mdx`, `en/manuals-index.mdx`) → locked {LANGUAGE_NAME} rendering. Extract candidate terms by reading all EN `controls.mdx`, `osd.mdx`, `installation*.mdx` files. Include a "Keep EN?" column; seed it from `translations/dnt.json`.
> 2. **Register rules:** {REGISTER_RULE}. Give 5 example sentence pairs (wrong register → right register).
> 3. **Compound/hyphenation rules** for this language (e.g. DE closed compounds `USB-C-Kabel`, FR noun+modifier `câble USB-C`, IT `cavo USB-C`), covering the three-part chain (`USB-C to USB-C cable`) explicitly — NL had inconsistency there, do not repeat it.
> 4. **Number formatting:** comma decimal, no thousands separator (`15,6"`, `2,5 cm`, `1820 gram` pattern).
> 5. **Document & section names table:** every `##`/`###` heading and frontmatter title in the EN corpus → locked rendering (mirror the NL glossary's section-names table).
> 6. **OSD caps labels:** listed verbatim as untranslatable (they render on the physical device in English).
> Do not translate any manual pages. Deliverable is the glossary file only. Commit it: `feat(i18n): locked {LANG} glossary`.

Register substitutions: de = "informal du, never Sie/Ihnen/Ihr"; fr = "formal vous, never tu/toi/ton"; it = "informal tu, never Lei/Suo".

- [ ] **Step 2: ORCHESTRATOR GATE — review each glossary**

Check per glossary: register rules match the locked decision; DNT list fully represented; section-names table covers all EN headings (spot-check 10 against `grep -h "^## " en/manuals/*/*.mdx | sort -u`); hyphenation rules address the three-part cable chain. Reject and re-dispatch with specific feedback if not.

---

### Task 6: Shared chapters — safety + display-settings (Opus ×3, one per language, parallel; after Task 3–5 gate)

**Files (per language `{L}` ∈ de, fr, it):**
- Overwrite: `{L}/manuals/{slug}/safety.mdx` for all 11 slugs; `{L}/manuals/{slug}/display-settings.mdx` for onecable, dual-flip, flip, expand, infinity, infinity-lite.

**Interfaces:**
- Consumes: glossary `translations/glossary-{L}.md`; EN+NL source pairs.
- Produces: 17 final files per language whose dedupe-group bodies are byte-identical (Task 8's checker enforces this).

- [ ] **Step 1: Dispatch one Opus agent per language with this brief**

> Translate the Screenmate shared chapters into {LANGUAGE_NAME}. Binding glossary: `translations/glossary-{L}.md` — read it fully first. Register: {REGISTER_RULE}.
>
> **Dual-source rule:** for each page read BOTH `en/...` and `nl/...` counterparts. EN is the structural template (headings, components, step counts — mirror exactly). NL is the semantic tiebreaker, register model, and number-format model. If EN and NL differ in MEANING (not phrasing), STOP translating that passage, write the discrepancy to `translations/flags/{L}-shared.md` (create it; format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`), and translate the passage that both agree on if one exists, otherwise follow EN and mark the flag `blocked`.
>
> **Safety = 5 distinct bodies, not 11.** Translate each body ONCE, then write every member file with the byte-identical translated body: Group A body (source: `en/manuals/onecable/safety.mdx` + `nl/manuals/onecable/safety.mdx`) → write to onecable, lite, lite-144hz, flip, expand, one-4k, one-4k-oled. Then dual-flip, infinity, infinity-lite, panorama each individually. Safety style: literal fidelity over idiomatic polish; preserve every negation ("never", "do not") explicitly.
>
> **display-settings = 3 distinct bodies.** Shared body (source: onecable) → write to onecable, dual-flip, flip, expand (frontmatter translated per file — flip's differs slightly from the others; read each). Then infinity, infinity-lite individually.
>
> **Rules:** overwrite the stub files completely (frontmatter + body). Translate frontmatter `title`, `description` and all alt text; keep `icon` and every `src` byte-identical; do NOT write any `*_link` frontmatter keys; OSD caps labels and DNT terms (`translations/dnt.json`) stay verbatim; comma decimals; OS-settings screenshots are English by design — translate surrounding prose only.
> Commit: `feat(i18n): {L} shared chapters (safety, display-settings)`.

- [ ] **Step 2: Spot-verify byte-identity after each agent reports**

```bash
for L in de fr it; do for p in onecable lite lite-144hz flip expand one-4k one-4k-oled; do printf "%s %-14s " "$L" "$p"; awk 'BEGIN{fm=0} /^---$/{fm++; next} fm>=2{print}' "$L/manuals/$p/safety.mdx" | md5sum | cut -c1-12; done; done
```
Expected: one hash per language across group A. (Full enforcement lands in Task 8.)

---

### Task 7: Product + index translation (Opus, 36 tasks: 11 products × 3 languages + 3 index pages; parallel after Task 3–5 gate, independent of Task 6)

**Files (per task, language `{L}`, slug `{S}`):**
- Overwrite: every `{L}/manuals/{S}/*.mdx` EXCEPT `safety.mdx` and `display-settings.mdx` (Task 6 owns those). Index tasks overwrite `{L}/manuals-index.mdx`.

**Interfaces:**
- Consumes: glossary `translations/glossary-{L}.md`, `translations/dnt.json`, EN+NL page pairs.
- Produces: final translated pages; optional `translations/flags/{L}-{S}.md` when EN/NL disagree.

- [ ] **Step 1: Dispatch per-product Opus agents with this brief** (one per row of the matrix below; batch dispatches in groups of ~6 to keep review manageable)

> Translate the Screenmate **{S}** manual pages into {LANGUAGE_NAME}: files {PAGE_LIST} (skip safety.mdx and display-settings.mdx — another task owns them). Binding glossary: `translations/glossary-{L}.md` — read fully first. Register: {REGISTER_RULE}.
>
> **Dual-source rule:** for each page read BOTH `en/manuals/{S}/<page>` and `nl/manuals/{S}/<page>`. EN = structural template: same headings (translated per the glossary's section-names table), same component sequence (`<Note>`, `<Warning>`, `<Tabs>`…), same number of numbered steps, same table rows, same images. NL = semantic tiebreaker, register model, number-format model. If EN and NL differ in MEANING, STOP on that passage and log to `translations/flags/{L}-{S}.md` (format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`).
>
> **Rules:** overwrite stubs completely; translate frontmatter `title`/`description` and all alt text; `icon` and `src` byte-identical; no `*_link` keys; DNT terms and OSD caps labels verbatim; comma decimals, no thousands separator; OS screenshots are English by design; hyphenate compounds per the glossary. For `manuals-index.mdx`: card titles per the glossary's section-names table, no card descriptions (cards are deliberately title-only).
> Commit: `feat(i18n): {L} {S} manual`.

Task matrix — every row is one dispatch (`de`+`fr`+`it` × each):

| # | Slug | Pages (excl. safety/display-settings) |
|---|---|---|
| 1 | onecable | index, installation, installation-windows, installation-mac, controls, troubleshooting |
| 2 | lite | index, installation, controls, osd |
| 3 | lite-144hz | index, installation, controls, osd |
| 4 | dual-flip | index, installation, controls, osd |
| 5 | flip | index, installation, controls, osd |
| 6 | expand | index, installation, controls, osd |
| 7 | infinity | index, installation, controls |
| 8 | infinity-lite | index, installation, controls |
| 9 | one-4k | index, installation, controls, osd |
| 10 | one-4k-oled | index, installation, controls, osd |
| 11 | panorama | index, installation, controls, osd |
| 12 | (site index) | manuals-index.mdx |

- [ ] **Step 2: ORCHESTRATOR GATE per batch** — after each batch of ~6 agents reports: skim one full page per agent against its EN/NL sources; check flags files; confirm no stub markers remain in completed slugs (`grep -rl "STUB-TRANSLATION-PENDING" de fr it | grep <slug> || echo clean`).

---

### Task 8: Verification script (Sonnet, TDD; can run parallel with Tasks 6–7)

**Files:**
- Create: `scripts/verify_translation.py`, `tests/test_verify_translation.py`

**Interfaces:**
- Consumes: `translations/dnt.json` (JSON array of strings).
- Produces: CLI `python scripts/verify_translation.py --base en --targets de fr it [--include-nl]` → exit 0 clean / exit 1 on any FAIL; prints FAIL/WARN lines `SEVERITY CHECK path: detail`.

- [ ] **Step 1: Write the failing tests**

`tests/test_verify_translation.py`:

```python
import json
import textwrap
from pathlib import Path

import pytest

from scripts.verify_translation import parse_page, verify_tree

def write(root: Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(textwrap.dedent(text), encoding="utf-8")

EN_PAGE = """\
    ---
    title: "Controls"
    description: "Buttons"
    icon: "gamepad"
    ---
    ## Ports
    The screen is 15.6" wide. Do not cover the vents.
    <Note>
    Use **Power Delivery** chargers only.
    </Note>
    <img src="/images/x.png" alt="Ports overview" />
    1. Press the button.
    2. Wait 5 seconds.
    """

DE_PAGE_OK = """\
    ---
    title: "Bedienung"
    description: "Tasten"
    icon: "gamepad"
    ---
    ## Anschlüsse
    Der Bildschirm ist 15,6" breit. Decke die Lüftungsschlitze nicht ab.
    <Note>
    Verwende nur **Power Delivery**-Ladegeräte.
    </Note>
    <img src="/images/x.png" alt="Übersicht der Anschlüsse" />
    1. Drücke die Taste.
    2. Warte 5 Sekunden.
    """

@pytest.fixture
def tree(tmp_path: Path) -> Path:
    (tmp_path / "translations").mkdir()
    (tmp_path / "translations" / "dnt.json").write_text(json.dumps(["Power Delivery"]))
    write(tmp_path, "en/manuals/lite/controls.mdx", EN_PAGE)
    write(tmp_path, "de/manuals/lite/controls.mdx", DE_PAGE_OK)
    return tmp_path

def test_clean_tree_passes(tree: Path) -> None:
    issues = verify_tree(tree, base="en", targets=["de"])
    assert [i for i in issues if i.severity == "FAIL"] == []

def test_parse_extracts_structure(tree: Path) -> None:
    page = parse_page(tree / "en/manuals/lite/controls.mdx")
    assert page["icon"] == "gamepad"
    assert [lvl for lvl, _ in page["headings"]] == [2]
    assert page["components"] == ["Note", "/Note"]
    assert page["srcs"] == ["/images/x.png"]
    assert page["steps"] == 2

def test_missing_heading_fails(tree: Path) -> None:
    bad = (tree / "de/manuals/lite/controls.mdx").read_text().replace("## Anschlüsse\n", "")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "structure" and i.severity == "FAIL" for i in issues)

def test_decimal_transform_accepted_and_missing_number_fails(tree: Path) -> None:
    # 15.6 -> 15,6 must be accepted (fixture already passes); dropping a number must fail
    bad = (tree / "de/manuals/lite/controls.mdx").read_text().replace("Warte 5 Sekunden", "Warte kurz")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "numbers" and i.severity == "FAIL" for i in issues)

def test_wrong_register_warns(tree: Path) -> None:
    bad = (tree / "de/manuals/lite/controls.mdx").read_text().replace("Drücke die Taste", "Drücken Sie die Taste")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "register" and i.severity == "WARN" for i in issues)

def test_missing_dnt_term_fails(tree: Path) -> None:
    bad = (tree / "de/manuals/lite/controls.mdx").read_text().replace("Power Delivery", "Stromlieferung")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "dnt" and i.severity == "FAIL" for i in issues)

def test_stub_marker_fails(tree: Path) -> None:
    write(tree, "de/manuals/lite/osd.mdx", '---\ntitle: "STUB"\n---\n{/* STUB-TRANSLATION-PENDING */}\n')
    write(tree, "en/manuals/lite/osd.mdx", '---\ntitle: "OSD"\nicon: "sliders"\n---\n## Menu\n')
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "stub" and i.severity == "FAIL" for i in issues)

def test_dedupe_divergence_fails(tree: Path) -> None:
    write(tree, "en/manuals/onecable/safety.mdx", '---\ntitle: "Safety"\nicon: "shield"\n---\nNever cover it.\n')
    write(tree, "en/manuals/flip/safety.mdx",     '---\ntitle: "Safety"\nicon: "shield"\n---\nNever cover it.\n')
    write(tree, "de/manuals/onecable/safety.mdx", '---\ntitle: "Sicherheit"\nicon: "shield"\n---\nDecke es niemals ab.\n')
    write(tree, "de/manuals/flip/safety.mdx",     '---\ntitle: "Sicherheit"\nicon: "shield"\n---\nDecke es nie ab.\n')
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "dedupe" and i.severity == "FAIL" for i in issues)
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_verify_translation.py -v
```
Expected: collection error / failures — `scripts.verify_translation` does not exist.

- [ ] **Step 3: Implement `scripts/verify_translation.py`**

```python
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
        "numbers": sorted(NUM_RE.findall(body)),
        "steps": len(STEP_RE.findall(body)),
        "table_rows": len(TABLEROW_RE.findall(body)),
        "icon": icon.group(1).strip() if icon else None,
        "body": body,
        "stub": STUB_MARKER in text,
    }


def body_hash(path: Path) -> str:
    return hashlib.md5(parse_page(path)["body"].encode("utf-8")).hexdigest()


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

    base_nums = sorted(n.replace(".", ",") for n in base["numbers"])
    tgt_nums = sorted(n.replace(".", ",") for n in tgt["numbers"])
    if base_nums != tgt_nums:
        missing = [n for n in base_nums if base_nums.count(n) > tgt_nums.count(n)]
        extra = [n for n in tgt_nums if tgt_nums.count(n) > base_nums.count(n)]
        issues.append(Issue("FAIL", "numbers", p,
                            f"missing {missing[:8]} extra {extra[:8]}"))

    for term in dnt:
        if term in base_body and term not in tgt["body"]:
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
```

Note for the implementer: `tests/` needs the repo root on `sys.path` for `from scripts.verify_translation import ...` — add an empty `scripts/__init__.py` if import fails, or a one-line `conftest.py` with `sys.path.insert(0, str(Path(__file__).parent.parent))`.

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_verify_translation.py -v
```
Expected: 8 passed.

- [ ] **Step 5: Run against the real tree (nl sanity check)**

```bash
python scripts/verify_translation.py --base en --targets nl
```
Expected: exit 0 or a small set of explainable WARNs (nl register/negation checks don't apply — only de/fr/it are in the REGISTER_RE/NEGATION_RE maps). Structure/numbers/dedupe FAILs here mean the checker is too strict — tune it against the known-good nl corpus and record what was tuned in the task report.

- [ ] **Step 6: Commit**

```bash
git add scripts/verify_translation.py tests/test_verify_translation.py
git commit -m "feat(i18n): mechanical translation verification script + tests"
```

---

### Task 9: Mechanical verification + fix loop (orchestrator runs; Opus/Sonnet fix agents as needed)

- [ ] **Step 1: Run the full check** (after Tasks 6–8 complete)

```bash
python scripts/verify_translation.py --base en --targets de fr it --include-nl
grep -rl "STUB-TRANSLATION-PENDING" de fr it && echo "STUBS REMAIN" || echo "no stubs"
mint broken-links
```

- [ ] **Step 2: Dispatch fix agents per failure cluster** — one agent per (language × check-type) cluster, with the exact FAIL lines in the brief plus the same dual-source + glossary rules as Task 7. Re-run Step 1. Loop until 0 FAIL. WARNs: orchestrator dispositions each (fix, or record as accepted with reason in `translations/qa/warn-dispositions.md`).

- [ ] **Step 3: Commit fixes + dispositions**

```bash
git add -A de fr it translations
git commit -m "fix(i18n): mechanical verification fixes for de/fr/it"
```

---

### Task 10: Semantic verification — back-translation + adversarial review (Opus; after Task 9 is clean)

Families (balanced by word count): **F1** onecable+infinity+infinity-lite · **F2** lite+lite-144hz+panorama · **F3** flip+dual-flip · **F4** expand+one-4k+one-4k-oled. Site index pages ride with F2.

- [ ] **Step 1: Blind back-translation — 12 Opus agents** (4 families × 3 languages), dispatched with this brief:

> You are given ONLY the {LANGUAGE_NAME} manual files listed: {FILE_LIST}. Do NOT open anything under `en/` or `nl/` — your value depends on never seeing the originals. Translate each file's prose content back into plain English (headings, steps, notes, alt text; skip frontmatter and component syntax). Write the result to `translations/qa/backtranslation-{L}-{FAMILY}.md` with one `## {file path}` section per file. Commit: `chore(i18n): back-translation {L} {FAMILY}`.

- [ ] **Step 2: Divergence comparison — 3 Opus agents** (one per language):

> Compare `translations/qa/backtranslation-{L}-*.md` against the original `en/` files section by section. List every SEMANTIC divergence (meaning changed, instruction inverted, quantity changed, warning weakened, content dropped/added) — ignore phrasing differences. Output `translations/qa/backtranslation-review-{L}.md`: table with file, EN passage, back-translated passage, severity (critical/moderate/cosmetic). Commit it.

- [ ] **Step 3: Adversarial review — 12 Opus agents** (4 families × 3 languages):

> You are reviewing a {LANGUAGE_NAME} translation for ERRORS. Your job is to find problems, not confirm quality — an empty report is a failed review unless you demonstrate real scrutiny. For each page in {FILE_LIST}, read EN + NL + {L} side by side. Hunt specifically: meaning drift vs BOTH sources, register violations ({REGISTER_RULE}), glossary violations (`translations/glossary-{L}.md`), unnatural calques of English syntax, wrong compound/hyphenation, number/unit errors, safety-negation weakening. Output `translations/qa/adversarial-{L}-{FAMILY}.md`: findings with file, line quote, problem, proposed fix. Commit it.

- [ ] **Step 4: ORCHESTRATOR GATE — disposition every finding.** Build `translations/qa/findings-disposition.md`: every back-translation divergence (critical/moderate) and adversarial finding → fixed / rejected-with-reason. Dispatch fix agents for accepted findings; re-run Task 9 Step 1 after fixes. Anything touching EN/NL copy or product facts goes to the user/Louie, not fixed unilaterally.

- [ ] **Step 5: Consolidate EN↔NL disagreement flags.** Merge all `translations/flags/*.md` into `translations/flags-consolidated.md` with dispositions. `blocked` items: escalate to user. Commit.

---

### Task 11: Link generation + final verification (orchestrator)

- [ ] **Step 1: Generate cross-language links**

```bash
python scripts/generate_language_links.py
```
Expected: `Parity: OK — every page exists in every language`; ~310 files change (every page gains its missing `<lang>_link` keys — en/nl pages gain 3 each, de/fr/it pages gain 4 each).

- [ ] **Step 2: Full final check**

```bash
python scripts/generate_language_links.py --check   # exit 0, idempotent
python scripts/verify_translation.py --base en --targets de fr it --include-nl   # exit 0
python -m pytest tests/test_verify_translation.py -q
mint broken-links
grep -rl "STUB-TRANSLATION-PENDING" de fr it && echo FAIL || echo clean
```
Expected: all pass, `clean`.

- [ ] **Step 3: Visual smoke test** — `mint dev`, open localhost: switcher shows 5 languages with flags in both themes; navigate de/fr/it index → one product each; language switcher preserves current page (the `_link` mechanism). Screenshot evidence per language.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat(i18n): cross-language links for 5 languages + final verification"
```

---

### Task 12: Delivery doc + merge gate (Fable writes; user approves merge)

**Files:**
- Create: `DELIVERY-LANGUAGE-EXPANSION.md` (repo root, English, client-facing)

- [ ] **Step 1: Write the delivery doc** with exactly these sections (per spec §8):
  1. **What shipped:** 186 new pages, URL scheme (`/de/manuals/...`), switcher behavior, flags.
  2. **Register choices:** DE du / FR vous / IT tu, with the FR-vous rationale spelled out.
  3. **Verification performed:** the 8 checks with actual result counts pulled from Task 9/10 outputs and `translations/qa/` reports.
  4. **What machine verification cannot prove:** native idiomaticity; regulatory fit. Stated plainly.
  5. **Review-partner ask (bounded):** the 5 distinct safety bodies + spec tables, ≈1,000 words × 3 languages, with exact file paths and the note that fixing one group-A file fixes seven.
  6. **GPSR note:** EU Reg. 2023/988 requires safety information in the language of the member state of sale — flagged as our reading, to be confirmed by their compliance person; not legal advice.

- [ ] **Step 2: Commit the doc**

```bash
git add DELIVERY-LANGUAGE-EXPANSION.md
git commit -m "docs: delivery report for IT/DE/FR language expansion"
```

- [ ] **Step 3: USER GATE — present summary + delivery doc; on explicit approval only:**

```bash
git checkout main && git merge --no-ff lang-expansion-de-fr-it && git push
```

(Push deploys. Do not run without the user's explicit go.)

---

## Self-Review Notes

- Spec §2–§9 all mapped: registers/plumbing (T2), dual-source (T6/T7 briefs), dedupe (T6 + T8 checker), DNT (T2/T8), verification 1–6 (T8/T9), 7–8 (T10), delivery (T12), out-of-scope respected (no new redirects; EN/NL frozen except T1 fix and T10 dispositions).
- Checker is deliberately tuned against known-good `nl` before judging new languages (T8 Step 5) to avoid false-positive whack-a-mole.
- `Infinity` before `Infinity Lite`? DNT list orders `"Infinity Lite"` before `"Infinity"` — irrelevant for the containment check used, but kept longest-first for safety.
