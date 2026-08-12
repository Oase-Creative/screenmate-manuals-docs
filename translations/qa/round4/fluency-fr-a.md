# Revue de fluidité monolingue — FR (lot A)

**Reviewer:** native French technical editor — monolingual read, French only (no `en/` or `nl/` file opened)
**Scope:** `fr/manuals-index.mdx` · onecable (8 pages) · lite (4 + safety frontmatter) · lite-144hz (4 + safety frontmatter) · flip (4 + safety/display-settings frontmatter) · expand (4 + safety/display-settings frontmatter)
**Date:** 2026-08-12 · **Mode:** READ-ONLY — no content file, `docs.json` or asset was modified.

Treated as deliberate and NOT flagged: formal *vous*; English technical terms (DisplayPort, HDMI, USB-C, OSD, DRIVERS (D:), product names, ALL-CAPS OSD labels); `charge inversée (reverse charging)`; French number/SI/non-breaking-space typography.

**Baseline, verified before the error hunt:** no *tu* leakage anywhere (grep-verified across all 24 files); no gender or agreement errors found; subjunctives correct and unforced; `&nbsp;` present before every `:` `;` `?` `!` in prose (grep found zero violations); guillemets `«&nbsp;…&nbsp;»`, decimal commas and `×` for dimensions used consistently; apostrophes uniformly straight (U+0027), no mixed U+2019.

Per the brief, **every Critical and Major is reported below, per file**. Minors are consolidated into a single capped table at the end (15 items, the most worthwhile of ~54 observed).

---

# CRITICAL

## fr/manuals/onecable/safety.mdx — body shared verbatim by lite, lite-144hz, flip, expand

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « 5. Le moniteur fonctionne avec une entrée CC comprise entre 5&nbsp;V et 20&nbsp;V (avec une tolérance de ±2&nbsp;V). » **vs** « 6. Utilisez l'appareil **uniquement** avec une source d'alimentation de 5&nbsp;V via le câble approprié. » | Direct contradiction on the safety page, visible reading French alone: item 5 authorises 5–20 V, item 6 restricts to 5 V with `uniquement`. A customer holding a 20 V USB-C PD charger cannot tell whether they are about to damage the monitor — and this page ships identically on all five products. Probably inherited from the source; it must be resolved either way, because as published the French is unsafe to follow. | If item 6 is about the bundled cable: « 6. Pour une alimentation en 5&nbsp;V, utilisez impérativement le câble fourni. » — otherwise delete item 6 as redundant with item 5. | **CRITICAL** |

---

# MAJOR — per file

## fr/manuals-index.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « Votre QR code **devrait vous avoir mené** directement au manuel de votre produit. » | Conditional-past calque of *should have taken you*. `devrait vous avoir mené` is a heavy compound tense that French consumer copy avoids; a native states the fact. | « En principe, votre QR code vous a conduit directement au manuel de votre produit. » | Major |

## fr/manuals/onecable/index.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « …en ajoutant deux écrans supplémentaires à votre ordinateur portable **avec une seule connexion par câble**. » | Word-for-word calque (*with a single cable connection*). `connexion par câble` is not something a French tech writer produces — and it lands in the product's one-line definition. | « …en ajoutant deux écrans supplémentaires à votre ordinateur portable à l'aide d'un seul câble. » | Major |
| « **Pour une utilisation économe en énergie**, nous vous recommandons de débrancher le câble d'alimentation… » | Adverbial calque (*voor energiezuinig gebruik*); French states the goal with a verb. Recurs verbatim in `flip/index.mdx` and `expand/index.mdx`. | « Pour économiser l'énergie, nous vous recommandons de débrancher le câble d'alimentation lorsque le moniteur n'est pas utilisé. » | Major |
| Spec row « **Précision des couleurs** \| 100&nbsp;%&nbsp;sRGB » | Wrong French concept: *précision des couleurs* = colour accuracy (ΔE), not gamut coverage. The trade term for a % sRGB/NTSC figure is *gamme de couleurs* / *couverture colorimétrique*. Same wrong label in `lite/index.mdx` (99 % sRGB) and `lite-144hz/index.mdx`. | « **Gamme de couleurs** \| 100&nbsp;%&nbsp;sRGB » | Major |

