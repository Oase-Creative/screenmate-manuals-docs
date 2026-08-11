# IT — One 4K: EN↔NL discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it/one-4k (pages: index, installation, controls, osd — safety owned by Task 6).
Phrasing-only differences are deliberately **not** listed here.
No blockers — both entries below are resolved by a binding glossary ruling.

## Product-name size string: EN **and** NL both keep `15.6"`, IT converts to `15,6"`

- [it/manuals/one-4k/index.mdx, §Specifiche tecniche ▸ Nome del prodotto] EN says `Screenmate One 4K 15.6"` / NL says `Screenmate One 4K 15.6"` (NL left the period even though it writes `15,6 inch` two rows down) — proceeded-with-`Screenmate One 4K 15,6"`
  (glossary §4.5 is explicit: the size is a **measurement**, not part of the protected product name, so it converts — the worked example `Screenmate Panorama 15.6"` → `Screenmate Panorama 15,6"` is the exact analogue. §4.2's defect grep makes any surviving `\d\.\d` in Italian body copy a defect, and `15.6` is not in the §4.3 structural whitelist. The DNT token from `dnt.json` is `One 4K`, which the rendering preserves verbatim. EN↔NL agree textually here; this flag records the deliberate IT divergence from **both** source pages. Same class as the `Backlight` spec-row entry in `it-lite.md`. Applied consistently: frontmatter `description`, the `<Note>` welcome line, the `Nome del prodotto` row and the `Dimensioni schermo` row all read `15,6"`; the `15.6` inside `src=` image paths is untouched.)

## `Menu Button (Power / OSD)`: NL keeps the EN word `Power`, IT translates it

- [it/manuals/one-4k/controls.mdx §Pulsante Menu (accensione / OSD)] EN says `### Menu Button (Power / OSD)` / NL says `### Menu-knop (Power / OSD)` (EN `Power` retained inside the parenthetical) — proceeded-with-`### Pulsante Menu (accensione / OSD)`
  (glossary §9.4 locks `Menu Button (Power / OSD)` → `Pulsante Menu (accensione / OSD)`. `Power` here names a *function*, not an engraved device string — it is not one of the 22 ALL-CAPS OSD tokens in `dnt.json`, and §7.1's verbatim scope does not reach it. Directly parallel to the `Power & Return Button` ruling already logged in `it-lite.md`. Note this makes the IT page diverge from NL on purpose; worth a client eyeball if the physical unit is silk-screened "Power".)

## Non-flags — checked and dismissed (recorded for the reviewer)

- `installation.mdx`: EN `## Getting Started` / NL `## Aansluiten` ("Connecting") — the two sources name the same seven-bullet section differently. Glossary §9.3 locks the EN form → `Per iniziare`; EN is the structural template, content is identical, no meaning conflict. Same class as the `2. Image Modes` / `Modusopties` non-flag in `it-lite.md`. (This is the corpus's only `Getting Started` section outside `one-4k-oled`, so `Per iniziare` is established here for the first time.)
- `controls.mdx §3.5mm Headphone Jack`: EN writes the unit closed up (`3.5mm`), NL already spaces and comma-fies it (`3,5 mm`). No meaning conflict — §4.1 (space between value and unit) plus §9.4 give `Jack per cuffie da 3,5 mm`, matching the rendering already shipped in `it/manuals/lite/controls.mdx` and `it/manuals/lite-144hz/controls.mdx`.
- `index.mdx §Dimensioni schermo`: EN `15.6"` / NL `15,6 inch` (spelled out). Notation only; §4.4 prefers the `"` prime in spec tables → `15,6"`.
- `controls.mdx` cross-link: EN link text `On-Screen Menu` / NL `Beeldscherminstellingen (OSD)` (NL appends the `(OSD)` suffix EN lacks). EN template followed → `Menu a schermo`, href localised to `/it/manuals/one-4k/osd` per the `it/manuals/expand/` precedent.
- `osd.mdx`: EN `### OSD Lock` (noun) / NL `### OSD vergrendeld` (adjectival, "OSD locked") — §9.4 locks `Blocco dell'OSD`. Phrasing only.
- `installation.mdx §5`: EN `To connect the Screenmate to an HDMI device` / NL `Om de draagbare monitor aan te sluiten` — coreferential, phrasing only (identical to the `it-lite.md` dismissal).
- `installation.mdx §2`: NL adds `eenvoudig` ("easily") which EN lacks. `index.mdx §Caratteristiche speciali`: EN `Built-in stand` / NL `Met ingebouwde standaard` ("With built-in stand"). `controls.mdx §Porta USB-C (alimentazione)`: EN `Dedicated power input` / NL `Aparte stroominvoer` ("separate"). All phrasing only.
- `osd.mdx` MDX comment `{/* The PDF only documents controls and shortcuts… */}`: NL translated its copy, IT leaves the EN verbatim per §10 (comments are never rendered). Not a meaning difference.
