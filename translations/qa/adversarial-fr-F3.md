# Adversarial FR review — family F3 (`flip`, `dual-flip`)

**Branch:** `lang-expansion-de-fr-it` · **Date:** 2026-08-11 · **Reviewer stance:** adversarial (hunting defects, not confirming quality)
**Scope:** 12 pages — `fr/manuals/flip/{index,installation,controls,osd,display-settings,safety}.mdx` and
`fr/manuals/dual-flip/{index,installation,controls,osd,display-settings,safety}.mdx`, each read against its EN and NL counterpart.
**Authorities applied:** `translations/glossary-fr.md` (§0 precedence — shipped pages win; §10.1.F reconciled to shipped chapters in `7d01398`), `translations/dnt.json`, ruling R9 (OSD alt shape).

**Verdict:** no critical defects. The two frozen chapter groups are intact, the locked terminology is applied
correctly, and every numeric value is faithful. The real weakness of this family is **cross-product consistency**:
byte-identical EN sentences are paraphrased differently between `flip`, `dual-flip` and their `expand` sibling,
which erodes the cross-product identity §0 requires `fr/` to preserve from `en/`.

---

## Findings

| # | Sev | File:line | Issue | Evidence / rule | Suggested fix |
|---|---|---|---|---|---|
| F3-01 | **Major** | all 12 F3 pages, frontmatter | **No `en_link:` / `nl_link:` on any FR page.** EN F3 pages carry `nl_link:`, NL F3 pages carry `en_link:`; the FR pages carry neither, and no EN/NL page carries `fr_link:`. This is the sole cause of the uniform `en=nl=fr+1` line-count delta on all 12 files. | Glossary §11 grep 13 requires it verbatim: `grep -L 'en_link:' fr/manuals/**/*.mdx` → currently returns **all 62** FR pages. The language switcher is frontmatter-driven. | Add `en_link:` + `nl_link:` to every FR page and `fr_link:` to the EN/NL counterparts. **Scope note:** corpus-wide (0/62 FR pages have it), so this is a branch-level wiring gap rather than an F3 translation error — but F3 fails the gate as written and should not ship without it. |
| F3-02 | **Minor** | `flip/installation.mdx:9,22,59,67,82`; `dual-flip/installation.mdx:9,33,41,56` | **Family paraphrase drift.** Byte-identical EN sentences get different French across the 4-product family. Six confirmed instances (table below). Worst case: one EN verb `Connect` becomes three different French verbs across three sibling products, two of which (`relier`, `raccorder`) are outside the §5.2 `brancher`/`connecter` split entirely. | §0: "Translate them **once** and paste the identical French into every product so `fr/` keeps the same cross-product identity `en/` has." §5.2 locks connect *(plug a cable in)* → `brancher`, connect *(establish the link)* → `connecter`. | Pick one rendering per EN sentence and propagate across `flip`/`dual-flip`/`expand` in one commit. Recommend `Branchez` for *Connect the other side …* (a cable is being plugged in) and `relier` for *connect one side of the Screenmate to your laptop*. |
| F3-03 | **Minor** | `flip/osd.mdx:20` | EN `Preset` → `prédéfinis`, where the two siblings render the same EN word `préréglés` (`dual-flip/osd.mdx:20`, `expand/osd.mdx:22`). `flip` is the outlier. | §5.4 locks `preset` → `préréglage`; `préréglés` is the stem-aligned adjective. (The EN noun genuinely differs — `picture modes` vs `display modes` — so `modes d'image` vs `modes d'affichage` is *correct* and must be kept; only the adjective is the defect.) | `modes d'image **préréglés** pour différents usages`. |
| F3-04 | Low | `flip/controls.mdx:23–25` | Capitalisation is inconsistent inside one 3-item parallel list: `- **M** — bouton du menu OSD.` (lowercase) vs `- **+** — Augmenter la luminosité.` / `- **−** — Diminuer la luminosité.` (capitalised). EN capitalises all three uniformly. | These are the **only** three `**X** — …` bullets in the entire FR corpus, so no house precedent exists either way — but they must match each other. | Lowercase all three (matches the §9.4 lock `### M — bouton du menu OSD` and the `**…&nbsp;:**` lowercase-run-in convention used everywhere else in F3). |
| F3-05 | Low | `flip/installation.mdx:80` | `Faites pivoter l'écran gauche de 180° **en sens inverse, dans le sens indiqué** sur l'image&nbsp;1.` reads as self-contradictory ("in the opposite direction, in the direction shown"). EN: *Rotate the left screen 180° back in the direction shown in image 1.* | Meaning drift — the EN `back` is an adverb of return, not a second direction. | `Faites pivoter l'écran gauche de 180° pour le ramener dans le sens indiqué sur l'image&nbsp;1.` (`dual-flip/installation.mdx:54`, whose EN has no `in the direction shown`, is correct as-is.) |
| F3-06 | Low | `flip/index.mdx:15` | `pour vous offrir deux écrans supplémentaires, **gage d'**une meilleure vue d'ensemble et d'une plus grande concentration.` EN is the plain *to give you two extra displays for more overview and focus*; NL likewise plain (*voor meer overzicht en focus*). | `gage de` = "guarantee of" — turns a benefit statement into a guarantee and lifts the register above the rest of the corpus. Register/meaning inflation. | `… deux écrans supplémentaires pour une meilleure vue d'ensemble et plus de concentration.` (`vue d'ensemble` is correct and must stay — §10.1.F.) |
| F3-07 | Low | `flip/index.mdx:8` | `valable pour les modèles 14" et 15,6"` for EN *covering both the 14" and 15.6" models*. | `valable pour` is a validity/legal register; the clause is about coverage. The rest of this Welcome block is byte-matched to the §10 lock, so this is the one deviating clause. | `… complet de votre Screenmate Flip, qui couvre les modèles 14" et 15,6".` |

