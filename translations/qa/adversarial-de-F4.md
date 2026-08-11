# Adversarial DE review — family F4 (`expand`, `one-4k`, `one-4k-oled`)

Branch `lang-expansion-de-fr-it`. 16 DE pages read against their EN and NL counterparts
(48 files total). Reference: `translations/glossary-de.md`, `translations/flags/de-expand.md`,
`de-one-4k.md`, `de-one-4k-oled.md`, `de-shared.md`.

**Verdict: no critical defects. 15 findings — 2 high, 5 medium, 8 low.** The dominant
problem is not mistranslation but **sibling drift**: where the EN source is byte-identical
across two pages, the German is not. NL holds those pairs identical; DE is the only
language that broke them.

Client-flagged known non-defects were checked and deliberately **not** reported: expand
`alt="…1 bis 6"` against 5 steps, the EN `Color Gamut`/`Color Accuracy` split, DIN 5008
unit spacing, EN-verbatim `{/* … */}` comments (§7.7 lock), Dutch-language screenshots.

---

## Findings

| # | File | Line & quote | Problem | Sev | Proposed fix |
|---|---|---|---|---|---|
| F4-01 | `de/manuals/one-4k/installation.mdx` + `de/manuals/one-4k-oled/installation.mdx` | L9–15, both `## Erste Schritte` blocks | **6 of 7 bullets diverge.** EN L8–16 in the two files is **byte-identical** (`diff` returns nothing); NL L8–16 is likewise byte-identical. DE is the only language where the sibling block drifted. The brief names this pair as a required check. Sub-rows F4-02…F4-05 itemise it. | **High** | Pick one rendering per bullet and apply to both files. Recommended base: `one-4k` for bullets 3–4 (§9 term), `one-4k-oled` for bullets 2, 5, 6, 7 (closer to EN structure). |
| F4-02 | `one-4k/installation.mdx` L11, L12 vs `one-4k-oled/installation.mdx` L11, L12 | one-4k: `…und passt die **Anzeigeeinstellungen** an` / `…über die **Anzeigeeinstellungen** deines Geräts aus` — oled: `…passt die **Bildschirmeinstellungen** an` / `…über die **Bildschirmeinstellungen** deines Geräts aus` | Same EN string (`the display settings` / `your device's display settings`) rendered with two different locked terms on sibling pages. Glossary §9 locks OS-level display settings → `Anzeigeeinstellungen`; §7.2 reserves `Bildschirmeinstellungen` for the **OSD** context (`Display settings via the on-screen menu`). The oled page uses the OSD term for an OS-level referent. | **High** | Change both oled occurrences to `Anzeigeeinstellungen`. |
| F4-03 | `one-4k/installation.mdx` L14 vs `one-4k-oled/installation.mdx` L14 | one-4k: `…**aktiviert** der Screenmate automatisch die Schnellladefunktion.` — oled: `…**schaltet** der Screenmate automatisch **auf** die Schnellladefunktion **um**.` | EN: `switches to fast-charge mode`. `aktiviert` = "activates", loses the *switching* sense the glossary §5 row cites verbatim ("One 4K 'switches to fast-charge mode'"). Also a straight sibling mismatch. | Medium | Use the oled form (`schaltet … um`) in both. |
| F4-04 | `one-4k-oled/controls.mdx` L13 | `Verwende den USB-C-Anschluss für Strom **und** Video, wenn dein Gerät…` | one-4k L13 has `Strom **& ** Video`; EN has `power & video` in both. Worse, four lines below, the **same page** heads the section `### USB-C-Anschluss (Strom & Video)` (the §7.4-locked form), so the body prose no longer matches the heading it refers to. | Medium | `Strom & Video` in the oled body, matching one-4k, EN, and the page's own §7.4 heading. |
| F4-05 | `one-4k/controls.mdx` L35; `one-4k/installation.mdx` L15; `one-4k-oled/installation.mdx` L15 | `…USB-2.0-Zubehör **wie zum Beispiel** einer Maus oder einer Tastatur` (×3) | Glossary §10.1 `such as`: bare **`wie`** for a short apposition (`Risiken wie Stromschlag oder Brand`, as shipped in the frozen safety chapter); `wie zum Beispiel` only "for a genuine enumeration of examples". Two coordinated nouns is the short-apposition shape, not an enumeration. (The 5-item HDMI device lists at `one-4k/installation.mdx` L67 and `one-4k-oled` L61 correctly keep `wie zum Beispiel`.) | Medium | `…USB-2.0-Zubehör **wie** einer Maus oder einer Tastatur` in all three spots. |
| F4-06 | `de/manuals/expand/osd.mdx` | L24 `- **Schärfe (SHARPNESS):** Passe die **Bildschärfe** an (0–4).` | Glossary §6.2.1 names `Schärfe` vs `Bildschärfe` **by name** as the per-product drift the locked vocabulary exists to prevent. This is the only file in the DE corpus using `Bildschärfe`; the four sibling OSD pages (`dual-flip`, `flip`, `lite`, `lite-144hz`) all use `Schärfe`. | Medium | `Passe die Schärfe des Bildes an (0–4).` (matches `de/manuals/dual-flip/osd.mdx:22`). |
| F4-07 | all 16 F4 pages (and all 62 DE, 62 FR, 62 IT pages) | frontmatter, e.g. `de/manuals/expand/index.mdx` L1–5 — no `en_link:` / `nl_link:` key | Every EN and NL page carries the cross-language key; **no** DE page does. `scripts/generate_language_links.py` docstring: product tabs are `hidden: true`, so "Mintlify's language switcher cannot infer a page's counterpart… Each page must therefore carry an explicit link". Running `--check` confirms the tree is stale. The switcher cannot resolve to or from any German page. Not a translation defect — a pending generator run — but it blocks these pages. | Medium | `python scripts/generate_language_links.py` from the repo root; re-run `--check` to confirm clean. Repo-wide, not F4-scoped. |
| F4-08 | `one-4k-oled/controls.mdx` L13 | `**Über diese eine Verbindung laufen** Strom und Video **zusammen** über ein einziges Kabel.` | EN (identical in both files): `This single connection carries both power and video over one cable.` one-4k L13 renders it tightly (`Diese eine Verbindung überträgt Strom und Video über ein einziges Kabel.`). The oled paraphrase adds `zusammen`, and `laufen … zusammen` reads as *converge*, which is not what a single cable does. | Low | Adopt the one-4k sentence verbatim. |
| F4-09 | `one-4k/controls.mdx` L43 | `Wenn der Monitor **an ist**, drücke sie, um das OSD-Menü zu öffnen.` | Colloquial predicative `an sein`. oled L43 has `Wenn der Monitor **eingeschaltet** ist`, which matches the house verb (§10.2 rejects `Drehe das Gerät an/aus` and locks `einschalten`). Same EN sentence. | Low | `Wenn der Monitor eingeschaltet ist, …` in one-4k. |
| F4-10 | `one-4k/osd.mdx` L13 | `Die ausgewählte Option **wird** gelb hervorgehoben.` | EN: `The selected option **is** highlighted in yellow` — a state, not a process. `wird … hervorgehoben` is process passive. oled L13 correctly has `**ist** gelb hervorgehoben`. | Low | `Die ausgewählte Option ist gelb hervorgehoben.` |
| F4-11 | `one-4k/osd.mdx` L9, L13, L17, L30 vs `one-4k-oled/osd.mdx` same lines | e.g. L17 one-4k `Ändere einen Wert mit der Taste + oder − und drücke die Power-Taste, um zu speichern.` vs oled `Verwende die Taste + oder −, um einen Wert zu ändern, und drücke die Power-Taste zum Speichern.` | EN `osd.mdx` for the two slugs differs **only** in `nl_link` and the `{/* … */}` comment — the six run-in lines and the OSD-Lock line are byte-identical. DE diverges on four of them (L9 clause order, L13 per F4-10, L17 phrasing, L30 `10 Sekunden **lang** gedrückt` vs `10 Sekunden gedrückt`). NL keeps its pair identical. | Low | Normalise `de/manuals/one-4k-oled/osd.mdx` L9/L13/L17/L30 onto one-4k (or vice versa); the pages must read the same. |
| F4-12 | `expand/controls.mdx` L9, `one-4k/controls.mdx` L9, `one-4k-oled/controls.mdx` L9 | `…Bedientasten **am** Screenmate Expand.` / `…Bedientasten **des** Screenmate One 4K.` / `Dieser Abschnitt gibt **dir** einen Überblick … **des** Screenmate One 4K OLED.` | Same EN opener (`…control buttons on the Screenmate X`) rendered three different ways inside a single review family. Corpus-wide the split is 8× `am` / 5× `des` and 3× with `dir` / 8× without. | Low | Pick one house opener and sweep all 11 DE `controls.mdx`. Suggest `…Bedientasten am Screenmate X.` (majority, and the shipped `onecable` form). |
| F4-13 | `expand/index.mdx` L15 | `…und zu zwei Full-HD-**Displays** aufklappst – eines auf jeder Seite. So wird aus deinem Laptop ein Arbeitsplatz mit drei **Bildschirmen**.` | §10.4 locks `Bildschirm` as the default "for individual screens of a multi-screen product" and reserves `Display` for the panel as a hardware component / the macOS `Displays` label. The two side screens are individual screens, and the sentence switches terms for the same referent mid-breath. (`panorama/index.mdx` L15 shares the habit; `infinity/index.mdx` L15 correctly writes `zwei 15,6"-Bildschirmen in Full HD`.) | Low | `…und zu zwei Full-HD-Bildschirmen aufklappst – einer auf jeder Seite.` (note the agreement change `eines` → `einer`). |
| F4-14 | `expand/osd.mdx` L61 | `Reduziert den Blaulichtanteil **auf dem** Bildschirm und entlastet so die Augen.` | EN: `blue light **from** the screen`. `auf dem Bildschirm` locates the blue light *on* the panel rather than *emitted by* it. Consistent with `dual-flip/osd.mdx:59`, so a two-file fix. | Low | `Reduziert den Blaulichtanteil des Bildschirms und entlastet so die Augen.` (apply to `dual-flip/osd.mdx:59` too). |
| F4-15 | `expand/installation.mdx` L29 | `2. Klappe die beiden Bildschirme in die Richtung auf, die in Abbildung 2 gezeigt wird.` | Heavier relative-clause paraphrase where the sibling page rendering the same EN (`in the direction shown in image 2`) uses the tighter participial attribute: `de/manuals/flip/installation.mdx:47` — `Klappe den rechten Bildschirm in die in Abbildung 2 gezeigte Richtung auf.` §10.1 locks the `wie in Abbildung 2 gezeigt` family. | Low | `2. Klappe die beiden Bildschirme in die in Abbildung 2 gezeigte Richtung auf.` |

