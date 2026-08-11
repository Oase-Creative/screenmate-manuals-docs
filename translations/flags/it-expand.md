# IT — Expand: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it (`it/manuals/expand/{index,installation,controls,osd}.mdx`).
Phrasing-only differences are deliberately **not** listed here.

## Package contents — "protective clips" vs "beschermkap" (protective cap)

- [it/manuals/expand/index.mdx, §Contenuto della confezione] EN says `6x protective clips` / NL says `6x beschermkap` (= protective **cap**, singular noun) — proceeded-with-`6 clip protettive`
  (EN is the structural/semantic template and the glossary locks `protective clips → clip protettive` (§5.1). The NL line is also internally odd: the quantity is 6 but the noun is singular. Note the same page's installation sibling has a separate `## Protective Cap` / `## Beschermkap` section for a *different* part (`cappuccio protettivo`), so NL uses one word for two distinct components. Client should confirm whether the box contains 6 clips or 6 caps.)

## Spec table — "Color Accuracy" vs "Kleurdekking" (colour coverage / gamut)

- [it/manuals/expand/index.mdx, §Specifiche tecniche ▸ tab `Expand 15,6"`] EN says `Color Accuracy | 72% NTSC` / NL says `Kleurdekking | 72% NTSC` (= colour **coverage** = colour gamut) — proceeded-with-`Precisione cromatica`
  (Glossary §5.4 locks `Color Accuracy → Precisione cromatica` and `Color Gamut → Gamma cromatica`; EN is the structural template so its field name is followed. **EN-side defect worth raising:** an `% NTSC` figure is a *gamut* value, not an accuracy value, and the 14" tab of the same table labels the identical kind of value `Color Gamut`. The IT page therefore carries two different field names for one measurement, faithfully mirroring EN. Recommend the client normalise the EN 15,6" row to `Color Gamut`, after which IT follows in one edit.)

## Non-flags — checked and dismissed (recorded for the reviewer)

- [installation.mdx] `alt="Installation steps 1 through 6"` names six steps but the list has five. EN and NL (`Installatiestappen 1 tot en met 6`) share the mismatch, so it is an upstream source defect, not an EN↔NL conflict. Mirrored faithfully as `Fasi di installazione da 1 a 6`; already covered by an existing client flag.
- [installation.mdx] EN heading `## Installation Steps` / NL `## Installatie instructies` (= Installation *Instructions*). Glossary §9.3 locks both EN variants separately (`Fasi di installazione` / `Istruzioni di installazione`); EN followed. Heading-name drift, not a meaning conflict.
- [installation.mdx step 4] EN `Press the button **again** to slide the stand back in` / NL omits "again". EN is more specific; rendered `Premi di nuovo il pulsante`. Omission, not a contradiction.
- [osd.mdx] EN `## Using the OSD` / NL `## Inleiding OSD-functies` (= Introduction to the OSD), and EN `### 4. OSD Settings` / NL `### 4. Instellingen (Set)`. Both EN forms are glossary-locked (§9.3, §9.6); EN followed.
- [osd.mdx] NL appends the EN device token to every OSD chapter heading (`### 1. Achtergrondverlichting (Backlight)`); EN does not. Per §7.2.1 the parenthetical is optional and §7.3 gives EN structural parity precedence — omitted on the IT page for all six headings.
- [osd.mdx] EN `Adjust the screen brightness (0–100)` / NL `Instelbaar van 0 tot 100`. Same instruction, different phrasing; EN followed per glossary §7.3's worked examples.
- [index.mdx] NL spec tables use `Schermgrootte | 15,6 inch` / `Grootte | 14"` and `Contrastverhouding` / `Contrast ratio` across the two tabs. NL-internal drift over formatting and field naming, no meaning conflict with EN.
- [controls.mdx] EN `description: Overview of ports and control buttons` / NL `Overzicht van poorten en knoppen`. Phrasing only; glossary §9.2 target used.
