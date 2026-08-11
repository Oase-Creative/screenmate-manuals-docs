# Adversarial FR review — family F4 (`expand`, `one-4k`, `one-4k-oled`)

Branch `lang-expansion-de-fr-it`. 16 FR pages read line-by-line against their EN and NL
counterparts, plus DE/IT where a cross-language control was useful.

- `fr/manuals/expand/` — index, installation, controls, osd, safety, display-settings (6)
- `fr/manuals/one-4k/` — index, installation, controls, osd, safety (5)
- `fr/manuals/one-4k-oled/` — index, installation, controls, osd, safety (5)

Binding references: `translations/glossary-fr.md`, `translations/flags/fr-{expand,one-4k,one-4k-oled,shared}.md`.

**Result: 6 findings — 0 critical, 3 major, 2 minor, 1 low.**

Every finding below is corroborated by at least one independent control (a sibling language that
handled the same source string differently, a sibling FR page, or a locked glossary rule). Items
the brief listed as known non-defects were checked and are recorded in §Evidence, not here.

---

## Findings

| # | Sev | File:line | Class | EN source | FR shipped | Problem | Fix |
|---|---|---|---|---|---|---|---|
| F4-1 | **Major** | `fr/manuals/expand/safety.mdx:16`, `fr/manuals/one-4k/safety.mdx:16`, `fr/manuals/one-4k-oled/safety.mdx:16` (+5 more, frozen chapter) | Safety — restriction scope | `Only use the device with a 5V power source via the appropriate cable.` | `Utilisez uniquement l'appareil avec une source d'alimentation de 5&nbsp;V via le câble approprié.` | `uniquement` is fronted before the direct object, so it scopes over **`l'appareil`** ("use only the device"), not over the power-source complement. The safety-critical restriction — *no supply other than 5&nbsp;V* — is grammatically detached from the thing it must restrict. NL, DE and IT all place the restrictive adverb **after** the object; FR is the sole outlier. FR's own item 8 on the same page uses the correct pattern (`Nettoyez l'écran uniquement avec…`). | `Utilisez l'appareil uniquement avec une source d'alimentation de 5&nbsp;V via le câble approprié.` **Frozen chapter** — must land on all 8 FR `safety.mdx` in one commit (7-file group + `dual-flip`). |
| F4-2 | **Major** | `fr/manuals/one-4k/installation.mdx:45` | Negation scope / factual inversion | `…not every USB-C port can output video.` | `…tous les ports USB-C ne peuvent pas transmettre de signal vidéo.` | Two compounding cues push this to the **total**-negation reading: (a) `tous … ne … pas` is the notoriously ambiguous French partial-negation frame; (b) the partitive `de` under negation (`ne … pas transmettre **de** signal vidéo`) is the standard French marker of *complete* negation. Combined, the salient reading is "no USB-C port can transmit any video signal" — which contradicts the first half of the same sentence and the product premise. EN (`not every`), NL (`niet elke`), DE (`nicht jeder`) and IT (`non tutte`) **all** front the negation onto the quantifier; FR alone does not. | `…les ports USB-C ne peuvent pas tous transmettre un signal vidéo.` (or `certains ports USB-C ne peuvent pas transmettre de signal vidéo`) |
| F4-3 | **Major** | all 16 F4 pages, frontmatter | Structural parity / build | `nl_link: "/nl/manuals/<slug>/<page>"` present on every EN page; `en_link:` on every NL page | *(no `*_link` key at all)* | Every F4 page ships without cross-language link frontmatter. `docs.json` registers `fr` as a language (line 443) and `scripts/generate_language_links.py` documents that all product tabs are `hidden: true`, so **Mintlify cannot infer a page's counterpart** — the language switcher has nothing to resolve. Glossary §11 grep 13 (`grep -L 'en_link:'`) is a required pre-ship gate and currently returns every FR file. Systemic, not F4-specific: **0/61 FR, 0/61 DE, 0/61 IT** pages carry any `*_link` key. | Run `python scripts/generate_language_links.py` at repo root (write mode) and commit. Not an FR-translation defect — a branch-level omission that nevertheless blocks all 16 F4 pages. |
| F4-4 | Minor | `fr/manuals/expand/osd.mdx:53` (also `fr/manuals/flip/osd.mdx:51`, `fr/manuals/dual-flip/osd.mdx:51`) | Meaning drift — dropped goal complement | `Choose RESET to restore all settings to factory defaults.` | `choisissez RESET pour rétablir tous les réglages d'usine.` | The EN has a patient (*all settings*) **and** a goal (*to factory defaults*). FR collapses both into one noun phrase, so `tous` re-attaches to `réglages d'usine`: it now reads "restore all the factory settings" rather than "return all settings to their factory values". NL (`alle instellingen terug te zetten **naar** de fabrieksinstellingen`), DE (`alle Einstellungen **auf** die Werkseinstellungen`) and IT (`tutte le impostazioni **ai valori di fabbrica**`) all preserve both arguments. FR is again the sole outlier, and the same wording was reused for two *different* EN paraphrases (`restore … to` on expand/dual-flip, `return … to their` on flip). | `choisissez RESET pour rétablir tous les réglages à leurs valeurs d'usine.` |
| F4-5 | Minor | `fr/manuals/one-4k/index.mdx:15` vs `fr/manuals/one-4k-oled/index.mdx:15` | Locked-sibling consistency | Byte-identical in both EN slugs: `is a 15.6" 4K UHD portable monitor with a…` | one-4k: `est un écran portable **4K UHD de 15,6"**`<br>oled: `est un écran portable **15,6" 4K UHD**` | Two different renderings of an EN fragment that is character-identical across the pair. DE (`ist ein tragbarer 15,6"-4K-UHD-Monitor` ×2) and NL are internally consistent; IT shares the FR drift. This **falsifies the verification claim** in `translations/flags/fr-one-4k-oled.md` §"Corpus-consistency notes" 1 — "every remaining difference between the two FR pages corresponds to a real EN difference". It does not. | Pick one and apply to both (the `one-4k` form `écran portable 4K UHD de 15,6"` is the more idiomatic French). Update the flag file's claim. |
| F4-6 | Low | `fr/manuals/one-4k/index.mdx:15`, `fr/manuals/one-4k-oled/index.mdx:15` | Modality drift | `…and **supports** both video and power over a single USB-C cable on compatible devices.` | `…et **transporte** à la fois la vidéo et l'alimentation sur un seul câble USB-C avec les appareils compatibles.` | A capability statement (*supports*) becomes an activity statement (*transporte*). The same slug uses `transporte` for EN `carries` at `controls.mdx:13`/`:19`, so EN's supports/carries distinction is collapsed onto one French verb. The `avec les appareils compatibles` qualifier does keep the claim honest, which is why this is Low and not Major. Glossary §6 locks `supports {N} connection scenarios` → `prend en charge` and FR applies it correctly at `installation.mdx:19`, so the verb is available. | `…et prend en charge la vidéo et l'alimentation sur un seul câble USB-C avec les appareils compatibles.` |

---

## Scrutiny evidence

Recorded so a later pass can see what was actually checked rather than re-deriving it.

### 1. Shared-chapter checksums — **PASS** (no divergence; this was the designated critical risk)

Frontmatter stripped, CR normalised, `md5sum` on the body.

`display-settings.mdx` (onecable canonical, glossary §9.3 four-way lock):

| Product | FR body md5 | EN body md5 |
|---|---|---|
| onecable | `ec24415c0551ca0628b4f8b22c7a6bdc` | `467551f5a59279929d98a427fcdce9d0` |
| dual-flip | `ec24415c…` | `467551f5…` |
| flip | `ec24415c…` | `467551f5…` |
| **expand** | **`ec24415c…`** | **`467551f5…`** |

FR is byte-identical across all four, and the FR partition matches the EN partition exactly.

`safety.mdx` — the EN group-of-7 (`expand, flip, lite-144hz, lite, one-4k-oled, one-4k, onecable`)
hashes `b709f7d9…`; the FR counterparts of the same seven all hash `7008d419…`, and the four
products EN keeps separate (`panorama`, `infinity`, `infinity-lite`, `dual-flip`) are separate in FR
too. All three F4 slugs sit inside the group and match it. **No shared-chapter divergence.**

### 2. Structural parity EN↔FR — **PASS** on all 16 pages

Heading level-sequence identical (not merely equal counts), `<img>` counts identical, `<Tab>` counts
identical, and every `src=` attribute byte-identical to EN (including the Dutch-derived
`…%20Handleiding%20images/…` paths). Sample: `expand/installation` h=7 img=7; `one-4k/controls`
h=9 img=1; `one-4k-oled/installation` h=7 img=5.

### 3. Locked glossary tables — **PASS**, 0 mismatches

Parsed §9.1/§9.2/§9.3/§9.4 (and every other two-column backticked table) out of
`translations/glossary-fr.md` into an EN→FR map, then diffed every F4 heading and every
`title:`/`description:` frontmatter value against it. Zero mismatches. Spot-confirmed by hand:
`## Utiliser l'OSD` (expand) vs `## Utiliser le menu OSD` (flip) kept distinct per the §9.3 collision
note; `## Étapes d'installation` vs `## Instructions d'installation`; `### Prise casque 3,5&nbsp;mm`
from EN's unspaced `3.5mm`; `### Bouton Menu (alimentation / OSD)`; `### Verrouillage de l'OSD`.

### 4. `## Pour commencer` — **PASS**, byte-identical across the sibling pair