---

## Scrutiny evidence

Everything below was executed, not assumed. Passing checks are listed so the empty
categories are demonstrably empty rather than unexamined.

### 1. Frozen shared chapters — PASS (no divergence)

Bodies compared with the frontmatter stripped (`awk` on the second `---`), because
frontmatter legitimately differs per product in EN/NL.

`display-settings.mdx` body MD5 (first 10 hex):

| slug | EN | NL | DE |
|---|---|---|---|
| onecable *(canonical)* | `467551f5a5` | `88f65c86c9` | `e6f54bf0a0` |
| **expand** | `467551f5a5` | `88f65c86c9` | **`e6f54bf0a0`** |
| dual-flip | `467551f5a5` | `88f65c86c9` | `e6f54bf0a0` |
| flip | `467551f5a5` | `88f65c86c9` | `e6f54bf0a0` |
| infinity-lite | `b6465dea60` | `d190cf5c26` | `05dc201010` |
| infinity | `57c58d4143` | `bf28c6bd6b` | `c548362955` |

`safety.mdx` body MD5: DE `expand`, `one-4k`, `one-4k-oled`, `flip`, `lite`, `lite-144hz`,
`onecable` all = **`cf3a7469a1`**, matching the canonical onecable body and mirroring the
EN group `b709f7d9c7` exactly. `dual-flip`, `infinity`, `infinity-lite`, `panorama` sit in
their own groups in DE exactly as in EN.

