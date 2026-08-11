# FR — infinity-lite: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-fr/infinity-lite (index, installation, controls). `safety.mdx` and
`display-settings.mdx` belong to Task 6 — see `fr-shared.md`. Phrasing-only differences are
deliberately **not** listed here.

## Flags

- [fr/manuals/infinity-lite/controls.mdx, §Ports et boutons] EN says `This section provides an overview of **the** physical ports…` / NL says `Deze sectie geeft een overzicht van **de** fysieke aansluitingen…` — **EN and NL agree**, but both differ from the other ten products, whose EN reads `an overview of **all** physical ports`. Glossary §10 locks that recurring sentence to `Cette section présente l'ensemble des ports physiques et des boutons de commande du Screenmate X.` — proceeded-with-`Cette section présente les ports physiques et les boutons de commande du Screenmate Infinity Lite.` (drops `l'ensemble des`, mirroring the EN variant). This is the **only** page in the corpus where the FR sentence deviates from the locked boilerplate, and it does so because the EN source deviates first. If the client would rather normalise, the fix is to restore `l'ensemble des` here and the FR corpus becomes uniform in one edit.

- [fr/manuals/infinity-lite/installation.mdx, §Déplier les écrans] EN says `deploy both extension screens` (plural) / NL says `beide uitbreidingsschermen` (plural) — **EN and NL agree**, so translated faithfully as `les deux écrans d'extension`. Recorded because it contradicts the product itself: `index.mdx` (EN + NL) describes the Infinity Lite as giving **one** extra display, and the whole installation chapter thereafter is singular (`### 3. Mount the screen support`, `release the single screen`). Upstream copy defect shared by EN and NL; **not** silently corrected. The FR page is faithful to the source and will need a one-line edit if the client fixes it.

