# Fluency review — French (batch B)

**Scope:** `fr/manuals/` — one-4k, one-4k-oled, dual-flip, infinity, infinity-lite, panorama
**Type:** monolingual native-reader fluency pass. No en/ or nl/ file was opened. Judged only as French written for French customers.
**Date:** 2026-08-12
**Mode:** read-only. No `.mdx` or config file was modified.

Format per finding: **[quoted French | issue | suggested rewrite | severity]**

Baseline note before the findings: the corpus is *clean* on the mechanical axes. Zero `tu` leakage, zero tu/vous mixing, zero gender/agreement errors, zero missing or wrong accents, zero typos found across 27 files. Guillemets are used correctly (never straight quotes for quotation — the only `"` characters are inch marks). The narrow non-breaking space before `: ; ! ?` is applied with near-perfect discipline. What follows is therefore almost entirely **word-choice, collocation, calque and internal-consistency** work, not error correction.

---

## fr/manuals/one-4k/

### index.mdx

- **"conçu pour vous offrir un second écran haute résolution pour votre ordinateur portable, votre téléphone…"** | `pour … pour` in the same clause; a French tech writer would not stack the two | "conçu pour servir de second écran haute résolution à votre ordinateur portable, votre téléphone, votre tablette ou votre console de jeu" | Minor
- **"| **Poids** | 860 grammes |"** | unit spelled out, in a table where every other quantity uses the SI symbol with a nbsp (`350&nbsp;cd/m²`, `1&nbsp;ms`) | `860&nbsp;g` | Minor *(see corpus-wide item T1)*
- **"| **Taux de contraste** | 1200:1 |"** | no thousands space, while `one-4k-oled/index.mdx` writes `100 000:1` with one — the French thousands convention is applied in one table and not the other | `1 200:1` | Minor *(T2)*
- **"| **Taille de l'écran** |"** | every sibling spec table says `Taille` | `Taille` | Minor *(T3)*
- Frontmatter `title` / `description`: correct and natural. No finding.

### controls.mdx

- **"ouvre le menu de raccourci de la luminosité en mode général"** | "en mode général" is a calque; there is no "general mode" on this device, and `dual-flip/controls.mdx` renders the identical concept as "en utilisation normale". A French reader looks for a "mode général" in the OSD and finds none | "ouvre le raccourci de luminosité **en utilisation normale**" | **Major**
- **"### Bouton Menu (alimentation / OSD)"** vs `osd.mdx` **"maintenez le **bouton d'alimentation** enfoncé"** | one physical button, two names across two pages of the same manual; the OSD page never mentions a "bouton Menu" and the controls page never mentions a "bouton d'alimentation" | pick one — recommend "bouton Menu (marche/arrêt et OSD)" on both pages, or gloss it once: "le bouton Menu, qui sert également de bouton d'alimentation" | **Major**
- **"Voyant d'état indiquant l'alimentation et l'état du signal."** under heading **"### Voyant lumineux"** | `état … état` inside one short sentence, plus a third name for the same part | heading "Témoin lumineux" → "Indique l'état de l'alimentation et la présence d'un signal." | Minor
- **"l'ensemble des ports physiques et des boutons de commande"** | "ports physiques" is an English habit; in French "les ports" already means the physical connectors | "l'ensemble des ports et des boutons de commande" | Minor
- **"le menu de raccourci de la luminosité"** | "menu de raccourci" is not a French UI collocation | "l'accès rapide à la luminosité" / "le réglage rapide de la luminosité" | Minor

### installation.mdx

- **"Si votre appareil prend en charge la charge via USB-C, l'écran se recharge automatiquement dès que le chargeur est raccordé au Screenmate."** | two problems in one sentence: (a) `prend en charge la charge` is cacophonous — no native writes it; (b) "l'écran se recharge" tells the customer the monitor has a battery, which nothing else in the manual supports. As written, the referent is almost certainly wrong | "Si votre appareil accepte la recharge par USB-C, il se recharge automatiquement dès qu'un chargeur est raccordé au Screenmate." — **confirm the referent with the product owner before applying** | **Major**
- **"Avec la prise en charge de Power Delivery (PD), le Screenmate passe automatiquement en mode de charge rapide."** | "Avec la prise en charge de X" is a word-for-word calque of an English absolute phrase; French needs a conditional subject | "Si votre appareil prend en charge Power Delivery (PD), le Screenmate bascule automatiquement en charge rapide." | **Major**
- **"le moniteur doit être alimenté séparément par une source d'alimentation supplémentaire"** | `alimenté … alimentation` in six words | "le moniteur doit être alimenté séparément par une source externe" | Minor
- **"les ports USB-C ne peuvent pas tous transmettre un signal vidéo"** vs `infinity/installation.mdx` **"les ports USB-C ne prennent pas tous en charge la sortie vidéo"** | the same caveat, two formulations across the range | standardise on "les ports USB-C ne prennent pas tous en charge la sortie vidéo" | Minor
- **alt="Connexion HDMI à un PC, une console ou un appareil photo"** | "appareil photo" appears nowhere in the section, which lists PC, ordinateur portable, Xbox, PlayStation, Nintendo Charging Dock | drop "ou un appareil photo" | Minor

### osd.mdx

