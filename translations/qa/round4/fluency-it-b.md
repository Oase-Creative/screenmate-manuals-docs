# Fluency review — Italian (batch B)

**Reviewer role:** native Italian technical editor, monolingual fluency pass
**Date:** 2026-08-12
**Scope:** `it/manuals/` — one-4k, one-4k-oled, dual-flip, infinity, infinity-lite, panorama (28 files read; `one-4k/safety.mdx`, `one-4k-oled/safety.mdx` and `dual-flip/display-settings.mdx` frontmatter only, per brief)
**Method:** Italian only. No en/ or nl/ file was opened. Findings are what an Italian customer or an Italian technical editor would react to, reading the page cold.

Format: `"quoted Italian" | issue | suggested rewrite | severity`

Recurring findings are itemised **once**, at the file where they first appear, with the other occurrences noted inline. Minors are capped at 15 per brief; a short "below the cap" list follows at the end.

---

## it/manuals/one-4k/index.mdx

**[MAJOR-01]** `"Si collega tramite USB-C o HDMI e supporta sia il video sia l'alimentazione su un solo cavo USB-C con i dispositivi compatibili."`
Two problems in one clause. `su un solo cavo` is a straight calque of "over a single cable" — Italian carries a signal *tramite / con* a cable, never *su*. And `con i dispositivi compatibili` is stranded at the end of the sentence, where an Italian reader expects a conditional clause.
→ *"Si collega tramite USB-C o HDMI e, sui dispositivi compatibili, trasporta video e alimentazione con un unico cavo USB-C."*
**Severity: Major** — also in `one-4k-oled/index.mdx`.

**[MINOR-01]** `"Questo è il tuo manuale digitale completo per lo Screenmate One 4K 15,6\"."`
`manuale ... per lo` mirrors English "manual for your". Italian idiom is *il manuale di*.
→ *"Questo è il manuale digitale completo del tuo Screenmate One 4K 15,6\"."*
**Severity: Minor** — identical wording on all six index pages (one-4k, one-4k-oled, dual-flip, infinity, infinity-lite, panorama).

**[MINOR-02]** `"pensato per darti un secondo schermo ad alta risoluzione per il tuo laptop, telefono, tablet o console di gioco"`
Three `per` in fourteen words; `darti ... per il tuo laptop` is clumsy.
→ *"pensato per offrirti un secondo schermo ad alta risoluzione da abbinare a laptop, telefono, tablet o console di gioco"*
**Severity: Minor** — same pattern in `one-4k-oled/index.mdx`.

**[MINOR-03]** `"| **Risoluzione** | 3840×2160 |"` vs `"| **Dimensioni** | 34,8 × 22,4 × 1,3 cm |"` (same table)
Page-internal typography inconsistency: the multiplication sign is unspaced in the resolution row and spaced in the dimensions row. `one-4k-oled/index.mdx` spaces both (`3840 × 2160`), so the house style clearly is spaced.
→ *"3840 × 2160"*
**Severity: Minor** — same split in `infinity/index.mdx`, `infinity-lite/index.mdx`, `panorama/index.mdx`.

---

## it/manuals/one-4k/controls.mdx

**[MAJOR-02]** `"**Pulsante +:** naviga verso l'alto nell'OSD; in modalità generale apre il menu delle scorciatoie per la luminosità."`
`in modalità generale` is not Italian — there is no "general mode" on this device; it is a word-for-word rendering of a source phrase meaning "in normal use". The Dual Flip page renders the same concept correctly as `nell'uso normale`. Second half: `menu delle scorciatoie` is a calque of "shortcut menu"; the Panorama page uses the natural `menu rapido`.
→ *"**Pulsante +:** sposta la selezione verso l'alto nell'OSD; durante l'uso normale apre il menu rapido della luminosità."*
**Severity: Major** — 2 occurrences here, 2 in `one-4k-oled/controls.mdx`.

**[MAJOR-03]** `"### Pulsante Menu (accensione / OSD)"` (this file) vs `"tieni premuto il pulsante di accensione per accendere il monitor"` (`osd.mdx`)
The same physical button is called **Pulsante Menu** on one page of the manual and **pulsante di accensione** on the next, with no bridge. The OSD page then compounds it with `"il pulsante sopra il pulsante di accensione"`. A reader flipping between the two pages has to work out that these are the same control.
→ Pick one name (recommend *pulsante Menu / accensione*) and use it on both pages.
**Severity: Major** — also one-4k-oled.

**[MINOR-04]** `"Quando viene ricevuto un segnale tramite la porta USB-C, lo Screenmate riconosce automaticamente gli accessori collegati."`
Agentless passive where Italian technical prose puts the device in the subject slot. Reads translated.
→ *"Quando riceve un segnale dalla porta USB-C, lo Screenmate riconosce automaticamente gli accessori collegati."*
**Severity: Minor** — also `one-4k/installation.mdx`, and both files' OLED twins (4 occurrences).

**[MINOR-05]** `"Questo singolo collegamento trasporta sia l'alimentazione sia il video con un solo cavo."`
`Questo singolo collegamento` is a calque of "This single connection", and the sentence then says "single" twice (*singolo collegamento* … *un solo cavo*).
→ *"Un unico cavo trasporta sia l'alimentazione sia il video."*
**Severity: Minor** — also one-4k-oled.

---

## it/manuals/one-4k/installation.mdx

**[MAJOR-04]** `"Se il tuo dispositivo supporta la ricarica tramite USB-C, lo schermo si ricarica automaticamente non appena colleghi il caricabatterie allo Screenmate."`
The subject switches mid-sentence: the condition is about *your device*, the result is about *lo schermo* (the Screenmate itself). An Italian reader cannot tell what is being charged — and since the monitor has no battery, the literal reading is nonsense.
→ *"Se il tuo dispositivo supporta la ricarica tramite USB-C, si ricarica automaticamente non appena colleghi il caricabatterie allo Screenmate."* — flag for source verification.
**Severity: Major** — also one-4k-oled.