## fr/manuals/onecable/controls.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « Ce port … peut également **recevoir de l'alimentation**. » / « Ce port **reçoit uniquement de l'alimentation** et est utilisé pour… » | Not a French collocation — one *reçoit du courant*, or *est alimenté*. Twice on one page. | « …et peut également assurer l'alimentation. » / « Ce port sert uniquement à l'alimentation. Il est utilisé pour… » | Major |

## fr/manuals/onecable/installation.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « La puissance de sortie est-elle inférieure à 10&nbsp;W&nbsp;? Une alimentation supplémentaire est **alors** nécessaire… » | **The signature translationese of the corpus.** Rhetorical question + `alors` answer is the Dutch `…? Sluit dan…` construction; French uses a conditional clause. Six occurrences: here ×2 (« Vous n'avez qu'un seul port USB… ? Branchez **alors** … »), `lite/installation.mdx` + `lite-144hz/installation.mdx` (« Besoin d'une alimentation supplémentaire&nbsp;? Utilisez **alors** … »), `installation-mac.mdx` (« … figure déjà dans la liste&nbsp;? Passez **alors** directement à l'étape&nbsp;5. »), `troubleshooting.mdx` (« Votre chargeur … n'a-t-il pas de sortie USB-C&nbsp;? Utilisez **alors** … »). The bare question alone is idiomatic French marketing; the `alors` is the tell. | « Si la puissance de sortie est inférieure à 10&nbsp;W, une alimentation supplémentaire est nécessaire pour que le Screenmate fonctionne de manière stable. » — and delete `alors` everywhere else. | Major |
| Heading « ## **Recharger le Screenmate OneCable** » over a section ending « Votre ordinateur portable se recharge désormais via le Screenmate » | The heading promises charging *the monitor*; the section explains charging *the laptop*. A French reader scanning the TOC for "how do I charge my monitor" is sent to the wrong place. | « ## Recharger votre ordinateur portable via le Screenmate (charge inversée) » | Major |
| « 3. Placez fermement **le support de fixation** sur une surface plane. » + « 4. **Le support réglable** se trouve à l'arrière du Screenmate. » | Two names in consecutive steps with nothing telling the reader whether it is one part or two; and a *support de fixation* (mounting bracket) that one lays on a table is semantically odd in French. The reader cannot map the words to the hardware in front of them. | Name each part once and reuse: « 3. Posez le Screenmate bien à plat sur une surface stable. » / « 4. Le pied réglable se trouve à l'arrière du Screenmate. » | Major |

## fr/manuals/onecable/installation-mac.mdx (+ installation-windows.mdx)

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « 6. Connectez le Screenmate à votre ordinateur portable**,** il est maintenant prêt à l'emploi. » — and `installation-windows.mdx` step 5 « Connectez le Screenmate**,** il est maintenant prêt à l'emploi. » | Comma splice joining two independent clauses. Worse, the *same* file solves it correctly seven lines earlier: « Connectez le Screenmate – il est maintenant prêt à l'emploi. » So the page punctuates the identical sentence two ways. | « Connectez le Screenmate&nbsp;: il est maintenant prêt à l'emploi. » in all three places. | Major |

## fr/manuals/onecable/safety.mdx (shared page)

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « 2. Utilisez uniquement l'adaptateur CA/CC fourni **comme alimentation**. » | Calque of *as the power supply*; French needs *comme source d'alimentation* or drops the phrase. Safety page — the sentence should be beyond reproach. | « 2. Utilisez uniquement l'adaptateur secteur CA/CC fourni. » | Major |
| « 7. **Évitez** toute exposition à l'humidité, à la poussière et à l'électricité statique afin d'**éviter** tout dommage aux composants électroniques. » | The same verb twice in one short sentence — no French editor lets this through. | « 7. Évitez toute exposition à l'humidité, à la poussière et à l'électricité statique afin de ne pas endommager les composants électroniques. » | Major |
| « le moniteur » (items 1, 5, 10) / « l'appareil » (6, 9) / « l'écran » (8, 14) / « votre Screenmate » (intro) | Four names for the product in fourteen numbered lines, with no discernible rule — item 8 says « Nettoyez l'écran », item 10 « Ne faites pas tomber le moniteur ». On a safety page this reads as though different objects were meant. | Fix one term — « le moniteur » — and reserve « l'écran » for the panel surface only. | Major |