- **"Maintenez le bouton situé au-dessus du bouton d'alimentation enfoncé pendant **10 secondes** pour le déverrouiller."** | the past participle `enfoncé` is stranded eleven words from its object; the reader has to re-parse. French puts the participle next to the verb and pushes the long complement to the end | "Maintenez enfoncé pendant **10 secondes** le bouton situé au-dessus du bouton d'alimentation pour le déverrouiller." | **Major**
- **"L'option sélectionnée est surlignée en jaune."** | "surligner" is the highlighter-pen sense; French UI language is "mise en surbrillance" | "L'option sélectionnée apparaît en surbrillance jaune." | Minor
- **"bouton d'alimentation"** throughout | see controls.mdx naming conflict above | — | *(counted once)*

### safety.mdx — frontmatter only

- `title: "Consignes de sécurité"` / `description: "Informations de sécurité et avertissements importants"` | idiomatic and consistent with the other five products | no finding

---

## fr/manuals/one-4k-oled/

The four in-scope pages are near-identical to one-4k. **All one-4k findings above recur verbatim** in `controls.mdx` ("en mode général", "Bouton Menu" vs "bouton d'alimentation", "ports physiques"), `installation.mdx` ("prend en charge la charge", "Avec la prise en charge de Power Delivery"), and `osd.mdx` (stranded "enfoncé", "surlignée"). Not re-listed. OLED-specific:

### controls.mdx

- **"### Port USB-A"** followed only by `{/* TODO: confirm with Louie … */}` | JSX comments do not render. The published French page shows a **section heading with no body text at all** — the reader sees "Port USB-A" and then jumps straight to "Voyant lumineux". The one-4k page documents this port in full | either port the one-4k sentence across ("Pour brancher des accessoires USB 2.0 tels qu'une souris ou un clavier…") or remove the heading until confirmed | **Major**

### index.mdx

- **"un taux de contraste de 100 000:1 — idéal pour la vidéo, la photo et le travail créatif"** | `idéal` (masc. sg.) grammatically attaches to "un taux de contraste", but the sense is that *the panel* is ideal. Grammatical, yet a native would not leave the apposition dangling on the number | "…et un taux de contraste de 100 000:1 — de quoi convenir parfaitement à la vidéo, à la photo et au travail créatif." | Minor
- **"| **Poids** | 860 grammes |"** | see T1 | `860&nbsp;g` | Minor
- Frontmatter: correct.

### safety.mdx — frontmatter only: no finding.

---

## fr/manuals/dual-flip/

### index.mdx

- **"| **Précision des couleurs** | 100&nbsp;%&nbsp;sRGB |"** | every other product calls this row **"Gamme de couleurs"**, and sRGB coverage *is* a gamut, not an accuracy figure. Both the internal inconsistency and the technical mislabel are visible to a French reader | "Gamme de couleurs" | **Major**
- **"Pour une utilisation économe en énergie, nous vous recommandons de débrancher le câble d'alimentation lorsque le moniteur n'est pas utilisé."** | "Pour une utilisation économe en énergie" is a nominal calque; French front-loads the purpose as a verb. Also `utilisation … utilisé` | "Pour limiter la consommation, débranchez le câble d'alimentation lorsque vous n'utilisez pas le moniteur." | **Major**
- **"- **Écran gauche&nbsp;:** 0° – 245° (s'incline de 180° vers le haut et vers le bas)"** / **"- **Écran droit&nbsp;:** 0° – 205° (s'incline vers le haut et vers le bas, tout comme l'écran gauche)"** | neither parenthetical parses against its range: a screen with a 0–245° travel cannot "s'incliner de 180° vers le haut **et** vers le bas", and the right-hand note says it behaves "tout comme l'écran gauche" immediately after quoting a different maximum. The customer cannot derive the safe limit, which is what this callout exists to give them | rewrite as a plain limit statement: "**Écran gauche :** rotation de 0° à 245° maximum. **Écran droit :** rotation de 0° à 205° maximum. Les deux écrans s'inclinent vers le haut et vers le bas." — verify angles with the product owner | **Major**
- **"se déplie en deux écrans supplémentaires de 16"" | "se déplier **en**" is not the French construction | "se déploie pour former deux écrans supplémentaires de 16"" | Minor
- **"(90 cm)" / "(60 cm)"** in the package list | no `&nbsp;`, while the spec table below uses `3,5&nbsp;cm` | `90&nbsp;cm` | Minor *(T4)*
- **"| **Poids** | 1900 grammes |"** | T1 | `1 900&nbsp;g` | Minor
- **"0° – 245°"** (spaced en dash) vs `osd.mdx` **"(0–100)"** (unspaced) | two range conventions in one manual | unspaced en dash throughout, or "de 0° à 245°" | Minor *(T5)*

### controls.mdx

- **"### Port USB-C" / "Alimentation et transfert vidéo." — repeated twice, identically, back to back** | the reader sees the same heading and the same one-line description twice and has no way to tell the two ports apart, which is the entire point of a ports page | label them: "### Port USB-C (gauche)" / "### Port USB-C (droit)", or merge into "### Ports USB-C (×2)" | **Major**
- **"Alimentation et transfert vidéo."** / **"Transfert vidéo (pas d'alimentation)."** | "transfert vidéo" is a calque; French says "signal vidéo" or "transmission du signal vidéo". "Transfert" implies moving files | "Alimentation et signal vidéo." / "Signal vidéo uniquement (pas d'alimentation)." | **Major**
- **"Augmente la luminosité en utilisation normale, et permet de naviguer dans le menu OSD et d'y augmenter les valeurs."** | comma before `et`, then a second `et` — the sentence trips | "Augmente la luminosité en utilisation normale ; dans le menu OSD, permet de naviguer et d'augmenter les valeurs." | Minor
- **"### Mini-HDMI"** vs **"### Port USB-C"**, and **"### M — bouton du menu OSD"** vs **"### Bouton + (augmenter la luminosité)"** | four heading patterns on one short page | one pattern, e.g. "### Port Mini-HDMI", "### Bouton M (menu OSD)" | Minor