### F3-02 detail — identical EN, divergent FR

| EN source (identical across products) | `flip` | `dual-flip` | `expand` |
|---|---|---|---|
| `Connect the other side using the HDMI cable …` | `Branchez l'autre côté…` | `Connectez l'autre côté…` | `Raccordez l'autre côté…` |
| `Use the included USB-C cable to connect one side …` | `…pour relier un côté…` | `…pour connecter un côté…` | `…pour relier un côté…` |
| `use the two included USB-C cables to connect your laptop to the Screenmate` | `…pour **le** connecter au Screenmate` | `…pour connecter votre ordinateur portable au Screenmate` | `…pour connecter votre ordinateur portable au Screenmate` |
| `first check which ports your laptop has` | `de quels ports dispose votre ordinateur portable` | `les ports dont dispose votre ordinateur portable` | `de quels ports dispose votre ordinateur portable` |
| `Use the icons below as a reference.` | `Servez-vous des icônes ci-dessous comme référence.` | *(n/a)* | `Utilisez les icônes ci-dessous comme référence.` |
| `… and store it in a safe place.` | `…et rangez-le en lieu sûr.` | `…et rangez-le dans un endroit sûr.` | *(n/a)* |

None of these is wrong French in isolation. The defect is the loss of cross-product identity, and it is
invisible to every mechanical grep — it only surfaces on a side-by-side family read.

---

## Recorded non-defects (do not "fix" these in a later pass)