**[MINOR-06]** `"il monitor deve essere alimentato separatamente tramite una fonte di alimentazione aggiuntiva"` (§1) vs `"alimenta il monitor separatamente tramite una fonte di alimentazione aggiuntiva"` (§3)
Same instruction, twice on one page, once as an impersonal passive and once as a *tu* imperative. The passive also echoes *alimentato / alimentazione*.
→ Use the imperative in both: *"alimenta il monitor separatamente con una fonte esterna"*.
**Severity: Minor** — same passive/imperative clash in `dual-flip/installation.mdx` ("lo Screenmate deve essere collegato a una fonte di alimentazione").

**[MINOR-07]** `"Con il supporto Power Delivery (PD), lo Screenmate passa automaticamente alla modalità di ricarica rapida."`
`Con il supporto X` = "With X support". Italian states the condition.
→ *"Se il dispositivo supporta il Power Delivery (PD), lo Screenmate passa automaticamente alla ricarica rapida."*
**Severity: Minor** — also one-4k-oled.

**[MINOR-08]** `"Nota: il tuo telefono o tablet deve avere una porta USB-C con supporto video – non tutte le porte USB-C possono trasmettere il video."`
Inline unstyled `Nota:` in running text on a page that otherwise puts every aside in a `<Note>` callout headed `**Importante:**`. Page-internal inconsistency.
→ Move into a `<Note>` block for consistency with the rest of the page.
**Severity: Minor**

**[MINOR-09]** `"Quando entrambi i collegamenti sono stati effettuati, il segnale video della console compare automaticamente sul monitor."`
Heavy passive periphrasis; Italian instructions use the participial shortcut.
→ *"Una volta effettuati entrambi i collegamenti, il segnale video della console compare automaticamente sul monitor."*
**Severity: Minor** — 2× on this page, 2× in one-4k-oled.

---

## it/manuals/one-4k/osd.mdx

**[MINOR-10]** frontmatter `description: "Impostazioni schermo dal menu a schermo"`
*schermo … schermo* in six words, in a string that shows in navigation and search results. Also `impostazioni schermo` without an article reads as a copy of the Windows UI label, not as prose.
→ *"Regola le impostazioni del monitor dal menu OSD"*
**Severity: Minor** — identical in `one-4k-oled/osd.mdx` and `dual-flip/osd.mdx`; the Panorama variant is worse (see MAJOR-33).

**[MINOR-11]** `"Tieni premuto il pulsante sopra il pulsante di accensione per **10 secondi** per sbloccarlo."`
*pulsante … pulsante* and *per … per* in one sentence, plus vague deixis ("the button above the power button" — which one?).
→ *"Per sbloccarlo, tieni premuto per 10 secondi il pulsante situato sopra quello di accensione."*
**Severity: Minor** — also one-4k-oled.

---

## it/manuals/one-4k/safety.mdx (frontmatter only)

`title: "Istruzioni di sicurezza"` / `description: "Informazioni di sicurezza e avvertenze importanti"` — both idiomatic. **No findings.**

---

## it/manuals/one-4k-oled/*

Shares MAJOR-01 to MAJOR-04, MINOR-01 to MINOR-11 with one-4k (counted there). File-specific:

**[MAJOR-05]** `controls.mdx`: `"### Porta USB-A"` followed by an MDX comment only
The heading renders with **no body text at all** — the customer sees a section title over blank space. Whatever the open question with the client, the published page should not ship an empty section; the one-4k twin has a full paragraph here.
→ Either carry over the one-4k wording or drop the heading until confirmed.
**Severity: Major** (published-page defect, visible to every reader)

**[MINOR — below cap]** `index.mdx`: `"un rapporto di contrasto di 100.000:1 – ideale per video, foto e lavori creativi"` — the appositive `ideale` grammatically attaches to *rapporto di contrasto*, not to the panel it is meant to describe.

---

## it/manuals/dual-flip/index.mdx

**[MAJOR-06]** `"è un'estensione pieghevole a doppio schermo che si fissa al tuo laptop e si apre in due schermi aggiuntivi da 16\""`
`si apre in due schermi` is a calque of "unfolds into two screens". In Italian something *si apre a formare* / *si apre rivelando*; *aprirsi in* means splitting/cracking, which is exactly the wrong image for a product you are told not to press on.
→ *"…si fissa al tuo laptop e si apre a formare due schermi aggiuntivi da 16\", uno per lato."*
**Severity: Major**

**[MAJOR-07]** `"| **Precisione cromatica** | 100% sRGB |"`
Every other product in this batch labels this row **Gamma cromatica** (one-4k, one-4k-oled, infinity, infinity-lite, panorama). Two names for one spec across the range — and *precisione* (accuracy, i.e. ΔE) is not what 100% sRGB expresses; it is coverage.
→ *"Gamma cromatica"*
**Severity: Major** (terminology inconsistency + wrong term)

**[MAJOR-08]** `"Per un funzionamento a basso consumo, ti consigliamo di scollegare il cavo di alimentazione quando il monitor non è in uso."`
`Per un funzionamento a basso consumo` is a calque, and it is self-defeating: unplugging the cable is not a *funzionamento*.
→ *"Per ridurre i consumi, ti consigliamo di scollegare il cavo di alimentazione quando non usi il monitor."*
**Severity: Major**