Glossary §9.3 locks `## Getting Started` → `## Pour commencer`; both slugs use it. The full 9-line
block (heading + 7 bullets) is byte-identical in FR (`201475fd5eaab926453194b4df36de5a`), exactly as
it is in EN (`d13b67cef5a7c0d0f846d409f053a0f8`).

The "11 realigned wordings" claim was verified the hard way — a full-file `diff` of
`fr/manuals/one-4k/installation.mdx` against `fr/manuals/one-4k-oled/installation.mdx`, mapped
against the same `diff` on the EN side. **Every** FR difference corresponds 1:1 to a real EN
difference (frontmatter `description`, the product name in the five-scenarios sentence, and the six
image/alt/paragraph blocks that genuinely differ upstream). `passe automatiquement`,
`associé au câble HDMI pour transporter le signal vidéo`, `prenant en charge le DisplayPort Alt Mode`,
`Voyant d'état indiquant l'alimentation et l'état du signal.`, `dans l'OSD`, `de la luminosité` /
`du volume`, `lorsque l'alimentation est raccordée`, `valider un réglage`, `pour l'enregistrer` and
the OSD-lock sentence are all confirmed identical across the pair. The `controls.mdx` and `osd.mdx`
pairs are likewise identical except where EN differs.

The one place the alignment **did** fail is `index.mdx:15` → **F4-5**.

