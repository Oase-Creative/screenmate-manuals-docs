# FR Lite flags

Task 7-fr / slug `lite`. Pages: index, installation, controls, osd (safety.mdx owned by Task 6).
Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 5. Blocked: 0.

## EN ↔ NL divergences

- [installation.mdx] EN says `**Important:**` / NL says `**Let op:**` (= "Note:") — proceeded-with
  `**Important&nbsp;:**`. Rationale: EN is the structural template, and glossary §6 / §10.1.I keep
  `Important:` → `Important&nbsp;:` distinct from `Note:` → `Remarque&nbsp;:`. The whole sentence is
  locked §10 boilerplate ("**Important&nbsp;:** si l'appareil connecté ne fournit pas une puissance
  suffisante, …"), so the EN lead-in wins. NL collapsed the two lead-ins; French keeps them apart.

- [osd.mdx] EN says `Choose User, Warm, or Cool` — on-device values in English / NL says
  `Kies uit Gebruikersinstelling, Warm of Koel` — two of the three values translated —
  proceeded-with `choisissez User, Warm ou Cool`. Rationale: glossary §7.1 lists `Warm`, `Cool`,
  `User` explicitly as firmware-rendered menu values that stay verbatim English, and the
  orchestrator ruling for this batch names NL the outlier here. The values are what the reader
  physically reads on the panel.

- [osd.mdx] EN says `**Aspect Ratio (16:9 / 4:3):**` — English gloss, no CAPS token / NL says
  `**Aspect Ratio (16:9 / 4:3):**` — left English while every sibling gloss on the same page is
  translated (`Helderheid`, `Contrast`, `Zwartniveau`, `Scherpte`, `Kleurtemperatuur`) —
  proceeded-with `**Format d'image (16:9 / 4:3)&nbsp;:**`. Rationale: §7.2 locks
  `Aspect / Aspect Ratio` → `Format / Format d'image`, and `Aspect Ratio` in title case is a gloss,
  not the CAPS device token `ASPECT` (§7). The `16:9 / 4:3` suffix is a ratio and stays verbatim
  per §7.3; its colons stay tight per §3.4. NL's keep-EN here is an isolated per-file
  inconsistency, not a device-label rule.

- [osd.mdx] EN says `### 2. Image Modes` / NL says `### 2. Modusopties` (= "mode options") —
  proceeded-with `### 2. Modes d'image`, per the §9.4 lock `### 2. Image Modes` →
  `### 2. Modes d'image`. Non-blocking; noted only because the NL heading names the menu
  differently from EN.

- [controls.mdx + osd.mdx] EN says `### Power & Return Button` (and, in `osd.mdx` prose, "Press the
  Power & Return button") / NL says `### Power & Return-knop` — NL keeps the English button name —
  proceeded-with `### Bouton d'alimentation et de retour` and `le bouton d'alimentation et de
  retour`, per glossary §5.1 / §9.4 and coordinator ruling R8 (descriptive button names translate
  naturally; the physical diagram labels this button in Dutch, so no English engraving exists to
  match). **Client eye, not blocking:** if "Power & Return" turns out to be silkscreened on the
  physical unit, this heading would no longer match the hardware — §7 covers only ALL-CAPS OSD
  labels and this string is not one, so the glossary lock stands, but a photo of the button would
  settle it. Same caveat recorded on the DE side.

## Coordinator ruling R9 — alt text (applied)

R9: image `alt` text translates FULLY into French, including OSD menu names and device-menu
references; do not mirror the product's NL alt behaviour.

Audit of all 13 alts on this slug: **no untranslated English was left**. The four `osd.mdx` alts
read `Menu Luminosité de l'OSD` / `Menu Image de l'OSD` / `Menu Température de couleur de l'OSD` /
`Menu Réglages de l'OSD` — one consistent `Menu {nom} de l'OSD` shape, rather than the NL
`OSD-menu {naam}` calque. One naming choice worth recording:

- [osd.mdx] EN says `alt="OSD Image menu"` / NL says `alt="OSD-menu Beeldmodus"` (= "image mode") —
  rendered `Menu Image de l'OSD`, following EN. The alt names the OSD **Image** menu; `Modes
  d'image` is reserved for the *heading* `### 2. Image Modes`, which is a different string, and EN
  itself keeps them distinct ("Image" in the alt, "Image Modes" in the heading).

Non-French tokens remaining in alts are DNT only: `Screenmate`, `Lite`, `USB-C`, `HDMI`, `OSD`,
`PC` (§5.2 / §10.1.G).

## Not flagged (recorded so a later pass does not re-open them)

- [installation.mdx, §5 lead-in] EN says "To connect **the Screenmate** to an HDMI device …" / NL
  says "Om **de draagbare monitor** aan te sluiten …" (= "the portable monitor"). Same referent,
  different noun choice — phrasing, not meaning. Followed EN: `Pour connecter le Screenmate à un
  appareil HDMI …`.
- [controls.mdx] `**General mode**` / `**OSD mode**` and the gesture labels `Short press:` /
  `Long press:` / `Rotate:` appear here as plain-colon list items, not bold `**…:**` run-ins, so
  §10.2 does not apply structurally — but the `&nbsp;` before the colon still does (§3.1, "a colon
  introducing prose"), and the noun forms `Appui court` / `Appui long` from §10.2 were reused so
  the two classes read alike across the corpus.
- Unit spacing on dimensions: `35,4 × 22,1 × 1,1 cm` and `609 grammes` use a **plain** space, while
  `3,5&nbsp;mm`, `350&nbsp;cd/m²`, `10&nbsp;ms`, `60&nbsp;Hz` and `99&nbsp;%&nbsp;sRGB` use
  `&nbsp;`. This follows the glossary's own locked literal strings (`40,6 × 23,7 × 2,5 cm` in §4,
  `(60 cm)` / `(1,2 m)` in §5.7, `1820 grammes` in §5.6) over the general "number + unit symbol"
  row in §4. Deliberate, and identical to how the locked examples are written — do not "normalise"
  it without a glossary change.

## Proposed glossary additions (§12)

Three strings on `controls.mdx` are not covered by any §5 or §9 table. All three are the
sub-labels of the Scroll Wheel / Power & Return sections.

```
Proposed glossary addition:
| General mode (bold sub-label) | Mode général | labels the non-OSD state of a control | — |
| OSD mode (bold sub-label)     | Mode OSD     | labels the in-menu state of the same control; keeps the DNT token OSD | partly ✓ |
| Rotate: (gesture list label)  | Rotation     | noun form, matching §10.2's Appui court / Appui long, which turn Short press / Long press into nouns rather than imperatives | — |
Reason: lite/controls.mdx:28,32,34 and lite-144hz/controls.mdx (same block). The imperative
alternative (`Faites pivoter&nbsp;:`) would clash with the two sibling bullets in the same list,
which §10.2 already locks as nouns.
```