**[MAJOR-09]** `"Non ruotare gli schermi oltre l'angolo massimo indicato qui sotto."` + `"**Schermo sinistro:** 0° – 245° (si inclina di 180° verso l'alto e verso il basso)"`
Two problems. (a) The instruction says *ruotare*, the specs say *si inclina* — one movement, two verbs, three lines apart. (b) The parenthesis (180°) contradicts the range it annotates (0°–245°), so the reader is left without a usable limit — on the one warning where a limit actually matters.
→ Unify the verb and restate: *"Schermo sinistro: apertura da 0° a 245°"*; verify the 180° figure.
**Severity: Major**

**[MINOR-12]** `"Abbi cura del tuo Screenmate Dual Flip e non premere sugli schermi per evitare danni."`
`Abbi cura` is correct but literary/elevated — it clashes with the plain *tu* voice used everywhere else ("Usa", "Collega", "Metti").
→ *"Maneggia con cura il tuo Screenmate Dual Flip e non premere sugli schermi, per evitare danni."*
**Severity: Minor**

---

## it/manuals/dual-flip/controls.mdx

**[MAJOR-10]** `"### Porta USB-C\n\nAlimentazione e trasmissione video."` — repeated **verbatim, twice in a row**
Two identical headings with identical bodies. The reader has no way to tell the two ports apart, which matters because `installation.mdx` then says to connect *"un lato"* and *"l'altro lato"*. It also produces two colliding anchors.
→ *"### Porte USB-C (2×)"* with one description, or label them *(sinistra)* / *(destra)*.
**Severity: Major**

**[MAJOR-11]** `"Aumenta la luminosità nell'uso normale e naviga / aumenta i valori all'interno del menu OSD."` (and the mirror sentence on the − button)
`navigare` is intransitive in Italian — `naviga … i valori` is ungrammatical as written, and the reader has to reverse-engineer that the object belongs only to the second verb. The bare slash between two conjugated verbs is not Italian punctuation practice.
→ *"Nell'uso normale aumenta la luminosità; nel menu OSD sposta la selezione e aumenta i valori."*
**Severity: Major** (2 occurrences)

**[MINOR-13]** `"Tieni premuto per tornare alla pagina precedente."`
An OSD has *menu* and *livelli*, not *pagine*; `one-4k/osd.mdx` correctly says `menu precedente`.
→ *"Tieni premuto per tornare al menu precedente."*
**Severity: Minor** — also `dual-flip/osd.mdx` ("per tornare alla pagina precedente").

---

## it/manuals/dual-flip/installation.mdx

Cleanest file in the batch. The step lists ("Estrai con cura lo Screenmate dalla confezione", "Appoggia lo Screenmate su una superficie piana") read as originally-Italian instructions. Only the shared passive/imperative clash (MINOR-06) applies.

---

## it/manuals/dual-flip/osd.mdx

**[MINOR-14]** `"**SHARPNESS (0–4):** regola la nitidezza dell'immagine."` / `"**LOW BLUE LIGHT:** riduce la quantità di luce blu"` alongside `"**DCR:** scegli ON o OFF"` / `"**RESET:** scegli RESET per riportare…"`
One bullet list, two grammatical voices: third-person descriptions of what the setting does, and second-person imperatives telling you what to do. The reader keeps re-parsing.
→ Standardise on the third person (*regola, riduce, ripristina, imposta*).
**Severity: Minor** — same mix in `panorama/controls.mdx` ("Naviga nel menu" / "Riduce valori" / "Apre il menu rapido").

**[MINOR — below cap]** `"riduce la quantità di luce blu sullo schermo per ridurre l'affaticamento degli occhi"` — *riduce … ridurre* echo; use *per limitare l'affaticamento*.

---

## it/manuals/dual-flip/safety.mdx

**[CRITICAL-01]** two consecutive bullets:
`"- Il monitor funziona con un ingresso DC compreso tra 5 V e 20 V (con una tolleranza di ±2 V)."`
`"- Usa il dispositivo esclusivamente con una fonte di alimentazione da 5 V tramite il cavo appropriato."`
The list states a 5–20 V input range and then, in the very next line, restricts the user **esclusivamente** to 5 V. An Italian reader following the safety list literally gets contradictory electrical instructions, in the one section where ambiguity is not acceptable. `esclusivamente` is the aggravating word — without it the two lines could be read as range + typical case.
→ Reconcile: *"Il monitor accetta una tensione di ingresso DC da 5 V a 20 V (tolleranza ±2 V). Usa solo l'alimentatore e i cavi in dotazione."* Requires source verification before rewording.
**Severity: Critical** (safety-relevant contradiction; likely source-inherited, but reader-facing)

**[MAJOR-12]** `"Usa esclusivamente l'alimentatore AC/DC in dotazione come alimentazione."`
`come alimentazione` is a calque of "as power supply" — in Italian an *alimentatore* **is** the supply, so the phrase is circular. A native writes the verb, not the apposition.
→ *"Alimenta il dispositivo esclusivamente con l'alimentatore AC/DC in dotazione."*
**Severity: Major** — same phrase in `infinity/safety.mdx`, `infinity-lite/safety.mdx`, `panorama/safety.mdx` (4 pages in this batch; the pattern also runs through the other product families site-wide).

**[MAJOR-13]** `"Assicurati che la presa di corrente sia correttamente dotata di messa a terra e adatta all'amperaggio corretto."`
*correttamente … corretto* in one sentence, and `adatta all'amperaggio corretto` is circular (suitable for the correct amperage — which is?).
→ *"Assicurati che la presa sia dotata di messa a terra e adeguata all'amperaggio richiesto dal dispositivo."*
**Severity: Major** — all 5 safety pages in this batch.

**[MAJOR-14]** `"Il monitor funziona con un ingresso DC compreso tra 5 V e 20 V"` / `"L'ingresso DC necessario è compreso tra 5 V e 20 V"` (infinity, infinity-lite, panorama)
`ingresso DC` is being used as if it were a *voltage*; in Italian *ingresso* is the port, *tensione* is the quantity that has a range. Two different phrasings of the same line across the batch compounds it.
→ *"La tensione di alimentazione DC deve essere compresa tra 5 V e 20 V (tolleranza ±2 V)."*
**Severity: Major** — 4 pages in this batch.

