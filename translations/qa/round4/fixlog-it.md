# Round 4 — Italian fix log

**Date:** 2026-08-12 · **Branch:** `round4-fixes` · **Scope touched:** `it/**`,
`translations/glossary-it.md`, `translations/qa/round4/*-it.md`

**Inputs triaged:** `fluency-it-a.md` (1 Critical, 34 Major, 16 Minor) ·
`fluency-it-b.md` (4 Critical, 38 Major, 18 Minor + ~24 below-cap) ·
`safety-align-it.md` (PASS — 1 Major, 4 Minor)

**Commits**

| SHA | Scope |
|---|---|
| `605570c` | glossary meaning-inversion fix (`Need more overview?`) + its 6 pages |
| `ed87722` | fluency wave — 29 Italian pages + 4 glossary additions |
| *(this file)* | QA logs |

**Headline counts**

| Outcome | Count |
|---|---|
| **Fixed** | 21 distinct findings → 43 edits across 30 Italian pages + 5 glossary rows |
| **Rejected** (glossary-locked / DNT / locked convention / reviewer misreading) | 24 |
| **Source-flagged** (EN or NL says the same thing — `source-flags-it.md`) | 38 |
| **Deferred** (frozen safety bodies, or taste where a rewrite risks drift) | 12 |

---

## 1. Triage method

Every finding was checked against its English counterpart at the same path under `en/`, and against
`nl/` wherever the meaning was disputed. The three-way classification from the brief was applied
without exception:

- **Real Italian defect** — Italian diverges from the source, or is wrong/unnatural Italian while
  the source is fine → fixed here.
- **Source-inherited** — EN/NL says the same wrong or contradictory thing → Italian untouched,
  logged in `source-flags-it.md`.
- **Reviewer preference against a locked convention** → rejected, one line below.

This is why the fixed count is far smaller than the reported Major count: roughly half of the
reported Majors turned out to be faithful renderings of English text that is itself odd,
contradictory or inconsistent. Both fluency reviews were explicitly monolingual (no `en/` or `nl/`
file was opened), which is what the cross-check exists to catch.

`safety.mdx` bodies were treated as frozen throughout. `git diff --stat -- 'it/**/safety.mdx'` is
empty against the round-4 base.

---

## 2. Accepted — before → after

### 2.1 Meaning inversion (commit `605570c`)

**`**Vuoi più spazio a schermo?**` for EN `**Need more overview?**`** — glossary-locked at
§6 line 669 and §9.10, so the page fix alone would have been reverted by the next pass.

The question promised *more screen space*; the instruction it introduces raises Windows scaling to
150%, which enlarges text and leaves **less** usable space. NL: `Behoefte aan meer overzicht?`
(= "need more overview"), FR already correct with `Besoin d'une meilleure vue d'ensemble ?`.

> before: `**Vuoi più spazio a schermo?**`
> after:  `**Vuoi una visione d'insieme migliore?**`

Applied to the 6 pages whose English reads `Need more overview?`:

| File | Line |
|---|---|
| `it/manuals/onecable/display-settings.mdx` | 34 |
| `it/manuals/expand/display-settings.mdx` | 34 |
| `it/manuals/flip/display-settings.mdx` | 34 |
| `it/manuals/dual-flip/display-settings.mdx` | 34 |
| `it/manuals/infinity-lite/display-settings.mdx` | 23, 59 |

**Glossary, and this is the load-bearing part:** §9.10 previously collapsed three *different*
English prompts onto this one Italian target. That collapse is now **split**, because the three
English prompts do not say the same thing:

| EN | IT (locked) | Pages |
|---|---|---|
| `Need more overview?` | `Vuoi una visione d'insieme migliore?` | the 6 above |
| `Want more on-screen space?` · `Need more room?` | `Vuoi più spazio a schermo?` *(unchanged — faithful)* | `infinity/display-settings.mdx`, `panorama/osd.mdx` |

`§6` line 669 records the old target as a rejected rendering with the reason, so it cannot be
reintroduced. The two retained occurrences are logged in `source-flags-it.md` §3.1 — the English
prompts themselves fit the answer badly, which is an EN-side call.

`safety-align-it.md` also flagged German as carrying the same error (`Brauchst du mehr Platz?`);
out of scope here, handed to the DE agent via the controller.

