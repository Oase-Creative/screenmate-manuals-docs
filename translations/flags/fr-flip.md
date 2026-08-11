# FR — flip: EN↔NL meaning discrepancies

Task 7-fr / slug `flip` (index, installation, controls, osd — `safety.mdx` and
`display-settings.mdx` belong to Task 6). Format:
`- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 1. Blocked: 0. Phrasing-only differences are deliberately **not** listed.

## Spec-table field name: Color Gamut vs Color Accuracy

- [fr/manuals/flip/index.mdx, §Caractéristiques techniques] EN says `**Color Gamut**` in the
  `Flip 14"` tab but `**Color Accuracy**` in the `Flip 15.6"` tab — two different field names for the
  identical value `45% NTSC` / NL says `Kleurdekking` (= *colour coverage / gamut*) in **both** tabs
  — proceeded-with the EN split: `Gamme de couleurs` (14") and `Précision des couleurs` (15,6").
  Glossary §5.4 and §5.6 lock the two EN field names to two different French targets
  (`Color Gamut → Gamme de couleurs`, `Color Accuracy → Précision des couleurs`), and the
  dual-source rule makes EN the structural template. NL normalised both tabs to the gamut reading;
  EN did not. **This is an EN-side editorial defect** (`45% NTSC` is a gamut figure, not an accuracy
  figure): recommend the client normalise the EN page to `Color Gamut` in both tabs, after which the
  FR 15,6" row changes in one edit. Same flag already raised on the DE and IT pages
  (`de-flip.md`, `it-flip.md`) — resolve all three together.

## Non-flags — checked and dismissed (recorded so a reviewer does not read them as drift)

- [index.mdx] EN bolds only the adjective — `- **Left** screen: 0° – 245°` — whereas glossary §10.2
  locks the run-in `**Left screen:**` → `**Écran gauche&nbsp;:**` and scopes that entry explicitly to
  `dual-flip/index` and `expand/index`, **not** `flip/index`. Flip's EN construction is therefore out
  of scope for §10.2, so the FR page mirrors EN's emphasis placement position-for-position with
  French head-initial word order: `Écran **gauche**&nbsp;:` / `Écran **droit**&nbsp;:`. Verified
  MDX-safe (the closing `**` is preceded by a letter and so is right-flanking; the §3.2 hazard only
  fires on whitespace *inside* a delimiter). Not an EN↔NL conflict.
- [index.mdx] EN package-contents line `**1× USB-C with USB-A Adapter (90 cm)**` (NL identical in
  meaning) is rendered with the locked §5.7 string `1 câble adaptateur USB-C vers USB-A (90 cm)`,
  which the glossary keys to the sibling `dual-flip` wording `1x USB-C with USB-A adapter cable
  (90 cm)`. Same item, and reusing the locked string keeps the two products identical in FR, per §10.
  The `×` count marker is dropped per §2.1 rule 5.
- [index.mdx] EN heading `## Package Contents` vs NL `## Onderdelen overzicht`, and
  [installation.mdx] EN `## Storing the Screenmate` vs NL `## Opbergen` (= "Storage", no object).
  Glossary §9.3 locks a distinct French heading for each EN form (`## Contenu de l'emballage`,
  `## Ranger le Screenmate`); NL abbreviating an EN heading is section-name variance, not meaning.
  Same class: [osd.mdx] EN frontmatter `title: "On-Screen Menu (OSD)"` vs NL `title: "OSD-menu"` —
  proceeded-with `Menu à l'écran (OSD)` per §9.1.
- [osd.mdx] NL translates the on-device menu **values** (`Film`, `Tekst`, `Energiebesparing`,
  `Koel`, `Gebruiker`, `AAN`/`UIT`, `Uit`). Glossary §7.1 rules these verbatim-English because the
  Flip firmware renders them in English, so the FR page keeps `Standard, Game, Movie, Text, FPS,
  RTS, Energy Saving`, `Warm, Cool, User, Standard`, `ON`/`OFF`, `Off, Auto, 2084`. Deliberate
  divergence from NL practice, per the locked ruling — not an nl↔fr parity defect.
- [osd.mdx] EN `Manually set the RGB values` → FR `définissez manuellement les valeurs RVB`, per
  glossary §5.4 (`RGB values | valeurs RVB | French uses RVB; keep RGB only when quoting the
  on-device menu`). The sentence is descriptive prose, not a quoted menu entry, so the carve-out does
  not apply. **This diverges from the DE and IT pages, which keep `RGB`** — correctly, since neither
  language localises the acronym. Not a defect; recorded because a cross-language diff will show it.
- [osd.mdx] R9 alt shape. Flip's six EN OSD alts (`OSD Backlight menu`, `OSD Image menu`,
  `OSD Color menu`, `OSD Settings menu`, `OSD Reset menu`, `OSD Other menu`) are the identical set the
  sibling `dual-flip` page carries, so the FR renderings are byte-identical to
  `fr/manuals/dual-flip/osd.mdx`: `Menu OSD Rétroéclairage`, `Menu OSD Image`, `Menu OSD Couleur`,
  `Menu OSD Réglages`, `Menu OSD Réinitialisation`, `Menu OSD Autres`. **Cross-product note for the
  orchestrator:** `fr/manuals/lite/osd.mdx` chose the other shape for its own (different) alt set —
  `Menu Luminosité de l'OSD`, `Menu Image de l'OSD`, … The FR corpus therefore carries two alt
  patterns. Both are correct French and neither is glossary-locked (§10.1.G is a rule, not a list),
  but if a single shape is wanted corpus-wide, `lite` and `lite-144hz` are the pages to change, not
  `flip`/`dual-flip`.
- [controls.mdx] EN `**Mini HDMI:**` → FR `**Mini-HDMI&nbsp;:**` (hyphenated) even though both EN and
  NL write it unhyphenated. `dnt.json` lists the hyphenated token and glossary §2 states it wins.
- [controls.mdx] EN `video transmission only (no power)` vs NL `beeldoverdracht (geen voeding)`
  (NL drops "only"); EN `power supply and video transmission` vs NL's comma-joined list. EN followed
  as the structural template. Phrasing only.
- [installation.mdx] EN `**Please note:**` vs NL `**Let op:**` — both collapse onto
  `**Remarque&nbsp;:**` per glossary §10.1.I, which documents the deliberate many-to-one merge with
  `**Note:**`. This is the corpus' only occurrence of `Please note:` (flip/installation.mdx:73).
  Not a conflict.

## Formatting divergences applied per glossary (not defects)

- Resolutions are spaced — `1920 × 1200`, `1920 × 1080` — where EN and NL both write `1920×1200`
  (§4, "Resolutions | `×` with spaces").
- French unit spacing: `250&nbsp;cd/m²`, `25&nbsp;ms`, `60&nbsp;Hz`, `45&nbsp;%&nbsp;NTSC`,
  `5&nbsp;V/2&nbsp;A` where EN/NL write the closed forms (§4, §4.1). Deliberate divergence from the
  NL pages, flagged as open item 2 in glossary §12.
- Inch mark, three contexts (§3.5, §10.1.A): `&quot;` inside `<Tab title="Flip 15,6&quot;">`, `\"` in
  the frontmatter `description`, literal `"` in the `### Flip 15,6"` heading and the `15,6"` /
  `14"` spec cells.
- Decimal commas: `15,6"`, `34,5 × 22 × 3,5 cm`, `39 × 23 × 3,5 cm`. Four-digit weights carry no
  separator: `1565 grammes`, `1875 grammes` (§4).