**[MINOR-15]** `"Evita l'esposizione a umidità, polvere ed elettricità statica per evitare danni ai componenti elettronici."`
*Evita … evitare* echo. The infinity/infinity-lite/panorama variant repeats it (*"Evita gli ambienti umidi … per evitare danni"*).
→ *"…per prevenire danni ai componenti elettronici."*
**Severity: Minor** — 4 pages.

**[MINOR — below cap]** `"garantisci una circolazione dell'aria sufficiente"` → *assicura una ventilazione sufficiente*; `"apparecchiature trasmittenti"` → *apparecchi che emettono segnali radio*.

---

## it/manuals/dual-flip/display-settings.mdx (frontmatter only)

**[MINOR — below cap]** `title: "Impostazioni schermo"` + `description: "Impostazioni schermo per Windows e macOS"` — the description restates the title verbatim. The Infinity pair does this properly (*title* "Impostazioni schermo e audio" / *description* "Configurazione degli schermi aggiuntivi e dell'audio su Windows e macOS").

---

## it/manuals/infinity/index.mdx

**[MAJOR-15]** `"…si aggancia dietro il tuo laptop e ti dà due schermi in più contemporaneamente."`
`contemporaneamente` dangles — "at the same time" as what? In the English/Dutch pattern it modifies "gives you two extra screens at once"; in Italian, *due schermi in più* already carries the plurality and the adverb reads as an unfinished comparison.
→ *"…si aggancia dietro il tuo laptop e ti offre due schermi aggiuntivi."*
**Severity: Major**

**[MAJOR-16]** `"Ogni schermo ha altoparlanti integrati"` (index) vs `"Ogni schermo ha un altoparlante integrato sul bordo esterno."` (`controls.mdx`)
Plural on one page, singular on the next, for the same hardware. The customer counting speakers gets two different answers from the same manual.
→ Pick the correct count and use it in both places.
**Severity: Major**

---

## it/manuals/infinity/controls.mdx

**[CRITICAL-02]** `"### Luminosità e volume\n\n- **Premi a destra (\"Plus\"):** aumenta la retroilluminazione (luminosità).\n- **Premi a sinistra (\"Min\"):** riduci il volume."`
Under a heading promising *brightness and volume*, the reader is told only how to **raise brightness** and **lower volume**. There is no documented way to lower brightness or raise volume — the pair is asymmetric and the device becomes undocumentable from this page. Two further defects in the same two lines: the voice flips between third person (`aumenta` = "it increases") and imperative (`riduci` = "reduce!"), and the sibling product `infinity-lite/controls.mdx` maps the same labels the *other* way round (there, left = brightness, right = volume), so a customer owning both is actively misled.
→ *"- **Premi a destra (+):** aumenta la luminosità; premi a sinistra (−) per ridurla.\n- …"* — needs the real gesture map from the client before rewording.
**Severity: Critical** (meaning-breaking; user cannot operate the control)

**[MAJOR-17]** `"(\"Plus\")"` / `"(\"Min\")"`
`Min` is not English and not Italian — it is Dutch (*min* = minus). To an Italian reader it parses as an abbreviation of *minimo*, i.e. the opposite of a direction. The brief's carve-out covers English technical terms and ALL-CAPS device labels; this is neither.
→ Use the physical symbols *(+)* / *(−)*, or *"Più"* / *"Meno"*.
**Severity: Major** — also `infinity-lite/controls.mdx` (both buttons).

**[MAJOR-18]** `"La disposizione è speculare sullo schermo sinistro e su quello destro."`
Wrong preposition: mirroring is a relation *between* two things. *Speculare su X e su Y* is not an Italian collocation.
→ *"La disposizione dello schermo destro è speculare rispetto a quella del sinistro."*
**Severity: Major**

**[MAJOR-19]** `"Un pulsante girevole sul retro di ogni schermo che comanda l'accensione, il menu a schermo, la luminosità e il volume."`
`girevole` means *rotating* — but every gesture documented ten lines below is a **press** (`Pressione breve`, `Premi a destra`, `Premi a sinistra`). The reader will try to turn a control that is pushed.
→ *"Un pulsante multidirezionale (levetta) sul retro di ogni schermo, che comanda…"*
**Severity: Major**

**[MINOR — see MINOR list]** `"per l'elenco completo dei gesti"` / `"Gli stessi gesti funzionano su entrambi gli schermi."` — in Italian *gesti* belongs to touch/trackpad interaction; for physical button presses a native writes *comandi* or *combinazioni*. **(MINOR-16 — over cap, retained as it recurs.)**

**[MINOR — below cap]** frontmatter `title: "Porte e comandi"` while the page's own H2 is `## Porte e pulsanti` (and every sibling product uses *Porte e pulsanti* for both). The reader clicks one label and lands on another.

---

## it/manuals/infinity/installation.mdx

**[MAJOR-20]** `"- 1 USB-C e 1 USB e 1 HDMI"`
Two `e` in a three-item list (Italian coordinates *A, B e C*), and `1 USB` is unqualified where the whole point is distinguishing USB-A from USB-C. `dual-flip/installation.mdx` gets the identical list right: *"1 USB-C, 1 USB-A e 1 HDMI"*.
→ *"1 USB-C, 1 USB-A e 1 HDMI"*
**Severity: Major**

