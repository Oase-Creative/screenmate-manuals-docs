# DE — dual-flip: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-de/dual-flip (index, installation, controls, osd). Phrasing-only differences are
deliberately **not** listed here. Nothing below is blocking.

## Spec-table field name: Color Accuracy vs Color Gamut

- [de/manuals/dual-flip/index.mdx, §Technische Daten] EN says `**Color Accuracy** | 100% sRGB` /
  NL says `**Kleurdekking**` (= *colour gamut*) — proceeded-with-`**Farbgenauigkeit**`
  Glossary §8 locks the two concepts to different German targets (`Color Accuracy →
  Farbgenauigkeit`, `Color Gamut → Farbraum`). EN is the structural template, so the DE page
  mirrors the EN field name. Same EN↔NL split already logged for `it/flip` — if the client
  normalises the EN spec rows, DE follows in one edit.

## Non-flags — checked and dismissed (recorded for the reviewer)

- [index.mdx] EN spec field `Size` vs NL `Schermgrootte` (= *Screen Size*). Glossary §8 lists both
  (`Size → Größe`, `Screen Size → Bildschirmgröße`); EN followed → `Größe`. Field-name variance,
  not meaning.
- [osd.mdx] NL glosses every ALL-CAPS run-in (`ECO (ECO-modus)`, `SOURCE (Bronselectie)`,
  `HDR (HDR-modus)`, `BRIGHTNESS (Helderheid)`) while EN gives the bare label. Glossary §6.2 rules
  the bare-label form unchanged, so DE keeps `**BRIGHTNESS (0–100):**`, `**ECO:**`, `**SOURCE:**`,
  `**HDR:**` with no added gloss. Deliberate divergence from NL practice.
- [osd.mdx] NL translates on-device menu *values* (`Standaard, Film, Tekst, Energiebesparing`,
  `Koel`, `Gebruiker`, `AAN`/`UIT`, `Uit`). Glossary §6.3 rules these verbatim-EN, so DE keeps
  `Standard, Game, Movie, Text, FPS, RTS, Energy Saving`, `Warm, Cool, User, Standard`, `ON`/`OFF`,
  `Off, Auto, 2084`.
- [osd.mdx] Image alt text: EN `OSD Settings menu` / NL `OSD-menu Set` (NL names the on-device
  menu "Set"). Per **gate ruling R9**, alt text translates fully — alt is assistive prose for the
  German reader, and R1 already translates the headings naming the same menus. The six OSD alt
  strings therefore use the §6.4 heading renderings: `OSD-Menü Hintergrundbeleuchtung`,
  `… Bildeinstellungen`, `… Farbeinstellungen`, `… Einstellungen`, `… Zurücksetzen`,
  `… Sonstiges` — matching the uniformly translated IT alts. NL is internally split on this
  (flip translates, dual-flip does not); that split is the client's flag, not DE's.
- [installation.mdx] EN `**Important:**` vs NL `**Let op:**`. Glossary §10.1 → `**Wichtig:**`.
  Callout-label variance, not meaning.
- [installation.mdx] EN heading `2. One USB-C cable, one HDMI cable, and one USB-A cable` vs NL
  `2. 1x USB-C-kabel, 1x HDMI-kabel en 1x USB-A-kabel`. Glossary §7.4 maps both to
  `2. Ein USB-C-Kabel, ein HDMI-Kabel und ein USB-A-Kabel`. Not a conflict.
- [index.mdx, installation.mdx] Unit spacing: NL locks the closed forms (`100% sRGB`, `5V/2A`),
  DE applies DIN 5008 (`100 % sRGB`, `5 V/2 A`) per glossary §4 + §11. Per the decision log this
  is **not** an nl↔de parity defect.