**Grouping is identical to EN in every group, including where NL drifted:**
`nl/manuals/onecable/safety.mdx` (`5bdf737959`) has fallen out of its own EN group
(`2d6f989569`). DE did **not** inherit that NL defect. All three F4 frozen chapters are
intact; no critical finding.

Whole-file MD5 for DE `display-settings.mdx` is identical across onecable/expand/dual-flip
only because DE carries no `*_link` frontmatter at all — that is F4-07, not a chapter defect.

### 2. Sibling-source identity — the basis for F4-01/F4-11

`diff en/manuals/one-4k/osd.mdx en/manuals/one-4k-oled/osd.mdx` → differs **only** at L5
(`nl_link`) and L27 (the `{/* … */}` comment). Every prose line is shared.

`diff en/manuals/one-4k/controls.mdx en/manuals/one-4k-oled/controls.mdx` → differs only at
L5 (`nl_link`), L10 (product name), L12 (image src/alt), L36 (real text vs `{/* TODO */}`),
L44 (link target). Lines 14, 16, 20, 24, 28, 32, 40 are shared.

`diff` of the EN `## Getting Started` blocks (L8–16) → **no output**.

The same three NL diffs return only the legitimate product-name / image / link / comment
deltas. The corresponding DE diffs return 5 extra prose deltas (controls), 4 extra
(osd) and 6 extra (installation). DE is the only language of the three that drifted.