**[MAJOR-21]** `"collega un'alimentazione esterna con un cavo da USB-A a USB-C"` (and 2 more occurrences on the page)
You connect a *power supply* (`un alimentatore`), not an *alimentazione* — the abstract noun cannot be the object of *collegare*. `infinity-lite/index.mdx` and `infinity-lite/installation.mdx` get this right with `collega un alimentatore esterno da 5 V/2 A`, so the corpus contradicts itself as well.
→ *"collega un alimentatore esterno con un cavo da USB-A a USB-C"*
**Severity: Major** (3 occurrences)

**[MAJOR-22]** `"Assicurati che il dispositivo supporti l'uscita video tramite USB-C e collega anche qui un'alimentazione esterna."`
`anche qui` is a positional calque ("here too"), but in Italian *qui* points at a place on the page, not at a scenario.
→ *"…e, anche in questo caso, collega un alimentatore esterno."*
**Severity: Major**

**[MINOR — below cap, 6 items]**
- `"Allora puoi collegare lo Screenmate direttamente con due cavi USB-C."` — the resumptive *Allora* after a question is a Dutch/English tic; Italian drops it.
- `"Lo Screenmate funziona anche con uno smartphone, Nintendo Switch, PlayStation o Xbox."` — articles present on the first item only → *"con uno smartphone, una Nintendo Switch, una PlayStation o una Xbox"*.
- `"Riponi il set completamente chiuso nella custodia in pelle in dotazione."` — the index calls it `Custodia protettiva`; also *in … in* stacking.
- `"Ogni schermo ruota al massimo di 90°."` then, six lines later, `"Ogni schermo ha una rotazione massima di 90°."` — verbatim redundancy.
- `"Assicurati che l'elemento centrale sia ben centrato rispetto al laptop."` — *centrale/centrato* echo.
- alt text `"Configurazione orizzontale"` vs the visible caption `"Vista orizzontale"` directly beneath it.

---

## it/manuals/infinity/display-settings.mdx

**[MAJOR-23]** `"Usa il pulsante **Identifica** per vedere quale schermo ha quale numero."`
`quale … quale` is a word-for-word rendering of "which screen has which number" and is not an Italian construction. The proof it is avoidable: `panorama/osd.mdx` writes the same instruction natively — *"per vedere quale numero corrisponde a ciascuno schermo"*.
→ *"Usa il pulsante Identifica per vedere quale numero corrisponde a ciascuno schermo."*
**Severity: Major** — also `infinity-lite/display-settings.mdx` (×2). The same calque appears in the other product families site-wide (onecable, flip, expand, dual-flip), so a global fix is worth scheduling.

**[MAJOR-24]** `"**Vuoi più spazio a schermo?** Fai clic su **Ridimensionamento** e impostalo su **150%** per testo ed elementi più grandi."`
The answer contradicts the question. Raising scaling to 150% gives you *less* usable desktop space and bigger elements. A customer who wants more room and follows this ends up with the opposite.
→ *"**Vuoi testo ed elementi più grandi?** Fai clic su Ridimensionamento e impostalo su 150%."*
**Severity: Major** — also `infinity-lite/display-settings.mdx` and `panorama/osd.mdx` (3 pages).

**[MINOR — below cap]** `"per sentire l'audio attraverso il tuo Screenmate"` — *attraverso* is a calque of "through"; Italian *riprodurre l'audio dagli altoparlanti dello Screenmate*. Also `"In fondo trovi una scorciatoia per le impostazioni audio complete"` — a link is *un collegamento*, not *una scorciatoia*.

---

## it/manuals/infinity/safety.mdx

Shares MAJOR-12/13/14 and MINOR-15.

**[MINOR — below cap]** `"- Adatto sia all'uso domestico sia a quello aziendale."` — a bare descriptive fragment dropped into a list of imperatives; and `panorama/safety.mdx` renders the identical item as `professionale`. Section headings also drift across the three files: `### Controlla prima dell'uso` (infinity) / `### Leggi prima dell'uso` (infinity-lite) / `### Prima dell'uso` (panorama).

---

## it/manuals/infinity-lite/index.mdx

**[MINOR — below cap]** `"…ti offre un display portatile in più per avere più spazio di lavoro ovunque ti trovi"` — *più … più* echo, and *display* appears in the same sentence as *schermo* / *estensione schermo*. Across the batch the same object is called *schermo*, *display* and *monitor* interchangeably (see also panorama/index and panorama/osd).

---

## it/manuals/infinity-lite/controls.mdx

**[CRITICAL-03]** `"### USB-C (per il cavo da HDMI a USB-C)\n\nLa porta più a sinistra in basso."` (this file)
vs `"Collega il cavo da HDMI a USB-C alla **terza** porta dello Screenmate per il segnale video."` (`installation.mdx`, inside a `<Warning>`)
The two pages give **incompatible port instructions** for the same cable: controls says the HDMI-to-USB-C cable goes in the *leftmost / first* port, installation says the *third*. Worse, controls documents only two USB-C ports plus a 3.5 mm jack, so "the third port" has no referent at all — and installation's other line (*"Inserisci il cavo nella prima o nella seconda porta"*) confirms only two exist. A customer following the Warning cannot get video at all.
→ Establish the real port map and use one numbering scheme on both pages (recommend naming, not ordinals: *"la porta USB-C contrassegnata HDMI"*).
**Severity: Critical** (meaning-breaking; blocks setup)

**[MAJOR-25]** `"### Pulsante sinistro \"Min\"\n\nSposta verso sinistra – regola la retroilluminazione (luminosità)."`
`Sposta verso sinistra` is a transitive imperative with no object — "move (what?) to the left". For a rocker the Italian verb is *spingi/premi*, and the object must be stated.
→ *"Spingi il pulsante verso sinistra per regolare la retroilluminazione (luminosità)."*
**Severity: Major** (2 occurrences: left and right buttons)

---

## it/manuals/infinity-lite/installation.mdx