| # | File:line | Observation | Why it is correct |
|---|---|---|---|
| N-01 | `flip/index.mdx:20` | EN `1× USB-C with USB-A Adapter (90 cm)` (no "cable") → `1 câble adaptateur USB-C vers USB-A (90 cm)`, adding `câble` and turning `with` into `vers`. | This is the §5.7 locked string, and it aligns `flip` with `dual-flip`, whose EN *does* say "adapter cable". Reverting would break the §2.1 chain and split the family. |
| N-02 | both `display-settings.mdx` (all 6 sites) | The EN Dutch-language OS glosses — `('Beeldscherminstellingen')`, `('Identificeren')`, `('Bureaublad uitbreiden naar dit beeldscherm')`, `('Beeldschermstand')`, `('Schaal')`, `(Schaal en indeling)` — are dropped rather than replaced. | A Dutch gloss is noise to a French reader; French UI labels already carry the meaning (§8). The drop is uniform across all four products by checksum and is inherited from the shipped canonical chapter (`7a96840`), which §0 precedence rule 3 makes authoritative. |
| N-03 | `flip/index.mdx:75–76` vs `dual-flip/index.mdx:52–53` | Two different bold shapes for the left/right screen labels. | Each mirrors its own EN source exactly: EN `**Left** screen:` → `Écran **gauche**&nbsp;:` (colon outside bold); EN `**Left screen:**` → `**Écran gauche&nbsp;:**` (colon inside bold, = §10.2 lock). Internally consistent in both files, and `expand` matches `dual-flip`. Verified across all three products. |
| N-04 | `flip/installation.mdx:9` | `Le Flip 14" comme le Flip 15,6" **peuvent** être connectés` — plural verb after `A comme B`. | Defensible: with `comme` used additively (no comma isolation) modern usage takes the plural. Not flagged. |
| N-05 | both `osd.mdx:43` | The OSD `LANGUAGE` value list is translated (`anglais, français, allemand…`) and lowercased. | Not a §7.1 device-value block; NL and DE both translate it, French lowercases language names, and all 12 entries are present in EN order. FR is in fact *stricter* than NL here — NL invents a gloss (`**LANGUAGE (Taal):**`) on `dual-flip`'s bare-caps label, whereas FR correctly keeps it bare per §7. |

---

## Scrutiny evidence

Every check below was executed, not assumed. Where a check returned nothing, the command is recorded so the
absence of a finding is falsifiable.

### 1. Frozen shared chapters — body checksums (`md5` of everything after the frontmatter)

**display-settings, 4-product group (onecable canonical):**

| Product | EN | NL | FR |
|---|---|---|---|
| onecable | `467551f5…` | `88f65c86…` | `ec24415c…` |
| flip | `467551f5…` | `88f65c86…` | `ec24415c…` |
| dual-flip | `467551f5…` | `88f65c86…` | `ec24415c…` |
| expand | `467551f5…` | `88f65c86…` | `ec24415c…` |

All four FR bodies are **byte-identical** (`ec24415c0551ca0628b4f8b22c7a6bdc`), matching the EN and NL grouping exactly. **No divergence.**

**safety, per-group:** FR reproduces the EN grouping precisely — `flip` shares its body hash with the
`onecable`/`expand`/`lite`/`one-4k` group (`7008d419…`, EN `b709f7d9…`), while `dual-flip` is its own hash
(`c9122c85…`, EN `7b08b090…`) because its EN uses bullets where the group uses a numbered list. FR text is
otherwise word-for-word identical between the two. **No divergence.** (Note: the *NL* side does **not**
reproduce this grouping — `nl/onecable/safety` diverges from `nl/flip/safety`. FR is cleaner than NL here.)

### 2. Structural parity with `en/`

Heading count (`^#{1,4} `) compared per file across all 12 pages → **zero mismatches**. Same files, same
heading levels, same order, same JSX components. The only per-file delta is the missing frontmatter link line (F3-01).

### 3. Glossary §11 verification greps — all run against F3, all clean

| Grep | Target | Result |
|---|---|---|
| 1 | register: `\b(tu\|toi\|ton\|ta\|tes)\b` | 0 hits |
| 1b | 2nd-person-singular imperatives (`Branche\|Appuie\|Vérifie\|…`) | 0 hits |
| 2 | plain space before `: ; ! ?` | 0 hits |
| 3 | banned U+202F | 0 hits |
| 4 | literal U+00A0 in body copy | 0 hits |
| 5 | typographic apostrophe U+2019 | 0 hits |
| 6 | period decimals (`15.6 cm`) | 0 real hits (2 `src=` path false positives: `Flip%2015.6`) |
| 7 | closed unit forms (`45W`, `100%`) | 0 real hits (all hits are `src=` paths / `USB-A 2.0`) |
| 8 | broken cable chain (`câble A à/>//- B`) | 0 hits |
| 9 | hyphen-chain compounds (`USB-C-câble`) | 0 hits |
| 10 | `USB C` / `USBC` / unhyphenated `Mini HDMI` | 0 hits |
| 11 | untranslated `driver(s)` | 0 hits |
| 15 | leftover EN JSX strings (`does not support the video tag`, `Important Information:`, `Please note:`, `Protective Case`, …) | 0 hits |
| 16 | literal `"` inside a `<Tab title=…>` (hard MDX parse error) | 0 hits |
| 17 | pre-`7a96840` glossary leads (`Envie d'étendre`, `est-il à l'envers`, …) | 0 hits |

