# Round 4 — French fix log

**Date:** 2026-08-12 · **Branch:** `round4-fixes` · **Scope touched:** `fr/**`, `translations/glossary-fr.md`, `translations/qa/round4/*-fr.md`

**Inputs:** `fluency-fr-a.md` (1 Critical, 30 Major, 15 Minor) · `fluency-fr-b.md` (3 Critical, 38 Major, 27 Minor) · `safety-align-fr.md` (PASS — 0 Critical, 0 Major, 5 Minor)

> **This file has two rounds.** §1–§6 record the first fix wave (commits `aea5af3`, `6c3cf8c`).
> **§7 records the second wave**, answering the independent review in `review-fr.md`
> (0 Critical, 1 Important, 8 Minor). Where the two disagree, **§7 wins** — the counts below are
> round-1 counts, superseded by §7.8. Three round-1 renderings were revised in §7
> (`onecable/installation.mdx:44`, the USB-A Note in flip/dual-flip, `panorama/controls.mdx:27`)
> and one round-1 log row was corrected (§1.3 #18).

| Outcome | Round 1 | Final (§7.8) |
|---|---|---|
| **Fixed** (distinct findings) | 33, as 60 replacements across 31 files | **36**, as **64 replacements across 31 files** |
| **Rejected** (locked convention / faithful to EN) | 31 | **31** |
| **Source-flagged** (EN/NL defect, French left faithful) | 39 | **41** — see `source-flags-fr.md` |
| **Deferred / recorded-only** | 11 | **14** |
| **Glossary changes** | 5 | **6** + 7 §12 proposals logged |

Every finding in the three reports was triaged against its `en/` counterpart before any edit, and
against `nl/` wherever the two sources could disagree. Nothing was changed on the strength of the
French reading alone.

---

## 1 · Accepted and applied

### 1.1 The Dutch question rhythm `…&nbsp;? … alors …` — 9 sites, 7 files

The controller pre-triaged 6 occurrences (fluency-fr-a scope). A corpus-wide grep found **9**;
all were fixed, because leaving the identical construction in sibling files would have recreated
exactly the inconsistency the review flags — and `lite`/`lite-144hz` and `one-4k`/`one-4k-oled` are
twin products whose FR bodies must stay identical apart from name and specs.

**Method:** keep the question, drop `alors`. The bare question + imperative is idiomatic French and
is already the corpus's own model (`Pas de chargeur USB-C&nbsp;? Utilisez un adaptateur secteur
approprié.`, `onecable/installation.mdx`). Restructuring the question into `Si …, …` was rejected —
it would change the sentence type the EN source uses. Now locked as glossary **§6.1**.

| # | File | Before | After |
|---|---|---|---|
| 1 | `onecable/installation.mdx` | …&nbsp;? Une alimentation supplémentaire est **alors** nécessaire… | …&nbsp;? Une alimentation supplémentaire est nécessaire… |
| 2 | `onecable/installation.mdx` | **Branchez alors** l'autre câble USB sur une prise de courant. | **Branchez** l'autre câble USB sur une prise de courant. |
| 3 | `onecable/installation-mac.mdx` | …&nbsp;? **Passez alors directement** à l'étape&nbsp;5. | …&nbsp;? **Passez directement** à l'étape&nbsp;5. |
| 4 | `onecable/troubleshooting.mdx` | …&nbsp;? **Utilisez alors** un chargeur PD d'au moins 45&nbsp;W. | …&nbsp;? **Utilisez** un chargeur PD d'au moins 45&nbsp;W. |
| 5 | `lite/installation.mdx` | Besoin d'une alimentation supplémentaire&nbsp;? **Utilisez alors** le câble… | …&nbsp;? **Utilisez** le câble… |
| 6 | `lite-144hz/installation.mdx` | *(identical to #5)* | *(identical)* |
| 7 | `one-4k/installation.mdx` | *(identical to #5)* | *(identical)* |
| 8 | `infinity/installation.mdx` | …&nbsp;? **Vous pouvez alors connecter** le Screenmate directement… | …&nbsp;? **Vous pouvez connecter** le Screenmate directement… |
| 9 | `infinity/installation.mdx` | …&nbsp;? **Suivez alors** ces étapes&nbsp;: | …&nbsp;? **Suivez** ces étapes&nbsp;: |

> **Glossary consequence, noted prominently:** #3 changes a **§6-locked** string
> (`Then proceed to step 5` → `Passez alors directement à l'étape&nbsp;5`). The glossary row was
> amended to the new shipped form in the same commit, per §0 precedence rule 3 ("shipped page wins
> and the glossary is amended to match"). No other locked string was altered to serve this fix.

`panorama/installation.mdx:66` (`…alors que le Panorama l'alimente également…`) is the **conjunction**
`alors que`, not the pattern — deliberately untouched.

### 1.2 `Vérifiez si` → `Vérifiez que` — 4 sites, 1 file

`onecable/troubleshooting.mdx` lines 15 (×2), 19, 33. EN reads *"Check if …"* throughout, but in
French `vérifier si` = *find out whether* (an open question); an instruction takes `vérifier que` /
`s'assurer que` (glossary §5.5). Calque of NL `controleer of`. Now locked as glossary **§6.2**.

- `Vérifiez si le voyant de la carte mère est allumé.` → `Vérifiez que le voyant de la carte mère est allumé.`
- `Vérifiez si votre ordinateur portable fournit une puissance suffisante` → `Vérifiez que votre ordinateur portable fournit…`
- `Vérifiez si l'ordinateur portable fournit une puissance suffisante.` → `Vérifiez que l'ordinateur portable fournit…`
- `Vérifiez si l'icône du pilote est visible…` → `Vérifiez que l'icône du pilote est visible…`

*(The paragraph's existing `Assurez-vous que les deux extrémités…` was left as-is, so the sequence
now reads `Vérifiez que … Assurez-vous que … Vérifiez que …` — varied, not repetitive.)*

### 1.3 Calques and wrong collocations

| # | File(s) | Before | After | Why it is a French defect, not an EN one |
|---|---|---|---|---|
| 10 | `onecable/index.mdx` | …à votre ordinateur portable **avec une seule connexion par câble**. | …à votre ordinateur portable **à l'aide d'un seul câble**. | EN *"with just one cable connection"* is idiomatic; `connexion par câble` is a word-for-word calque no French tech writer produces — and it lands in the product's one-line definition. §5.2 already locks `un seul câble`. |
| 11 | `onecable/controls.mdx` | …et peut également **recevoir de l'alimentation**. | …et peut également **recevoir du courant**. | `recevoir de l'alimentation` is not a French collocation. `alimentation` is the supply; `courant` is what flows through the port. New glossary row added (§5.2). |
| 12 | `onecable/controls.mdx` | Ce port **reçoit uniquement de l'alimentation** et est utilisé pour&nbsp;: | Ce port **reçoit uniquement du courant** et est utilisé pour&nbsp;: | Same collocation, same page. `uniquement` keeps its EN scope (*only receives power*, i.e. not data/video). |
| 13 | `flip/installation.mdx`, `dual-flip/installation.mdx` | **Cela se fait facilement via** le port USB-A de votre ordinateur portable. | **Le port USB-A de votre ordinateur portable convient parfaitement pour cela.** | Textbook translationese: impersonal pronominal passive + `via`. French wants a concrete subject. Rendering matches the already-shipped `expand/installation.mdx` sentence — EN's two variants (*"This can easily be done via…"* / *"The USB-A port on your laptop works well for this"*) are null variance, collapsed to one French form per the E2/E3 precedent in `safety-align-fr.md`. |
| 14 | `expand/controls.mdx` ×3, `dual-flip/controls.mdx` ×3 | **transfert vidéo** | **transmission vidéo** | `transfert` implies moving files. EN alternates *video transfer* / *video transmission* with no meaning difference; `flip/controls.mdx` already ships `transmission vidéo`. Aligns with §5.4 `signal vidéo`. |
| 15 | `one-4k/installation.mdx`, `one-4k-oled/installation.mdx` | Si votre appareil **prend en charge la charge** via USB-C… | Si votre appareil **est compatible avec la recharge par** USB-C… | Cacophonous repeated root; EN *"supports charging"* has no such problem. *(The `l'écran se recharge` referent was **not** touched — it is faithful to EN and source-flagged as P9.)* |
| 16 | `one-4k/installation.mdx`, `one-4k-oled/installation.mdx` | **Avec la prise en charge de** Power Delivery (PD), le Screenmate passe… | **Lorsque Power Delivery (PD) est pris en charge**, le Screenmate passe… | Word-for-word calque of an English absolute phrase. The passive keeps EN's deliberate vagueness about *whose* PD support — the reviewer's suggested `Si votre appareil prend en charge…` would have added a fact EN withholds. |
| 17 | `infinity/index.mdx` | …pour vous offrir deux écrans supplémentaires **à la fois**. | …pour vous offrir **simultanément** deux écrans supplémentaires. | `à la fois` in final position reads as *at a time* (alternately), inverting EN's *at once*. `simultanément` keeps the meaning without dropping it. |
| 18 | `infinity-lite/controls.mdx` ×2 | **Basculement vers la gauche – règle** le rétroéclairage… | **Basculez vers la gauche pour régler** le rétroéclairage… | Nominal-style calque of *"Toggle left – adjusts…"*; every other bullet on the page is a `vous`-imperative. **Corrected 2026-08-12 (review M-7):** an earlier draft of this row claimed the U+2013 dash "was left as-is". It was not — the rewrite into a `pour`-infinitive **removes the dash entirely**, which is faithful to `en/manuals/infinity-lite/controls.mdx:51,55`. No U+2013 survives at these two lines. |
| 19 | `infinity-lite/installation.mdx` | Ouvrez le cadre **jusqu'au clic** pour le déployer. | Ouvrez le cadre **jusqu'au déclic** pour le déployer. | In French `clic` is a mouse click; the sound a mechanism makes when it latches is a `déclic`. Controller-verified. |

### 1.4 Wrong or unusable French words

| # | File(s) | Before | After | Why |
|---|---|---|---|---|
| 20 | `infinity/display-settings.mdx`, `infinity-lite/display-settings.mdx` | …vous devez choisir **l'entrée** **S6-R / Screenmate**… | …vous devez choisir **l'option** **S6-R / Screenmate**… | **False friend.** EN says *"the S6-R / Screenmate **entry**"* — a list item, not an input. The reader is in the macOS **Sortie** tab picking an output device; `l'entrée` sends them to the wrong tab. Controller asked to verify EN said "output": it does not, it says "entry", so the correct fix is `l'option`, not `la sortie`. |
| 21 | `infinity-lite/installation.mdx` | Maintenez des deux mains les deux **emplacements** indiqués par les flèches rouges… | Maintenez des deux mains les deux **points** indiqués par les flèches rouges… | You cannot hold an `emplacement` (a location/slot). EN *"hold both red arrow positions"*. `libérer l'écran unique` kept — faithful to EN's *"release the single screen"*. |
| 22 | `infinity-lite/installation.mdx` | …réglez-le sur le bon **angle d'appui**… | …réglez-le sur le bon **angle d'inclinaison**… | `angle d'appui` is not a French collocation (it reads as *bearing angle*). EN *"the correct support angle"* means the tilt of the stand. `bon` kept — EN says *correct*, not *desired*. |
| 23 | `panorama/installation.mdx` | …peut provoquer des **interférences**. | …peut provoquer **un conflit d'alimentation**. | **Meaning error on a glossary-locked term — flagged prominently.** §5.2 locked `interference → interférences`, which in French means *electromagnetic* interference. Here EN describes a second charger fighting the Panorama for the same laptop: a power-negotiation conflict. The French as shipped pointed the customer at the wrong phenomenon. Glossary §5.2 was split into an EM row (unchanged — it is the correct rendering for the `safety.mdx` "magnetic fields / transmitting equipment" line, ×8 files, all left alone) and a new power-conflict row. |
| 24 | `panorama/controls.mdx` | …connecter votre ordinateur portable à un **écran individuel**. | …connecter votre ordinateur portable à un **écran précis**. | `écran individuel` reads as a *personal/private* display; EN *"an individual screen"* means *one of the three panels*. `précis` carries the intended sense without inventing the count. |
| 25 | `one-4k/osd.mdx`, `one-4k-oled/osd.mdx` | L'option sélectionnée **est surlignée** en jaune. | L'option sélectionnée **apparaît en surbrillance** jaune. | `surligner` is the highlighter-pen sense; the French UI term for a highlighted menu item is *mise en surbrillance*. |
| 26 | `lite-144hz/index.mdx` | …doté d'un **taux de rafraîchissement rapide** de 144&nbsp;Hz | …doté d'un **taux de rafraîchissement élevé** de 144&nbsp;Hz | Collocation error in the product's opening sentence: in French a *taux* is *élevé*, never *rapide* (a rate is high or low, not fast). EN *"a fast 144 Hz refresh rate"* is fine English. |

### 1.5 Grammar and construction

| # | File(s) | Before | After | Why |
|---|---|---|---|---|
| 27 | `onecable/installation-mac.mdx`, `onecable/installation-windows.mdx` | Connectez le Screenmate (à votre ordinateur portable)**,** il est maintenant prêt à l'emploi. | Connectez le Screenmate (à votre ordinateur portable)**&nbsp;:** il est maintenant prêt à l'emploi. | Comma splice joining two independent clauses. The mac page already punctuates the identical sentence correctly seven lines earlier (`Connectez le Screenmate – il est maintenant prêt à l'emploi.`), so the page shipped two punctuations of one sentence. |
| 28 | `flip/installation.mdx`, `dual-flip/installation.mdx` | - **1 USB-C et 1 USB-A et 1 HDMI** | - **1 USB-C, 1 USB-A et 1 HDMI** | `et … et` in an enumeration is not French; EN's `&…&` is acceptable list shorthand. `expand/installation.mdx` and `infinity/installation.mdx` already ship the comma form. |
| 29 | `expand/installation.mdx` | Si votre ordinateur portable **ne dispose pas d'assez de** ports HDMI… | Si votre ordinateur portable **n'a pas assez de** ports HDMI… | The `de + assez de` sequence trips the reader mid-sentence; natives avoid it. |
| 30 | `flip/osd.mdx`, `expand/osd.mdx`, `dual-flip/osd.mdx` | choisissez RESET pour **rétablir tous les réglages à leurs valeurs d'usine**. | choisissez RESET pour **réinitialiser tous les réglages aux valeurs d'usine**. | `rétablir X **à** Y` is the English *restore X to Y* pattern; French has no such preposition. §5.4 already locks `rétablir les réglages d'usine`. Now locked as §6.2. |
| 31 | `dual-flip/osd.mdx`, `flip/osd.mdx`, `lite/osd.mdx`, `lite-144hz/osd.mdx` | **basculez le format d'image entre** 4:3 et WIDE | **basculez entre les formats** 4:3 et WIDE | `basculer` in the *switch between modes* sense is intransitive; transitive `basculer qqch` means to tip it over. `expand/osd.mdx` already shipped the correct intransitive form — all four now match it. Locked as §6.2. |
| 32 | `infinity/installation.mdx` | Assurez-vous que la **pièce centrale est bien centrée** sur votre ordinateur portable. | Assurez-vous que la **pièce centrale est bien positionnée au milieu de** votre ordinateur portable. | Repeated root. EN *"the center piece sits neatly in the middle"* uses two different words; the new French is closer to EN, not further. §5.1 `pièce centrale` kept. |
| 33 | `infinity-lite/installation.mdx` | …**afin d'éviter** tout dommage à l'appareil. Rangez votre Screenmate avec soin **afin d'éviter** d'endommager le matériel. | …afin d'éviter tout dommage à l'appareil. Rangez votre Screenmate avec soin **pour ne pas endommager** le matériel. | The same purpose clause twice in consecutive sentences about the same object. EN uses *to avoid* / *to prevent*. The first clause keeps the §6-locked `afin d'éviter tout dommage`; only the duplicate was rewritten. |
| 34 | `one-4k/osd.mdx`, `one-4k-oled/osd.mdx` | **Maintenez le bouton** situé au-dessus du bouton d'alimentation **enfoncé** pendant **10 secondes**… | **Maintenez enfoncé le bouton** situé au-dessus du bouton d'alimentation pendant **10 secondes**… | The past participle was stranded eleven words from its verb, forcing a re-parse. Antéposition before a long object is the standard French repair and keeps the §5.5 `Maintenez … enfoncé` frame. |
| 35 | `panorama/installation.mdx` | …le long câble blanc pour l'alimentation, et **le câble noir court**… | …le long câble blanc pour l'alimentation, et **le court câble noir**… | Two parallel noun phrases in one sentence with the adjectives on opposite sides. |
| 36 | `panorama/controls.mdx` ×2 | - **Diminuer/Augmenter des valeurs** telles que la luminosité ou le volume. | - **Diminuer/Augmenter les valeurs** telles que la luminosité ou le volume. | Partitive `des valeurs` where French takes the definite article before `telles que`. |

---

## 2 · Rejected — locked convention, or French is faithful and EN is fine

One line each. None of these was changed.

**Glossary-locked terminology (§5, §7, §9, §10):**

1. `Précision des couleurs` / `Gamme de couleurs` split — §5.6 lock; EN itself alternates *Color Accuracy* / *Color Gamut*. → source-flag H2/H3.
2. `Paysage (inversé)` for bare EN `Flipped` — §8 lock, already adjudicated; FR is the *correct* side. → E4.
3. Dutch UI glosses dropped in display-settings — deliberate FR localisation, §10.1.F / BT row 10.
4. `Lumière bleue faible (LOW BLUE LIGHT)` — §7 CAPS table + §7.2 gloss vocabulary. → §12 proposal R4-P4.
5. `écran portable triple` — §5.1 term + §9.2 descriptions (expand, panorama). → §12 proposal R4-P3.
6. `Real-Time Strategy (RTS)` / `First-Person Shooter (FPS)` left in English — §7.1 lock, explicit.
7. `câble double USB-A vers USB-C` — §2.1 lock, mirrors EN *dual USB-A to USB-C cable*.
8. Cable direction `USB-A vers USB-C` vs `USB-C vers USB-A` — §2.1 rule 2: order mirrors EN, reversing it is a factual error.
9. `1820 / 1900 / 2390 / 1261 / 3000 grammes` (reviewer T1) — §4 locks 4-digit thousands without separator and the spelled-out unit; §5.6 locks `1820 grams → 1820 grammes`.
10. `1200:1` without a thousands space next to `100 000:1` (T2) — §4 locks "4 digits: no separator, 5+ digits: plain space". Deliberate, gate ruling R5.
11. `Taille` vs `Taille de l'écran` (T3) — §5.6 has both; EN differs per product.
12. `(90 cm)`, `(1,2 m)` with a plain space in package lists (T4) — §5.7 locks these strings verbatim.
13. `-20&nbsp;°C` with an ASCII hyphen (T6) — §10 locked boilerplate, and the line sits in a **frozen** `safety.mdx`.
14. `Réglages d'affichage` vs `Réglages d'affichage et de son` (T7) — §9.1 lock; the EN titles genuinely differ.
15. `Voyant lumineux` / `Voyant LED` / `Voyant d'état` (T8) — §9.4 locks `### Indicator Light` and `### LED Indicator` separately.
16. `adaptateur secteur` vs `adaptateur CA/CC` (T9) — §5.2 locks both; EN uses *power adapter* and *AC/DC adapter* in different chapters.
17. `10 secondes` with a plain space (T10) — §4 applies `&nbsp;` between a number and a **unit symbol**; `secondes` is a word.
18. `«&nbsp;Min&nbsp;»` / `«&nbsp;Plus&nbsp;»` button labels — §9.4 + §10.2 locks; the labels come from EN. → source-flag P2.
19. `### 3 × ports Mini-HDMI` — §9.4 lock, and §4 names it as the one heading where `×` counts ports.
20. `moniteur DP` — §5.2 lock; `DP` is glossary open item #1.
21. `support de fixation` / `support réglable` / `pied` — §5.1 locks `bracket` and `adjustable stand` separately. → source-flag D17.
22. `Support pour écran unique` vs `support simple` caption — §5.7 and §10.1.D lock them separately.
23. `pochette de transport en cuir` vs `Étui de protection` — §5.1 locks both EN terms. → source-flag H7.
24. `clips de protection` vs `capuchon de protection` — §5.1/§5.7 locks. → source-flag H6.
25. `pieds de verrouillage` / `verrou avant` — §5.1 locks both.
26. `Le support pivote à 360°` — §10.1.D locked caption.
27. `Bouton d'alimentation et de retour`, `Bouton Menu (alimentation / OSD)`, `Bouton + (augmenter la luminosité)`, `### Double écran — avant et arrière à l'horizontale` — §9.4 locked headings; harmonising them would break heading parity with `en/`.
28. `espace à l'écran` (infinity-lite/index) — the phrase is the §10.1.F-locked rendering of *on-screen space*; changing it here would desync the locked question lead.
29. `**Luminosité -**` with an ASCII hyphen (onecable/controls) — EN writes `**Brightness -**` with an ASCII hyphen on that line; U+2212 is used only where EN uses it.
30. `Attention&nbsp;:` + `prenez garde à vos doigts` (panorama/installation) vs `Attention à vos doigts` (safety) — §6 locks `Caution: → Attention&nbsp;:` and `Watch your fingers → Attention à vos doigts`; the installation line carries both EN elements, so repeating "Attention" was correctly avoided.
31. `fonctionne en plug-and-play` — the reviewer recorded this as preference, not error.

---

## 3 · Source-flagged — 39 items

Full write-up in **`translations/qa/round4/source-flags-fr.md`**, grouped as:

- **A · Safety-relevant (2)** — the 5 V vs 5–20 V contradiction across 8 products (**Critical**, the only Critical in the corpus that is not a product-fact question), and the unactionable *motherboard indicator light* step.
- **B · Product facts (9)** — the infinity multifunction-button mapping (**Critical**), the `Min`/`Plus` Dutch labels, the Lite power-button/scroll-wheel inversion, infinity-lite's plural *"both extension screens"* on a single-screen product (**Critical**, EN-verified), contradictory port numbering, the undocumented "connection mode", panorama's 360° viewing angle, the dual-flip/flip tilt-angle parentheticals, and the "the screen charges" battery implication.
- **C · Headings and labels documenting the wrong thing (12)** — including *"Charging the Screenmate OneCable"* over a reverse-charging section, the *Color Accuracy* mislabel and its opposite-direction tab split in flip/expand, the two contradictory *"first check which ports…"* headings, and *"so your screen is clamped tightly"*.
- **D · Style/register inherited from EN (18)** — the announced-but-missing bullet list, the leaked `Day Mode` / `Night Mode` alt text, the colour-temperature-as-intensity description, `"gestures"` for button presses, `"1× USB"` as a port type, the duplicated display-settings block in infinity-lite, and the device-naming drift.
- **E · Already on the client list (3)** — `'Flipped'`, the three-way safety H3 split, and the null EN variances.

---

## 4 · Deferred

Real observations, but taste-level or unfixable without drifting from the source. No edit made.

1. `menu de raccourci de la luminosité` (one-4k, one-4k-oled, panorama) — EN *"the brightness shortcut menu"*; any French repair either keeps the awkward `menu de raccourci` or drops the *menu* node EN names.
2. `Voyant d'état indiquant l'alimentation et l'état du signal` (one-4k) — `état … état`, but EN repeats *status … state* the same way; the natural repairs all shift *state* → *presence*.
3. `Le port principal est destiné aux données et à la vidéo, le port Power sert uniquement à l'alimentation.` — parallel juxtaposition by comma is idiomatic French (unlike the sequential comma splice fixed in #27).
4. `Augmente la luminosité en utilisation normale, et permet de naviguer…` (dual-flip/controls) — comma-before-`et` mirrors EN's comma; grammatical.
5. `réglez la transparence du menu OSD pour une meilleure visibilité` (lite, lite-144hz) — EN's *"for a better view"* is genuinely ambiguous; see source-flag D7.
6. `Faites un clic droit sur votre Bureau` (display-settings ×4) — `le Bureau` is the French Windows form, but `votre` mirrors EN's possessive and the line sits in the checksum-frozen 4-product chapter; not worth a 4-file propagation for a Minor.
7. `Cela évite une alimentation instable.` (onecable/installation) — flat but grammatical and faithful.
8. `se déplie en deux écrans supplémentaires` (dual-flip/index) — EN *"unfolds into two extra displays"*; `se déplier en` is defensible.
9. `La disposition est en miroir sur l'écran gauche et sur l'écran droit.` (infinity/controls) — heavy, faithful.
10. `Réservé au câble HDMI vers USB-C lorsque la vidéo et l'alimentation sont séparées.` (infinity-lite/controls) — elliptical, but every repair adds detail EN does not give.
11. `Téléchargez … la page de téléchargement de Silicon Motion` (panorama/installation) — EN repeats *download* identically; unremarkable in both languages.

**For a native reviewer — style suggestions on the FROZEN `safety.mdx` bodies (not applied):**
`Évitez … afin d'éviter …`, `espaces humides` for *damp environments*, `comme alimentation` for
*as power supply*, `Maintenez les ouvertures de ventilation dégagées`, `ampérage`,
`les équipements émetteurs`, `Convient à un usage domestique comme professionnel.` (verbless
fragment), and the four-way product naming (`le moniteur` / `l'appareil` / `l'écran` /
`votre Screenmate`) across fourteen numbered lines. All are logged as glossary §12 proposals
**R4-P5**, **R4-P6** and **R4-P7**; each touches a §10-locked string inside a byte-identical frozen
group (7 files and 3 files respectively) and needs sign-off plus a full-group re-propagation.

---

## 5 · Glossary changes

| Change | Section | Why |
|---|---|---|
| **New ruling: the `…&nbsp;? … alors …` rhythm is banned** | **§6.1** (new) | Codifies §1.1 with the 4 corrected patterns, the "keep the question, drop `alors`" rule, the existing corpus model, and a defect grep. |
| **New ruling: three banned constructions** | **§6.2** (new) | `Vérifiez si` → `Vérifiez que`; `rétablir X à Y` → `réinitialiser X aux valeurs d'usine`; transitive `basculer le format` → intransitive `basculer entre`. |
| **Row corrected:** `Then proceed to step 5` | §6 | `Passez alors directement à l'étape&nbsp;5` → `Passez directement à l'étape&nbsp;5`. **The only locked string this pass changed.** Amended per §0 precedence rule 3. |
| **Row split + corrected:** `interference` | §5.2 | EM sense keeps `interférences` (correct, and used correctly ×8 in `safety.mdx`); a second row adds `conflit d'alimentation` for the power-negotiation sense with the panorama citation. **Meaning error on a locked term — see fix #23.** |
| **Row added:** `receive power (a port)` | §5.2 | `recevoir du courant`, with the reason `recevoir de l'alimentation` is wrong. |
| **7 proposals logged, not applied** | §12 "Round-4 proposals" | R4-P1…R4-P7 — every §10-locked string flagged by the reviewers, with the proposed French, the file spread and which reviewer raised it. |

---

## 6 · Verification

All commands run from the repo root on `round4-fixes` after every edit was applied.

### 6.1 Translation gate

```
$ python scripts/verify_translation.py --base en --targets fr --include-nl
0 FAIL, 0 WARN
```

Identical to the pre-edit baseline (`0 FAIL, 0 WARN`) — **no new warn classes**.

### 6.2 Test suite

```
$ python -m pytest tests/test_verify_translation.py -q
....................                                                     [100%]
20 passed in 0.21s
```

### 6.3 `safety.mdx` bodies unchanged

```
$ git diff --stat -- 'fr/manuals/*/safety.mdx'
(empty)
```

**No French safety chapter was touched.** All safety-page style findings are logged above and as
§12 proposals R4-P5/P6/P7.

### 6.4 `display-settings` body identity — the 4-product frozen group

Frontmatter stripped (`awk 'BEGIN{c=0} /^---$/{c++; next} c>=2{print}' FILE | md5sum`):

| Product | FR body md5 | EN body md5 |
|---|---|---|
| `onecable` | `ec24415c0551ca0628b4f8b22c7a6bdc` | `467551f5a59279929d98a427fcdce9d0` |
| `flip` | `ec24415c0551ca0628b4f8b22c7a6bdc` | `467551f5a59279929d98a427fcdce9d0` |
| `dual-flip` | `ec24415c0551ca0628b4f8b22c7a6bdc` | `467551f5a59279929d98a427fcdce9d0` |
| `expand` | `ec24415c0551ca0628b4f8b22c7a6bdc` | `467551f5a59279929d98a427fcdce9d0` |

**4 identical FR hashes, matching the 4 identical EN hashes** — the FR sharing group still equals
the EN sharing group. The hash is unchanged from the value recorded in `safety-align-fr.md`
(`ec24415c`), because no edit landed in this chapter: the two `l'entrée → l'option` fixes are in
`infinity` and `infinity-lite`, which have their own distinct bodies.

### 6.5 Twin-product parity

Diffing the edited lines of each twin pair:

| Pair | Result |
|---|---|
| `lite` / `lite-144hz` — `installation.mdx`, `osd.mdx` | **identical edits** |
| `lite` / `lite-144hz` — `index.mdx` | only the 144 Hz-only sentence differs (`taux de rafraîchissement rapide → élevé`); `lite/index.mdx` has no refresh-rate sentence, matching EN |
| `one-4k` / `one-4k-oled` — `osd.mdx` | **identical edits** |
| `one-4k` / `one-4k-oled` — `installation.mdx` | `alors` fix is one-4k-only because `one-4k-oled` has no *"Need extra power?"* paragraph — a pre-existing EN divergence, not drift |

### 6.6 Residual greps

```
$ grep -rn "alors" fr/            → 1 hit, panorama/installation.mdx:66 ("alors que", the conjunction)
$ grep -rn "Vérifiez si" fr/      → 0 hits
$ grep -rn "transfert vidéo" fr/  → 0 hits
$ grep -rn "rétablir tous les réglages" fr/ → 0 hits
$ grep -rn "Cela se fait" fr/     → 0 hits
$ grep -rn "prend en charge la charge" fr/ → 0 hits
```

---

# 7 · Fix round 2 — responses to `review-fr.md`

**Date:** 2026-08-12 · Review verdict: **NEEDS FIXES** — 0 Critical, 1 Important, 8 Minor.
All 9 findings addressed below: **4 page/glossary fixes applied, 2 documentation corrections,
3 recorded-only (no change warranted).**

## 7.1 · I-1 (REQUIRED) — the cross-paragraph conditional

`fr/manuals/onecable/installation.mdx:44`. The review is right and this was a real regression:
sites #1 and #2 of the `alors` class are **not** the same shape. Site #2's question and answer are
separate paragraphs, so `alors` was the only thing scoping the imperative to the one-USB-port case.
Verified independently — both sources carry an explicit connector across the break:

| | |
|---|---|
| `en/manuals/onecable/installation.mdx:44` | *"**Then** connect the other USB cable to a power outlet."* |
| `nl/manuals/onecable/installation.mdx:44` | *"Sluit **dan** de andere USB-kabel aan op het netstroom."* |

| Before (shipped in `aea5af3`) | After |
|---|---|
| `Branchez l'autre câble USB sur une prise de courant.` | `Dans ce cas, branchez l'autre câble USB sur une prise de courant.` |

`Dans ce cas` restores the condition without reintroducing the banned `alors` rhythm, and keeps the
two paragraphs separate so the block structure still matches `en/`.

**Glossary §6.1 gained the carve-out** in the same commit: *the rule applies inside a sentence; across
a paragraph break, replace `alors` with `Dans ce cas`, do not delete it* — with the EN/NL evidence, a
wrong/right pair, and the note that of the nine corrected sites eight are intra-sentence and one is
cross-paragraph. Re-audited the other eight: **all confirmed intra-sentence, all still correct.**

## 7.2 · M-2 — the §6.1 defect grep repaired

The published guard was doubly broken and is replaced by **two passes**:

```
# 1. same-sentence form
grep -rnE '&nbsp;\?[^|]*\balors\b' fr/

# 2. cross-paragraph form — needs PCRE
LC_ALL=C.UTF-8 grep -rlzP '&nbsp;\?\s*\n\s*\n[^\n]*\balors\b' fr/
```

Two defects confirmed by reproduction against `ebbda95`:

1. **Dead alternative.** The old first alternative `\?\*{0,2}&nbsp;\? [^.]*\balors\b` finds **0**
   lines on its own (it needs a literal `?` before optional asterisks before `&nbsp;?`, which never
   occurs). The full old expression found 8 — all from the second alternative. Removed.
2. **The carve-out was unguardable.** The review's suggested `-E` replacement still misses it:
   GNU grep's **POSIX ERE reads `\n` as a literal `n`**, so the `&nbsp;\?\n\n…` alternative matches
   nothing. It appeared to work only because the same file also contains site #1. Verified:
   `grep -czE '&nbsp;\?\n\n[^\n]*\balors\b' fr/manuals/onecable/installation.mdx` → **0**;
   the PCRE form → **matches**. Hence PCRE, and hence two passes rather than one.

Validation on the pre-fix tree: pass 1 → the 8 intra-sentence sites; pass 2 → exactly
`fr/manuals/onecable/installation.mdx`. Post-fix, both return nothing. A "do not simplify these
back into one expression" warning is now in the glossary.

## 7.3 · M-3 — the USB-A Note follows the Dutch, not EN-expand

The review is right that the null-variance justification was wrong, and the **NL tiebreaker settles
it in the opposite direction** from the collapse target chosen in round 1:

| | |
|---|---|
| `nl/…/flip:76`, `nl/…/dual-flip:50`, `nl/…/expand:63` | *"Dit kan **gemakkelijk** via de USB-A-poort van je laptop."* — **all three** |
| `en/…/flip:76`, `en/…/dual-flip:50` | *"This can **easily** be done via your laptop's USB-A port."* |
| `en/…/expand:63` | *"The USB-A port on your laptop works well for this."* — **the drifted side** |

So `convient parfaitement` was modelled on the one English sentence that had already lost the Dutch
`gemakkelijk`. Fixed at the two sites the round-1 pass touched:

| File | Before | After |
|---|---|---|
| `flip/installation.mdx:76` | Le port USB-A de votre ordinateur portable **convient parfaitement pour cela**. | Le port USB-A de votre ordinateur portable **permet de le faire facilement**. |
| `dual-flip/installation.mdx:50` | *(identical)* | *(identical)* |

`expand/installation.mdx:63` is **deliberately left** at `convient parfaitement pour cela` — that
line predates this round and is faithful to its own EN. French now mirrors the real EN per-file
split instead of flattening it. The EN-expand drift is logged as **source-flag D19**, with the note
that if EN-expand is repaired the three should collapse onto the `facilement` sentence.

## 7.4 · M-4 — `conflit d'alimentation` stands, with a client flag

Kept: `interférences` genuinely read as EMI and misdirected the reader, so the change is a net
improvement whichever way the client rules. But the review is right that the replacement is more
specific than either source (EN *"interference"*, NL *"storingen"* — both generic). Logged as
**source-flag F1** in a new section *"French is more specific than both sources — for the native
reviewer to confirm"*, with the two ways to close the gap: fix EN/NL to say what they mean, or
soften the French to `des perturbations` / `des dysfonctionnements`. No page or glossary change.

## 7.5 · M-6 — `écran précis` → `l'un des écrans`

Accepted. `précis` means *specific*, where EN:27 says *"an **individual** screen"* and NL:27 says
*"een **los** beeldscherm"* (= *a separate screen*) — both meaning **one of the three panels**.

| Before | After |
|---|---|
| …pour connecter votre ordinateur portable à un **écran précis**. | …pour connecter votre ordinateur portable à **l'un des écrans**. |

(The original `écran individuel` remains correctly rejected: in French it reads *personal/private*.)

## 7.6 · M-7 — stale dash claim corrected

Fixlog §1.3 row #18 claimed the U+2013 dash "was left as-is". It was not: rewriting
`Basculement vers la gauche – règle…` into `Basculez vers la gauche pour régler…` removes the dash
entirely, which is faithful to `en/manuals/infinity-lite/controls.mdx:51,55`. The row now says so.
**Documentation-only correction — the shipped edit was and remains correct.**

## 7.7 · Recorded only — no change warranted

| # | Item | Disposition |
|---|---|---|
| **M-5** | `angle d'appui` → `angle d'inclinaison` renames *support angle* to *tilt angle* | The review's own conclusion: `angle d'appui` is a non-collocation, no French phrasing of "support angle" is idiomatic, and the stand's adjustable property *is* its inclination. Recorded, not reversed. |
| **M-8** | Two intentional harmonisations: the `RESET` bullet (3 files — EN alternates *their factory defaults* / *factory defaults*) and `transmission vidéo` (6 hunks — EN alternates *video transfer* / *video transmission*) | Both are null EN variance with no French distinction available, collapsed per the E2/E3 precedent in `safety-align-fr.md`. Flagged here for whoever maintains EN↔FR parity: these are harmonisations, not mirrors. |
| **M-9** | `onecable/index.mdx:19` drops the *connection* node (EN *"one cable connection"*, NL *"één kabelaansluiting"*) | `connexion par câble` was a genuine calque; the dropped noun carries no information the sentence needs and `à l'aide d'un seul câble` is the right register for a product one-liner. Recorded. |

## 7.8 · Revised counts

| Outcome | Round 1 | After fix round 2 |
|---|---|---|
| Fixed (distinct findings) | 33 | **36** (+I-1, +M-3, +M-6) |
| Replacements / files touched | 60 / 31 | **64 / 31** (4 further replacements, all in files already in scope) |
| Rejected | 31 | 31 |
| Source-flagged | 39 | **41** (+D19, +F1) |
| Deferred / recorded-only | 11 | **14** (+M-5, +M-8, +M-9) |
| Glossary changes | 5 | **6** (+§6.1 carve-out; §6.1 grep replaced; §6 row annotated) |

## 7.9 · Verification after fix round 2

```
$ python scripts/verify_translation.py --base en --targets fr --include-nl
0 FAIL, 0 WARN

$ python -m pytest tests/test_verify_translation.py -q
....................                                                     [100%]
20 passed
```

Unchanged from baseline — **no new WARN class**.

**Frozen `safety.mdx`, against the pre-round-4 merge base:**

```
$ git diff --stat a0525eb..HEAD -- 'fr/manuals/*/safety.mdx'
(empty)
```

**`display-settings` 4-group body md5** (frontmatter stripped):

| Product | FR body | EN body |
|---|---|---|
| `onecable` / `flip` / `dual-flip` / `expand` | `ec24415c0551ca0628b4f8b22c7a6bdc` ×4 | `467551f5a59279929d98a427fcdce9d0` ×4 |

Unchanged; the FR sharing group is still congruent with the EN sharing group.

**Structural parity:** heading counts identical to `en/` in all 62 files; `git diff --numstat` for
this round shows **4 added / 4 deleted**, balanced 1:1 in each of the 4 files — replacements only,
no line added or removed.

**Defect greps, current tree:**

```
$ grep -rnE '&nbsp;\?[^|]*\balors\b' fr/                              → 0
$ LC_ALL=C.UTF-8 grep -rlzP '&nbsp;\?\s*\n\s*\n[^\n]*\balors\b' fr/   → 0
$ grep -rn 'alors' fr/        → 1 (panorama/installation.mdx:66, the conjunction 'alors que')
$ grep -rn 'écran précis' fr/ → 0
$ grep -rn 'convient parfaitement pour cela' fr/ → 1 (expand/installation.mdx:63, deliberate — D19)
```