**[MAJOR-26]** `"Segui questi passaggi nell'ordine indicato per posizionare in sicurezza entrambi gli schermi aggiuntivi dietro il laptop."` (also `### 6. Apri gli schermi`, `### 7. Chiudi gli schermi`)
The Infinity **Lite** is a single-screen extension — its own index says `"ti offre un display portatile in più"`. This page repeatedly says *entrambi gli schermi* / *gli schermi*, which reads as leftover copy from the two-screen Infinity and leaves the customer looking for a second panel.
→ Singular throughout: *"per posizionare in sicurezza lo schermo aggiuntivo dietro il laptop"*.
**Severity: Major**

**[MAJOR-27]** `"Fissa il supporto principale"` / `"Monta il sostegno dello schermo"` / `"Regola il supporto"` / `"completa l'installazione del supporto per schermo"` / `"Appoggia il piccolo sostegno"`
Within seven numbered steps the same family of parts is called *supporto*, *supporto principale*, *sostegno*, *sostegno dello schermo*, *supporto per schermo* and *piccolo sostegno*. The reader cannot tell how many distinct parts exist — which is fatal in an assembly sequence.
→ Fix one term per physical part (e.g. *supporto* for the main stand, *piedino* for the small foot) and use it consistently.
**Severity: Major**

**[MAJOR-28]** `"Apri il telaio con uno scatto per estrarlo."`
Not Italian: you do not "open something with a click" in this sense. The intended action (a snap/click release) needs a different verb.
→ *"Fai scattare il telaio verso l'esterno per estrarlo."*
**Severity: Major**

**[MAJOR-29]** `"Segui la sequenza corretta durante l'apertura e la chiusura per evitare danni al dispositivo. Riponi lo Screenmate con cura per evitare danni all'apparecchiatura."`
The same purpose clause twice in consecutive sentences, with two different nouns (*dispositivo* / *apparecchiatura*) for the same object — reads like two source lines pasted together.
→ *"Segui la sequenza corretta in apertura e in chiusura, e riponi lo Screenmate con cura, per evitare danni al dispositivo."*
**Severity: Major**

**[MAJOR-30]** `"Passa alla modalità di collegamento corretta (è necessaria un'alimentazione esterna) per usare lo Screenmate con un telefono, una console di gioco o un altro dispositivo USB-C. Anche la modalità telefono richiede un'alimentazione esterna."`
Three defects: the external-power requirement is stated twice in two sentences; `modalità telefono` appears out of nowhere and is defined nowhere; and the reader is told to switch to "the correct connection mode" without being told what the modes are or how to switch.
→ *"Per usare lo Screenmate con un telefono, una console di gioco o un altro dispositivo USB-C serve sempre un alimentatore esterno."* (plus the actual switching instructions, if any).
**Severity: Major**

**[MINOR — below cap]** Two plain assembly instructions are wrapped in `<Warning>` callouts (steps 3 and 5: *"Tieni con entrambe le mani i due punti…"*, *"Apri il supporto, regolalo sull'angolo…"*). Warning styling on non-warnings dilutes the real ones. Also `"per collegare il prodotto al laptop"` — *il prodotto* is impersonal shop-talk in a *tu*-voice manual (→ *per collegarlo al laptop*).

---

## it/manuals/infinity-lite/display-settings.mdx

**[CRITICAL-04]** `"Seleziona lo schermo interessato, vai su 'Orientamento dello schermo' e scegli 'Duplicato' per correggerlo."` (Tabs section)
vs, on the **same page**, `"Seleziona lo schermo interessato, vai su **Orientamento dello schermo** e scegli **Capovolto** per correggerlo."`
The page gives two different answers to the same problem, and the second one is wrong on its own terms: *Duplicato* is not an orientation value at all — it is a multi-display mode. A customer with an upside-down screen who follows the Tabs version will mirror their desktop instead of fixing rotation, then have to undo it.
→ Delete the `Duplicato` variant; keep `Capovolto` (ideally the full Windows label, *"Orizzontale (capovolto)"*).
**Severity: Critical** (wrong UI value; user is actively misdirected)

**[MAJOR-31]** `"3. Fai clic su **Disponi** come mostrato nell'immagine 1."` vs `"3. Fai clic su Disposizione."` — same page, same macOS button
Two names for one button, and `Disposizione` is not the macOS Italian label (it is **Disponi**). The reader will hunt for a control that isn't there.
→ Use `Disponi` in both places.
**Severity: Major**

**[MAJOR-32]** `"è indicato come **S6-L (HD Audio Driver for Display Audio)** (l'altro schermo compare come **S6-R**)"`
`l'altro schermo` presupposes a second panel; the Infinity Lite has one. Copy carried over from the Infinity page without adaptation, and the reader will look for an S6-R entry that never appears.
→ Drop the parenthesis on this product.
**Severity: Major**

**[MINOR-17]** UI strings are quoted three different ways on one page: `**Estendi il desktop a questo schermo**` (bold, top section), `'Estendi il desktop a questo schermo'` (single quotes, Tabs section), and plain unmarked `Impostazioni schermo`. The sibling pages (infinity, panorama) apply a consistent rule — bold for controls, bold+quotes for values.
→ Adopt the sibling rule page-wide.
**Severity: Minor**

**[MINOR — below cap]** `"Disponi tutti e tre gli schermi nella vista **Identifica**"` — *Identifica* is a button, not a view.

---

## it/manuals/panorama/index.mdx

**[MAJOR-33]** `"Il driver dello schermo necessario consente di gestire tre schermi indipendenti con un solo cavo."`
Nominal, calqued word order — *il driver … necessario* postposed reads like a spec-sheet fragment, and the reader has no idea at this point that a driver must be installed at all (that comes only in installation.mdx). The sentence describes a requirement as though it were a feature.
→ *"Per gestire tre schermi indipendenti con un solo cavo devi installare l'apposito driver video (vedi Installazione)."*
**Severity: Major**

