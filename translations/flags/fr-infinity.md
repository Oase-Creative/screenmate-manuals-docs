# FR — infinity: EN↔NL meaning discrepancies

Task 7-fr / slug `infinity` (index, installation, controls — `safety.mdx` and
`display-settings.mdx` belong to Task 6). Format:
`- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 1. Blocked: 0. Phrasing-only differences are deliberately **not** listed.

## Screen layout: mirrored vs identical

- [fr/manuals/infinity/controls.mdx, §Ports et boutons] EN says the layout **"is mirrored on both
  the left and right screen"** / NL says **"De indeling is identiek op het linker- en rechterscherm"**
  (= *identical*) — these describe two physically different products (a mirrored pair vs two
  identical units) — proceeded-with `La disposition est en miroir sur l'écran gauche et sur l'écran
  droit.` per orchestrator ruling **R10**: EN is the correct side and the NL `identiek` is a probable
  NL-side defect, already client-flagged. DE (`spiegelbildlich`) and IT (`speculare`) resolved the
  same way, so all three new languages agree with EN. **The NL page still says `identiek`** — it is
  the outlier and should be corrected in a separate NL pass.

## Known quirk — mirrored, not fixed (per brief)

- [controls.mdx, §Luminosité et volume] The two multifunction-button gestures are asymmetric in the
  source: right (`"Plus"`) **increases the backlight**, left (`"Min"`) **decreases the volume** —
  two different properties, so the pair does not read as an inverse of each other, and the direction
  convention contradicts the sibling `infinity-lite` page. **EN and NL agree with each other inside
  `infinity`**, so this is not an EN↔NL divergence and was translated faithfully:
  `**Appui vers la droite («&nbsp;Plus&nbsp;»)&nbsp;:** augmenter le rétroéclairage (luminosité).` /
  `**Appui vers la gauche («&nbsp;Min&nbsp;»)&nbsp;:** diminuer le volume.`
  Recorded so a later reviewer does not "fix" it in FR alone. The cross-product contradiction with
  `infinity-lite` is a source-content question for the client.

## Applied decisions worth recording

### In-page anchor retargeted (the corpus' only one)

- [controls.mdx:20] EN links `[On-Screen Menu](#on-screen-menu-osd)` at its own H2
  `## On-Screen Menu (OSD)`. The FR H2 is `## Menu à l'écran (OSD)` (§9.3), so the anchor was
  retargeted to `[Menu à l'écran](#menu-à-lécran-osd)` — the NL precedent, which retargets to
  `#osd-instellingen` for its own heading. **Verified, not assumed:** the target slug was computed
  with `github-slugger` (the slugger `mint` uses, resolved from the installed `mint` npx tree) —
  `"Menu à l'écran (OSD)" → "menu-à-lécran-osd"` (accents preserved, apostrophe and parentheses
  stripped). All 8 FR headings on the page were slugged and the anchor was confirmed to resolve
  against one of them. Same convention as DE (`#bildschirmmenü-osd`, umlaut preserved).

### Proposed glossary addition (§12) — `sticker`

```
Proposed glossary addition:
| sticker | autocollant (m.) | `un **autocollant bleu** / **rouge**` — the coloured port markers on
  the back of each Infinity screen | — |
Reason: en/manuals/infinity/installation.mdx:39,47,48 and en/manuals/infinity/controls.mdx:24,28
(5 occurrences, all inside a `**bold**` run). Not in §5. `autocollant` is the standard French term
for an adhesive label; `étiquette` would suggest a printed spec label rather than a colour marker.
DE used `Aufkleber`, IT `adesivo` — same reading.
```

The word appears **only** in the `infinity` and `infinity-lite` product families, so this is a
small addition; recorded rather than assumed silently.

## Non-flags — checked and dismissed (recorded so a reviewer does not read them as drift)

- [controls.mdx] EN frontmatter `title: "Ports and Controls"` vs NL `"Aansluitingen en knoppen"`
  (= *Ports and Buttons*). §9.1 locks the two EN titles to two different French targets
  (`Ports et commandes` / `Ports et boutons`); EN is the structural template, so the page frontmatter
  is `Ports et commandes` while the page's H2 — EN `## Ports and Buttons` — is `## Ports et boutons`.
  The apparent title/heading mismatch is present in EN too and is intentional.
- [controls.mdx] EN `## On-Screen Menu (OSD)` vs NL `## OSD-instellingen`; EN
  `### Menu / Select / Confirm` vs NL `### Menu / Selectie / Bevestigingsknop`; EN
  `### Brightness and volume` vs NL `### Helderheid en volume aanpassen`. §9.3/§9.4 lock a French
  form for each EN heading (`Menu à l'écran (OSD)`, `Menu / Sélectionner / Confirmer`,
  `Luminosité et volume`). NL abbreviating or expanding an EN heading is section-name variance,
  not meaning.
- [index.mdx] EN `**Protective case**` vs NL `**Beschermhoes**` (Dutch uses one word for both
  *case* and *sleeve*). §5.1/§5.7 explicitly "keep the EN case/sleeve distinction", so the FR line is
  the locked `Étui de protection`. Not a conflict — a gap in NL's vocabulary, not a claim about a
  different item.
- [index.mdx, §Caractéristiques techniques] EN `**Color Gamut**` and NL `Kleurdekking` **agree**
  here (both = gamut) for the value `72% NTSC` → `Gamme de couleurs`. Noted because the sibling
  `flip` page carries a real EN-side Gamut/Accuracy defect (`fr-flip.md`); `infinity` does not.
- [installation.mdx] EN `## Setup` vs NL `## Installatie`, EN `## Storage` vs NL `## Opbergen`,
  EN `### Setup instructions` vs NL `### Set-up instructies`. §9.3/§9.4 locked forms used
  (`## Installation`, `## Rangement`, `### Instructions de montage`). Phrasing.
- [installation.mdx] EN `switch dock (such as the one for the Nintendo Switch)` → FR
  `station d'accueil (comme celle de la Nintendo Switch)` per §5.2; NL kept the English
  `switch-dock`. Deliberate divergence from NL practice, per the locked glossary.

## Formatting divergences applied per glossary (not defects)

- Count markers dropped per §2.1 rule 5, in **both** the package list and the connection bullets:
  EN `2x USB-A to USB-C cable` → `2 câbles USB-A vers USB-C`, and EN `- 2× USB-C` /
  `- 1× USB-C & 1× USB & 1× HDMI` → `- 2 USB-C` / `- 1 USB-C, 1 USB et 1 HDMI`. The `×` sign is
  reserved by §4 for dimensions and resolutions (and the one `3 × ports Mini-HDMI` heading), which
  these bullets are not. **Cross-language note:** DE kept `2×` and the literal `&`; IT dropped `×`
  and used `e` twice. FR additionally renders the three-item bullet as a comma list, matching the
  §9.4 locked enumeration `### 2. 1 USB-C, 1 HDMI et 1 USB-A` rather than repeating `et`. A
  cross-language diff will show all three shapes — none is a defect.
- Straight quotes converted to guillemets per §3.5 and the §10.2 `("Plus")` precedent:
  EN `**"L"** for **Left** and **"R"** for **Right**` → `**«&nbsp;L&nbsp;»** pour **gauche** et
  **«&nbsp;R&nbsp;»** pour **droite**`. The engravings `L` / `R` stay verbatim (§7); `gauche` /
  `droite` are lowercase because they are common adjectives in French, not label nouns.
  **IT kept the straight ASCII quotes** on this line — FR follows its own §3.5, which bans them.
- Resolution spaced — `1920 × 1080` — where EN and NL both write `1920×1080` (§4).
- French unit spacing: `300&nbsp;cd/m²`, `10&nbsp;ms`, `60&nbsp;Hz`, `72&nbsp;%&nbsp;NTSC`,
  `36,1 × 21,6 × 4,5&nbsp;cm` where EN/NL write the closed forms (§4, §4.1). Deliberate divergence
  from the NL pages, flagged as open item 2 in glossary §12.
- Angle degrees take **no** space (§4): `235°`, `90°`, `360°`, `178°`.
- Decimal commas: `15,6"`, `36,1 × 21,6 × 4,5`. The four-digit weight carries no separator:
  `2390 grammes` (§4).
- Locked §10.1.D caption pair reused verbatim: `Placez l'écran sur le support simple` and
  `Le support pivote à 360°`, and the four layout captions
  (`Disposition paysage` / `Disposition portrait` / `Disposition mixte portrait et paysage` /
  `Écrans détachés`) — the *physical arrangement* sense, not the §5.4 `mode paysage` OS-orientation
  sense.
- R9 alt handling: all 25 `alt=` strings translated in full; `src`, `className` and `icon` are
  byte-identical to EN (verified by diff). No OSD-menu alts exist on this product, so the locked
  `Menu OSD {Section}` shape does not apply here.
