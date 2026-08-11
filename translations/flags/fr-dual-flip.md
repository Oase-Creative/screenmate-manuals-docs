# FR — dual-flip: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-fr (dual-flip: index, installation, controls, osd). `safety.mdx` and
`display-settings.mdx` belong to Task 6 and are covered by `fr-shared.md`.
Phrasing-only differences are deliberately **not** listed. Nothing below is blocking.

## Spec-table field: colour accuracy vs colour coverage

- [fr/manuals/dual-flip/index.mdx, §Caractéristiques techniques] EN says `**Color Accuracy** | 100% sRGB` / NL says `**Kleurdekking**` (= *colour coverage / gamut*) — proceeded-with-`**Précision des couleurs**`
  Glossary §5.4 + §5.6 lock the two concepts to distinct French targets (`Color Accuracy →
  Précision des couleurs`, `Color Gamut → Gamme de couleurs`), so the EN/NL split cannot be
  collapsed silently. EN is the structural template, hence no block.
  **Client note (identical to the DE and IT flags for this same row):** the value `100 % sRGB` is a
  gamut-*coverage* figure, so the NL field name is arguably the technically correct one and the EN
  field name the defect. If the client confirms, the EN page should change to `Color Gamut` and FR
  follows in one edit to `Gamme de couleurs`. The field recurs across the other product index
  pages — worth normalising corpus-wide, not per product.

## Non-flags — checked and dismissed (recorded so a later pass does not re-open them)

- [index.mdx] EN package line `1x USB-C **with** USB-A adapter cable (90 cm)` / NL
  `1x USB-C-**met**-USB-A-adapterkabel` — EN and NL agree, but glossary §5.7 records this row (the
  only "adapter cable" line in the whole EN corpus) as `1x USB-C **to** USB-A adapter cable (90 cm)`
  → **`1 câble adaptateur USB-C vers USB-A (90 cm)`**, and that rendering is binding (§0 precedence
  3, §12 forbids improvising). Not a factual error: `installation.mdx` describes the very same cable
  as "the USB-C **to** USB-A cable", so the `vers` form matches the EN corpus's own second wording
  and §2.1's A→B direction rule. **Cross-language note:** DE (`USB-C-Kabel mit USB-A-Adapter`) and
  IT (`cavo USB-C con adattatore USB-A`) both kept the "with" reading, so FR reads differently
  here by glossary mandate. Worth one client sentence if the three languages are diffed.
- [index.mdx] EN spec field `Size` / NL `Schermgrootte` (= *Screen Size*). Glossary §5.6 lists both
  (`Size → Taille`, `Screen Size → Taille de l'écran`); EN followed → `Taille`. Field-name variance,
  not meaning.
- [index.mdx] EN `Protective case` / NL `Beschermhoes` (= *sleeve*). Glossary §5.1 + §5.7
  deliberately keep the EN case/sleeve split (`case → étui de protection`,
  `sleeve → housse de protection`); EN followed → `Étui de protection`.
- [index.mdx] EN `The Screenmate **uses** a small amount of power…` / glossary §10 boilerplate is
  keyed on `**consumes** a small amount of power…`. Same meaning; the locked French boilerplate
  (`Le Screenmate consomme une faible quantité d'énergie en mode veille. …`) was reused verbatim so
  the string stays byte-identical across all FR products.
- [index.mdx, installation.mdx] Unit spacing: NL locks the closed forms (`100% sRGB`, `5V/2A`), FR
  applies SI/French typography (`100&nbsp;%&nbsp;sRGB`, `5&nbsp;V/2&nbsp;A`) per glossary §4 + §4.1.
  Explicitly **not** an nl↔fr parity defect — see glossary §12 open item 2.
- [installation.mdx] EN `**2× USB-C**` / `**1× USB-C & 1× USB-A & 1× HDMI**` → FR `**2 USB-C**` /
  `**1 USB-C et 1 USB-A et 1 HDMI**`. The count prefix drops its multiplier per glossary §2.1 rule 5
  ("counts drop the `x`") and §9.4 (`2x USB-A and 2x HDMI → 2 USB-A et 2 HDMI`), and `&` → `et` per
  §9.4 (`USB-C + HDMI & USB-A → USB-C + HDMI et USB-A`). This removes U+00D7 entirely from the FR
  installation page — an intentional character-inventory divergence from EN, not an omission.
  Matches IT; DE kept the `×`.
