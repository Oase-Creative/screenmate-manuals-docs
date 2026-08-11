# FR — Expand: EN↔NL discrepancies

Task 7-fr, slug `expand`. Pages: `fr/manuals/expand/{index,installation,controls,osd}.mdx`
(`safety.mdx` and `display-settings.mdx` belong to Task 6 — see `fr-shared.md`).

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 2. Blocked: 0.

## Meaning-level divergences

- [index.mdx, §Contenu de l'emballage] EN says `**6x protective clips**` (clips, plural) /
  NL says `**6x beschermkap**` (= protective **cap**, singular) — proceeded-with
  `**6 clips de protection**`. EN is the structural and semantic template, and glossary §5.1
  locks `protective clips → clips de protection` and `protective cap → capuchon de protection`
  as two distinct Expand parts — the cap has its own `## Capuchon de protection` chapter in
  `installation.mdx`, so NL is using one Dutch word for two different components. The NL line
  is also internally odd (quantity 6 with a singular noun). **Client should confirm** whether
  the box contains 6 clips or 6 caps; the same flag was raised independently on the DE and IT
  Expand pages.

- [index.mdx, §Caractéristiques techniques] EN labels the `72% NTSC` row `**Color Accuracy**`
  in the `Expand 15,6"` tab but labels the equivalent `45% NTSC` row `**Color Gamut**` in the
  `Expand 14"` tab / NL flattens both to `**Kleurdekking**` (= colour coverage / gamut) —
  proceeded-with the EN distinction: `**Précision des couleurs**` (15,6") and
  `**Gamme de couleurs**` (14"), per glossary §5.6. EN is the structural template so its field
  names are mirrored, which means the FR page carries two different field names for one kind of
  measurement. **EN-side defect worth raising upstream:** an `% NTSC` figure is a gamut value,
  not an accuracy value; the 15,6" row should read `Color Gamut`, after which FR follows in a
  one-cell edit. A client flag already exists for this.

## Checked and dismissed — recorded so a later pass does not re-open them

- [installation.mdx] `alt="Installation steps 1 through 6"` names six steps but the list has
  only **five**. EN and NL (`Installatiestappen 1 tot en met 6`) share the mismatch, so it is an
  upstream source defect, not an EN↔NL conflict. Mirrored faithfully as
  `Étapes d'installation 1 à 6` per the orchestrator instruction; an existing client flag covers
  it. If the source image is ever renumbered, all four language alts change together.
- [installation.mdx] EN heading `## Installation Steps` / NL `## Installatie instructies`
  (= Installation *Instructions*). Glossary §9.3 locks both EN variants separately
  (`Étapes d'installation` / `Instructions d'installation`); EN followed. Heading-name drift,
  not a meaning conflict.
- [installation.mdx, step 4] EN `Press the button **again** to slide the stand back in` / NL
  omits "again" — rendered `Appuyez de nouveau sur le bouton`. Omission, not a contradiction.
- [installation.mdx, §2 `<Note>`] EN splits "The USB-A port on your laptop works well for this."
  into its own sentence; NL merges it into the preceding clause. Same content, EN sentence
  structure followed.
- [osd.mdx] EN `## Using the OSD` / NL `## Inleiding OSD-functies` (= Introduction to the OSD),
  and EN `### 4. OSD Settings` / NL `### 4. Instellingen (Set)`. Both EN forms are
  glossary-locked (§9.3, §9.4); EN followed. Note §9.3 keeps `Utiliser l'OSD` and
  `Utiliser le menu OSD` deliberately distinct — this page is the former.
- [osd.mdx] NL appends the EN device token to every OSD chapter heading
  (`### 1. Achtergrondverlichting (Backlight)`); EN does not. Glossary §7 ("Headings are not
  caps labels") forbids inventing the gloss, so all six FR headings are bare.
- [osd.mdx] EN `Adjust the screen brightness (0–100)` / NL `Instelbaar van 0 tot 100`
  (= adjustable from 0 to 100). Same instruction, different phrasing; EN followed per §7.3.
- [controls.mdx] EN link text `[On-Screen Menu]` / NL `[OSD-menu]` — EN followed
  (`[Menu à l'écran]`, glossary §9.1). Internal `href` re-pointed to `/fr/…` per the
  language-first path architecture, matching the DE and IT Expand pages.
- [index.mdx] NL spec tables drift internally (`Schermgrootte | 15,6 inch` vs `Grootte | 14"`,
  `Contrastverhouding` vs `Contrast ratio`). NL-internal formatting drift, no conflict with EN.

## Deliberate divergences from the EN/NL source (glossary-mandated, not defects)

- **Resolution normalised** to `1920 × 1080` in **both** tabs. EN writes it spaced in the 15,6"
  tab and unspaced (`1920×1080`) in the 14" tab, and NL copies that inconsistency; glossary §4
  locks `×` with spaces. Purely typographic.
- **French unit spacing** (§4, §4.1): `72&nbsp;%&nbsp;NTSC`, `5&nbsp;V/2&nbsp;A`,
  `300&nbsp;cd/m²`, `6&nbsp;mm`, `2,5&nbsp;cm`, `25&nbsp;ms`, `60&nbsp;Hz`. This deliberately
  diverges from the EN source's closed forms and from the NL lock — do **not** report it as an
  nl↔fr parity defect (glossary §12, open item 2).
- **Counts drop the `x`** (§4): EN `2x USB-C to USB-C cables` → `2 câbles USB-C vers USB-C`;
  the connection-list bullet `1x USB-C & 1x USB-A & 1x HDMI` → `1 USB-C, 1 USB-A et 1 HDMI`,
  matching the locked heading form in §9.4 (`### 2. 1 USB-C, 1 HDMI et 1 USB-A`).
- **OSD image `alt` text is fully French** per orchestrator ruling **R9**, including the menu
  names: `Menu Rétroéclairage de l'OSD`, `Menu Image de l'OSD`, `Menu Couleur de l'OSD`,
  `Menu Réglages de l'OSD`, `Menu Réinitialisation de l'OSD`, `Menu Autres de l'OSD`. This
  matches the already-committed `fr/manuals/lite/osd.mdx` pattern (`Menu Luminosité de l'OSD`).
- **Gloss + CAPS label OSD style** (`**Luminosité (BRIGHTNESS)&nbsp;:**`) mirrors this product's
  EN source per §7. Sibling FR products whose EN source uses the bare-caps style keep that style
  instead — the divergence between FR pages is correct, not a consistency defect.
