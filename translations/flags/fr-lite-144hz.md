# FR — `lite-144hz` (index, installation, controls, osd)

Task 7-fr / lite-144hz. Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 4. Blocked: 0.

## EN↔NL meaning divergences

- [osd.mdx] EN says the Color Temperature presets are **`User, Warm, or Cool`** (English on-device
  values) / NL says **`Gebruikersinstelling, Warm of Koel`** — NL translated one of the three preset
  values — proceeded-with `choisissez User, Warm ou Cool`. Glossary §7.1 lists `Warm`, `Cool`, `User`
  as device-rendered menu values that stay English, and the standing ruling confirms the presets stay
  EN with NL as the outlier. Worth reporting upstream: the NL page contradicts its own OSD-verbatim
  rule (same divergence already flagged on the IT side).

- [osd.mdx] EN frontmatter `title: "On-Screen Menu (OSD)"` and `## On-Screen Menu Settings` /
  NL frontmatter `title: "Beeldscherminstellingen (OSD)"` and `## Beeldscherminstellingen`
  (= *Display settings* — NL names the chapter after the settings, EN after the menu) —
  proceeded-with `Menu à l'écran (OSD)` / `## Réglages du menu à l'écran`, both locked against the EN
  strings by glossary §9.1 and §9.3. EN is the structural template.

- [osd.mdx] EN says `### 2. Image Modes` / NL says `### 2. Modusopties` (= *mode options*) —
  proceeded-with `### 2. Modes d'image`, the §9.4 locked target for the EN heading.

- [installation.mdx] EN §5 opens "To connect **the Screenmate** to an HDMI device…" / NL opens
  "Om **de draagbare monitor** aan te sluiten…" (= *the portable monitor*) — same referent, different
  noun — proceeded-with `le Screenmate`, following the EN template. Recorded only so a later pass does
  not re-open it.

## Glossary-vs-source notes (no EN/NL conflict — recorded for the reviewer)

- [controls.mdx, osd.mdx] Both EN and NL keep the on-device button name in English
  (`Power & Return Button` / `Power & Return-knop`). Glossary §5.1 and §9.4 nevertheless lock
  `Power & Return Button` → `bouton d'alimentation et de retour`, and the string is **not** in
  `dnt.json` nor in the §7 CAPS token list. Translated per the binding glossary (ruling R8:
  descriptive button names translate naturally), in the `### Bouton d'alimentation et de retour`
  heading and in the `osd.mdx` intro sentence alike. If the physical button is silk-screened
  "Power & Return", the client may want the EN token restored — an asset question, not a translation
  one. Same note was raised on the IT side.

- [index.mdx] Unit spacing in the spec table follows glossary §4/§4.1 (`350&nbsp;cd/m²`,
  `10&nbsp;ms`, `144&nbsp;Hz`, `99&nbsp;%&nbsp;sRGB`) and the resolution is normalised to
  `1920 × 1080` per §4. The dimensions value keeps a plain space before `cm`
  (`35,4 × 22,1 × 1,1 cm`), matching the §4 dimension example `40,6 × 23,7 × 2,5 cm` verbatim.
  This is a visible difference from the IT page (which keeps all closed EN spacing) and matches
  the FR glossary's deliberate divergence note in §4.

- [index.mdx, all pages] `144 Hz` inside the product name `Screenmate Lite 144 Hz` keeps a plain
  space (DNT product name **Lite 144**, §4 "sizes as product variants"); `144 Hz` as a measurement
  (prose refresh rate, spec-table value) takes `144&nbsp;Hz` per §4. Both forms are intentional.

## Proposed glossary additions (§12) — used on these pages, not yet in `glossary-fr.md`

| English | French (used) | Reason |
|---|---|---|
| `General mode` *(controls bold run-in)* | `Mode général` | `controls.mdx` — bold run-in above the scroll-wheel / power-button bullet lists; no §9 or §10.2 row covers it. Mirrors NL `Algemene modus`. |
| `OSD menu mode` *(controls bold run-in)* | `Mode menu OSD` | `controls.mdx` — sibling of the above. `menu OSD` per §2. |
| `Rotate` *(gesture label in a bullet)* | `Rotation` | `controls.mdx` scroll-wheel bullet. Noun, parallel to `Appui court` / `Appui long` (§10.2 turns press gestures into nouns). |
| `picture mode` | `mode d'image` | `osd.mdx` ECO-modes bullet; already implied by §5.4 `picture mode / display mode`, restated here because it is the sub-list lead. |
| `widescreen` *(lowercase prose, not the `WIDE` token)* | `format large` | `osd.mdx` Aspect Ratio bullet — §5.4 row; distinct from the §7.1 device token `WIDE`, which is untouched. |
| `RGB value` | `valeur RVB` | `osd.mdx` Red/Green/Blue bullets. §5.4 locks `RGB values` → `valeurs RVB` (RGB kept only when quoting the on-device menu; this is descriptive prose). |
| `power users` | `utilisateurs exigeants` | `index.mdx` intro. Avoids the anglicism `power users` and the literal `utilisateurs avancés` reads narrower. |
| `connection scenario` | `scénario de connexion` | `installation.mdx` intro — already fixed by the §10 boilerplate row; recorded for completeness. |