## fr/manuals/onecable/troubleshooting.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « **Vérifiez si** le voyant … est allumé. » / « **Vérifiez si** votre ordinateur portable fournit une puissance suffisante. » / « **Vérifiez si** l'ordinateur portable fournit… » / « **Vérifiez si** l'icône du pilote est visible… » | Four occurrences of the `controleer of` calque. In French `vérifier si` = *find out whether* (an open question); an instruction takes `vérifiez que` / `assurez-vous que`. The most repeated register slip in the corpus. | « Vérifiez que le voyant … est allumé. » / « Assurez-vous que votre ordinateur portable fournit une puissance suffisante. » | Major |
| « Vérifiez si le voyant de la **carte mère** est allumé. » | A French customer cannot see a *carte mère* on a sealed portable monitor — the very first troubleshooting instruction is unactionable. | « Vérifiez que le voyant d'alimentation du moniteur est allumé. » (confirm which LED is meant) | Major |
| « C'est possible **si les conditions suivantes sont réunies&nbsp;:** Le port USB-C … prend en charge Power Delivery (PD). La connexion est établie avec un câble USB-C. L'alimentation est compatible PD. » | The colon announces a list; three flat sentences then run on inside one paragraph. French readers expect the bullets the sentence just promised, and the three conditions are hard to separate at a glance. | Set the three conditions as a bulleted list. | Major |

## fr/manuals/lite/controls.mdx + fr/manuals/lite-144hz/controls.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « ### **Bouton d'alimentation et de retour** — Mode général · Appuyez pour ouvrir le menu des réglages à l'écran (OSD) », while « ### **Molette** — Appui court&nbsp;: allumer l'appareil / Appui long&nbsp;: éteindre l'appareil » | Read in French only: the control named *d'alimentation* never powers anything, and the *Molette* does. `osd.mdx` repeats the same pairing, so the contradiction is corpus-wide. Likely inherited from the source and needs a hardware check — but as published it misdirects a French reader looking for the power button. | If the wheel is the power control: « ### Molette (marche/arrêt et navigation) » + « ### Bouton Menu / Retour ». | Major |

## fr/manuals/lite/osd.mdx + fr/manuals/lite-144hz/osd.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « **RTS&nbsp;:** optimisé pour les jeux **Real-Time Strategy** (RTS). » / « **FPS&nbsp;:** optimisé pour les jeux **First-Person Shooter** (FPS). » | The OSD label (RTS/FPS) rightly stays English, but the *gloss* exists precisely to explain the label — left in English it explains nothing and the line becomes circular for a French reader. | « optimisé pour les jeux de stratégie en temps réel (RTS). » / « optimisé pour les jeux de tir à la première personne (FPS). » | Major |
| « **Température de couleur&nbsp;:** choisissez User, Warm ou Cool pour ajuster **l'intensité globale des couleurs**. » | Colour temperature adjusts warmth/tone, not intensity — the French sentence describes saturation instead. A reader who follows it looks for the wrong effect and concludes the setting is broken. | « …pour ajuster la tonalité générale des couleurs (chaude ou froide). » | Major |

## fr/manuals/lite-144hz/index.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « …doté d'un **taux de rafraîchissement rapide** de 144&nbsp;Hz » | Collocation error: in French a *taux* is *élevé*, never *rapide* (a rate is high or low, not fast). It sits in the product's opening sentence. | « …doté d'un taux de rafraîchissement élevé de 144&nbsp;Hz » | Major |

