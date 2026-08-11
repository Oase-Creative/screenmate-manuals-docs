# DE Expand flags

Task 7-de / slug `expand`. Pages: index, installation, controls, osd
(safety.mdx and display-settings.mdx belong to Task 6).

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 5. Blocked: 0.

- [installation.mdx] EN says `alt="Installation steps 1 through 6"` but the list has only
  **5** numbered steps / NL says `alt="Installatiestappen 1 tot en met 6"` — same
  mismatch — proceeded-with `Installationsschritte 1 bis 6`. Known upstream quirk,
  mirrored deliberately (EN and NL share it; a client flag already exists). If the
  client renumbers the source image, all three language alts change together.

- [index.mdx] EN says `**6x protective clips**` (clips, plural) / NL says
  `**6x beschermkap**` (= protective *cap*, singular) — proceeded-with
  `**6× Schutzclips**`. Glossary §1.1 locks `protective clips → Schutzclips` and
  `protective cap → Schutzkappe` as distinct Expand parts, and `Schutzkappe` already has
  its own chapter in `installation.mdx`. NL's package-contents line looks like a Dutch
  slip, not a spec difference; EN governs.

- [index.mdx] EN says `**Color Accuracy**` in the 15,6" tab but `**Color Gamut**` in the
  14" tab / NL flattens both to `**Kleurdekking**` — proceeded-with the EN distinction:
  `Farbgenauigkeit` (15,6") and `Farbraum` (14"), per glossary §8. EN is the structural
  template and the two fields are genuinely different measures; NL's normalisation was
  not followed.

- [index.mdx] EN writes the resolution `1920 × 1080` (spaced) in the 15,6" tab but
  `1920×1080` (unspaced) in the 14" tab; NL copies the same inconsistency —
  proceeded-with `1920 × 1080` in **both** tabs, per glossary §4 (`Resolution | × with
  spaces`) and the §11 precedent of normalising EN-source inconsistencies in German.
  Purely typographic; no meaning change.

- [index.mdx] EN says `**Size** | 15.6"` / NL says `**Schermgrootte** | 15,6 inch`
  (field renamed to "screen size", unit spelled out) — proceeded-with `**Größe** | 15,6"`,
  per glossary §8 (`Size → Größe`) and §4 ("Inches … do **not** expand to `Zoll`").
  Note the EN 14" tab already uses the bare `Size` field, so EN is self-consistent here.

## Non-flag decisions worth recording

- **OSD headings** are fully translated with **no** parenthetical device name —
  `### 1. Hintergrundbeleuchtung`, not NL's one-off
  `### 1. Achtergrondverlichting (Backlight)`. Glossary §6.4 names this NL file
  explicitly as the per-file inconsistency the German pass must not replicate. All six
  chapter headings follow suit, including `### 4. OSD-Einstellungen` (EN
  `4. OSD Settings`, where NL drifted to `4. Instellingen (Set)`).
- **OSD image alt text is fully German** per orchestrator ruling **R9**:
  `alt="OSD-Menü Hintergrundbeleuchtung"`, `"OSD-Menü Bildeinstellungen"`,
  `"OSD-Menü Farbeinstellungen"`, `"OSD-Menü Einstellungen"`,
  `"OSD-Menü Zurücksetzen"`, `"OSD-Menü Sonstiges"`. NL is internally inconsistent on
  alt text across products and was deliberately not mirrored. **Cross-product note:** the
  already-committed `de/manuals/dual-flip/osd.mdx` still carries the pre-R9 English menu
  names (`alt="OSD-Menü Backlight"`, `"OSD-Menü Image"`, …) — it predates the ruling and
  needs a follow-up sweep by whoever owns that slug. Out of scope for this task.
- **Gloss+label OSD style** (`**Helligkeit (BRIGHTNESS):**`) mirrors this product's EN
  source per §6.2. The sibling `dual-flip` uses the bare-label style
  (`**BRIGHTNESS (0–100):**`) because *its* EN source does — the divergence between the
  two German pages is correct, not a consistency defect.
- **DIN 5008 unit spacing** applied: `5 V/2 A` (EN `5V/2A`), `72 % NTSC` / `45 % NTSC`
  (EN `72% NTSC`). Per glossary §4 and the §11 decision log this deliberately differs
  from the NL lock and must **not** be reported as an nl↔de parity defect.
- **Em dashes → en dashes** (§3.6) in the index product description and the second
  installation `<Note>`.