### 2.2 Cross-page harmonisation (commit `ed87722`)

**a. `quale schermo ha quale numero` → `quale numero corrisponde a ciascuno schermo`** — 7
occurrences. The EN correlative `which screen has which number` has no Italian equivalent;
`panorama/osd.mdx` already carried the natural rendering, which is now the locked target
(glossary §9.10).

> before: `Usa il pulsante 'Identify' ('Identifica') per vedere quale schermo ha quale numero.`
> after:  `Usa il pulsante 'Identify' ('Identifica') per vedere quale numero corrisponde a ciascuno schermo.`

Files: the 4-product shared body (`onecable`, `expand`, `flip`, `dual-flip` display-settings L23),
`infinity/display-settings.mdx` L18, `infinity-lite/display-settings.mdx` L16 and L48.

**b. Index boilerplate, 11 pages.** `manuale … per lo Screenmate X` is an EN/NL calque (`for the` /
`voor de`); Italian marks the relation with the genitive, and `it/manuals-index.mdx` already said
`il manuale digitale completo del tuo prodotto Screenmate`.

> before: `Questo è il tuo manuale digitale completo per lo Screenmate Expand.`
> after:  `Questo è il manuale digitale completo del tuo Screenmate Expand.`

All 11 `it/manuals/*/index.mdx`. Added to glossary §9.9 boilerplate.

**c. Resumptive `Allora` after a rhetorical question — 4 occurrences.** The question itself is
source structure (EN `…? Then …`, NL `…? Dan …`) and is preserved; only the resumptive adverb,
which Italian does not use, is dropped. `one-4k/installation.mdx` already had the correct pattern
(`Serve alimentazione aggiuntiva? Usa il cavo…`).

| File | before | after |
|---|---|---|
| `onecable/installation.mdx` L30 | `…inferiore a 10 W? **Allora serve** un'alimentazione aggiuntiva…` | `…inferiore a 10 W? **Serve** un'alimentazione aggiuntiva…` |
| `onecable/installation.mdx` L44 | `**Allora collega** l'altro cavo USB…` | `**Collega** l'altro cavo USB…` |
| `onecable/troubleshooting.mdx` L41 | `…uscita USB-C? **Allora usa** un caricabatterie PD…` | `…uscita USB-C? **Usa** un caricabatterie PD…` |
| `infinity/installation.mdx` L42 | `…l'alimentazione? **Allora puoi** collegare…` | `…l'alimentazione? **Puoi** collegare…` |

Reviewer A reported 11 occurrences; 4 are literal `Allora`, the other 7 line references are plain
question-headers that mirror the English structure and were left alone.

**d. `Dopo un'installazione riuscita` → `A installazione completata` — 3 occurrences.** Word-for-word
rendering of `After successful installation`; Italian uses the absolute construction.
`onecable/installation-windows.mdx` L37, `onecable/installation-mac.mdx` L38 and L54.

**e. Spec-list coordination `A e B e C` → `A, B e C` — 2 files.** Italian coordinates a list with
commas and a final `e`; `flip/installation.mdx` and `dual-flip/installation.mdx` already did.

> `expand/installation.mdx`: `- 1 USB-C e 1 USB-A e 1 HDMI` → `- 1 USB-C, 1 USB-A e 1 HDMI`
> `infinity/installation.mdx`: `- 1 USB-C e 1 USB e 1 HDMI` → `- 1 USB-C, 1 USB e 1 HDMI`

(`1 USB` is left unqualified because the English says `1× USB` — naming it `USB-A` would invent a
product fact. Logged for the client.)

### 2.3 Collocation and grammar (commit `ed87722`)