### installation.mdx

- **"Cela se fait facilement via le port USB-A de votre ordinateur portable."** | textbook translationese — an impersonal "Cela se fait … via" where French uses a concrete subject | "Le port USB-A de votre ordinateur portable convient parfaitement." | **Major**
- **"- **1 USB-C et 1 USB-A et 1 HDMI**"** | `et … et` in an enumeration; French uses commas and a single final "et" | "**1 USB-C, 1 USB-A et 1 HDMI**" | **Major**
- **"Branchez l'autre côté à l'aide du câble HDMI et du câble USB-C vers USB-A."** | "l'autre côté" is ambiguous — the other side of the laptop, of the cable, or the other screen? | "Raccordez le second écran à l'aide du câble HDMI et du câble USB-C vers USB-A." | Minor
- **"vérifiez d'abord de quels ports dispose votre ordinateur portable"** vs `infinity/installation.mdx` **"vérifiez d'abord les ports dont dispose votre ordinateur portable"** | identical sentence, two structures across the range | standardise | Minor

### osd.mdx

- **"- **LOW BLUE LIGHT&nbsp;:** réduit la quantité de lumière bleue…"** | every other bullet in the six OSD sections is an imperative addressed to the reader ("réglez", "choisissez", "activez", "basculez"); this one alone slides into third-person description. The register break is audible | "réduisez la quantité de lumière bleue affichée afin de limiter la fatigue oculaire" | **Major**
- **"- **RESET&nbsp;:** choisissez RESET pour rétablir tous les réglages à leurs valeurs d'usine."** | "rétablir X **à** Y" is a calque of *restore X to Y*; French is "rétablir les valeurs d'usine" or "réinitialiser X **aux** valeurs d'usine" | "choisissez RESET pour réinitialiser tous les réglages aux valeurs d'usine" | **Major**
- **"- **ASPECT&nbsp;:** basculez le format d'image entre **4:3** et **WIDE**."** | "basculer" is intransitive in this sense ("basculer entre deux modes"); "basculez le format d'image" reads as tipping the format over | "choisissez le format d'image : **4:3** ou **WIDE**." | **Major**
- **"- **COLOR TEMP&nbsp;:** réglez manuellement les valeurs RVB, ou choisissez un préréglage…"** | comma before "ou" joining two short alternatives | drop the comma | Minor
- **"- **DCR (taux de contraste dynamique)&nbsp;:** choisissez ON ou OFF pour activer ou désactiver le contraste dynamique."** | the gloss already said what DCR is; the sentence then re-says it | "choisissez ON ou OFF." | Minor
- **HDR listed under "### 5. Réinitialisation"** | a French reader looking for HDR will not look under "Réinitialisation" | structural — flag to the content owner | Minor

### safety.mdx

- **"Le moniteur fonctionne avec une entrée CC comprise entre 5&nbsp;V et 20&nbsp;V (avec une tolérance de ±2&nbsp;V)."** immediately followed by **"Utilisez l'appareil uniquement avec une source d'alimentation de 5&nbsp;V via le câble approprié."** | two consecutive safety bullets contradict each other: the first authorises 5–20 V, the second restricts to 5 V *only*. On a safety page the customer cannot tell which instruction binds, and the word "uniquement" makes the second one read as a prohibition | reconcile with the product owner. If 5–20 V is the true input window and 5 V is only the USB-A fallback, say so: "L'entrée CC admissible est de 5 à 20 V (±2 V). Lorsque vous alimentez le moniteur par un port USB-A, utilisez une source de 5 V et le câble fourni." | **Critical** |
- **"Utilisez uniquement l'adaptateur CA/CC fourni comme alimentation."** | "comme alimentation" is a calque of *as power supply*; French needs "comme source d'alimentation", or better, drops it. Note also that the installation pages call this part "l'adaptateur secteur" | "Utilisez uniquement l'adaptateur secteur fourni." | **Major**
- **"Évitez toute exposition à l'humidité, à la poussière et à l'électricité statique afin d'éviter tout dommage aux composants électroniques."** | `Évitez … afin d'éviter` — a native rewrites rather than repeats the verb | "Protégez l'appareil de l'humidité, de la poussière et de l'électricité statique afin de ne pas endommager les composants électroniques." | **Major**
- **"Maintenez les ouvertures de ventilation dégagées"** | "maintenir … dégagé" is stiff | "Ne bouchez pas les ouvertures de ventilation" | Minor
- **"adaptée à l'ampérage requis"** | "ampérage" is colloquial in a technical safety notice | "adaptée à l'intensité requise" | Minor
- **"entre -20&nbsp;°C et 60&nbsp;°C"** | ASCII hyphen used as a minus sign, on pages that elsewhere use U+2212 for the "−" button | "de −20&nbsp;°C à 60&nbsp;°C" | Minor *(T6)*
- **"les équipements émetteurs"** | vague calque of *transmitting equipment* | "les appareils émetteurs radio" | Minor

### display-settings.mdx — frontmatter only

- `title: "Réglages d'affichage"` / `description: "Réglages d'affichage pour Windows et macOS"` | correct French; note only that the equivalent pages under infinity and infinity-lite are titled "Réglages d'affichage et de son" — worth aligning if the bodies now match | Minor *(T7)*

---

## fr/manuals/infinity/

### index.mdx