**[MINOR — below cap]** `"un monitor portatile a tre schermi che ti offre tre display Full HD da 15,6\""` — *monitor*, *schermi* and *display* for the same object inside one sentence (recurs in `panorama/osd.mdx`: *"per configurare ciascun display"*). Also `"(oppure con USB-A + HDMI come alternativa)"` — *oppure* and *come alternativa* say the same thing twice. Content flag, not language: `| **Angolo di visione** | 360° |` is implausible (every sibling IPS panel lists 178°) — worth a source check.

---

## it/manuals/panorama/controls.mdx

**[MINOR-18]** `"### 3 × porte Mini-HDMI"`
The multiplication sign as a prefixed quantifier before a noun is English/Dutch spec-sheet style; Italian either writes the numeral plainly or puts the multiplier in parentheses.
→ *"### Porte Mini-HDMI (3×)"*
**Severity: Minor**

**[MINOR — below cap]** `"conferma una selezione o passa al passaggio successivo del menu"` — *passa/passaggio* echo, and a menu has *voci*, not *passaggi* → *"o passa alla voce successiva del menu"*.

---

## it/manuals/panorama/installation.mdx

**[MAJOR-34]** `"**Attenzione:** bada alle dita quando pieghi gli schermi, per evitare di schiacciarle."`
`bada alle dita` is colloquial and, in this construction, unidiomatic — *badare a* means "to look after / mind (a child, the shop)". No Italian technical writer would use it in a pinch-point warning. The same product's `safety.mdx` gets it right: *"Fai attenzione alle dita quando richiudi o apri gli schermi."*
→ *"**Attenzione:** fai attenzione alle dita quando pieghi gli schermi, per evitare di schiacciarle."*
**Severity: Major**

**[MAJOR-35]** `"La porta USB-C di un laptop da sola non fornisce abbastanza alimentazione per far funzionare il Panorama alla massima luminosità."`
*Alimentazione* is not a quantifiable substance in Italian — you cannot have "enough alimentazione"; the quantifiable nouns are *energia*, *potenza*, *corrente*. Word order is also inverted-calqued (*di un laptop da sola*).
→ *"Da sola, la porta USB-C del laptop non eroga potenza sufficiente per far funzionare il Panorama alla massima luminosità."*
**Severity: Major**

**[MAJOR-36]** `"Sul monitor, collega il cavo HDMI alla porta HDMI accanto al cavo di alimentazione bianco."`
The monitor has **Mini-HDMI** ports — `controls.mdx` says so explicitly (`### 3 × porte Mini-HDMI`), and the same paragraph calls the cable `da Mini-HDMI a HDMI`. Telling the user to plug into "the HDMI port on the monitor" sends them to the wrong end of the cable.
→ *"Sul monitor, collega l'estremità Mini-HDMI alla porta Mini-HDMI accanto al cavo di alimentazione bianco."*
**Severity: Major**

**[MINOR — below cap]** `"Usa il cavo bianco lungo per l'alimentazione e il cavo nero corto…"` — two stacked postnominal adjectives without coordination; Italian → *"il cavo bianco più lungo … il cavo nero più corto"*. Also `"Collegare un caricabatterie separato al laptop mentre anche il Panorama fornisce alimentazione può causare interferenze."` — impersonal infinitive subject in a *tu*-voice page → *"Se colleghi un caricabatterie separato…, potresti causare interferenze."* And `## Installa il driver dello schermo` is the only imperative H2 among noun-phrase H2s (*Montaggio*, *Opzioni di collegamento*).

---

## it/manuals/panorama/osd.mdx

**[MAJOR-37]** frontmatter `description: "Impostazioni schermo per singolo schermo dal menu a schermo"`
*schermo* three times in eight words. This string is what shows in navigation and search; no Italian editor would let it out.
→ *"Impostazioni indipendenti per ciascuno schermo dal menu OSD"*
**Severity: Major**

**[MAJOR-38]** `"Il Panorama gestisce tre schermi indipendenti, quindi potresti voler modificare la disposizione del desktop nel sistema operativo."`
`potresti voler + infinitive` is the textbook calque of English "you may want to". Italian expresses this with an impersonal usefulness construction, not with a modal chain.
→ *"…quindi può essere utile sistemare la disposizione del desktop nel sistema operativo."*
**Severity: Major**

**[MINOR — below cap]** `"Premi il pulsante **Esci**"` — `controls.mdx` names it `Pulsante Conferma / Esci`; and `"(monitor DP)"` is an unexplained abbreviation for a consumer reader → *"(lo schermo collegato in DisplayPort)"*.

Positive note: this page contains the batch's **best** rendering of the Windows instruction — *"per vedere quale numero corrisponde a ciascuno schermo"* — which is the phrasing the other five display-settings pages should adopt (MAJOR-23).

---

## it/manuals/panorama/safety.mdx

Shares MAJOR-12/13/14 and MINOR-15.

**[MINOR — below cap]** Heading `### Attenzione durante la chiusura` but the sentence under it covers both directions (*"quando richiudi o apri gli schermi"*) → *"Attenzione in apertura e chiusura"*.

---

# Totals by severity

| Severity | Count | Notes |
| :--- | ---: | :--- |
| **Critical** | 4 | 2 contradictory-instruction pairs (infinity-lite port map; infinity-lite orientation value), 1 broken control map (infinity brightness/volume), 1 safety-list voltage contradiction (dual-flip) |
| **Major** | 38 | itemised MAJOR-01 … MAJOR-38 |
| **Minor** | 18 itemised (cap ~15, 3 over) + ~24 listed compactly as "below the cap" | polish-level; the below-cap items are one-liners, not full entries |
| **Total itemised** | **60** | across 28 files |