### 5. OSD alts and the `d9007f3` fix — **PASS**

`d9007f3 fix(i18n): fr — unify OSD alt shape on Menu OSD {Section} (R9)` touched
`fr/manuals/expand/osd.mdx` (6 alts) and `fr/manuals/lite/osd.mdx` (4 alts), replacing
`Menu {Section} de l'OSD` with `Menu OSD {Section}`. Verified applied on expand
(`Menu OSD Rétroéclairage / Image / Couleur / Réglages / Réinitialisation / Autres`) and verified
that the shape is now uniform corpus-wide: `dual-flip`, `expand`, `flip` (6 each), `lite`,
`lite-144hz` (4 each, incl. `Menu OSD Luminosité`, `Menu OSD Température de couleur`). `one-4k` and
`one-4k-oled` OSD pages contain zero images, so R9 has no site there — consistent with
`translations/flags/fr-one-4k.md`. No residual `de l'OSD` alt anywhere.

*Observation (not a finding):* `Menu OSD Rétroéclairage` is a three-noun stack; the form it replaced
was the more idiomatic French. The unification was a deliberate R9 ruling and consistency was the
stated goal, so it is not scored as a defect — but `Menu {Section} de l'OSD` would have been both
idiomatic **and** uniform, and is the better target if R9 is ever revisited.

### 6. §3/§4/§4.1 typography and numbers — **PASS**

- **Register (§1):** `grep -Ei '\b(tu|toi|ton|ta|tes)\b'` → 0 hits. `veuillez`, `s'il vous plaît`,
  impersonal `on peut/doit/va` → 0 hits. `vous` throughout, bare `vous`-imperative in every numbered
  step and every run-in gloss.
