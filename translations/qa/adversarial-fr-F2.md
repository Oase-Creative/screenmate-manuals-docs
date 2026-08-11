# Adversarial FR review — family F2 (lite, lite-144hz, panorama, manuals-index)

**Branch:** `lang-expansion-de-fr-it` · **Date:** 2026-08-11 · **Reviewer:** adversarial pass (find errors, not confirm quality)

**Scope reviewed (16 files, EN + NL + FR side by side):**
`fr/manuals/lite/{index,installation,controls,osd,safety}.mdx`,
`fr/manuals/lite-144hz/{index,installation,controls,osd,safety}.mdx`,
`fr/manuals/panorama/{index,installation,controls,osd,safety}.mdx`,
`fr/manuals-index.mdx`.

**Reference:** `translations/glossary-fr.md` (all 12 sections, incl. §4.1 spacing ruling R5),
`translations/dnt.json`, commit `d9007f3` (OSD alt-shape unification R9).

**Non-defects excluded per brief and NOT reported below:** Color Temperature presets kept EN;
panorama client-dictated Info cable block; `Bouton d'alimentation et de retour` (R8);
FR-vs-EN/NL unit-spacing divergence (glossary open item 2).

---

## Findings

**Totals: 12 — Major 2, Moderate 5, Minor 5.**