## fr/manuals/flip/index.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| Tab « Flip 14" »&nbsp;: « **Gamme de couleurs** \| 45&nbsp;%&nbsp;NTSC » **vs** Tab « Flip 15,6" »&nbsp;: « **Précision des couleurs** \| 45&nbsp;%&nbsp;NTSC » | Two labels for the identical spec row in two tabs of one page — the reader sees the switch happen when toggling tabs. `Gamme de couleurs` is the correct term. | « **Gamme de couleurs** » in both tabs. | Major |

## fr/manuals/flip/installation.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « Pour déterminer les câbles dont vous avez besoin, vérifiez d'abord **quels ports sont concernés**. » | `quels ports sont concernés` is vague to the point of being unusable — concerned by what? The reader cannot tell whether to look at the monitor or at the laptop, which is exactly what the sentence is supposed to tell them. | « …vérifiez d'abord de quels ports vous disposez. » | Major |
| « ### Flip 14" — Vérifiez d'abord de quels ports dispose **le Screenmate**. » **vs** « ### Flip 15,6" — Vérifiez d'abord de quels ports dispose **votre ordinateur portable**. » | Two parallel size headings give contradictory instructions, as if the 14" and 15,6" procedures genuinely differed. Nothing in the French explains the difference, so the reader assumes they missed something. | Make both say the same thing (check the laptop's ports; the Screenmate's ports are shown in the image). | Major |

## fr/manuals/flip/osd.mdx + fr/manuals/expand/osd.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « choisissez RESET pour **rétablir tous les réglages à leurs valeurs d'usine**. » (both files) | `rétablir X à Y` is an English/Dutch pattern; the French construction has no such preposition — one *rétablit les réglages d'usine* or *restaure les valeurs d'usine*. | « …pour rétablir les réglages d'usine. » | Major |
| flip: « **Source (SOURCE)&nbsp;:** choisissez **parmi deux** sources de signal&nbsp;: Type-C1 / Type-C2 et HDMI. » · expand: « choisissez **entre deux** sources… » | The sentence announces two sources, then lists three items (Type-C1, Type-C2, HDMI). A French reader counts, stops and re-reads. Bonus inconsistency: `parmi` vs `entre` between the two files. | « **Source (SOURCE)&nbsp;:** choisissez la source du signal&nbsp;: Type-C1, Type-C2 ou HDMI. » | Major |
| « **Lumière bleue faible** (LOW BLUE LIGHT)&nbsp;: réduit la quantité de lumière bleue… » (both files) | Word-for-word calque of the English label. No French product labels this feature *Lumière bleue faible*; the established terms are *Filtre de lumière bleue* / *Réduction de la lumière bleue*. As written it reads as a description of the screen rather than a setting. | « **Réduction de la lumière bleue (LOW BLUE LIGHT)&nbsp;:** » | Major |

## fr/manuals/expand/index.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| Frontmatter description « Manuel d'utilisation complet de votre **écran portable triple Screenmate Expand**, disponible en 14" et 15,6" » + body « Le Screenmate Expand est un **écran portable triple** qui… » | `écran portable triple` is self-contradictory in French (a single screen that is triple), and the description stacks two adjectives in front of the brand name so the noun phrase has to be re-read. This is both the page's opening sentence and its search-result snippet. | Description: « Manuel d'utilisation complet du Screenmate Expand, l'écran portable à triple affichage, disponible en 14" et 15,6". » · Body: « Le Screenmate Expand est un écran portable double qui se fixe sur votre ordinateur portable… » | Major |
| Box contents « **6 clips de protection** » **vs** `installation.mdx` « ## **Capuchon de protection** … utilisez le capuchon de protection » | The accessory the installation page tells you to fit is not listed under that name in the box contents, and vice versa. A French customer with the open box cannot identify the part being referred to. | One name in both places (« clips de protection » or « capuchons de protection », whichever matches the hardware). | Major |
| Tab « Expand 15,6" »&nbsp;: « **Précision des couleurs** \| 72&nbsp;%&nbsp;NTSC » **vs** Tab « Expand 14" »&nbsp;: « **Gamme de couleurs** \| 45&nbsp;%&nbsp;NTSC » | Same tab-to-tab label mismatch as flip, in the opposite direction. | « **Gamme de couleurs** » in both tabs. | Major |