### 4. §4.1 spacing — exhaustive, not sampled

Every `?`, `!` and `%` in the 12 files was listed and inspected individually.

- **10 `?`** — all `&nbsp;?`: 4× `**Vous souhaitez étendre votre espace de travail&nbsp;?**`, 4× `**Écran à l'envers&nbsp;?**`, 2× `**Besoin d'une meilleure vue d'ensemble&nbsp;?**` (2 of these are the H2 `## Qu'est-ce que le Screenmate {Flip,Dual Flip}&nbsp;?`). A negative grep for `?` *not* preceded by `;` returned zero.
- **2 `!`** — both `**Bienvenue&nbsp;!**`.
- **5 `%`** — `150&nbsp;%`, `45&nbsp;%&nbsp;NTSC` ×2, `100&nbsp;%&nbsp;sRGB`. Double `&nbsp;` (before `%` and between `%` and the unit token) per §4.
- Ratios correctly left tight throughout: `16:9`, `16:10`, `1000:1`, `4:3` — the §3.4 carve-out was not over-applied.
- `&nbsp;` correctly reaches inside JSX `alt=` attributes: `alt="Ports du Screenmate&nbsp;: deux ports USB-C…"`, `alt="Échelle et disposition&nbsp;: réglez l'Échelle"` (§10.1.G).

### 5. Numbers and units — token-level diff, all 12 pages

Extracted every numeric token from each EN page and its FR counterpart, normalised the decimal comma, and diffed. **Zero mismatches on all 12 pages.** Spot-confirmed transformations:

`1920×1200` → `1920 × 1200` · `1920×1080` → `1920 × 1080` · `2560 × 1600` (kept) · `250 cd/m²` → `250&nbsp;cd/m²` ·
`450 cd/m²` → `450&nbsp;cd/m²` · `25 ms` → `25&nbsp;ms` · `60 Hz` → `60&nbsp;Hz` · `15.6"` → `15,6"` · `16"`/`14"` (kept) ·
`1565/1875/1900 grams` → `… grammes` (4-digit, no separator, §4) · `34.5 × 22 × 3.5 cm` → `34,5 × 22 × 3,5 cm` ·
`39 × 24 × 3.5 cm` → `39 × 24 × 3,5 cm` · `178°`/`180°`/`245°`/`205°` (no space, §4) · `0° – 245°` (en dash, spaced) ·
`5V and 20V` → `5&nbsp;V et 20&nbsp;V` · `±2V` → `±2&nbsp;V` · `5V/2A` → `5&nbsp;V/2&nbsp;A` · `-20°C … 60°C` → `-20&nbsp;°C … 60&nbsp;°C` ·
`10–60 seconds` → `10–60 secondes` (§7.3 unit-word trap) · `0–100`, `0–4` (verbatim ranges) · `150%` → `150&nbsp;%`.

Character-level: `±` is U+00B1, `°` is U+00B0, `−` in `**−**` / `**+ / −**` is U+2212 (not a hyphen), `-20` uses ASCII hyphen matching EN. `×` in dimensions is U+00D7.

### 6. Tab titles vs markdown headings (the `&quot;` trap)

| Site | Form | Verdict |
|---|---|---|
| `flip/index.mdx:30` | `<Tab title="Flip 14&quot;" icon="display">` | entity preserved, whole number, no comma ✓ |
| `flip/index.mdx:49` | `<Tab title="Flip 15,6&quot;" icon="display">` | entity preserved **and** decimal comma applied ✓ (§10.1.A) |
| `flip/installation.mdx:14` | `### Flip 14"` | markdown heading, literal `"` ✓ |
| `flip/installation.mdx:20` | `### Flip 15,6"` | markdown heading, literal `"` + comma ✓ (§9.4) |
| `dual-flip/index.mdx:11` | `alt="Le Screenmate Dual Flip 16&quot;"` | entity preserved inside `alt` ✓ |
| frontmatter | `…14\" et 15,6\"` / `…Dual Flip 16\"` | YAML-escaped, no `&nbsp;`, no entity ✓ (§3.3) |