- **"pour vous offrir deux écrans supplémentaires à la fois"** | "à la fois" is a calque of *at once* and is doing no work — worse, it can be misread as "alternately". French either drops it or says "d'un seul coup" | "…pour vous offrir deux écrans supplémentaires." | **Major**
- **"Chaque écran dispose de haut-parleurs intégrés"** vs `controls.mdx` **"Chaque écran est équipé d'un haut-parleur intégré sur son bord extérieur"** | plural on one page, singular on the next, for the same hardware | singular, per controls.mdx | **Major**
- **"| **Poids** | 2390 grammes |"** | T1 | `2 390&nbsp;g` | Minor
- **"- **Support pour écran unique**"** vs `installation.mdx` caption **"Placez l'écran sur le support simple"** | two names for one accessory the customer must find in the box | "support pour écran unique" everywhere | Minor

### controls.mdx

- **"- **Appui vers la droite («&nbsp;Plus&nbsp;»)&nbsp;:** augmenter le rétroéclairage (luminosité).**" / "- **Appui vers la gauche («&nbsp;Min&nbsp;»)&nbsp;:** diminuer le volume."** | three compounding problems. (a) **«&nbsp;Min&nbsp;»** is Dutch for *moins*; a French reader parses it as "minimum", not as the minus direction. (b) The mapping as documented is unusable: right increases **brightness**, left decreases **volume** — the page gives the customer no way to lower brightness or raise volume, and there is no third gesture listed. (c) `infinity-lite/controls.mdx` documents the *opposite* mapping (left = rétroéclairage, right = volume) for the same control family | replace the Dutch labels with the physical directions and document all four actions: "**Appui vers la droite :** augmente la valeur du réglage actif (luminosité ou volume). **Appui vers la gauche :** diminue la valeur du réglage actif." — mapping must be confirmed against the hardware | **Critical** |
- **"Consultez la section [Menu à l'écran] ci-dessous pour l'ensemble des **gestes**."** and **"Les mêmes **gestes** fonctionnent sur les deux écrans."** | in French "geste" means a touch/trackpad gesture. These are button presses on a rotary control; the word sends the reader looking for a touchscreen | "pour le détail des commandes" / "Les mêmes commandes s'appliquent aux deux écrans." | **Major**
- **"Un bouton rotatif situé à l'arrière de chaque écran, qui commande l'allumage, le menu à l'écran, la luminosité et le volume."** | verbless fragment; the comma before "qui" makes it worse | "Bouton rotatif situé à l'arrière de chaque écran. Il commande l'allumage, le menu à l'écran, la luminosité et le volume." | Minor
- **frontmatter `title: "Ports et commandes"`** vs the page's own `## Ports et boutons` and all five sibling products' "Ports et boutons" | the sidebar label and the page title disagree | "Ports et boutons" | Minor
- **"La disposition est en miroir sur l'écran gauche et sur l'écran droit."** | "en miroir sur … et sur …" is an English construction | "Les deux écrans présentent une disposition symétrique." | Minor

### installation.mdx

- **"- 1 USB-C, 1 USB et 1 HDMI"** | "1 USB" is not a port type; the whole page turns on distinguishing USB-A from USB-C, and `dual-flip` spells it out | "1 USB-C, 1 USB-A et 1 HDMI" | **Major**
- **"Placez l'ensemble entièrement replié dans la **pochette de transport en cuir** fournie."** vs `index.mdx` package list **"Étui de protection"** | the customer is told to use an item that is not in the stated box contents, under a different name and a different material | one term — "l'étui de protection fourni" | **Major**
- **"Assurez-vous que la pièce centrale est bien **centrée** sur votre ordinateur portable."** | `pièce centrale … centrée` | "Assurez-vous que la partie centrale est bien alignée sur l'axe de votre ordinateur portable." | Minor
- **"Chaque écran pivote au maximum de 90°."** (step 5) then **"Chaque écran a une rotation maximale de 90°."** (next section) | the same fact, twice, two sentences apart, in two phrasings | delete one | Minor
- **"### Double écran — avant et arrière à l'horizontale"** | "avant et arrière" gives the French reader nothing; the steps describe mounting each screen on the *opposite* stand arm | "### Double écran monté en vis-à-vis — disposition horizontale" | Minor
- **"1. Détachez l'écran du support."** (singular) vs storage **"1. Retirez les écrans gauche et droit du support."** (plural) | same action, opening and closing the page | plural in both | Minor
- **"Le support pivote à 360°."** | "pivoter à" → "pivoter sur" | "Le support pivote sur 360°." | Minor

### display-settings.mdx

- **"…mais vous devez choisir **l'entrée** **S6-R / Screenmate** pour entendre le son via votre Screenmate."** | the reader is in the **Sortie** tab selecting an output device; calling it "l'entrée" is a genuine term error that sends them to the wrong tab | "…mais vous devez sélectionner **S6-R / Screenmate** pour entendre le son via votre Screenmate." | **Major**
- **"les *Haut-parleurs du MacBook* sont mis en évidence"** | italics for a UI string on a page that bolds every other UI string | bold | Minor
- **"Sur la capture d'écran, le **Speaker (Realtek(R) Audio)** mis en évidence est le haut-parleur intégré de votre ordinateur portable, et non le Screenmate — choisissez plutôt **S6-L**."** | 38-word sentence with a bolded English product string, a nested parenthesis and a dash clause; comprehensible but heavy | split: "Sur la capture d'écran, l'entrée **Speaker (Realtek(R) Audio)** est mise en évidence : il s'agit du haut-parleur de votre ordinateur portable. Choisissez plutôt **S6-L**." | Minor
- Windows/macOS UI strings ("Étendre le Bureau à cet écran", "Orientation de l'affichage", "Paysage (inversé)", "Réglages Système", "Moniteurs", "Disposition", "menu Pomme") are the genuine French OS strings — correct throughout. No finding.