- **§3.1 spacing:** every `**…:**` run-in in F4 carries `&nbsp;` before the colon — a scripted sweep
  for `\*\*([^*]+?):\*\*` whose captured text does not end in `&nbsp;` returns **0**. The `&nbsp;`
  sites were then classified by the following character: `:` ×67, `?` ×9, `%` ×5, `;` ×3, `!` ×3,
  plus unit symbols (`V` ×13, `m`/`mm`/`ms` ×7, `c`(`cm`/`cd`) ×5, `Hz` ×3, `°C` ×6, `A` ×1), the
  guillemet interiors on `display-settings`, and `l'image&nbsp;2` (§6). No stray `&nbsp;` anywhere else.
- **§3.4 carve-out:** `16:9`, `4:3`, `1000:1`, `1200:1`, `100 000:1`, `https://` all left tight — no
  `&nbsp;` was injected into a ratio or URL.
- **§3.5:** U+2019 → 0. Curly double quotes → 0. Straight `"` prime used for inches; escaped `\"` in
  YAML; `&quot;` in `<Tab title=…>` (`Expand 15,6&quot;`, `Expand 14&quot;`) with no literal `"`
  inside a JSX attribute.
- **§3.2 hazard:** literal U+00A0 anywhere in F4 → **0**. Banned U+202F → **0**. Entity form only.
- **§4.1 R5 (`100 000:1`):** occurs exactly twice, both in `fr/manuals/one-4k-oled/index.mdx` — the
  `## Qu'est-ce que…` prose (line 15) **and** the `**Taux de contraste**` spec row (line 27). Byte-checked:
  `['0x31','0x30','0x30','**0x20**','0x30','0x30','0x30','0x3a','0x31']` — a **plain** U+0020 between
  digit groups, colon tight, exactly as R5 requires. `grep -E '100[,.]000'` → 0 hits.
- **Glyphs:** `−` is U+2212 everywhere (expand/controls ×1, expand/osd ×1, one-4k/controls ×2,
  one-4k/osd ×4, one-4k-oled/controls ×2, one-4k-oled/osd ×4) — never a hyphen. `≡` U+2261,
  `—` U+2014 (plain spaces, per §3.5), `–` U+2013 for ranges, `×` for resolutions/dimensions. Counts
  match the EN source in every file.
- **Numbers:** `1920 × 1080` normalised in **both** expand tabs (EN writes it unspaced in the 14"
  tab); `3840 × 2160` on one-4k (EN unspaced); `15,6"` comma decimal in all four one-4k positions
  and both `Expand 15,6&quot;` tab titles; `1750 / 1450 / 860 grammes` with no thousands separator
  (4 digits, §4); `72&nbsp;%&nbsp;NTSC`, `45&nbsp;%&nbsp;NTSC`, `100&nbsp;%&nbsp;sRGB`;
  `-20&nbsp;°C`/`60&nbsp;°C`; `178°` with no space; `5&nbsp;V/2&nbsp;A`; `±2&nbsp;V`.

### 7. Compounds, cable chains, calques — **PASS**