### 3. Mechanical sweeps — all clean

Run over `de/manuals/{expand,one-4k,one-4k-oled}`:

- **Register (§2).** `\b(Sie|Ihnen|Ihr|Ihre|Ihrem|Ihren|Ihrer|Ihres|Bitte)\b` case-sensitive → **0 hits.**
  Capitalised `Du|Dein|…` → 7 hits, **all sentence-initial** and therefore correct
  (`Dein Browser unterstützt…` ×2, `Dein Computer erkennt…` ×2, `Dein Laptop hat keinen…` ×2,
  `Hinweis: Dein Smartphone…` ×1).
- **Durchkopplung (§3).** `USB-?C zu|USB-C auf [A-Z]|USB [CA]|USB-C Kabel|USB-C Anschluss|HDMI Kabel|HDMI Anschluss|OSD Menü|Mini HDMI` → **0 hits.**
  All chains present are the locked `X-auf-Y-Kabel` form; `3,5-mm-Klinkenanschluss` correct in both controls pages.
- **Counts (§4).** `[0-9]x ` → **0 hits** (all are `2×`, `6×`, `1×`, `3×`).
- **Dashes (§3.6).** `—` → 3 hits, all inside `{/* … */}` comments locked to EN by §7.7 — not body copy. No em dash in any German sentence. `−` is U+2212 everywhere it appears as a button glyph (11 occurrences across 8 files).
- **Double space after a full stop** → 0 hits.
- **Cross-language link leakage.** `\]\(/(en|nl|fr|it)/` in DE → **0 hits**; all 4 internal links resolve under `/de/`.

### 4. Structural parity EN↔DE — 16/16 PASS

Per page, compared counts of: markdown headings, `<img `, bullet items, numbered steps,
`<Note>`, table pipes, and `**…:**` bold run-ins. **Zero mismatches across all 16 pages.**
No dropped step, table row, callout or run-in label anywhere in F4.

### 5. Numeric fidelity EN↔DE — 16/16 PASS

Extracted every digit run from each page (frontmatter and URLs excluded), normalised the
decimal/thousands separator, and multiset-compared EN against DE. **Zero differences.** No
transcription error in any spec table, angle range, timing or voltage.

Locked figures verified individually:

- **`100.000:1` appears in both required places** — `de/manuals/one-4k-oled/index.mdx` L15
  (prose: `…und ein Kontrastverhältnis von 100.000:1 –`) **and** L27 (spec row
  `| **Kontrastverhältnis** | 100.000:1 |`). German period separator per §4/§11; EN writes
  `100,000:1`. Correct.
- **Four-digit figures keep no separator:** `1750 Gramm`, `1450 Gramm`, `1200:1`, `1000:1`,
  `3840 × 2160`, `1920 × 1080`. Correct.
- **`3,5-mm-` compounds** — `### 3,5-mm-Klinkenanschluss` in both `one-4k/controls.mdx` L29
  and `one-4k-oled/controls.mdx` L29; comma decimal, full Durchkopplung, no standalone
  spaced form leaked in. Correct.

### 6. Inch-mark parse hazard (§4.1) — all three contexts correct

- **Frontmatter (`\"`):** `expand/index.mdx` L3 `…erhältlich in 14\" und 15,6\"`;
  `one-4k/index.mdx` L3 and `one-4k-oled/index.mdx` L3 `… 15,6\"`. All three parsed with
  `yaml.safe_load` — **no failures**, no early string termination.
- **JSX (`&quot;`):** the only two `<Tab title=…>` in F4 are `expand/index.mdx` L32/L51 —
  `title="Expand 15,6&quot;"` and `title="Expand 14&quot;"`. Entity preserved; the literal
  `"` was **not** pasted in from §1.2. No build hazard.
- **Markdown (literal `"`):** table cells `| **Größe** | 15,6" |`, `| 14" |`,
  `| **Bildschirmgröße** | 15,6" |`, `| **Produktname** | Screenmate One 4K 15,6" |`, and
  the two `<Note>` prose mentions. Correct form for the context.
- DE applies the comma in **all** positions including frontmatter, correctly avoiding the
  NL defect §4.1 documents (`nl/manuals/one-4k/index.mdx` L3 still reads `15.6\"`).

### 7. `## Erste Schritte` consistency — PASS on the heading, FAIL on the body

Both `one-4k/installation.mdx` L7 and `one-4k-oled/installation.mdx` L7 read exactly
`## Erste Schritte`, per §7.3 and the two flag files. The heading is aligned; the seven
bullets underneath are not — see F4-01 through F4-03. These are the corpus's only two
`## Getting Started` pages, so the pair has no third arbiter.

### 8. Safety chapter — negation and modality intact

All 14 numbered items in `de/manuals/expand/safety.mdx` (= the frozen canonical body,
shared with both one-4k pages) checked against EN item by item. No negation dropped,
inverted or softened:

- L18 `Verwende **keine** Flüssigkeiten oder aggressiven Reinigungsmittel.` (EN `Do not use…`)
- L19 `Berühre das Gerät **nicht** mit nassen Händen und verwende es **nicht** in feuchten Umgebungen.` (both negations preserved)
- L20 `**Lass** den Monitor **nicht** fallen…`
- L12 `Verwende **ausschließlich** das mitgelieferte AC/DC-Netzteil` — exclusivity preserved (EN `Only use…`)
- L16 `Verwende das Gerät **ausschließlich** mit einer 5-V-Stromquelle`
- L15 `…arbeitet mit einem DC-Eingang zwischen 5 V und 20 V (mit einer Toleranz von ±2 V)` — matches the §10.2 trap row exactly (not `operiert auf`)
- L23 `zwischen −20 °C und 60 °C` — U+2212 minus, DIN space before `°C`
- L9 drops "Please" per §2.2 (`Lies die folgenden Hinweise sorgfältig durch, bevor du den Monitor verwendest.`)

`expand/index.mdx` L75 also preserves the rotation warning intact:
`Drehe die Bildschirme **nicht** über die unten angegebenen maximalen Winkel hinaus.`

### 9. Glossary spot-checks that passed

