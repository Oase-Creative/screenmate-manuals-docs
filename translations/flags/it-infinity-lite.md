# IT — infinity-lite: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it/infinity-lite (index, installation, controls). `safety.mdx` and
`display-settings.mdx` belong to Task 6 — see `it-shared.md`. Phrasing-only differences are
deliberately **not** listed here.

## Flags

- [it/manuals/infinity-lite/index.mdx, §Specifiche tecniche] EN says `**Color Gamut** | 120% sRGB` / NL says `**Kleurdekking**` (= colour gamut) — **no conflict, recorded for contrast**: EN and NL agree, so the field renders `Gamma cromatica` per glossary §5.4. Recorded only because the sibling `flip` page carries a real `Color Accuracy` vs `Kleurdekking` conflict (`it-flip.md`); infinity-lite does **not**.

- [it/manuals/infinity-lite/installation.mdx, §5. Regola il supporto + §2. Fissa il supporto principale] EN says `360° rotatable mount` / `360° rotatable support` / NL says `360° draaibare ondersteuning` — proceeded-with-`attacco girevole a 360°`
  Not an EN↔NL meaning conflict — a **glossary gap**. The glossary locks `stand → supporto` and `screen support → sostegno dello schermo`, and both targets are already in use on this page for two *different* physical parts. Rendering "rotatable mount/support" as a third `supporto` would collapse three distinct parts onto one Italian word in adjacent sentences. Proposed glossary addition:

  ```
  Proposed glossary addition:
  | rotatable mount / rotatable support | attacco girevole | the 360° pivot joining screen to stand; kept distinct from `supporto` (stand) and `sostegno` (screen support) | — |
  Reason: en/manuals/infinity-lite/installation.mdx:22,44 — the same page names three different
  parts that would otherwise all render as `supporto`.
  ```

## Cross-product contradiction — multifunction control direction (client question)

- [it/manuals/infinity-lite/controls.mdx, §Pulsante sinistro "Min" / §Pulsante destro "Plus"] EN says left = backlight (brightness), right = volume / NL says `Naar links schakelen – achtergrondverlichting (helderheid)`, `Naar rechts schakelen – volume` — **EN and NL agree within this product** → rendered `Sposta verso sinistra – regola la retroilluminazione (luminosità)` / `Sposta verso destra – regola il volume`.
  **The sibling product contradicts it.** `en/manuals/infinity/controls.mdx:42-43` (and its NL twin) assign the *opposite* directions: `**Press right ("Plus"):** increase the backlight (brightness)` / `**Press left ("Min"):** decrease the volume`. The two products ship what appears to be the same three-button toggle, so at most one of the two pages can be correct on the hardware. Translated faithfully per product; **not** normalised. Pending client question — do not "fix" either Italian page until the client rules on which direction the firmware actually uses.
  (Also note infinity's EN pairs each direction with a single polarity — right *increases* brightness, left *decreases* volume — whereas infinity-lite's EN describes each toggle as adjusting its setting in both directions. Same underlying EN-side inconsistency.)

## Known EN-internal inconsistency — Flipped vs Mirrored (cross-reference)

- `en/manuals/infinity-lite/display-settings.mdx` uses **`Flipped`** (line 18) and **`Mirrored`** (line 54) for the same Windows control on the same page. That page is Task 6's, and the split is already logged in `it-shared.md`; the Italian side mirrors it as `Capovolto` / `Duplicato` per glossary §8.
  **Consequence for this task:** none of my three pages (index, installation, controls) reference the setting, so no rendering choice was needed here. Confirming for the reviewer that the glossary's single locked target per EN term (`Flipped → Capovolto`, `Mirrored → Duplicato`) was applied consistently and that no fourth variant was introduced anywhere in the infinity-lite slug. Recommend the client normalise the EN page to one term; the IT page then follows in one edit.

## Non-flags — checked and dismissed (recorded for the reviewer)

- [index.mdx] `## Package Contents` (EN) vs NL `## Onderdelen overzicht` (= "parts overview"). Glossary §9.3 locks `Contenuto della confezione`. Section-name variance, not meaning.
- [index.mdx] EN `display extension` / NL `schermuitbreiding` — same concept; glossary §9.2 locks the description to `estensione schermo portatile`. The Italian head noun is feminine, so the body copy agrees `è pensata`, not `è pensato`.
- [installation.mdx, §Opzioni di collegamento] EN says `two main connection methods`; NL drops "main" (`twee aansluitmethoden`). EN followed (`due modalità di collegamento principali`). Phrasing only.
- [installation.mdx, §5] EN `finish the installation of the display stand` vs NL `rond de installatie van de schermsteun af` (NL says *screen support*, EN says *display stand*). EN followed → `supporto per schermo`. Sub-part naming drift, not a meaning conflict.
- [controls.mdx, §Pulsante Menu / Selezione / Conferma] EN `Press and hold for **3 seconds** to turn the screen off` vs NL `Houd **3 seconden** ingedrukt om uit te schakelen` (NL drops the object). EN followed. Phrasing only.
- [controls.mdx] NL renames the two toggle headings to describe the gesture (`Naar links schakelen – "Min"`) instead of naming the button (EN `Left "Min" Button`). Glossary §9.4 locks the EN-shaped forms `Pulsante sinistro "Min"` / `Pulsante destro "Plus"`. Heading-shape variance, not meaning.
- [installation.mdx] EN `5V/2A`, `5V`, `20V`, `±2V` closed up throughout; rendered with SI spacing (`5 V/2 A`, `±2 V`) per glossary §4.1 and decision-log item 5. Deliberate, matches every other Italian page.