### safety.mdx

- **"Évitez les **espaces humides** et l'accumulation de poussière…"** | "espaces humides" is not French for damp environments; `dual-flip/safety.mdx` gets it right with "environnements humides". Also `Évitez … afin d'éviter` again | "Évitez les environnements humides et l'accumulation de poussière, qui peuvent endommager les composants électroniques." | **Major**
- **"Utilisez uniquement **un** adaptateur CA/CC comme alimentation."** | the indefinite article turns a restriction into permission to use any adapter — the opposite of the safety intent; dual-flip says "l'adaptateur … fourni". Plus the "comme alimentation" calque | "Utilisez uniquement l'adaptateur secteur fourni." | **Major**
- **"Convient à un usage domestique comme professionnel."** | subjectless fragment; abrupt in a numbered safety list | "Ce produit convient aussi bien à un usage domestique qu'à un usage professionnel." | Minor
- **"entre -20&nbsp;°C et 60&nbsp;°C"** | T6 | — | Minor

---

## fr/manuals/infinity-lite/

### index.mdx

- **"pour plus d'espace à l'écran en déplacement"** | "espace à l'écran" is a calque of *screen space*; French says "espace de travail" or "surface d'affichage" | "pour élargir votre espace de travail en déplacement" | Minor
- **"- **Aimant**"** | a bare noun in a package list; the customer cannot tell what it is for, and no other page mentions it | "**Aimant de fixation**" plus one clause of purpose | Minor
- **"| **Poids** | 1261 grammes |"** | T1 | `1 261&nbsp;g` | Minor
- **"fonctionne en plug-and-play"** | anglicism where "prêt à l'emploi" exists — but plug-and-play is widely understood in French consumer copy. Recorded as **preference, not error** | optional: "fonctionne immédiatement, sans installation" | Minor

### controls.mdx

- **"### Bouton «&nbsp;Min&nbsp;» gauche"** / **"### Bouton «&nbsp;Plus&nbsp;» droit"** | «&nbsp;Min&nbsp;» is Dutch. In French "Min" reads as *minimum*, so "Bouton Min gauche" suggests a button that sets the minimum. The modifier order is also wrong — French puts the position adjective after the noun it qualifies, not after the quoted label | "### Bouton gauche («&nbsp;−&nbsp;»)" / "### Bouton droit («&nbsp;+&nbsp;»)" | **Major**
- **"Basculement vers la gauche – règle le rétroéclairage (luminosité)."** | nominal-style calque ("Basculement vers la gauche" as a bare heading-in-a-sentence), and a spaced **en dash** where the rest of the corpus uses an em dash | "Basculez vers la gauche pour régler le rétroéclairage (luminosité)." | **Major**
- **mapping conflict with `infinity/controls.mdx`** (left = rétroéclairage here, left = volume there) | see the Critical under infinity/controls.mdx | — | *(counted once)*
- **"Le port le plus à gauche sur la **face inférieure**"** vs **"trois boutons sur le **bord inférieur**"** | two names for the same edge, eight lines apart | "bord inférieur" in both | Minor
- **"### Voyant LED"** vs one-4k's "Voyant lumineux" | T8 | — | Minor
- **"Réservé au câble HDMI vers USB-C lorsque la vidéo et l'alimentation sont séparées."** | elliptical — separated from what? | "…lorsque le signal vidéo et l'alimentation transitent par deux câbles distincts." | Minor

### installation.mdx

- **"Suivez ces étapes dans l'ordre pour déployer en toute sécurité **les deux écrans d'extension** derrière votre ordinateur portable."** — plus the headings **"## Déplier les écrans"**, **"### 6. Ouvrir les écrans"**, **"### 7. Fermer les écrans"** | `index.mdx` describes the Infinity Lite as a **single**-screen extension ("vous offre un écran portable supplémentaire") and `controls.mdx` describes one panel. The installation page tells the customer to unfold two. A French customer following this page on a one-screen product is stopped cold at step 1 | singularise throughout: "…pour déployer en toute sécurité l'écran d'extension derrière votre ordinateur portable" / "## Déplier l'écran" / "### 6. Ouvrir l'écran" / "### 7. Fermer l'écran" | **Critical** |
- **"Maintenez des deux mains les deux **emplacements** indiqués par les flèches rouges et tirez l'écran vers l'extérieur pour **libérer l'écran unique**."** | "emplacements" cannot be held — French needs "points"/"zones"; and "libérer l'écran unique" is opaque (unique to what?) | "Saisissez des deux mains les deux zones indiquées par les flèches rouges et tirez l'écran vers l'extérieur pour le détacher." | **Major**
- **"Ouvrez le cadre jusqu'au **clic** pour le déployer."** | in French, "clic" is a mouse click; the sound a mechanism makes when it latches is a **déclic** | "Ouvrez le cadre jusqu'au déclic." / "…jusqu'à ce qu'il s'enclenche." | **Major**
- **"réglez-le sur le bon **angle d'appui**"** | "angle d'appui" is not a French collocation, and "le bon" begs the question of which one | "réglez-le à l'angle d'inclinaison souhaité" | **Major**
- **"Respectez le bon ordre lors de l'ouverture et de la fermeture **afin d'éviter** tout dommage à l'appareil. Rangez votre Screenmate avec soin **afin d'éviter** d'endommager le matériel."** | the same purpose clause twice in consecutive sentences, saying the same thing about the same object | "Respectez l'ordre indiqué à l'ouverture comme à la fermeture, et rangez votre Screenmate avec soin, afin de ne pas l'endommager." | **Major**
- **"Basculez sur le mode de connexion approprié **(alimentation externe requise)** pour utiliser le Screenmate avec un téléphone, une console de jeu ou un autre appareil USB-C. **Le mode téléphone nécessite lui aussi une alimentation externe.**"** | the second sentence repeats the parenthesis it just read; and "Basculez sur le mode de connexion approprié" refers to a mode switch that no page on this product describes | "Pour utiliser le Screenmate avec un téléphone, une console de jeu ou un autre appareil USB-C, branchez systématiquement une alimentation externe." — and document the mode switch, or drop the reference | **Major**
- **"Branchez le câble HDMI vers USB-C sur le **troisième** port du Screenmate"** vs `controls.mdx` **"USB-C (pour HDMI vers USB-C) — Le port **le plus à gauche** sur la face inférieure"** | the two pages number the same port differently; the installation page also says "le premier ou le deuxième port" for power, so the reader cannot map either instruction onto the hardware | align the two pages on one numbering, stated once and referenced thereafter | **Major**
- **`<Warning>` used for ordinary assembly steps** (steps 3, 5, and part of 7) | in French docs a "Attention" box signals a hazard; wrapping "Ouvrez le support, réglez-le… placez-le derrière l'écran" in one trains the reader to ignore the real warnings | demote steps 3 and 5 to body text or `<Note>` | Minor
- **"### 1. Détacher l'écran du support"** with the body **"Dépliez complètement le moniteur afin d'éviter tout dommage."** | heading says detach, body says unfold | align | Minor
- **"Placez le petit support et utilisez la fixation rotative à 360° pour le mettre en position."** | "Placez … pour le mettre en position" is circular | "Positionnez le petit support, puis orientez-le à l'aide de la fixation rotative à 360°." | Minor