- [fr/manuals/infinity-lite/installation.mdx, §2. Fixer le support principal + §5. Régler le support] EN says `360° rotatable mount` / `360° rotatable support` / NL says `360° draaibare ondersteuning` — proceeded-with-`fixation rotative à 360°`
  Not an EN↔NL meaning conflict — a **glossary gap**. Glossary §5.1 locks `stand → support`, `screen stand / single screen stand → support d'écran / support pour écran unique` and `bracket → support de fixation`; all three targets are already used on this page for three different physical parts. Rendering "rotatable mount/support" as a fourth `support` would collapse distinct parts onto one French word in adjacent sentences. Proposed glossary addition:

  ```
  Proposed glossary addition:
  | rotatable mount / rotatable support | fixation rotative (f.) | the 360° pivot joining screen to stand; kept distinct from `support` (stand) and `support d'écran` (screen support) | — |
  Reason: en/manuals/infinity-lite/installation.mdx:22,44 — the same page names four different
  parts that would otherwise all render as `support`.
  ```

- [fr/manuals/infinity-lite/index.mdx, §Qu'est-ce que le Screenmate Infinity Lite&nbsp;?] EN says `plug-and-play` / NL says `plug-and-play` — **EN and NL agree**; the term is absent from `translations/dnt.json` and from glossary §5. Proceeded-with-`plug-and-play` (unchanged, hyphenated), which is the standard form in French consumer-hardware copy and matches the NL precedent. Proposed glossary addition:

  ```
  Proposed glossary addition:
  | plug-and-play | plug-and-play | keep EN, always hyphenated; standard in FR tech copy | ✓ |
  Reason: en/manuals/infinity-lite/index.mdx:16 — only occurrence in the corpus.
  ```

## Cross-product contradiction — multifunction control direction (client question)

- [fr/manuals/infinity-lite/controls.mdx, §Bouton «&nbsp;Min&nbsp;» gauche / §Bouton «&nbsp;Plus&nbsp;» droit] EN says left = backlight (brightness), right = volume / NL says `Naar links schakelen – achtergrondverlichting (helderheid)`, `Naar rechts schakelen – volume` — **EN and NL agree within this product** → rendered `Basculement vers la gauche – règle le rétroéclairage (luminosité).` / `Basculement vers la droite – règle le volume.`
  **The sibling product contradicts it.** `en/manuals/infinity/controls.mdx` (and its NL twin) assign the *opposite* directions: `**Press right ("Plus"):** increase the backlight (brightness)` / `**Press left ("Min"):** decrease the volume`. The two products ship what appears to be the same three-button toggle, so at most one of the two pages can be correct on the hardware. Translated faithfully per product; **not** normalised. Pending client question — do not "fix" either French page until the client rules on which direction the firmware actually uses.
  (Also note infinity's EN pairs each direction with a single polarity — right *increases* brightness, left *decreases* volume — whereas infinity-lite's EN describes each toggle as adjusting its setting in both directions. Same underlying EN-side inconsistency.)
  **Register note:** the gesture is rendered as a noun (`Basculement vers la …`), not an imperative, matching the locked nominal treatment of the sibling product's run-ins in glossary §10.2 (`**Press right ("Plus"):**` → `**Appui vers la droite («&nbsp;Plus&nbsp;»)&nbsp;:**`). The EN en dash `–` (U+2013) is copied through unchanged.

## Known EN-internal inconsistency — Flipped vs Mirrored (cross-reference)

- `en/manuals/infinity-lite/display-settings.mdx` uses **`Flipped`** (line 18) and **`Mirrored`** (line 54) for the same Windows control on the same page. That page is Task 6's, and the split is already logged in `fr-shared.md`; glossary §8 maps **both** EN terms to the single French rendering `Paysage (inversé)`, and the shipped FR page uses it in both positions (lines 17 and 53 — verified).
  **Consequence for this task:** none of my three pages (index, installation, controls) reference the setting, so no rendering choice was needed here. Confirming for the reviewer that no fourth variant was introduced anywhere in the infinity-lite slug and that the FR page is self-consistent where the EN page is not. Recommend the client normalise the EN page to one term; the FR page then needs no change at all, since both EN terms already resolve to the same French string.

## Non-flags — checked and dismissed (recorded for the reviewer)

- [index.mdx] EN `## Package Contents` vs NL `## Onderdelen overzicht` (= "parts overview"). Glossary §9.3 locks `Contenu de l'emballage`. Section-name variance, not meaning.
- [index.mdx] EN `display extension` / NL `schermuitbreiding` — same concept; glossary §9.2 locks the description to `extension d'écran portable`. The French head noun is feminine, so the body copy agrees `est une extension … qui se monte`, while the following sentence resumes with masculine `Il` for `le Screenmate Infinity Lite` per §2.2.
- [index.mdx] EN `more screen real estate on the go` / NL `meer werkruimte` (= *more workspace*) — rendered `plus d'espace à l'écran en déplacement`, reusing the locked §6 pairs `Want more on-screen space? → Besoin de plus d'espace à l'écran` and `on the go → en déplacement`. Semantic overlap, not a conflict.
- [index.mdx] EN spec row `**Color Gamut** | 120% sRGB` / NL `**Kleurdekking**` — EN and NL agree; §5.6 locks `Gamme de couleurs`. (The sibling `flip` page carries a real `Color Accuracy` vs `Kleurdekking` conflict — see `fr-flip.md`; infinity-lite does **not**.)
- [installation.mdx, §Options de connexion] EN says `two main connection methods`; NL drops "main" (`twee aansluitmethoden`). EN followed (`deux principales méthodes de connexion`). Phrasing only.
- [installation.mdx, §5] EN `finish the installation of the display stand` vs NL `rond de installatie van de schermsteun af` (NL says *screen support*, EN says *display stand*). EN followed → `support d'écran`. Sub-part naming drift, not a meaning conflict.
- [controls.mdx, §Bouton Menu / Sélection / Confirmation] EN `Press and hold for **3 seconds** to turn the screen off` vs NL `Houd **3 seconden** ingedrukt om uit te schakelen` (NL drops the object). EN followed → `pour éteindre l'écran`. Phrasing only.
- [controls.mdx] NL renames the two toggle headings to describe the gesture (`Naar links schakelen – "Min"`) instead of naming the button (EN `Left "Min" Button`). Glossary §9.4 locks the EN-shaped forms `Bouton «&nbsp;Min&nbsp;» gauche` / `Bouton «&nbsp;Plus&nbsp;» droit`. Heading-shape variance, not meaning.
- [controls.mdx] EN `Status LED` / NL `Statusindicator`. §5.1 locks `indicator light / status LED → voyant lumineux / voyant d'état` and the heading `### LED Indicator → ### Voyant LED`. Both applied; the heading and the body line intentionally use different French nouns because the EN does too.
- [index.mdx, installation.mdx] EN `5V/2A`, `5V`, `20V`, `±2V`, `300 cd/m²`, `10 ms`, `60 Hz`, `120% sRGB` closed up throughout; rendered with SI spacing (`5&nbsp;V/2&nbsp;A`, `±2&nbsp;V`, `300&nbsp;cd/m²`, `120&nbsp;%&nbsp;sRGB`) per glossary §4 and §4.1. Deliberate divergence from EN/NL, matches every other French page.
- [index.mdx] `1920×1080` normalised to `1920 × 1080` (§4, resolutions row); `36.2 × 20.9 × 1.6 cm` → `36,2 × 20,9 × 1,6 cm` and `1261 grams` → `1261 grammes` with a **plain** space before `cm`/`grammes`, matching the locked forms in §4 and §5.7 and the shipped `fr/manuals/{lite,dual-flip}/index.mdx` precedent.