## fr/manuals/expand/installation.mdx

| Quoted French | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| « 3. Placez le support de fixation contre l'arrière de l'écran de votre ordinateur portable et assurez-vous qu'il tient fermement, **de sorte que votre écran soit bien serré**. » | Read in French, this instructs the customer to clamp their laptop screen tight: *serrer un écran* suggests squeezing the panel. Alarming to read and a genuine over-tightening risk on a laptop lid. | « …et assurez-vous qu'il tient fermement, afin que le Screenmate reste bien en place sur votre écran. » | Major |
| « Si votre ordinateur portable **ne dispose pas d'assez de** ports HDMI… » | The `de + assez de` sequence trips the reader mid-sentence; natives avoid it. | « Si votre ordinateur portable n'a pas assez de ports HDMI… » | Major |

---

# MINOR — capped at the 15 most worthwhile

(~54 low-severity items were observed; the brief caps the list, so these are the ones worth an editor's time. The rest are single-instance wording preferences.)

| # | File | Quoted French | Issue | Suggested rewrite |
|---|---|---|---|---|
| 1 | onecable/troubleshooting.mdx + onecable/index.mdx vs lite/flip/expand | « le câble **double USB-A vers USB-C** » / « 2 câbles **USB-A vers USB-C** » vs « câble **USB-C vers USB-A** » everywhere else | Same physical cable named in two directions across the French corpus; `câble double` also reads as *two cables*. | Fix one direction corpus-wide; « câble en Y USB-C vers USB-A ». |
| 2 | onecable/safety.mdx (shared) | « Température ambiante recommandée&nbsp;: entre **-20**&nbsp;°C et 60&nbsp;°C. » | Hyphen-minus instead of the true minus `−` (which the corpus does use for the flip/expand buttons); and *recommandée* is odd for a −20…60 °C span, which is a tolerated range. | « Température ambiante admissible&nbsp;: entre −20&nbsp;°C et 60&nbsp;°C. » |
| 3 | onecable/controls.mdx | « **Luminosité -** (écran gauche) » | Hyphen-minus for the minus button, while flip/expand use `−` (U+2212). | « **Luminosité −** (écran gauche) » |
| 4 | onecable/controls.mdx | « Le port principal est destiné aux données et à la vidéo**,** le port Power sert uniquement à l'alimentation. » | Comma splice; plus three names for the same port on one product (`le port Power`, `port USB-C Power`, `Port USB-C (alimentation uniquement / Power Delivery)`). | « …à la vidéo, tandis que le port Power sert uniquement à l'alimentation. » + one port name. |
| 5 | onecable/installation.mdx | Standalone one-word paragraph « **Ou** » | Layout artefact; an orphaned `Ou` paragraph is jarring in French. | « **Ou&nbsp;:** », or fold the alternative into the next sentence. |
| 6 | onecable/installation.mdx | « **Cela évite une alimentation instable.** » | Grammatical but flat; *éviter une alimentation instable* is a weak calque. | « Vous éviterez ainsi toute instabilité de l'alimentation. » |
| 7 | onecable/installation-windows.mdx | alt=« Installation du pilote Windows **- mode jour** » / « **- mode nuit** » | Internal asset vocabulary (day/night image variants) leaked into user-visible alt text — a French screen-reader user hears « mode jour », which describes nothing. Hyphen also used as a dash. | alt=« Installation automatique du pilote sous Windows » for both variants. |
| 8 | onecable/installation-mac.mdx | « Suivez ces étapes sur votre **MacBook** » / « redémarrez votre **Mac** » / « redémarrez votre **ordinateur portable** » | Three names for the same machine on one page — and the Mac-only fallback list tells the reader to restart their *ordinateur portable*. | « votre Mac » throughout. |
| 9 | onecable/display-settings.mdx (shared with flip, expand) | « Allez dans **Paramètres d'affichage** » / « choisissez «&nbsp;Étendre le Bureau à cet écran&nbsp;» » / « Ouvrez les Réglages Système. » | Three markup conventions for UI strings on one page (bold, guillemets, bare); the Windows half quotes, the macOS half does not. | One convention — guillemets for UI strings — applied to both halves. |
| 10 | onecable/display-settings.mdx (shared) | « Faites un clic droit sur **votre** Bureau » | Possessive calque of *your desktop*; French Windows terminology is *le Bureau*. | « Cliquez avec le bouton droit sur le Bureau… » |
| 11 | lite/osd.mdx + lite-144hz/osd.mdx | « **Rouge (0–100)&nbsp;:** réglez **la luminosité de la valeur RVB rouge**. » | Three-noun stack no native would write; `expand/osd.mdx` says « réglez le canal rouge » for the identical setting. | « réglez l'intensité du rouge. » (align with expand/flip) |
| 12 | lite/osd.mdx + lite-144hz/osd.mdx | « **Transparence (0–100)&nbsp;:** réglez la transparence du menu OSD **pour une meilleure visibilité**. » | Non sequitur — raising transparency reduces the menu's visibility. | « …pour laisser apparaître l'image située derrière le menu. » |
| 13 | lite/controls.mdx vs lite-144hz/controls.mdx vs both osd.mdx | « **Mode OSD** » vs « **Mode menu OSD** » vs « le menu des réglages à l'écran (OSD) » vs page title « Menu à l'écran (OSD) » vs « ## Utiliser l'OSD » (expand) / « ## Utiliser le menu OSD » (flip) | Five names for the OSD across otherwise-identical sibling pages. | Fix « menu à l'écran (OSD) » on first use, « le menu OSD » thereafter. |
| 14 | flip/index.mdx | « un **moniteur multi-écran** pliable … votre espace de travail **multi-moniteur** » ; « **1 câble adaptateur USB-C vers USB-A (90 cm)** » | Two coinages for one idea in consecutive sentences; and plain spaces before `cm` while the spec tables on the same page use `&nbsp;`. | « un écran pliable à deux dalles … votre espace de travail multi-écran » ; « (90&nbsp;cm) ». |
| 15 | flip/installation.mdx | « - **1 USB-C et 1 USB-A et 1 HDMI** » ; « 2. …**dans le sens indiqué sur** l'image&nbsp;2. » / « 3. …**comme illustré sur** l'image&nbsp;3. » | Repeated `et` where `expand/installation.mdx` correctly writes « 1 USB-C, 1 USB-A et 1 HDMI »; and two phrasings for the identical cross-reference in consecutive steps (a third, « voir l'image&nbsp;6 », in step 5). | « **1 USB-C, 1 USB-A et 1 HDMI** » ; standardise « comme illustré sur l'image&nbsp;N ». |

Frontmatter of the skipped bodies — `lite/safety.mdx`, `lite-144hz/safety.mdx`, `flip/safety.mdx`, `expand/safety.mdx` (« Consignes de sécurité » / « Informations de sécurité et avertissements importants ») and `expand/display-settings.mdx` (« Réglages d'affichage » / « Réglages d'affichage pour Windows et macOS ») — idiomatic, no findings. One exception: `flip/display-settings.mdx` carries the description « Configurer vos écrans sous Windows et macOS » while the two pages with a byte-identical body use « Réglages d'affichage pour Windows et macOS » — align them.

---

# Totals

| Severity | Count |
|---|---|
| **Critical** | 1 |
| **Major** | 30 |
| **Minor** (itemised; ~54 observed, capped per brief) | 15 |
| **Reported total** | 46 |

Majors by cluster (recurring items counted once):

- **Translationese / calque — 12:** `…? … alors` question pattern (6 occurrences) · `Vérifiez si` (4) · `connexion par câble` · `Pour une utilisation économe en énergie` (3 files) · `recevoir de l'alimentation` · `comme alimentation` · `rétablir … à leurs valeurs d'usine` (2 files) · `Lumière bleue faible` (2 files) · `taux de rafraîchissement rapide` · `ne dispose pas d'assez de` · untranslated RTS/FPS glosses · `devrait vous avoir mené`.
- **Terminology / naming — 7:** *Précision* vs *Gamme de couleurs* (onecable/lite/lite-144hz + tab-to-tab mismatch in flip and expand) · device naming drift on the safety page · `support de fixation` / `support réglable` · `clips` / `capuchon de protection` · power-button vs molette naming.
- **Meaning visible to a French reader — 7:** voltage contradiction (Critical) · `carte mère` LED · `Recharger le Screenmate` heading · `deux sources` + three items · colour temperature described as intensity · Flip 14"/15,6" contradictory instructions · `écran soit bien serré`.
- **Grammar / structure — 4:** comma splices in the two installation pages · `Évitez … afin d'éviter` · announced-but-missing bullet list · `quels ports sont concernés`.

Pages with zero Critical/Major findings: `onecable/installation-windows.mdx`, `onecable/display-settings.mdx` (and its flip/expand twins), `flip/controls.mdx`, `expand/controls.mdx`, `lite/installation.mdx`, `lite-144hz/installation.mdx`, `lite/index.mdx`.

---

# Verdict

**Would a French customer notice this is a translation?**

Most of them, on most pages — **no**. An attentive one, on two pages — **yes**.

**Readability grade: near-native.**

1. **The French mechanics are genuinely good.** Across 24 files: no agreement errors, no gender mistakes, no missing or wrong accents, no typos, no *tu* leakage. Subjunctives are correct and unforced (`à condition que l'ordinateur portable fournisse`, `afin que le Screenmate s'ajuste`). French typography is applied with more discipline than most *published* French manuals — non-breaking spaces before every double punctuation mark, guillemets, decimal commas, `×` for dimensions, SI spacing. That baseline alone puts this well above "noticeably translated".

2. **Several pages read as though written in French.** The five connection scenarios in `lite/installation.mdx` and `lite-144hz/installation.mdx`, the storage section of `flip/installation.mdx`, the protective-cap section of `expand/installation.mdx` and all of `flip/controls.mdx` contain sentences a French copywriter would sign: « Choisissez celui qui correspond à votre appareil et aux câbles dont vous disposez », « les ports USB-C ne peuvent pas tous transmettre un signal vidéo », « Ce port se reconnaît souvent à un symbole de charge ou d'éclair », « ce qui vous permet d'emporter partout votre espace de travail ».

3. **What gives it away is a small number of repeated patterns, concentrated in the OneCable pages.** `Question ? … alors …` (6 occurrences) and `Vérifiez si` (4 occurrences) are the two tells — both are Dutch sentence habits transplanted whole. A French reader will not be able to name the problem, but `onecable/installation.mdx` and `onecable/troubleshooting.mdx` will feel to them like a manual "translated from somewhere": the rhythm is not French. Remove those two patterns and roughly half the foreign impression disappears.

4. **A second, quieter tell is terminology drift** — four names for the product on the safety page, five for the OSD, two for the same spec row inside one tab group, two for the same accessory between the box list and the installation step, two directions for the same cable. Individually invisible; together they signal that no single French author owned the text end to end.

5. **What blocks a "native" grade is not style but three reader-facing defects:** the 5 V / 5–20 V contradiction on the shared safety page (**Critical**, shipping on all five products), the « voyant de la carte mère » instruction a customer cannot act on, and the « Recharger le Screenmate OneCable » heading documenting the opposite operation. None is a French-language failure as such — all three are visible only when the French is read as a customer would read it, which is what this pass exists to do.

**Bottom line:** clean, correct, formal French with a Dutch backbone showing through in roughly a fifth of the sentences. Clearing the two repeated calque patterns, the eight terminology pairs and the Critical safety contradiction would move this to native.