### display-settings.mdx

- **the entire "## Organiser vos écrans (vidéo)" `<Tabs>` block** | it repeats, almost word for word, the Windows and macOS instructions already given 30 lines above — and switches convention while doing so: the first pass bolds UI strings (**Étendre le Bureau à cet écran**), the repeat puts them in guillemets («&nbsp;Étendre le Bureau à cet écran&nbsp;»). The French reader reads the same procedure twice, formatted two ways, and wonders what changed | keep the videos, drop the duplicated prose, and use one convention for UI strings | **Major**
- **"…vous devez choisir **l'entrée** **S6-R / Screenmate**"** | same term error as infinity/display-settings.mdx — output device called an input | "sélectionnez **S6-R / Screenmate**" | **Major**
- **"**Besoin d'une meilleure vue d'ensemble&nbsp;?** … réglez-la sur **150&nbsp;%** pour un texte et des éléments plus grands."** | scaling *up* to 150 % reduces the overview; the question and the answer pull in opposite directions. `infinity/display-settings.mdx` heads the identical passage "Vous souhaitez plus d'espace à l'écran ?", which has the same problem | "Texte trop petit ? Cliquez sur **Échelle** et réglez-la sur **150&nbsp;%**." | Minor
- **inline SVG OS logos in `###` headings** here, `<Tabs>` in infinity's equivalent page | identical content, two presentations across sibling products | Minor *(presentation, not language)*

### safety.mdx

- Same three shared items as infinity/safety.mdx: **"un adaptateur CA/CC comme alimentation"** (**Major**), **"espaces humides … afin d'éviter"** (**Major**), **"Convient à un usage domestique comme professionnel."** (Minor), **"-20&nbsp;°C"** (Minor). Not re-counted — see infinity/safety.mdx.
- **"### À lire avant utilisation"** (numbered list) vs infinity's **"### À vérifier avant utilisation"** (bulleted) vs panorama's **"### Avant utilisation"** (bulleted) | three headings and two list styles for one identical block of ten safety points | one heading, one list style | Minor

---

## fr/manuals/panorama/

### index.mdx

- **description: "…de votre **écran portable triple** Screenmate Panorama 15,6""** and body **"Le Screenmate Panorama est un **écran portable triple** qui vous offre…"** | wrong adjective position. French says "un **triple écran**" — and the range already does, in `infinity/index.mdx`: "un **double écran** portable pliable". "Écran portable triple" reads like a machine translation and is the first sentence a French customer sees | "un **triple écran portable** qui vous offre trois écrans Full HD de 15,6"…" and the same in the frontmatter description | **Major**
- **"| **Angle de vision** | 360° |"** | a 360° viewing angle is physically meaningless for an LCD; the sibling products state 172°/178°. A French reader who compares the range will spot it | verify with the product owner — likely 178° | Minor
- **"| **Poids** | 3000 grammes |"** | T1 | `3&nbsp;kg` | Minor
- **"(1,2 m)" / "(0,5 m)"** | T4 | `1,2&nbsp;m` | Minor

### controls.mdx