| # | Sev | File : line | Quoted string | Problem | Proposed fix |
|---|---|---|---|---|---|
| 1 | **Major** | `fr/manuals/lite-144hz/installation.mdx:57` | `… ou **une** Nintendo Charging Dock (et non la console Nintendo Switch elle-même) …` | Wrong grammatical gender. `dock` is masculine in French (`le dock`, `un dock`), and §2.2 gives no feminine override for third-party product names. It also directly contradicts the sibling page `fr/manuals/lite/installation.mdx:57`, which writes `un Nintendo Charging Dock` for the byte-identical EN sentence. One of the two is wrong; the feminine one is. | `… ou **un** Nintendo Charging Dock …` |
| 2 | **Major** | `fr/manuals/lite/installation.mdx` ↔ `fr/manuals/lite-144hz/installation.mdx` (11 line pairs — see table below) | see "Divergence inventory" | The two EN pages are **byte-identical in the body** (mechanical diff: the only differing line is `nl_link:`). The FR pages diverge on **11 sentence/alt pairs**. This breaks the cross-product identity the EN corpus has and that §10 exists to preserve ("translate them once and paste the identical French into every product"). It is also a support hazard: two FR pages describe the same procedure in different words for two near-identical SKUs. | Pick one rendering per pair and apply to both files in one commit. Recommended winners marked ✓ in the inventory below. |
| 3 | Moderate | `fr/manuals/lite-144hz/controls.mdx:38` | `- Appuyez pour ouvrir le menu **de** réglages à l'écran (OSD)` | §5.4 locks `settings menu` → **`menu des réglages`**. `menu de réglages` is a glossary violation, and the sibling `fr/manuals/lite/controls.mdx:38` already has the locked form for the identical EN line. | `… ouvrir le menu **des** réglages à l'écran (OSD)` |
| 4 | Moderate | `fr/manuals/lite/installation.mdx:35` | `vous pouvez **connecter** votre téléphone ou votre tablette directement **au** port USB-C du Screenmate` | §5.2 splits the verb by object: `connecter` = establish the link to a *device*, `brancher` = plug into a *port*. The object here is a port, so it takes `brancher … sur`. `fr/manuals/lite-144hz/installation.mdx:35` already applies the rule correctly — lite is the deviant. | `vous pouvez **brancher** votre téléphone ou votre tablette directement **sur le** port USB-C du Screenmate` |
| 5 | Moderate | `fr/manuals/panorama/installation.mdx:28` | `**Attention&nbsp;:** faites attention à vos doigts lorsque vous repliez les écrans…` | Three problems in one line. (a) §6 locks `Watch your fingers` → **`Attention à vos doigts`**; this is a deviation. (b) The *same EN string* is rendered with the locked form at `fr/manuals/panorama/safety.mdx:26` (`Attention à vos doigts lorsque vous repliez ou dépliez les écrans…`) — an intra-product inconsistency for one source string. (c) It produces the stutter "Attention : faites attention…", which is what a French reviewer flags first. The locked form cannot be pasted verbatim here either (it would read "Attention : attention…"), so the callout needs a synonym. | `**Attention&nbsp;:** prenez garde à vos doigts lorsque vous repliez les écrans afin d'éviter tout pincement.` |
| 6 | Moderate | `fr/manuals/lite/safety.mdx:16` **and** `fr/manuals/lite-144hz/safety.mdx:16` | `6. Utilisez **uniquement l'appareil** avec une source d'alimentation de 5&nbsp;V via le câble approprié.` | Restriction scope is misplaced, weakening a safety instruction. EN: "**Only use the device with** a 5V power source" — the restriction is on the *power source*. In the FR word order `uniquement` attaches to `l'appareil`, so it reads "use only the device (and nothing else) with a 5 V source", which is not a restriction at all. Note the file contradicts itself: item 2 (`Utilisez uniquement **l'adaptateur CA/CC fourni**`) and item 8 (`Nettoyez l'écran uniquement **avec un chiffon doux et sec**`) both place `uniquement` immediately before the restricted phrase. | `6. N'utilisez l'appareil **qu'avec** une source d'alimentation de 5&nbsp;V via le câble approprié.` (apply to both files) |
| 7 | Moderate | `fr/manuals/lite/osd.mdx:28,30` ↔ `fr/manuals/lite-144hz/osd.mdx:28,30` | lite: `- **Text&nbsp;:** lisibilité optimale **pour le** texte.` / `- **Game&nbsp;:** optimisé pour **les jeux**.`  ·  144hz: `… lisibilité optimale **du** texte.` / `… optimisé pour **le jeu**.` | The EN OSD bodies are byte-identical across the two products (mechanical diff: only `nl_link` differs). FR diverges on two preset glosses. Additionally, lite's `Game: optimisé pour les jeux` collides with lines 26–27 (`optimisé pour les jeux Real-Time Strategy`, `optimisé pour les jeux First-Person Shooter`) and loses the generic/specific contrast EN keeps with "Optimized for gaming". | Adopt the 144hz forms on both files: `lisibilité optimale du texte.` and `optimisé pour le jeu.` |
| 8 | Minor | `fr/manuals/lite/controls.mdx:32` ↔ `fr/manuals/lite-144hz/controls.mdx:32` | lite: `- Appui court&nbsp;: revenir **en arrière d'une étape**`  ·  144hz: `- Appui court&nbsp;: revenir **d'une étape en arrière**` | EN is identical on both pages (`Short press: go back one step`). Gratuitous divergence. (The neighbouring `**Mode OSD**` / `**Mode menu OSD**` split is *correct* — it mirrors a real EN differentiator, `OSD mode` vs `OSD menu mode`.) | Standardise on `revenir en arrière d'une étape` in both. |
| 9 | Minor | `fr/manuals/lite/index.mdx:15` | `Le Screenmate Lite est un écran portable Full HD **15,6" léger**, conçu pour…` | `léger` is stranded after the inch measurement, so the adjective floats away from its noun and reads like an unedited machine gloss (EN: "a lightweight 15.6" Full HD portable monitor"). The sibling `fr/manuals/lite-144hz/index.mdx:15` handles the same construction cleanly (`un écran portable Full HD léger de 15,6"`). | `… est un écran portable Full HD léger de 15,6", conçu pour…` |
| 10 | Minor | `fr/manuals/panorama/index.mdx:15` | `… avec un seul câble USB-C (ou USB-A + HDMI **en alternative**)` | Meaning softening. EN says `as a fallback`; `en alternative` presents the two paths as equal-rank options. The page's own `### Option 2 — USB-A + HDMI` (installation.mdx:67–69) explicitly frames it as the path *for laptops whose USB-C port does not carry video* — i.e. a fallback, not a free choice. (NL has the same softening — `als alternatief` — so this is inherited, not introduced, but the FR source of truth is EN.) | `(ou USB-A + HDMI en solution de repli)` |
| 11 | Minor | `fr/manuals/panorama/installation.mdx:54` | `Utilisez le long câble blanc pour l'alimentation, et **le court câble noir** pour connecter le Panorama…` | `le court câble noir` is grammatical but unidiomatic: stacking a prenominal `court` in front of a noun that already carries a postnominal colour adjective is not how French describes cables. `le long câble blanc` survives the same structure; `le court câble noir` does not. | `… et le câble noir court pour connecter le Panorama…` (or `le petit câble noir`) |
| 12 | Minor *(systemic, not F2-specific)* | all 16 F2 files, e.g. `fr/manuals/lite/index.mdx:1–5` frontmatter | frontmatter ends at `icon: "book-open"` — no `en_link:` | Glossary §11 grep 13 declares `en_link:` **required on every FR page**, and the language switcher (`ab10152`) resolves the cross-language jump from this key. Every EN page carries `nl_link:` and every NL page carries `en_link:`; no FR page carries either. Verified scope: **62 of 62** FR pages (`fr/manuals/*/*.mdx` + `fr/manuals-index.mdx`) are missing it, so this is a pending global wiring step for the whole FR locale rather than an F2 translation defect — flagged so it is not lost. | Add `en_link: "/en/manuals/{product}/{page}"` to all FR pages in one dedicated commit (out of F2 scope). |

### Divergence inventory for finding 2 (`installation.mdx`, lite ↔ lite-144hz)

EN body diff between the two products: **0 lines**. FR body diff: **11 line pairs**. ✓ marks the recommended surviving form.

| Line | `fr/manuals/lite/installation.mdx` | `fr/manuals/lite-144hz/installation.mdx` |
|---|---|---|
| 13 | ✓ `…ordinateur portable **à l'aide du** câble USB-C vers USB-C.` | `…ordinateur portable **avec le** câble USB-C vers USB-C.` |
| 19 (alt) | ✓ `Connexion USB-C à **l'**ordinateur portable` | `Connexion USB-C à **un** ordinateur portable` |
| 23 (alt) | ✓ `Connexion USB-C à **l'**ordinateur portable avec alimentation supplémentaire` | `…à **un** ordinateur portable avec alimentation supplémentaire` |
| 27 | ✓ `Connectez le Screenmate **à l'aide d'un** câble HDMI…` | `Connectez le Screenmate **via un** câble HDMI…` |
| 31 (alt) | ✓ `Connexion HDMI à **l'**ordinateur portable` | `Connexion HDMI à **un** ordinateur portable` |
| 35a | `vous pouvez **connecter** … directement **au** port USB-C` *(see finding 4 — lite loses here)* | ✓ `vous pouvez **brancher** … directement **sur le** port USB-C` |
| 35b | `un port USB-C **prenant en charge la vidéo**` | ✓ `un port USB-C **compatible vidéo**` *(either is fine; pick one)* |
| 35c | ✓ `ne peuvent pas transmettre **de signal vidéo**` | `ne peuvent pas transmettre **d'image**` *(EN: "can output video" — `signal vidéo` is the §5.4 term)* |
| 37 (alt) | ✓ `Connexion USB-C **au téléphone ou à la tablette**` | `Connexion USB-C **à un téléphone ou une tablette**` |
| 41 (alt) | ✓ `Connexion USB-C **au téléphone ou à la tablette** avec alimentation supplémentaire` | `…**à un téléphone ou une tablette**…` |
| 47 / 59 | ✓ `raccordez-le au moniteur **à l'aide du** câble USB-C vers USB-A.` | `raccordez-le au moniteur **avec le** câble USB-C vers USB-A.` |
| 57 | ✓ `**un** Nintendo Charging Dock` | `**une** Nintendo Charging Dock` *(finding 1 — hard error)* |

---

## Scrutiny evidence

Everything below was actively probed and came back **clean**; recorded so the empty result is auditable rather than assumed.

### 1. Register (§1) — clean

- `grep -nEi '\b(tu|toi|ton|ta|tes)\b'` over all 16 files → **0 hits**.
- Second-person-singular imperative sweep (`Branche|Connecte|Appuie|Vérifie|Ouvre|Choisis|Utilise|Règle|Retire|Clique|Télécharge|Installe|Redémarre|Débranche|Range|Plie|Déplie|Place|Sélectionne|Maintiens|Fais`) → **0 hits**.
- `Assure-toi|-toi\b` → 0. Manual read confirms `vous`/`votre`/`vos` throughout and bare `vous`-imperatives in every numbered step (`Retirez`, `Assurez-vous`, `Branchez`, `Appuyez`, `Placez`, `Positionnez`, `Repliez`, `Saisissez`, `Faites pivoter`).
- No `Veuillez` / `S'il vous plaît` anywhere (§1 locked exception check) → 0 hits. `Please read the following guidelines carefully` is correctly dropped to `Lisez attentivement les consignes suivantes` in all three safety pages.

### 2. French spacing (§3.1, §4.1) — clean

- Glossary grep 2 (`[^ |] [:;!?]( |$)`, plain space before French punctuation) → **0 hits**.
- Custom AST-free scanner walked **every** `:` `;` `!` `?` outside frontmatter in all 16 files and classified each: 13 sites unexplained, all of which are machine-facing (`| :--- | :--- |` table alignment × 6, Tailwind `dark:border-gray-700` × 7). **Zero prose sites lack `&nbsp;`.**
- Every question lead confirmed carrying the entity: `code&nbsp;?`, `Hz&nbsp;?`, `Lite&nbsp;?`, `Panorama&nbsp;?`, `supplémentaire&nbsp;?`, `USB-C&nbsp;?`, `l'envers&nbsp;?`, `d'espace&nbsp;?`, `d'aide&nbsp;?` — 9/9.
- §3.4 carve-out verified: `16:9`, `4:3`, `1000:1`, `https://www.siliconmotion.com/…` all correctly left tight. No "fix the spacing" pass has damaged a ratio.
- Character-level scan for banned code points across all 16 files: **U+202F = 0, literal U+00A0 = 0, U+2019 = 0, U+2018/201C/201D = 0.** Apostrophes are ASCII `'` throughout, per §3.5.
- Straight-quote scan: every `"…"` hit is a YAML frontmatter value or a JSX attribute. **No straight quotes in prose.** Guillemets used correctly and only where required — `«&nbsp;Étendre le Bureau à cet écran&nbsp;»`, `«&nbsp;Paysage (inversé)&nbsp;»` (`panorama/osd.mdx:41,43`), each retaining the EN `**bold**` wrapper per §3.5.

### 3. OSD alt shape `Menu OSD {Section}` (R9 / `d9007f3`) — clean, no stragglers

- Straggler grep `alt="…de l'OSD…"` / `alt="…OSD menu…"` over all F2 files → **0 hits**.
- All 8 OSD screenshot alts in scope enumerated and confirmed on-shape:
  `lite/osd.mdx` 13/22/36/45 and `lite-144hz/osd.mdx` 13/22/36/45 = `Menu OSD Luminosité`, `Menu OSD Image`, `Menu OSD Température de couleur`, `Menu OSD Réglages` — identical strings on both products.
- Checked the trap: `osd.mdx:36` alt is `Menu OSD Température de couleur`, which tracks the **EN alt** (`OSD Color Temperature menu`) and not the H3 heading (`### 3. Réglages de couleur` / `### 3. Color Settings`). That is correct — the alt must mirror the EN alt.
- `panorama/osd.mdx` carries no OSD-menu screenshots (its images are Windows/macOS display-settings captures), so R9 does not apply there; its alts correctly use the `&nbsp;` rule inside the attribute per §10.1.G (`alt="Image 1&nbsp;: réglages Moniteurs de macOS…"`).

### 4. Glossary term compliance (§2, §2.1, §5, §7, §9, §10) — clean

- Cable chain (§2.1): grep 8 (`câble X à|>|/|- Y`) → **0 hits**. Every occurrence uses `câble {A} vers {B}` with A→B order preserved (`câble USB-C vers USB-A`, `câble Mini-HDMI vers HDMI`, `câble USB-A vers USB-C`). Counts drop the `x` per §4 (`1 câble USB-C vers USB-C (1,2 m)`).
- Hyphen-chain compounds (grep 9) → **0 hits**. Unhyphenated connector tokens (grep 10: `USB C|USBC|Mini HDMI`) → **0 hits in prose**; `Mini-HDMI` is hyphenated everywhere including `### 3 × ports Mini-HDMI`, which matches the §9.4 lock character-for-character.
- Untranslated `driver` (grep 11) → 1 hit, and it is inside an image `src` filename (`driver-download-list.png`) — machine-facing, correctly untouched. Body prose uses `pilote` / `pilote d'affichage` throughout (`panorama/installation.mdx:33,35,39`).
- §7 CAPS labels: `RTS`, `FPS`, `ON/OFF`, `Real-Time Strategy (RTS)`, `First-Person Shooter (FPS)` verbatim. §7.3 suffix pattern applied correctly, including the unit-word trap — `**Minuterie OSD (10–60 secondes)&nbsp;:**` (translated `seconds`, kept the range).
- §7.2 gloss vocabulary: `Modes ECO` correctly **plural** on both lite and lite-144hz (the EN `ECO modes` is plural for exactly these two products); `Niveau de noir`, `Netteté`, `Température de couleur`, `Transparence`, `Langue`, `Format d'image` all match.
- `**DCR (taux de contraste dynamique) (ON/OFF)&nbsp;:**` matches the §7 reversed-order rule exactly on both products.
- §10.2 bold run-ins verified against the locked table: `**Alimentation&nbsp;:**` ×4, `**Connexion de la console&nbsp;:**` ×2, `**Connexion de l'appareil HDMI&nbsp;:**` ×2, `**Appui court&nbsp;:**`, `**Appui long&nbsp;:**`, `**Appui long (1 seconde)&nbsp;:**`, `**Étendre votre espace de travail&nbsp;:**` — all byte-match the glossary.
- §10.1.F frozen question leads: `**Écran à l'envers&nbsp;?**` (`panorama/osd.mdx:43`) matches the shipped lock. Grep 17 (pre-`7a96840` glossary forms) → **0 hits**.
- §8 OS-UI labels: `Paramètres d'affichage`, `Étendre le Bureau à cet écran`, `Identifier`, `Orientation de l'affichage`, `Paysage (inversé)`, `Échelle`, `Réglages Système`, `Moniteurs`, `Disposition` — 9/9 correct, `Bureau` capitalised per §5.3.
- §9.1/§9.2/§9.3/§9.4: every frontmatter title, frontmatter description, H2 and H3 in the 16 files cross-checked against the locked tables. Exact matches include `Configuration de l'affichage (système d'exploitation)`, `### 3 × ports Mini-HDMI`, `### Prise casque 3,5&nbsp;mm`, `### Bouton Bas (−)` / `### Bouton Haut (+)` (with U+2212, not a hyphen), `### Bouton Confirmer / Quitter`, `### Précaution lors du pliage`, `### Avant utilisation`, `### Option 1 — USB-C (câble unique)`.
- `fr/manuals-index.mdx` diffed against `en/manuals-index.mdx`: all 11 card titles follow the `Manuel {Product}` lock, the three help cards match §10 verbatim, `## Besoin d'aide&nbsp;?` matches §9.3, the `<Tip>` QR block matches §10, and the `{/* … */}` scaffold comment with its `/en/` href is correctly left English per §10.1.H.

### 5. Numbers, units, calques — clean

- Grep 6 (period decimals) → **0 hits**. Decimal comma applied everywhere: `15,6"`, `3,5 mm`, `1,2 m`, `0,5 m`, `2,8 cm`, `35,4 × 22,1 × 1,1 cm`.
- Resolutions normalised from the EN `1920×1080` to `1920 × 1080` per §4 on all three products.
- Angle degrees correctly take **no** space (`172°`, `360°`) while `°C` correctly takes one (`-20&nbsp;°C`, `60&nbsp;°C`) — the §4 split is applied, not blurred.
- `±2&nbsp;V`, `5&nbsp;V`, `20&nbsp;V`, `65&nbsp;W`, `144&nbsp;Hz`, `60&nbsp;Hz`, `10&nbsp;ms`, `350&nbsp;cd/m²`, `300&nbsp;cd/m²`, `99&nbsp;%&nbsp;sRGB`, `100&nbsp;%&nbsp;sRGB`, `150&nbsp;%` — all carry the entity.
- Four-digit weights carry no separator per §4: `3000 grammes` (panorama), `609 grammes` (lite/lite-144hz). Grep 14 (`100[,.]000`) → 0 (no 5-digit figure exists in F2).
- §6 calque traps swept: `comme par exemple`, `dans les manières`, `prenez bon soin`, `supporte `, `délivre` → **0 hits**. `prend en charge cinq scénarios de connexion`, `ne fournit pas une puissance suffisante`, `comme illustré sur l'image&nbsp;1`, `afin d'éviter tout dommage` all use the locked forms.
- `charge inversée (reverse charging)` (`panorama/installation.mdx:62`) glosses the EN exactly once on the page, per §5.2.

### 6. Structural parity (§0) — clean

- Heading-count parity EN↔FR across all 15 manual pages + `manuals-index` (`grep -c '^#\{1,4\} '`): **0 mismatches**.
- Component parity confirmed by read: `<Note>`, `<Info>`, `<Tip>`, `<CardGroup>`, `<Card>`, `<div className="space-y-4">`, `<img>` all present in the same positions and counts as EN. No component added, dropped or converted.
- All `src`, `href`, `className`, `icon` attributes untouched, including the Dutch-named image paths (`Handleiding%20images`) — correct per §10.1.G.

### 7. Cross-product consistency lite ↔ lite-144hz — mechanically diffed

Ran a normalised diff (product name folded, `src` stubbed) of FR lite vs FR lite-144hz, with the same diff on the EN pair as the baseline for what *should* differ:

| Page | EN body lines differing | FR body lines differing | Verdict |
|---|---|---|---|
| `index` | 2 | 2 | ✅ correct — both are the real 144 Hz differentiators (marketing sentence, refresh-rate spec row) |
| `installation` | **0** | **11** | ❌ finding 2 |
| `controls` | 2 (`OSD mode` → `OSD menu mode` ×2) | 4 | ⚠️ 2 correct (differentiator mirrored as `Mode OSD` → `Mode menu OSD`), 2 gratuitous → findings 3 and 8 |
| `osd` | **0** | **2** | ❌ finding 7 |
| `safety` | **0** | **0** | ✅ byte-identical, correct |

Differentiators independently verified as **correct**, not accidental: `144&nbsp;Hz` in the spec row and the marketing sentence on `lite-144hz/index.mdx`; `60&nbsp;Hz` retained on `lite/index.mdx`; `Mode menu OSD` on lite-144hz vs `Mode OSD` on lite; `Screenmate Lite 144 Hz` product-name expansion in every title, description, H2 and alt. No differentiator is missing and none has leaked into the wrong product.

### 8. Panorama FR-only infinitive bullets (deliberate, recorded) — internally consistent

`fr/manuals/panorama/controls.mdx:32–34` and `38–40` render the unlabelled bullets as infinitives
(`Naviguer dans le menu.` / `Diminuer des valeurs…` / `Ouvrir le menu de raccourci de la luminosité.`
and the parallel `Naviguer` / `Augmenter` / `Ouvrir … du volume`). Checked for internal consistency:

- **All 6 unlabelled bullets are infinitive.** No mixing.
- The two lists are exactly parallel in structure and verb choice (`Naviguer` / `Diminuer`↔`Augmenter` / `Ouvrir`), which is stronger than the EN, where the third bullet silently switches to third person (`Opens the brightness shortcut menu`).
- The **labelled** bullets in the same file (`27–28`, `44–45`) are uniformly third-person indicative (`éteint`, `ouvre`, `confirme`, `passe`, `quitte`). This is a clean two-register split — infinitive for bare bullets, indicative after a `**Appui …&nbsp;:**` label — and it is applied without exception. It also silently repairs an EN inconsistency (`Switch the monitor off.` imperative vs `Opens the OSD menu…` indicative on adjacent lines).
- No leakage: `fr/manuals/lite/controls.mdx` and `fr/manuals/lite-144hz/controls.mdx` use infinitives after `Appui court&nbsp;:` / `Appui long&nbsp;:` / `Rotation&nbsp;:` (`allumer`, `éteindre`, `revenir`, `naviguer`), which is the same convention applied to the same bullet shape. Consistent across the family.

**Verdict: the FR-only infinitive choice is internally consistent and needs no change.**

### 9. Safety-negation strength — one defect found (finding 6), rest clean

Every negative and restrictive construction in the three safety chapters plus the panorama installation cautions was checked for weakening:

- `N'utilisez pas de liquides ni de produits de nettoyage agressifs.` — `ni` correctly extends the negation to the second object (a `ou` here would have weakened it). ✅
- `Ne touchez pas l'appareil avec les mains mouillées **et ne** l'utilisez pas dans des environnements humides.` — negation repeated on the second verb rather than elided. ✅
- `Ne faites pas tomber le moniteur` ✅ · `N'utilisez pas d'objets tranchants sur l'écran ou à proximité.` ✅ · `Maintenez les ouvertures de ventilation dégagées` ✅ · `Limitez l'exposition aux champs magnétiques puissants` ✅
- `Le port USB-C d'un ordinateur portable **ne fournit pas à lui seul** une puissance suffisante … Branchez **toujours** l'adaptateur 65&nbsp;W` (`panorama/installation.mdx:58`) — both the negation and the `Always` are intact at full strength. ✅
- `Utilisez uniquement l'adaptateur CA/CC fourni` (lite/lite-144hz item 2) vs `Utilisez uniquement un adaptateur CA/CC` (panorama) — correctly tracks the EN `the included` vs `an`, not an error. ✅
- **Failure:** item 6 in both lite safety files — see finding 6.