- **§10.5 bold run-ins.** All 6 OSD run-ins (`**Einschalten:**`, `**OSD-Menü öffnen:**`,
  `**Navigieren:**`, `**Auswählen:**`, `**Einstellungen anpassen:**`, `**Zurück:**`),
  `**Taste +:**` / `**Taste −:**`, `**Stromversorgung:**`, `**Konsole anschließen:**`,
  `**HDMI-Gerät anschließen:**`, `**Schritte:**`, `**Linker/Rechter Bildschirm:**`,
  `**Mini-HDMI:**`, `**USB-C-Anschluss:**`, `**+ Helligkeit erhöhen:**`,
  `**− Helligkeit verringern:**`, `**≡ Menütaste:**` — every one matches its locked target.
- **§10.1 callout lead-ins.** `**Wichtig:**` (3), `**Hinweis:**` (2), `**Wichtige Informationen:**` (1),
  `**Willkommen!**` (3) — all correct, and `Important:` is kept distinct from `Note:` as §10.1 requires.
- **§10.1 locked constructions.** `Achte darauf, dass du den richtigen USB-C-Anschluss…`,
  `Brauchst du mehr Strom?`, `Dein Laptop hat keinen USB-C-Anschluss?`,
  `Bildschirm steht auf dem Kopf?`, `Brauchst du mehr Platz?`,
  `Wähle die Variante, die zu … passt.`, `gehe so vor:`, `Sobald beide Verbindungen hergestellt sind`,
  `Geh sorgsam mit deinem Screenmate Expand um`, `Wir empfehlen, das Netzkabel abzuziehen` — all match.
- **§6 OSD.** All 22 ALL-CAPS labels verbatim; menu *values* (`Standard`, `Game`, `Movie`,
  `Text`, `FPS`, `RTS`, `Energy Saving`, `Warm`, `Cool`, `User`, `ON`, `OFF`, `Off`, `Auto`,
  `2084`, `Type-C1`, `Type-C2`, `HDMI`, `4:3`, `WIDE`, `RESET`) untranslated; all six chapter
  headings translated with **no** parenthetical device name — correctly avoiding the NL
  `expand/osd.mdx` one-off (`### 1. Achtergrondverlichting (Backlight)`) that §6.4 names.
- **§7.1/§7.2 frontmatter.** All 16 titles and descriptions match their locked rows, including
  the `Screenmate X – Handbuch` en-dash appositive on all three index pages.
- **§10.3 sentence structure.** Subordinate-clause commas and `um … zu` commas present
  throughout; verb-final in `wenn`/`dass`/`sobald` clauses; no 40-word Schachtelsätze.
- **§7.3/§7.4 headings.** `Lieferumfang`, `Technische Daten`, `Die richtigen Kabel wählen`,
  `Installationsschritte`, `Schutzkappe`, `Anschlussmöglichkeiten`, `Anschlüsse und Tasten`,
  `Bedienung und OSD-Menü`, `Schnellzugriff für Lautstärke und Helligkeit`, `OSD-Sperre`,
  `Erste Schritte`, and the numbered connection-scenario headings — all match locked targets.
- **`docs.json`.** All 16 F4 DE pages are registered (expand 6, one-4k 5, one-4k-oled 5).
  No orphan, no missing entry.
- **Ruling R9 (alt text).** Every `alt` in F4 is fully German; the only non-German tokens are
  DNT (`Screenmate`, product names, `USB-C`, `USB-A`, `HDMI`). The pre-R9 English OSD menu
  names that `de-expand.md` flags on `de/manuals/dual-flip/osd.mdx` do **not** appear in F4.

### 10. Flag-file claims re-verified against the tree

Each "proceeded-with" decision in the three F4 flag files was checked in the shipped files
rather than taken on trust. All hold: `6× Schutzclips` (expand index L25),
`Farbgenauigkeit`/`Farbraum` split (L46/L65), `1920 × 1080` normalised in **both** tabs
(L36/L55), `Größe` not `Bildschirmgröße` in expand (L40/L59), `## Erste Schritte` over NL's
`## Aansluiten`, `hochauflösenden` over NL's `hoogwaardig` (one-4k index L15), `Wichtig:` over
NL's `Let op:`, `den Screenmate` over NL's `de draagbare monitor`, `100 % sRGB`, and both
`{/* … */}` comments byte-identical to their EN source.