- **"### 3 × ports Mini-HDMI"** | "3 × ports" is not French — the multiplication sign is used *after* a noun ("Ports Mini-HDMI (×3)") or replaced by a numeral ("Trois ports Mini-HDMI") | "### Ports Mini-HDMI (×3)" | **Major**
- **"pour connecter votre ordinateur portable à un **écran individuel**"** | "un écran individuel" suggests a personal/private display; the meaning is *one of the three panels* | "pour connecter votre ordinateur portable à **l'un des trois écrans**" | **Major**
- **register split within one page:** **"- Naviguer dans le menu. / - Diminuer des valeurs… / - Ouvrir le menu de raccourci…"** (infinitives, under Bouton Bas and Bouton Haut) against **"**Appui long (1 seconde)&nbsp;:** éteint le moniteur."** and **"**Appui court&nbsp;:** confirme une sélection"** (third person, under Bouton d'alimentation and Bouton Confirmer/Quitter) | four button entries, two grammatical modes; the page reads as assembled from two sources | one mode throughout — third person indicative reads best for a ports-and-buttons reference | **Major**
- **"- **Appui long (1 seconde)&nbsp;:** éteint le moniteur."** | the page documents how to switch the monitor *off* but never how to switch it *on* | add the power-on gesture | Minor
- **"Diminuer des valeurs telles que la luminosité ou le volume."** | partitive "des valeurs" where French wants the definite | "Diminuer les valeurs (luminosité, volume…)." | Minor

### installation.mdx

- **"…alors que le Panorama l'alimente également peut provoquer des **interférences**."** | in French "interférences" means electromagnetic interference. The intended sense is a power-negotiation conflict between two chargers; as written the warning points the customer at the wrong phenomenon | "Évitez de brancher un chargeur sur votre ordinateur portable pendant que le Panorama l'alimente : les deux sources risquent d'entrer en conflit." | **Major**
- **"Utilisez **le long câble blanc** pour l'alimentation, et **le câble noir court** pour connecter le Panorama…"** | the two parallel noun phrases put the adjectives in opposite positions in the same sentence | "Utilisez le long câble blanc pour l'alimentation et le court câble noir pour relier le Panorama à votre ordinateur portable." | Minor
- **"branchez le câble HDMI sur le **port HDMI** situé à côté du câble d'alimentation blanc"** | `controls.mdx` calls these "ports Mini-HDMI"; the customer is looking at a Mini-HDMI socket | "sur le port Mini-HDMI situé à côté…" | Minor
- **"**Téléchargez** le pilote depuis la page de **téléchargement** de Silicon Motion"** | root repeated in one clause | "Récupérez le pilote sur la page de téléchargement de Silicon Motion" | Minor
- **"**Attention&nbsp;:** prenez garde à vos doigts lorsque vous repliez les écrans afin d'éviter tout pincement."** vs `safety.mdx` **"Attention à vos doigts lorsque vous repliez ou dépliez les écrans, afin d'éviter tout pincement."** | the same warning, two formulations, two pages | one wording | Minor
- **"Repliez les **pieds de verrouillage** vers l'intérieur"** then **"jusqu'à ce que les pieds s'engagent dans le **verrou avant**"** | "pieds de verrouillage" and "verrou avant" are two different parts under near-identical names | name them distinctly | Minor

### osd.mdx

- **"## Configuration de l'affichage (système d'exploitation)"** | the bare parenthetical reads as a note-to-self | "## Configurer l'affichage dans votre système d'exploitation" | Minor
- **"Le Panorama pilote trois écrans indépendants, vous souhaiterez donc peut-être adapter la disposition du Bureau…"** | two independent clauses joined by a comma; "donc" carries it, but French prefers a subordinate or a semicolon | "Comme le Panorama pilote trois écrans indépendants, vous souhaiterez peut-être adapter la disposition du Bureau…" | Minor
- **"Le réglage du volume n'est disponible que sur l'écran gauche **(moniteur DP)**."** | "DP" is never introduced anywhere in the French manual | "(l'écran raccordé en DisplayPort)" | Minor
- **UI-string convention mixed within one page:** **«&nbsp;Étendre le Bureau à cet écran&nbsp;»** and **«&nbsp;Paysage (inversé)&nbsp;»** in guillemets, but **Identifier**, **Échelle** and **Orientation de l'affichage** in bold alone | one convention per page | Minor
- **"pour ouvrir le menu de luminosité"** vs `controls.mdx` **"Ouvrir le menu de raccourci de la luminosité"** | same menu, two names | Minor

### safety.mdx

- Shares the infinity/infinity-lite safety text; same **Major** items ("un adaptateur CA/CC comme alimentation", "espaces humides … afin d'éviter") already counted there.
- **"### Précaution lors du pliage"** / **"Attention à vos doigts…"** | heading is a noun, the parallel headings on the page are prepositional ("Avant utilisation") | fine as is; only the wording duplication with installation.mdx (above) is worth fixing | Minor

---

## Corpus-wide typography and terminology (counted once, in the Minor tally)

| # | Item | Where | Suggested |
|---|---|---|---|
| T1 | Weights written as "860 / 1900 / 2390 / 1261 / 3000 **grammes**" — unit spelled out, no French thousands space, in tables that otherwise use SI symbols + nbsp | all six index.mdx | `860&nbsp;g`, `1&nbsp;900&nbsp;g`, `2&nbsp;390&nbsp;g`, `1&nbsp;261&nbsp;g`, `3&nbsp;kg` |
| T2 | Thousands space applied to `100 000:1` but not to `1200:1` | one-4k vs one-4k-oled | `1 200:1` |
| T3 | Spec row named "Taille de l'écran" in one-4k/one-4k-oled, "Taille" in the four others | index.mdx ×6 | "Taille de l'écran" everywhere |
| T4 | Cable/dimension figures in package lists have no `&nbsp;` ("90 cm", "1,2 m") while spec tables do (`3,5&nbsp;cm`) | dual-flip, infinity, panorama | `90&nbsp;cm` |
| T5 | Ranges written three ways: `0° – 245°` (spaced en dash), `0–100` (unspaced), `10–60 secondes` | dual-flip index vs osd | one convention |
| T6 | `-20&nbsp;°C` uses an ASCII hyphen; the corpus uses U+2212 `−` for the minus button | four safety.mdx | `−20&nbsp;°C` |
| T7 | Page titled "Réglages d'affichage" (dual-flip) vs "Réglages d'affichage et de son" (infinity, infinity-lite) | frontmatter | align once bodies match |
| T8 | Status indicator called "Voyant lumineux" / "Voyant LED" / "Voyant d'état" | one-4k, infinity-lite | "Témoin d'état" everywhere |
| T9 | Power brick called "adaptateur secteur" on installation pages, "adaptateur CA/CC" on safety pages | all products | "adaptateur secteur (CA/CC)" on first mention, then "adaptateur secteur" |
| T10 | Durations "10 secondes", "2 secondes", "3 secondes" carry a plain space while every unit symbol carries `&nbsp;` | one-4k/osd, infinity/controls, infinity-lite/controls | `10&nbsp;secondes` for consistency |

---

## Totals by severity

| Severity | Count |
|---|---|
| **Critical** | **3** |
| **Major** | **38** |
| **Minor** | **17 reported** (plus the 10 corpus-wide typography/terminology items in the table above, counted as 10 — total 27 logged; a longer tail of preference-level polish was deliberately not written up per the cap) |

**The three Criticals:**
1. `fr/manuals/dual-flip/safety.mdx` — consecutive bullets authorise 5–20 V and then restrict to "uniquement 5 V". Safety-relevant, unresolvable by the reader. *(The same two lines exist in one-4k/safety.mdx and one-4k-oled/safety.mdx, whose bodies were out of scope for this reviewer — worth routing to whoever covers the shared safety text.)*
2. `fr/manuals/infinity-lite/installation.mdx` — the page instructs the customer to unfold "**les deux écrans d'extension**" on a product that index.mdx and controls.mdx both describe as a single screen.
3. `fr/manuals/infinity/controls.mdx` — the multifunction-button mapping is undocumentable as written (right = brightness up, left = volume down, no way to reverse either), uses the Dutch label «&nbsp;Min&nbsp;», and contradicts the mapping given for the same control family in infinity-lite/controls.mdx.

Note on honesty of the split: of the 38 Majors, roughly two thirds are genuine **language** defects (calques, wrong collocations, register breaks, verbless fragments) and one third are **within-French consistency or content** defects surfaced by reading as a customer (port numbering that contradicts itself, an accessory named two ways, an empty rendered heading). Both kinds break the illusion of native authorship, but only the first kind is a translator's fault. The four items I could most easily be talked out of are marked in the body as preference or as "verify with the product owner".

---

## Verdict

### Would a French customer notice this is a translation?

**Yes — but not immediately, and not on every page.**

The first two minutes of reading are convincing. Frontmatter, index pages, the OSD tables and the whole display-settings family read like French. The register is a steady, correct formal *vous* with no slippage anywhere in 27 files. Genuine French Windows and macOS UI strings are used ("Étendre le Bureau à cet écran", "Réglages Système", "Moniteurs", "Paysage (inversé)", "menu Pomme") — that is the single strongest native signal in the corpus, and it is the thing machine output usually gets wrong. French typography is respected far beyond what most localised manuals bother with: the narrow non-breaking space before `: ; ! ?` is essentially perfect, guillemets are real guillemets, decimal commas are commas.

What gives it away is concentrated and diagnosable. Three tells:

1. **Dutch and English residue in the control descriptions.** «&nbsp;Min&nbsp;» and «&nbsp;Plus&nbsp;» as button labels are the loudest — a French reader does not read "Min" as *moins*, they read it as *minimum*, and the sentence stops making sense. "En mode général", "transfert vidéo", "Cela se fait facilement via", "Avec la prise en charge de Power Delivery", "Basculement vers la gauche – règle…" are all recognisable as source-shaped French.

2. **Repeated-root sentences that no French writer produces.** "Évitez … afin d'éviter", "prend en charge la charge", "la pièce centrale est bien centrée", "Téléchargez … page de téléchargement", "alimenté … alimentation". Individually each is a shrug; five of them across a manual set reads as unrevised output.

3. **Small word-choice errors with real consequences.** "l'entrée S6-R" for an output device, "interférences" for a power conflict, "jusqu'au clic" for *déclic*, "espaces humides" for damp environments, "angle d'appui", "3 × ports". These are the ones that make a reader pause and re-read, and they cluster on exactly the pages where a customer is holding hardware in one hand.

The pages a French customer is most likely to flag: **infinity-lite/installation.mdx** and **infinity-lite/controls.mdx** (the worst of the set — a single-screen product described in the plural, four unnatural collocations, a port-numbering contradiction with its own sibling page), **infinity/controls.mdx**, **dual-flip/controls.mdx** and the shared **safety.mdx** text. The pages that would pass unremarked: every index.mdx, every display-settings.mdx, panorama/installation.mdx, and both osd.mdx files for one-4k.

### Readability grade: **near-native**

Not "native": a native technical editor writing from scratch would not have produced the Dutch button labels, the repeated-root sentences, or "écran portable triple" in the opening line of a product description. Not "noticeably translated" either: there is no grammatical damage anywhere, the tone is consistent and professional, the typography is better than most French-original consumer documentation, and the OS-specific vocabulary is right. The gap between this and native is roughly one focused editing pass — perhaps forty findings, most of them one-line substitutions, concentrated in the controls and installation pages of three products. Fix the three Criticals and the fifteen or so Majors that involve a wrong word rather than a wrong fact, and this crosses into native.
