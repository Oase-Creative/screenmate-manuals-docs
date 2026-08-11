# IT — Lite: EN↔NL discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it/lite. Phrasing-only differences are deliberately **not** listed here.
No blockers — all three entries below are resolved by a binding glossary ruling.

## OSD preset values: NL translates them, IT keeps them English

- [it/manuals/lite/osd.mdx, §3. Impostazioni colore ▸ Temperatura colore] EN says `Choose User, Warm, or Cool` / NL says `Kies uit Gebruikersinstelling, Warm of Koel` (NL localised `User` → *Gebruikersinstelling* and `Cool` → *Koel*) — proceeded-with-`scegli User, Warm o Cool`
  (glossary §7.2 locks `Warm`, `Cool`, `User` as on-device preset values that render in English on the panel; EN is the structural template and §7.2 is binding, so the NL localisation is not followed. Same ruling silently covers the §2 image-mode presets `Standard / RTS / FPS / Text / Movie / Game`, where NL already keeps EN.)

## `Power & Return` button name: NL keeps the EN device name, IT translates

- [it/manuals/lite/controls.mdx §Pulsante di accensione e ritorno; it/manuals/lite/osd.mdx §Impostazioni del menu a schermo] EN says `Power & Return Button` / NL says `Power & Return-knop` (EN name retained) — proceeded-with-`pulsante di accensione e ritorno`
  (glossary §9.4 locks `Power & Return Button` → `Pulsante di accensione e ritorno`, and §10 rules `&` → `e` in prose and headings. The button carries no engraved English label in the source images — it is not an OSD caps token — so it is not DNT. Applied identically in the heading and in the osd.mdx body reference. Note this makes the IT page diverge from NL on purpose; worth a client eyeball if the physical unit is silk-screened "Power/Return".)

## Backlight spec row

- [it/manuals/lite/index.mdx, §Specifiche tecniche] EN says `**Backlight** | LED` / NL says `**Backlight** | LED` (NL left the field name in English) — proceeded-with-`**Retroilluminazione** | LED`
  (glossary §5.4 + decision-log ruling R1: `Backlight` was removed from `dnt.json` in `12b31e3` and always translates, spec-table field and OSD chapter heading alike. EN↔NL agree textually here; the flag records the deliberate IT divergence from the NL page.)

## Non-flags — checked and dismissed (recorded for the reviewer)

- `installation.mdx §5`: EN `To connect the Screenmate to an HDMI device` / NL `Om de draagbare monitor aan te sluiten` — coreferential, phrasing only.
- `installation.mdx §2`: NL adds `eenvoudig` ("easily") which EN lacks; `index.mdx` NL `Aansluiten gaat via…` vs EN `It connects via…` — phrasing only.
- `osd.mdx`: EN `### 2. Image Modes` vs NL `### 2. Modusopties` ("mode options") — glossary §9.6 locks the EN form → `2. Modalità immagine`. EN is the structural template; no meaning conflict.
- `index.mdx`: EN `Dimensions (folded)` vs NL `Afmetingen ingeklapt` (no parentheses) — punctuation only; EN template followed → `Dimensioni (da chiuso)` per §9.x.