| # | File | before → after | Why |
|---|---|---|---|
| 1 | `one-4k/index.mdx`, `one-4k-oled/index.mdx` | `…l'alimentazione **su un solo cavo** USB-C **con i** dispositivi compatibili.` → `…l'alimentazione **tramite un solo cavo** USB-C **sui** dispositivi compatibili.` | Italian carries a signal *tramite/con* a cable, never *su*; EN `over a single cable … on compatible devices` is fine. Twin pages kept identical. |
| 2 | `lite-144hz/index.mdx` | `con **una** frequenza di aggiornamento **rapida** di 144 Hz` → `con **un'elevata** frequenza di aggiornamento di 144 Hz` | A frequency is *elevata*; *rapido* belongs to response time. EN `a fast … refresh rate` is standard English. |
| 3 | `flip/installation.mdx` | `quali porte sono **coinvolte**` → `quali porte sono **interessate**` | *Coinvolto* belongs to people and processes; *interessato* is the standard Italian for "affected/involved" in technical prose — and the corpus already uses `lo schermo interessato`. |
| 4 | `expand/index.mdx` | `si aggancia al tuo laptop e **apre** due display Full HD` → `…e **dispiega** due display Full HD` | A monitor does not "open" displays in Italian; *dispiegare* carries EN `unfolds` without drifting to "adds". |
| 5 | `expand/installation.mdx` | `Se lo schermo del tuo laptop **è spesso meno di** 6 mm` → `…**ha uno spessore inferiore a** 6 mm` | Garden path: *spesso* is read first as "often". EN `less than 6 mm thick` has no such collision. |
| 6 | `dual-flip/index.mdx` | `si apre **in** due schermi aggiuntivi da 16"` → `si apre **a formare** due schermi aggiuntivi da 16"` | *Aprirsi in* = to crack/split open — the wrong image for a product you are told not to press on. EN `unfolds into`. |
| 7 | `dual-flip/controls.mdx` ×2 | `…e **naviga / aumenta i valori** all'interno del menu OSD.` → `…**e, all'interno del menu OSD, naviga e aumenta i valori.**` | *Navigare* is intransitive and cannot take `i valori`; the bare slash between two conjugated verbs is not Italian punctuation. Both verbs, both scopes and the sentence order are preserved. Mirror edit on the `−` button. |
| 8 | `infinity/controls.mdx` | `La disposizione è speculare **sullo** schermo sinistro **e su** quello destro.` → `…speculare **tra lo** schermo sinistro **e** quello destro.` | Mirroring is a relation *between* two things; *speculare su X e su Y* is not an Italian collocation. |
| 9 | `infinity-lite/controls.mdx` ×2 | `**Sposta** verso sinistra – regola la retroilluminazione…` → `**Premi** verso sinistra – …` | *Sposta* is a transitive imperative with no object ("move what?"). *Premi verso* matches the glossary-locked `Premi a destra / a sinistra` on the sibling `infinity/controls.mdx`. |
| 10 | `onecable/installation-mac.mdx` | `Scarica il driver **dal** pulsante qui sopra.` → `…**tramite il** pulsante qui sopra.` | In Italian you download *from a source*, not *from a button*; EN says `via the button`. |
| 11 | `onecable/troubleshooting.mdx` | `**L'alimentazione** è compatibile con PD.` → `**L'alimentatore** è compatibile con PD.` | The condition sits in a list of checkable properties (`la porta … supporta PD`, `il collegamento … con un cavo USB-C`); PD compatibility is a property of the physical unit, and EN `The power supply is PD-compatible` means the device. See §3 for the glossary note this required. |
| 12 | `panorama/index.mdx` | `**Il driver dello schermo necessario consente di** gestire tre schermi indipendenti con un solo cavo.` → `**Per** gestire tre schermi indipendenti con un solo cavo **è necessario un apposito driver dello schermo.**` | Calqued postposed adjective reading as a spec-sheet fragment, and it presented a requirement as a feature. Requirement and cable-count both preserved; no forward reference invented. |
| 13 | `panorama/installation.mdx` | `**Attenzione:** **bada** alle dita quando pieghi gli schermi…` → `**Attenzione:** **presta attenzione** alle dita…` | *Badare a* means "to look after"; no Italian technical writer uses it in a pinch-point warning. `panorama/safety.mdx` (frozen) already has `Fai attenzione alle dita`; `presta attenzione` matches it without echoing the `Attenzione:` lead-in. |
| 14 | `panorama/installation.mdx` | `non fornisce **abbastanza alimentazione**` → `non fornisce **potenza sufficiente**` | *Alimentazione* is not quantifiable in Italian. Glossary §5.2 already maps `power (output capability)` → `potenza`, and `onecable/troubleshooting.mdx` uses it correctly. |
| 15 | `panorama/osd.mdx` | `quindi **potresti voler modificare** la disposizione del desktop` → `quindi **può essere utile modificare** la disposizione del desktop` | Textbook calque of `you may want to`; Italian uses an impersonal usefulness construction. |