- §2.1 chain: every occurrence is `câble {A} vers {B}` — `câble USB-C vers USB-C`,
  `câble USB-C vers USB-A`, `câble Mini-HDMI vers HDMI`. No `à`, `>`, `/` or hyphen chain
  (grep 8's single hit was the false positive `câble transporte à la fois`).
- §2 hyphen-chain grep (`(USB-[CA]|HDMI)-(câble|port|…)`) → 0. Unhyphenated `USB C` / `USBC` /
  `Mini HDMI` → 0; `Mini-HDMI` hyphenated even where EN writes `Mini HDMI`.
- Counts drop the `x`: `2 câbles USB-C vers USB-C`, `6 clips de protection`,
  `- 1 USB-C, 1 USB-A et 1 HDMI`.
- §11 grep 11 (`\bdriver(s)?\b`) → 0. §11 grep 17 (pre-`7a96840` question leads) → 0.
- §10.1.F frozen leads present verbatim on `expand/display-settings`:
  `**Vous souhaitez étendre votre espace de travail&nbsp;?**`, `**Écran à l'envers&nbsp;?**` ×2,
  `**Besoin d'une meilleure vue d'ensemble&nbsp;?**`, and
  `Votre navigateur ne prend pas en charge la balise vidéo.` ×2.
- §8 OS labels: `Paramètres d'affichage`, `Étendre le Bureau à cet écran`, `Identifier`,
  `Orientation de l'affichage`, `Paysage (inversé)`, `Échelle`, `Réglages Système`, `Moniteurs`,
  `Disposition`, `Rotation`, `Standard`. EN's bold `**Display settings**` stays bold in FR (§3.5);
  EN's single-quoted labels become `«&nbsp;…&nbsp;»`. No Dutch gloss carried over.
- §7 CAPS labels reproduced character-for-character, including `COLOR TEMP.` **with** the trailing
  period on expand; device values (`Standard, Game, Movie, Text, FPS, RTS, Energy Saving`,
  `Warm, Cool, User`, `Off, Auto, 2084`, `ON`/`OFF`, `WIDE`, `Type-C1 / Type-C2`) kept English;
  no `(BACKLIGHT)`-style gloss invented on any heading; `seconds` → `secondes` inside the
  `(10–60 …)` suffix (§7.3 trap) — correct.
- Negation sweep: all 26 negated clauses in F4 read individually. Only
  `one-4k/installation.mdx:45` is defective (**F4-2**). `N'utilisez pas de liquides ni de produits de
  nettoyage agressifs`, `Ne touchez pas … et ne l'utilisez pas …`, `ne fournit pas d'alimentation`,
  `ne fournit pas une puissance suffisante`, `ne dispose pas d'assez de ports HDMI`,
  `ne répondent plus` are all correct and preserve EN force.

### 8. Deliberately **not** flagged (per brief) — verified present, then set aside

| Item | Status |
|---|---|
| `alt="Étapes d'installation 1 à 6"` naming 6 steps over a 5-item list | Present at `expand/installation.mdx:34`; EN and NL share the mismatch → upstream source defect, faithfully mirrored. Not scored. |
| EN `Color Accuracy` (15,6" / `72% NTSC`) vs `Color Gamut` (14" / `45% NTSC`) | FR mirrors the EN split (`Précision des couleurs` / `Gamme de couleurs`) per §5.6. EN-side defect — an `% NTSC` figure is a gamut value. Not scored. |
| `{/* TODO … */}` comments EN-verbatim | `one-4k-oled/controls.mdx:35` and `one-4k-oled/osd.mdx:26` byte-identical to EN; `one-4k/osd.mdx:26` likewise. NL translated them; FR correctly did not. Not scored. |
| Dutch-language Windows screenshots on `display-settings` | FR prose now names French OS labels beside Dutch labels in the image. Client content decision, already logged in `fr-shared.md`. Not scored. |
| Unit-spacing divergences | FR `45&nbsp;W`/`100&nbsp;%`/`-20&nbsp;°C` vs EN/NL closed forms (glossary §12 open item 2), **and** the internal FR `cm` split (`expand/index` `2,5&nbsp;cm` vs `one-4k*/index` `1,3 cm`), which glossary §4 and §4.1 contradict each other on. Both confirmed present. Not scored. |

### 9. Upstream EN observations (not FR defects, worth a client line)

- `en/manuals/one-4k-oled/index.mdx:35` labels the row `Dimensions (folded)` for a product with a
  fixed built-in stand and no fold, while `en/manuals/one-4k/index.mdx:37` uses plain `Dimensions`
  for the **identical** `34.8 × 22.4 × 1.3 cm` figures. FR faithfully mirrors both
  (`Dimensions (plié)` / `Dimensions`), so the FR pages inherit the inconsistency.
- `en/manuals/expand/installation.mdx:18` lists the connection as `1x USB-C & 1x USB-A & 1x HDMI`
  while the heading three lines down (`### 2. 1x USB-C, 1x HDMI and 1x USB-A`) reverses the last two.
  FR mirrors both orders faithfully (`1 USB-C, 1 USB-A et 1 HDMI` / `### 2. 1 USB-C, 1 HDMI et 1 USB-A`),
  per the §9.4 lock. Harmless, but the EN should pick one order.
- `translations/flags/fr-one-4k-oled.md` claims full FR line-alignment across the `one-4k` /
  `one-4k-oled` pair. That claim needs the one-line correction described in **F4-5**.
