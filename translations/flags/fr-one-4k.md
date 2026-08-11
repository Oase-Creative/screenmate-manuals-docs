# FR — One 4K: EN↔NL discrepancies

Task 7-fr, slug `one-4k` (pages: index, installation, controls, osd — safety owned by Task 6).
Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 4. Blocked: 0. Phrasing-only differences are deliberately not listed.

## 1. `index.mdx` — "high-resolution" vs "high-quality"

- [fr/manuals/one-4k/index.mdx §Qu'est-ce que le Screenmate One 4K ?] EN says "a **high-resolution**
  second screen" / NL says "een **hoogwaardig** tweede scherm" (= *high-quality*) — these are
  different claims, not two phrasings — proceeded-with-`un second écran **haute résolution**`.
  EN is the structural template and is the factually specific claim for a 3840 × 2160 panel;
  the NL wording reads as a softening. Matches the same ruling logged in `de-one-4k.md`.

## 2. Product-name size string: EN **and** NL both keep `15.6"`, FR converts to `15,6"`

- [fr/manuals/one-4k/index.mdx — frontmatter `description`, the `<Note>` welcome line, the
  `Nom du produit` row and the `Taille de l'écran` row] EN says `Screenmate One 4K 15.6"` /
  NL says `Screenmate One 4K 15.6"` in the frontmatter, the Note and the `Productnaam` row, but
  switches to `15,6 inch` two rows down in `Schermgrootte` (NL is internally inconsistent) —
  proceeded-with-`15,6"` in **all four** positions.
  Glossary §4 locks the comma decimal (`Flip 15.6"` → `Flip 15,6"`) and §9.2 already ships the
  locked FR description `…Screenmate One 4K 15,6\"`. The DNT token is `One 4K`, which the rendering
  preserves verbatim — the size is a measurement, not part of the protected product name. §3.5
  locks the straight `"` prime (escaped `\"` inside the YAML scalar). The `15.6` inside `src=`
  image paths is untouched. This records a deliberate FR divergence from **both** source pages;
  DE and IT took the identical decision (`de-one-4k.md`, `it-one-4k.md`).

## 3. `controls.mdx` — `Menu Button (Power / OSD)`: NL keeps the EN word `Power`, FR translates it

- [fr/manuals/one-4k/controls.mdx §Bouton Menu (alimentation / OSD)] EN says
  `### Menu Button (Power / OSD)` / NL says `### Menu-knop (Power / OSD)` (EN `Power` retained
  inside the parenthetical) — proceeded-with-`### Bouton Menu (alimentation / OSD)`.
  Glossary §9.4 locks this heading verbatim. `Power` here names a *function*, not an engraved
  device string: it is not one of the 22 ALL-CAPS OSD tokens in `dnt.json`, so §7's verbatim scope
  does not reach it. Same ruling as `it-one-4k.md`. Worth a client eyeball if the physical unit is
  silk-screened "Power".

## 4. `controls.mdx` — cross-link label

- [fr/manuals/one-4k/controls.mdx §Bouton Menu (alimentation / OSD)] EN link text is
  `On-Screen Menu` / NL appends the `(OSD)` suffix EN lacks (`Beeldscherminstellingen (OSD)`) —
  proceeded-with-`[Menu à l'écran](/fr/manuals/one-4k/osd)`, EN template followed, href localised
  to `/fr/…` per the shipped `fr/manuals/expand/controls.mdx:17` precedent.

---

## Non-flags — checked and dismissed (recorded for the reviewer)

- `installation.mdx`: EN `## Getting Started` / NL `## Aansluiten` ("Connecting") — the two sources
  name the same seven-bullet block differently, and the NL heading collides semantically with
  `## Aansluitmogelijkheden` immediately below it. Glossary **§9.3 is not silent**: it locks
  `## Getting Started` → **`## Pour commencer`**. EN is the structural template, the bullet content
  is identical, no meaning conflict. **`one-4k-oled/installation.mdx` carries the same section and
  must use the identical `## Pour commencer`.**
- `controls.mdx §Prise casque 3,5 mm`: EN writes the unit closed up (`3.5mm`), NL already spaces
  and comma-fies it (`3,5 mm`). Notation only. Glossary §9.4 lists both EN spacing variants against
  one FR rendering `### Prise casque 3,5&nbsp;mm`; §4.1 supplies the `&nbsp;` between value and
  unit. Byte-identical to the shipped `fr/manuals/lite/controls.mdx:17`.
- `index.mdx §Taille de l'écran`: EN `15.6"` / NL `15,6 inch` (spelled out). Notation only —
  see flag 2; §3.5 prefers the `"` prime.
- `index.mdx §Caractéristiques particulières`: EN `Built-in stand` / NL `Met ingebouwde standaard`
  ("With built-in stand"). Phrasing only → `Support intégré` (§5.1 `stand` → `support`).
- `index.mdx §Couleur`: EN `Black` — rendered `Noir`, extending the §5.6 `Grey` → `Gris` precedent
  (the only other colour value in the corpus). §5.6 lists three changing values and predates this
  slug; `Black` → `Noir` is the same class, not an invention.
- `osd.mdx §Verrouillage de l'OSD`: EN `### OSD Lock` (noun) / NL `### OSD vergrendeld`
  (adjectival, "OSD locked") — §9.4 locks `Verrouillage de l'OSD`. Phrasing only.
- `installation.mdx §5`: EN "To connect the Screenmate to an HDMI device" / NL "Om de draagbare
  monitor aan te sluiten" — coreferential. `installation.mdx §2`: NL adds `eenvoudig` ("easily")
  which EN lacks. `controls.mdx §Port USB-C (alimentation)`: EN "Dedicated power input" /
  NL "Aparte stroominvoer" ("separate"). All phrasing only.
- `osd.mdx:27` MDX comment (`{/* The PDF only documents controls and shortcuts… */}`): NL translated
  its copy; FR keeps the **EN source byte-identical** — the comment is never rendered. Matches the
  DE and IT handling of the same line. (The brief mentioned two such comments for this slug; this
  slug has exactly **one** — `en/manuals/one-4k/osd.mdx:27`. The second lives in `one-4k-oled`.)
- **R9 (`alt` shape `Menu OSD {Section}`) does not apply to this slug** — `one-4k/osd.mdx` contains
  no images at all (`<img>` count: en=0, fr=0). The only alt strings on this slug are the overview
  photo, the ports diagram and the seven connection diagrams, all ordinary descriptive prose
  translated fully per §10.1.G. The seven `installation.mdx` alts are byte-identical to the shipped
  `fr/manuals/lite/installation.mdx` renderings (the EN bodies of the two pages are byte-identical
  after product-name normalisation — verified by diff).

## Proposed glossary addition (§12)

```
| shortcut menu | menu de raccourci (m.) | `ouvre le menu de raccourci de la luminosité` | — |
Reason: en/manuals/one-4k/controls.mdx:48–49 ("opens the brightness shortcut menu", "opens the
volume shortcut menu"); also one-4k-oled/controls.mdx. NL renders it as a compound
("helderheids-snelkoppeling"), which §2 forbids in French. `menu de raccourci` keeps the head noun
first and matches the locked heading `### Raccourcis volume et luminosité` (§9.4).
```