### 2.4 Glossary changes

| § | Change |
|---|---|
| §6 (line 669) | `Need more overview?` — new correct target `Vuoi una visione d'insieme migliore?`; the old `Vuoi più spazio a schermo?` moved to the ✗ column with the meaning-inversion reason. **Binding-string correction.** |
| §9.10 | Three-way prompt collapse split into two rows (see §2.1); intro paragraph amended so a future pass collapses only EN variants that genuinely say the same thing. |
| §9.10 bodies | New locked row: `…to see which screen has which number.` → `…per vedere quale numero corrisponde a ciascuno schermo.` |
| §9.9 boilerplate | New locked row for the 11-page index sentence. |
| §9.9 bold run-ins | New locked row: `Toggle right/left –` → `Premi verso destra/sinistra –`. |
| §5.2 `power supply` | Context exception added: render `alimentatore` where EN `power supply` denotes the physical unit rather than the supply of power. Narrow, with the one page it applies to named. |

---

## 3. Rejected — one line each

Reviewer preferences that contradict a locked convention, a DNT token, or the source.

1. `ingresso DC` → `tensione di alimentazione DC` (fluency-b MAJOR-14) — glossary §5.2 locks
   `DC input` → `ingresso DC` with `DC` kept verbatim; 4 of the 5 sites are frozen safety bodies.
2. `spina USB-A` → `connettore` (fluency-a) — glossary §5.1 locks `plug` → `spina`, with the exact
   phrase `la spina USB-A nera`.
3. `("Min")` / `("Plus")` → `(−)` / `(+)` (fluency-b MAJOR-17) — EN source strings, glossary-locked
   at §9.9.
4. `Abbi cura del tuo Screenmate` → `Maneggia con cura` (fluency-b MINOR-12) — glossary §6 locks
   `Take good care of your Screenmate` → `Abbi cura del tuo Screenmate`.
5. `Quando entrambi i collegamenti sono stati effettuati` → participial shortcut (MINOR-09) —
   glossary §6 locks this exact rendering.
6. `Formato (ASPECT)` → `Rapporto d'aspetto (ASPECT)` (fluency-a) — glossary §7.3 locks
   `Aspect (ASPECT)` → `Formato (ASPECT)`, and EN itself writes `Aspect` on Expand and
   `Aspect Ratio` on Flip. Harmonising Italian would flatten a distinction the source makes.
7. `spia della scheda madre` → `spia di stato del monitor` (fluency-a) — glossary §5.1 locks
   `motherboard indicator light`; changing it would invent a product fact.
8. `Precisione cromatica` → `Gamma cromatica` corpus-wide — both are glossary-locked §5.4 targets of
   two different EN labels; see `source-flags-it.md` §2.1.
9. Windows/macOS UI-citation convention rewrite on `display-settings.mdx` (fluency-a, 2 Majors) —
   every label is glossary-locked §8 and the Italian mirrors the English page's own two conventions.
10. `'Capovolto'` → `'Landscape (flipped)' ('Orizzontale capovolto)'` — glossary §8 locks
    `Flipped` → `Capovolto`; presentation ruling already adjudicated.
11. `«caporali»` or single-treatment UI quoting — glossary §10 mandates straight ASCII quotes for
    structural parity with EN/NL.
12. `1.000:1`, `1.820 g`, `100 %` (fluency-a) — glossary §4.1/§4.3; reviewer B independently
    verified the current formatting as correct.
13. `1920 × 1080` / `1920×1080` unification — mirrors the EN tables row for row.
14. Ventilation-opening polarity restatement — pre-adjudicated; glossary §6. **[frozen body]**
15. `### Attenzione durante la chiusura` → `Attenzione in apertura e chiusura` — pre-adjudicated;
    glossary §9, closer to the Dutch source than the EN heading is. **[frozen body]**
16. `Modalità generale` → `nell'uso normale` (fluency-b MAJOR-02) — `**General mode**` is a device
    mode label in `lite/controls.mdx`; EN `in general mode` on one-4k is the same concept, and the
    Italian is consistent across both products.
17. `menu delle scorciatoie` → `menu rapido` (MAJOR-02) — EN says `shortcut menu` on one-4k and
    `quick menu` on panorama; the Italian tracks each.
