# IT — flip: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it/flip (index, installation, controls, osd). Phrasing-only differences are
deliberately **not** listed here.

## Spec-table field name: Color Accuracy vs Color Gamut

- [it/manuals/flip/index.mdx, §Specifiche tecniche ▸ Tab `Flip 15,6"`] EN says `**Color Accuracy** | 45% NTSC` / NL says `**Kleurdekking**` (= *colour gamut*, the same field name it uses in the `Flip 14"` tab) — proceeded-with-`**Precisione cromatica**`
  These are different concepts, and glossary §5.4 locks them to different targets
  (`Color Accuracy → Precisione cromatica`, `Color Gamut → Gamma cromatica`). The EN page's own
  two tabs disagree: the `Flip 14"` tab labels the identical value `45% NTSC` as `Color Gamut`.
  NL normalised both tabs to the gamut reading; EN did not. EN is the structural template, so the
  IT page mirrors the EN split — `Gamma cromatica` in the 14" tab, `Precisione cromatica` in the
  15,6" tab. **This is an EN-side editorial defect** (`45% NTSC` is a gamut figure, not an
  accuracy figure): recommend the client normalise the EN page to `Color Gamut` in both tabs,
  after which the IT page follows in one edit.

## Non-flags — checked and dismissed (recorded for the reviewer)

- [index.mdx] `**Left** screen:` (EN bolds only the adjective) vs the glossary §9.9 locked run-in
  `**Schermo sinistro:**` / `**Schermo destro:**`, which names `flip/index` explicitly. Italian is
  head-initial, so a position-for-position bold span would give `Schermo **sinistro**:`. The
  glossary is binding and its entry is product-specific, so the whole label is bolded with the
  colon inside, matching the sibling `expand/index` (whose EN already reads `**Left screen:**`).
  Not an EN↔NL conflict — recorded only so the bold-span delta against EN is not read as drift.
- [index.mdx] `## Storing the Screenmate` (EN) vs NL `## Opbergen`. Glossary §9.3 + §11.3 note 8
  already rule this pair: flip takes `Come riporre lo Screenmate`. Section-name variance, not
  meaning.
- [osd.mdx] NL translates on-device preset values (`Standaard, Film, Tekst, Energiebesparing`,
  `Koel`, `Gebruiker`, `AAN`/`UIT`, `Uit`). Glossary §7.2 rules these verbatim-EN, so the IT page
  keeps `Standard, Game, Movie, Text, FPS, RTS, Energy Saving`, `Warm, Cool, User, Standard`,
  `ON`/`OFF`, `Off, Auto, 2084`. Deliberate divergence from NL practice, per the locked ruling.
- [controls.mdx] EN `video transmission only (no power)` vs NL `beeldoverdracht (geen voeding)`
  (NL drops "only"); EN `power supply and video transmission` vs NL's comma-joined list. EN
  followed. Phrasing only.
- [installation.mdx] EN `**Please note:**` vs NL `**Let op:**` — both collapse onto `**Nota:**`
  per glossary §5.5 / §9.9. Only occurrence of `Please note:` in the corpus. Not a conflict.