Grep 16 (literal `"` inside a Tab title) returns zero. `icon="display"` never translated.

### 7. OSD chapters — CAPS labels, gloss pattern, and the bare-caps rule

`flip/osd.mdx` uses the **glossed** EN form and `dual-flip/osd.mdx` uses the **bare-caps** form. FR reproduces both correctly and does not cross-contaminate:

- `flip`: `**Luminosité (BRIGHTNESS)&nbsp;:**`, `**Contraste (CONTRAST)&nbsp;:**`, `**Mode ECO (ECO)&nbsp;:**`, `**Netteté (SHARPNESS)&nbsp;:**`, `**Format d'image (ASPECT)&nbsp;:**`, `**Température de couleur (COLOR TEMP.)&nbsp;:**` (trailing period preserved, §7), `**Rouge/Vert/Bleu (RED/GREEN/BLUE)&nbsp;:**`, `**Langue (LANGUAGE)&nbsp;:**`, `**Minuterie OSD (OSD TIMER)&nbsp;:**`, `**Transparence (TRANSPARENCY)&nbsp;:**`, `**Réinitialisation (RESET)&nbsp;:**`, `**Mode HDR (HDR MODE)&nbsp;:**`, `**Source (SOURCE)&nbsp;:**`, `**Lumière bleue faible (LOW BLUE LIGHT)&nbsp;:**` — all match §7 / §7.2 exactly.
- `dual-flip`: `**BRIGHTNESS (0–100)&nbsp;:**`, `**CONTRAST (0–100)&nbsp;:**`, `**ECO&nbsp;:**`, `**SHARPNESS (0–4)&nbsp;:**`, `**ASPECT&nbsp;:**`, `**COLOR TEMP&nbsp;:**` (no trailing period — EN has none here), `**RED/GREEN/BLUE (0–100)&nbsp;:**`, `**LANGUAGE&nbsp;:**`, `**OSD TIMER (10–60 secondes)&nbsp;:**`, `**TRANSPARENCY&nbsp;:**`, `**RESET&nbsp;:**`, `**HDR&nbsp;:**`, `**SOURCE&nbsp;:**`, `**LOW BLUE LIGHT&nbsp;:**` — **kept bare, no invented French gloss** (§7, "structural parity beats helpfulness").
- `**DCR (taux de contraste dynamique)&nbsp;:**` in both — the reversed-order §7 case, correct in both files.
- Device values kept English throughout: `Standard, Game, Movie, Text, FPS, RTS, Energy Saving` / `Warm, Cool, User, Standard` / `Off, Auto, 2084` / `ON`, `OFF` / `Type-C1`, `Type-C2`, `HDMI` / `4:3`, `WIDE`. `RGB` correctly becomes `RVB` in prose (§5.4) while the caps device labels stay.
- Signal-source counts follow their own EN: `flip` "two" → `deux`, `dual-flip` "three" → `trois`.
- OSD headings translated plainly with **no** invented `(BACKLIGHT)`/`(RESET)` gloss (§7): `## Rétroéclairage`, `## Image`, `## Couleur`, `## Réglages`, `## Réinitialisation`, `## Autres` (flip) and `### 1.–6.` numbered variants (dual-flip). `## Utiliser le menu OSD` vs `## Introduction au menu OSD` — the §9.3 collision pair was not collapsed.

### 8. OSD alt shape (ruling R9)

All 26 `Menu OSD …` alts in the FR corpus follow the `Menu OSD {Section}` shape. A negative grep — every FR
`alt=` on an `osd-*.png` that does **not** start `Menu OSD ` — returns zero. F3's 12 alts use the six canonical
section names (`Rétroéclairage`, `Image`, `Couleur`, `Réglages`, `Réinitialisation`, `Autres`), each matching
the section heading on the same page.

### 9. Frontmatter titles & descriptions vs §9.1/§9.2