18. `aumenta` / `riduci` voice mismatch in `infinity/controls.mdx` (CRITICAL-02, second half) —
    misreading: `aumenta` is the `tu` imperative of *aumentare*, identical in form to the third
    person. Both bullets are imperative, like their neighbours.
19. `gesti` → `comandi` (MINOR-16) — EN says `gesture reference`; the button is documented as
    rotatable, so *gesti* is not wrong.
20. `pulsante girevole` → `pulsante multidirezionale` (MAJOR-19) — EN says `a rotatable button`;
    changing it in Italian only would contradict the English page.
21. `pagina precedente` → `menu precedente` (fluency-a, MINOR-13) — EN says `previous page` on
    flip/expand/dual-flip and `previous menu` on one-4k; the Italian tracks each.
22. Frontmatter description rewrites (`panorama/osd`, `one-4k/osd`, `flip/display-settings`,
    `dual-flip/display-settings`) — all four are glossary-locked §9.2 renderings of four *different*
    English descriptions.
23. Wrapping bare `Nota:` paragraphs in `<Note>` callouts — structural parity with EN forbids it.
24. `Disponi tutti e tre gli schermi nella vista Identifica` → "*Identifica* is a button, not a
    view" — EN says `in the **Identify** view`.

---

## 4. Source-flagged

38 findings written up in **`translations/qa/round4/source-flags-it.md`**, grouped as:

- **§1 Reader-blocking contradictions carried by the source** (9) — including all four Criticals
  from `fluency-it-b.md` and the Critical from `fluency-it-a.md`: the 5–20 V vs. 5 V safety
  contradiction, the Infinity Lite port map, the Infinity brightness/volume map, and the
  `Duplicato` orientation value (EN says `'Mirrored'`, which glossary §8 already records as
  superseded — the EN page is stale).
- **§2 Terminology drift that originates in English** (7) — `Color Gamut`/`Color Accuracy`,
  `≡`/`M`, duplicated `USB-C Port` bullets, the mount-hardware vocabulary (English uses
  `protective clips` where Dutch says `beschermkap`), menu/button naming splits, speaker count,
  `professional`/`business`.
- **§3 Prompts and sentences whose oddness is in the source** (17).
- **§4 Not defects** (5) — recorded so a future reviewer does not "correct" them back.

---

## 5. Deferred

### 5.1 Frozen safety bodies — for the native reviewer

`safety.mdx` passed four rounds of meaning verification and is frozen for this pass. These are
worthwhile **style** suggestions only; none changes meaning, and none should be applied without a
fresh alignment check.

| File(s) | Suggestion |
|---|---|
| all 5 safety bodies | `Assicurati che la presa di corrente sia **correttamente** dotata di messa a terra e adatta all'**amperaggio corretto**.` — *correttamente … corretto* in nine words. `correttamente` is load-bearing per glossary §5.2 and verified intact in round 3 (`safety-align-it.md` §R1), so only the second half could move: `adeguata all'amperaggio richiesto`. |
| all 5 | `Evita l'esposizione a umidità, polvere ed elettricità statica **per evitare** danni…` — *Evita … evitare* echo → `per prevenire danni`. |
| onecable family, infinity, infinity-lite, panorama | `Usa esclusivamente l'alimentatore AC/DC in dotazione **come alimentazione**.` — the apposition is redundant after *alimentatore*. EN says `as power supply`, so any change is a shared EN/IT decision. |
| onecable family | `Leggi attentamente le indicazioni seguenti… **Garantiscono** un funzionamento sicuro…` — the instructions do not guarantee anything; following them does. |
| infinity, panorama | `garantisci una circolazione dell'aria sufficiente` → `assicura una ventilazione sufficiente`; `apparecchiature trasmittenti` → `apparecchi che emettono segnali radio`. |
| infinity, infinity-lite, panorama | `### Controlla prima dell'uso` / `### Leggi prima dell'uso` / `### Prima dell'uso` — three headings for one section across sibling products. All three are glossary-locked §9 renderings of three different EN headings, so this is an EN-side harmonisation. |

Content issue, not language: `Usa esclusivamente l'alimentatore AC/DC in dotazione` is served
verbatim under products whose `Contenuto della confezione` lists no AC/DC adapter (OneCable, Flip,
Expand). Raised by `fluency-it-a.md`; needs per-product gating on the EN side.