- [installation.mdx] EN callout lead-in `**Important:**` / NL `**Let op:**` (= *Caution*). Glossary
  §6 + §10.1.I give distinct French targets (`Important&nbsp;:` / `Attention&nbsp;:`); EN followed
  as the structural template. Callout-register drift, not meaning.
- [installation.mdx] EN heading `2. One USB-C cable, one HDMI cable, and one USB-A cable` / NL
  `2. 1x USB-C-kabel, 1x HDMI-kabel en 1x USB-A-kabel`. Glossary §9.4 maps both EN variants to
  `2. Un câble USB-C, un câble HDMI et un câble USB-A`. Not a conflict.
- [osd.mdx] NL glosses every ALL-CAPS run-in (`BRIGHTNESS (Helderheid)`, `ECO (ECO-modus)`,
  `SOURCE (Bronselectie)`, `HDR (HDR-modus)`, `ASPECT (Beeldverhouding)`…) while EN gives the bare
  label. Glossary §7 rules the bare-caps form is kept bare — "do **not** add a French gloss that is
  not in the source. Structural parity beats helpfulness" — and names `dual-flip/osd.mdx`
  explicitly. FR therefore keeps `**BRIGHTNESS (0–100)&nbsp;:**`, `**ECO&nbsp;:**`,
  `**ASPECT&nbsp;:**`, `**COLOR TEMP&nbsp;:**`, `**LANGUAGE&nbsp;:**`, `**SOURCE&nbsp;:**`,
  `**LOW BLUE LIGHT&nbsp;:**`, `**RESET&nbsp;:**`, `**HDR&nbsp;:**` unglossed. Deliberate divergence
  from NL practice. The one exception is `**DCR (Dynamic Contrast Ratio)&nbsp;:**`, where §7 locks
  the parenthetical *as* translatable expansion → `**DCR (taux de contraste dynamique)&nbsp;:**`.
- [osd.mdx] NL translates on-device menu **values** (`Standaard, Film, Tekst, Energiebesparing`,
  `Koel`, `Gebruiker`, `AAN`/`UIT`, `Uit`). Glossary §7.1 rules these verbatim-EN, so FR keeps
  `Standard, Game, Movie, Text, FPS, RTS, Energy Saving`, `Warm, Cool, User, Standard`, `ON`/`OFF`,
  `Off, Auto, 2084`, `Type-C1, Type-C2, HDMI`, `4:3`/`WIDE`. NL-side deviation from DNT policy, not
  an EN↔NL meaning difference.
- [osd.mdx, all `<img alt>`] EN `OSD Backlight menu` … `OSD Settings menu` / NL keeps the English
  OSD chapter word and even renames one menu (`OSD-menu Backlight`, `OSD-menu Set` for Settings).
  Per **gate ruling R9** alt text translates fully, so FR uses the §9.4 heading renderings:
  `Menu OSD Rétroéclairage`, `Menu OSD Image`, `Menu OSD Couleur`, `Menu OSD Réglages`,
  `Menu OSD Réinitialisation`, `Menu OSD Autres` — matching the uniformly translated DE and IT
  alts. NL is internally split on this (flip translates, dual-flip does not); that split is the
  client's flag, not FR's.
- [osd.mdx, `COLOR TEMP`] EN `Manually set the RGB values` → FR `réglez manuellement les valeurs
  RVB`. Glossary §5.4 locks `RGB values → valeurs RVB` and keeps `RGB` only "when quoting the
  on-device menu"; the device labels here are the separate `RED` / `GREEN` / `BLUE` bullets, which
  stay verbatim. `RGB` is not a `dnt.json` token. NL likewise wrote a translated form
  (`RGB-waarden`), so this is a glossary application, not an EN↔NL split.
- [osd.mdx, `HDR`] EN `if the connected device supports it` / NL `als het apparaat compatibel is` —
  same condition, phrasing only.
- [osd.mdx, `ASPECT`] EN `Switch the aspect ratio between 4:3 and WIDE` / NL `Pas de
  beeldverhouding aan naar 4:3 of WIDE` — both describe the same two-value toggle. Phrasing only.
- [controls.mdx] EN heading `### M — OSD Menu Button` / NL `### M — OSD-menuknop`. Glossary §9.4
  locks `### M — bouton du menu OSD` (sentence case after the em dash, §3.5). No divergence.
- [controls.mdx] Button engravings `+` and `−` (U+2212) copied verbatim in their leading EN position
  per glossary §7 / §10.2; `−` is **not** swapped for a hyphen. Verified U+2212 present.