All 12 titles and all 12 descriptions were compared to their EN source and to the §9.1/§9.2 lock tables —
**12/12 exact matches**, including the two that differ between the products on purpose:
`flip/display-settings` → `Configurer vos écrans sous Windows et macOS` vs `dual-flip/display-settings` →
`Réglages d'affichage pour Windows et macOS` (mirrors a real EN frontmatter difference, §0), and
`flip/osd` → `Régler les paramètres d'affichage…` vs `dual-flip/osd` → `Réglages d'affichage…`.
No `&nbsp;`, no entity, and no `: ; ! ? %` in any frontmatter string (§3.3 satisfied by phrasing, as required).

### 10. Register (`vous`) and callout lead-ins

Zero `tu`/`toi`/`ton`/`ta`/`tes` and zero second-person-singular imperatives. All instructions use the bare
`vous`-imperative (`Retirez`, `Dépliez`, `Faites pivoter`, `Placez`, `Connectez`, `Débranchez`, `Repliez`,
`Appuyez sur`, `Maintenez … enfoncé`, `Assurez-vous que`, `Nettoyez`, `Évitez`, `Limitez`, `Éteignez`) — no
`veuillez`, no `s'il vous plaît`, no `il faut`. The §1 locked exception is honoured: the safety opener drops
EN "Please" entirely (`Lisez attentivement les consignes suivantes…`).