**Distribution of the Majors:** 9 are cross-file recurrences (each counted once): the safety boilerplate accounts for 3 Majors × 4–5 pages, the display-settings boilerplate for 2 Majors × 3 pages, `in modalità generale` for 1 × 4 occurrences. Deduplicated, roughly **half the Major count comes from four shared text blocks** — fixing those blocks once clears ~20 page-level defects.

**What I did NOT flag** (deliberate conventions, per brief, all verified correct):
- *tu* register: consistent across all 28 files. **Zero** *Lei*/*voi* leakage found. The only register wobbles are impersonal passives/infinitives (MINOR-06, panorama below-cap), not honorific mixing.
- English technical terms (DisplayPort, HDMI, USB-C, OSD, DP Alt Mode, product names, ALL-CAPS OSD labels such as BRIGHTNESS/DCR/LOW BLUE LIGHT) — left alone. The one exception raised is `"Min"`, which is Dutch, not English (MAJOR-17).
- Number/unit formatting: Italian decimal comma (`15,6"`, `34,8 × 22,4`), dot thousands (`100.000:1`), SI spacing (`65 W`, `5 V/2 A`, `350 cd/m²`, `-20 °C`, `±2 V`) — all correct and consistent. Percentages are consistently unspaced (`100% sRGB`, `150%`), which matches Italian typographic practice; I did not treat that as an error.
- `ricarica inversa (reverse charging)` in panorama/installation — correctly glossed on first use.
- Apostrophes and quotes are uniformly straight (`'`, `"`) across all 28 files — no curly/straight mixing anywhere. Elisions are all correct (`un'alimentazione`, `un'estensione`, `un'esperienza`, `un adattatore`, `un alimentatore`).

**Morphology and orthography:** clean. I found **no** gender or number agreement errors, **no** missing or wrong accents (`è`, `dà`, `finché`, `perché` all correct where they appear), **no** wrong articles (`lo Screenmate` before *s impura* is right throughout), and no typos. `sia … sia` is used correctly and consistently in place of `sia … che`. This is genuinely well-formed Italian at the word level.

---

# Verdict

## Would an Italian customer notice this is a translation?

**Yes — a moderately attentive one would, and a technical reader certainly would. But not from the grammar: from the collocations, the echoes, and the drift.**

**Readability grade: near-native**, with two qualifications — the shared boilerplate (safety pages, display-settings pages) drops to **noticeably translated**, and four passages fail on *usability* rather than language.

### Reasoning

**What holds up.** Sentence-by-sentence the copy is fluent. Word-level Italian is essentially flawless — no agreement errors, no accent errors, no article errors, correct elisions, correct `sia…sia`, correct `finché non`, correct locale number formatting throughout. The *tu* voice is genuinely consistent across 28 files, which is harder than it sounds and is the single strongest signal of a controlled translation process. Several passages are indistinguishable from originally-authored Italian: the whole of `dual-flip/installation.mdx`, the Panorama assembly steps (*"Afferra gli schermi e tirali verso l'alto finché i piedini non entrano nel blocco anteriore"*), and the Panorama OSD Windows instruction, which is the best sentence in the batch.

**What gives it away.** Not errors — *collocations*. An Italian reader doesn't consciously parse `su un solo cavo`, `collega un'alimentazione esterna`, `come alimentazione`, `non fornisce abbastanza alimentazione`, `si apre in due schermi`, `potresti voler modificare`, `quale schermo ha quale numero`, `anche qui`, `in modalità generale`, `Sposta verso sinistra`, `Apri il telaio con uno scatto`. They register as a faint wrongness that accumulates: the prepositions are one notch off, the abstract nouns are being handled like countable ones, and the modal chains are English-shaped. Layered on top is a repetition texture no Italian editor would sign off — *Evita … evitare*, *riduce … ridurre*, *correttamente … corretto*, *passa … passaggio*, *centrale … centrato*, *evitare danni al dispositivo / evitare danni all'apparecchiatura* — which is the classic fingerprint of translating clause-by-clause without a final read-aloud pass.

**Where it stops being a style question.** Four findings are not fluency at all — they are places where the Italian page cannot be acted on. The Infinity Lite tells you to use the *third* port and the *leftmost* port for the same cable, on a product with two. The Infinity documents how to raise brightness and lower volume, and nothing else, from a two-direction control. The Infinity Lite tells you to fix an upside-down screen with `Duplicato`, three sections after telling you to use `Capovolto`. The Dual Flip safety list allows 5–20 V and then restricts you *esclusivamente* to 5 V. Three of these are almost certainly inherited from the source and will need Louie to adjudicate rather than an editor to reword — but they reach the Italian customer through the Italian page, so they belong in this report.

**Terminology drift** is the third axis and the most fixable: *supporto/sostegno* (five names, one assembly sequence), *Gamma cromatica/Precisione cromatica*, *pulsante Menu/pulsante di accensione*, *menu delle scorciatoie/menu rapido*, *schermo/display/monitor*, *Porte e comandi/Porte e pulsanti*, *aziendale/professionale*, *custodia protettiva/custodia in pelle*. None of these confuse on their own; together they tell the reader that no single hand held the whole product range.

### Recommendation

Do not re-translate — the base is sound. Three targeted passes clear most of it:
1. **The four Criticals**, with the client, before anything else.
2. **Four shared blocks** (safety boilerplate ×5 pages, display-settings boilerplate ×3, the `in modalità generale` control bullets ×4, the `ingresso DC` line ×4). Roughly half the Major count, fixed in four edits.
3. **A collocation sweep** for the recurring calques listed above, plus an Italian glossary entry per product part to stop the *supporto/sostegno* class of drift.

With those three passes the batch would read **native**. As it stands it reads like a very good translation — which is exactly the thing this review exists to catch.