### 5.2 Taste, where a rewrite would risk drift

| File | Item | Why deferred |
|---|---|---|
| `flip/index.mdx` | `si aggancia intorno al tuo laptop … per una visione d'insieme più ampia e una maggiore concentrazione` | Faithful to EN `clips around your laptop to give you two extra displays for more overview and focus`. The proposed rewrite (`più spazio di lavoro sott'occhio`) would reintroduce exactly the space/overview inversion fixed in §2.1. |
| `infinity/installation.mdx` ×3 | `collega un'alimentazione esterna` | Glossary §5.2 maps `external power supply` → `alimentazione esterna`, and the collocation is attested in Italian technical prose. Worth a glossary-owner ruling alongside §2.3 item 11 rather than a unilateral change. |
| `infinity/installation.mdx` | `collega **anche qui** un'alimentazione esterna` | EN `connect an external power supply here as well`; *anche qui* is understandable and faithful. |
| `infinity/index.mdx` | `ti dà due schermi in più **contemporaneamente**` | EN `to give you two extra screens at once` dangles the same way. |
| `infinity-lite/installation.mdx` | `Apri il telaio **con uno scatto** per estrarlo.` | EN `Click open the frame to extend it.` is itself odd; the Italian is comprehensible and any rewrite guesses at the mechanism. |
| `dual-flip/index.mdx` and 3 others | `Per un funzionamento a basso consumo…` | Idiomatic Italian rendering of an idiomatic English phrase; the self-defeat is the source's (`source-flags-it.md` §3.5). |
| `panorama/installation.mdx` | `Collegare un caricabatterie separato … può causare interferenze.` | Infinitive **subject** in a declarative, not an impersonal instruction — glossary §1 bans the latter, not the former. |
| `panorama/installation.mdx` | `## Installa il driver dello schermo` is the only imperative H2 among noun-phrase H2s | Mirrors the EN heading set exactly; §9 heading targets are locked. |
| `infinity-lite/installation.mdx` | Two plain assembly steps wrapped in `<Warning>` | Component choice is structural parity with EN. |
| various | ~40 below-cap polish items (filler adverbs, alt-text drift, `fasi`/`passaggi` wobble, `-20 °C` hyphen) | Not itemised by the reviewers; below the value threshold for a hand pass and mostly EN-parity anyway. |
| `manuals-index.mdx` | Card titles `Manuale OneCable` vs page titles `Manuale Screenmate OneCable` | Glossary §9.8 locks card titles; mirrors the EN index. |
| `it/manuals-index.mdx` | `avrebbe dovuto portarti` in the QR tip | Below the reviewer's own Minor cap; EN uses the same past conditional. |

---

## 6. Verification

Run after the last edit, before the log commit.

```
$ python scripts/verify_translation.py --base en --targets it --include-nl

0 FAIL, 0 WARN
```

No new warn classes (the baseline was also 0/0).

```
$ python -m pytest tests/test_verify_translation.py -q
....................                                                     [100%]
20 passed in 0.35s
```

**display-settings 4-product body identity** (frontmatter stripped, `awk 'BEGIN{c=0} /^---$/{c++;
next} c>=2{print}' FILE | md5sum`) — four identical hashes after propagation:

```
onecable   9a7b67c0a2662cc94be8774d99299a9a
expand     9a7b67c0a2662cc94be8774d99299a9a
flip       9a7b67c0a2662cc94be8774d99299a9a
dual-flip  9a7b67c0a2662cc94be8774d99299a9a
```

`infinity` and `infinity-lite` display-settings have their own bodies, as expected, and were edited
independently.

**Twin-product parity** — `lite` / `lite-144hz` and `one-4k` / `one-4k-oled` received identical
edits where their English pages are identical apart from product name and specs
(`one-4k`/`one-4k-oled` index sentence; the `lite` pair needed no edit beyond the shared index
boilerplate).

**Frozen safety bodies:**

```
$ git diff --stat -- 'it/**/safety.mdx'
(no output)
```

**Scope discipline:** both commits used explicit pathspecs (`it/`,
`translations/glossary-it.md`, `translations/qa/round4/`). No `git add -A`, no `--amend`, and no
file under `de/`, `fr/`, `nl/` or `en/` was modified — the concurrent DE and FR working-tree
changes were left untouched.