Callout lead-ins are correctly differentiated by EN source rather than merged by convenience:
`**Please note:**` (`flip/installation`, the corpus's only occurrence per §10.1.I) → `**Remarque&nbsp;:**`;
`**Important:**` (`dual-flip/installation`) → `**Important&nbsp;:**`;
`**Important Information:**` (both `index.mdx`) → `**Informations importantes&nbsp;:**`.

### 11. Safety chapters — negation and restriction strength (line-by-line)

All 14 items in each file were checked individually for weakened negation, dropped restriction or softened modality.

| EN construct | FR | Strength |
|---|---|---|
| `Only use the included AC/DC adapter` | `Utilisez **uniquement** l'adaptateur CA/CC fourni` | preserved |
| `Only use the device with a 5V power source` | `Utilisez **uniquement** l'appareil avec une source d'alimentation de 5&nbsp;V` | preserved |
| `Clean the screen only with a dry, soft cloth. Do not use liquids or aggressive cleaning agents.` | `Nettoyez l'écran **uniquement** avec un chiffon doux et sec. **N'**utilisez **pas** de liquides **ni** de produits de nettoyage agressifs.` | preserved (`ni` correctly carries the second negative) |
| `Do not touch … with wet hands and do not use it in humid environments` | `**Ne** touchez **pas** … et **ne** l'utilisez **pas** …` | both negations preserved |
| `Do not drop the monitor and protect the screen from …` | `**Ne** faites **pas** tomber le moniteur et protégez l'écran contre …` | preserved |
| `Prevent exposure to … to prevent damage` | `**Évitez toute** exposition … **afin d'éviter tout** dommage` | preserved (§5.5) |
| `Keep ventilation openings clear` | `**Maintenez** les ouvertures de ventilation **dégagées**` | preserved |
| `Make sure the power outlet is properly grounded` | `**Assurez-vous que** la prise de courant est correctement **mise à la terre**` | preserved (§5.2 `grounded`) |
| `Limit exposure to strong magnetic fields` | `**Limitez** l'exposition aux champs magnétiques puissants` | preserved |
| `Do not press on the screens` / `Do not rotate the screens beyond …` (index) | `**n'**appuyez **pas** sur les écrans` / `**Ne** faites **pas** pivoter les écrans **au-delà de**…` | preserved |

**No safety-negation weakening found.** The two locked safety boilerplate strings (`Recommended ambient
temperature…` and `The monitor operates on a DC input…`) match §10 character-for-character. Singular/plural
faithfulness confirmed: `flip` EN "maximum angle**s**" → `des angles maximaux indiqués`; `dual-flip` EN
"maximum angle" → `de l'angle maximal indiqué`.

### 12. Frozen display-settings body — content review (a defect here is a 4-product defect)

All six §10.1.F question leads present and matching the shipped locks exactly:
`**Vous souhaitez étendre votre espace de travail&nbsp;?**`, `**Écran à l'envers&nbsp;?**` (×2),
`**Besoin d'une meilleure vue d'ensemble&nbsp;?**`. Grep 17 (pre-`7a96840` variants) returns zero.
`Votre navigateur ne prend pas en charge la balise vidéo.` present ×2; the EN string is absent.
OS labels match §8: `Paramètres d'affichage`, `Étendre le Bureau à cet écran`, `Identifier`,
`Orientation de l'affichage`, `Paysage (inversé)` (for EN `Flipped`), `Échelle`, `Réglages Système`,
`Moniteurs`, `Disposition`, `Rotation`, `Standard`. `Bureau` capitalised as the Windows label, distinct from
lowercase `bureau` (desk) — §5.1/§5.3 respected. Quote handling follows §3.5 precisely: EN `**Display
settings**` (bold) stays **bold**, EN `'Extend desktop to this display'` (single quotes) becomes
`«&nbsp;Étendre le Bureau à cet écran&nbsp;»` — bold is never converted to guillemets and vice versa.
`src`/`type`/`className`/`icon` untouched; video URLs and tokens byte-identical to EN.

### 13. Terminology spot-checks beyond the greps

- **case vs sleeve distinction preserved** (§5.1): `flip` EN `Protective Sleeve` → `Housse de protection`; `dual-flip` EN `Protective case` → `Étui de protection`. Consistent between each product's `index.mdx` and `installation.mdx`.
- **`Mini-HDMI` hyphenated everywhere** including inside `alt=` attributes and headings, normalising the EN `Mini HDMI` (§2 / `dnt.json`).
- **cable chain** always `câble {A} vers {B}`, order mirroring EN, only `câble` inflecting: `2 câbles USB-C vers USB-C`, `1 câble Mini-HDMI vers HDMI`, `1 câble adaptateur USB-C vers USB-A`, `câble USB-C vers USB-A`.
- **`ordinateur portable`** used throughout — never bare `portable`, never `laptop`.
- **`écran` vs `moniteur`** follows the EN `screen`/`monitor` split rather than being flattened (safety chapter uses `moniteur` where EN says `monitor`, `écran` where EN says `screen`).
- **spec-table field names** all match §5.6; `Grey` → `Gris`; identifiers `IPS`/`LCD`/`LED`/`NTSC`/`sRGB` untouched.
- **`transmission vidéo` (flip) vs `transfert vidéo` (dual-flip/expand)** — checked and **not** a defect: EN itself differs (`video transmission` vs `video transfer`); FR mirrors each source.
- **Calque sweep** (`supporter`, `digital`, `librairie`, `réaliser`, `basé sur`, `prévenir dommage`, `il faut`, `veuillez`, `s'il vous plaît`, `stick USB`, `dispositif`, `laptop`) → 0 hits.
- **§6 locked phrasings present**: `Prenez soin de` (not `Prenez bon soin de`), `afin d'éviter tout dommage`, `comme illustré sur l'image&nbsp;2`, `prend en charge deux scénarios de connexion`, `Choisissez celui qui correspond à…`, `des manières suivantes` correctly varied to `de l'une des manières suivantes` where the EN says "in one/either of the following ways".

### 14. Site wiring

All 12 FR F3 pages are registered in `docs.json` under the `"language": "fr"` block
(lines 496–501 and 508–513). `fr/manuals-index.mdx` exists. The only wiring gap is F3-01.

---

## Summary

| Severity | Count |
|---|---|
| Critical | **0** |
| Major | **1** (F3-01 — missing `en_link`/`nl_link`; corpus-wide) |
| Minor | **2** (F3-02 family paraphrase drift, F3-03 `préréglés` outlier) |
| Low | **4** (F3-04 … F3-07) |
| Recorded non-defects | 5 (N-01 … N-05) |

Frozen-chapter integrity: **intact**. Glossary compliance on locked strings: **100% on every string checked**.
Numbers: **100% faithful across all 12 pages**. Register and safety negation: **clean**.
The one blocking item is F3-01, and it is a branch-wide wiring gap rather than a translation error.
