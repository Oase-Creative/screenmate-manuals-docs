# DE flip flags

Task 7-de / slug `flip`. Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 3. Blocked: 0.

- [flip/index.mdx] EN says `**Color Gamut**` in the Flip 14" spec tab but `**Color Accuracy**` in the Flip 15.6" tab — two different field names for the identical value `45% NTSC` / NL says `Kleurdekking` (= colour coverage/gamut) in **both** tabs — proceeded-with the EN split: `Farbraum` (14") and `Farbgenauigkeit` (15,6"), per the dual-source rule (EN = structural template) and glossary §8, which lists both field names separately. The sibling `dual-flip` DE page renders its EN `Color Accuracy` row as `Farbgenauigkeit`, so the 15,6" tab stays consistent across products. **Client decision needed:** if the two Flip tabs are meant to describe the same spec (NL assumes they are), the EN source should be normalised to one field name and the DE 14" row changed to match.

- [flip/osd.mdx] EN keeps every on-device menu *value* in English (`Standard, Game, Movie, Text, FPS, RTS, Energy Saving`; `ON`/`OFF`; `Warm, Cool, User, Standard`; `Off, Auto, 2084`) / NL translates them (`Film`, `Tekst`, `Energiebesparing`, `AAN`/`UIT`, `Koel`, `Gebruiker`, `Uit`) — proceeded-with the English values verbatim, per glossary §6.3 ("the device speaks English") and rule 5 of §0. The Flip firmware renders these strings in English, so the NL rendering does not match the hardware; German deliberately follows EN here. Not blocking, and not an nl↔de parity defect.

- [flip/installation.mdx] EN heading says `## Storing the Screenmate` / NL says `## Opbergen` (= "Storage", no object) — proceeded-with `## Den Screenmate verstauen`, the locked glossary §7.3 rendering of the EN heading. Same class of difference in `flip/osd.mdx` frontmatter: EN `title: "On-Screen Menu (OSD)"` / NL `title: "OSD-menu"` — proceeded-with `Bildschirmmenü (OSD)` per glossary §7.1. Both are NL abbreviating an EN heading, not a meaning conflict.

## Formatting divergences applied per glossary (not defects, logged so a reviewer does not "fix" them)

- Resolutions are spaced in DE — `1920 × 1200`, `1920 × 1080` — where EN and NL both write `1920×1200` (glossary §4, "Resolution | `×` with spaces"). Matches the sibling DE `dual-flip` page (`2560 × 1600`).
- DIN 5008 unit spacing: `45 % NTSC` (EN/NL `45% NTSC`) and `5 V/2 A` (EN `5V/2A`, NL `5V/2A`) — glossary §4 and §11, explicitly *not* an nl↔de parity defect.
- `**Please note:**` (the corpus' only occurrence, `flip/installation.mdx`) collapses onto `**Hinweis:**`, the same target as `**Note:**` — glossary §10.1.
- Inch mark, three contexts (§4.1): `&quot;` inside `<Tab title="Flip 15,6&quot;">`, `\"` in frontmatter `description`, literal `"` in the `### Flip 15,6"` heading and spec-table cells.
