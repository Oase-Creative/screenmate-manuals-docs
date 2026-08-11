# Adversarial IT review — family F2 (Lite / Lite 144 Hz / Panorama)

**Branch:** `lang-expansion-de-fr-it` · **Date:** 2026-08-11 · **Reviewer:** adversarial pass, EN + NL + IT side by side
**Scope:** `it/manuals/lite/` (5), `it/manuals/lite-144hz/` (5), `it/manuals/panorama/` (5), `it/manuals-index.mdx` (1) = 16 pages
**Authority:** `translations/glossary-it.md` (all sections), `translations/dnt.json`

**Verdict:** no High/Critical defects. No register violations, no glossary term violations, no number/unit errors,
no safety-negation weakening, no untranslated strings. The defects that exist are **cross-product consistency
failures**: `lite` and `lite-144hz` have byte-identical EN sources but ship 10+ divergent Italian sentences, and the
`Welcome!` banner has four different Italian shapes for one English sentence. Findings 01–05 all trace to that
single root cause — the two Lite pages were translated independently instead of as one checksum-locked pair.

Pre-ruled non-defects were verified as instructed and are **not** counted: OSD presets `User` / `Warm` / `Cool` kept EN
(§7.2), `Pulsante di accensione e ritorno` (R8), the panorama `<Info>` cable block (client-dictated verbatim),
`Capovolto` for *Flipped* (locked), `RTS` / `FPS` kept EN.

---

## Findings

| # | Sev | File(s) : line | EN source | IT as shipped | Defect | Rule |
|---|---|---|---|---|---|---|
| F2-01 | Medium | `it/manuals/lite/index.mdx:8`<br>`it/manuals/lite-144hz/index.mdx:8`<br>`it/manuals/panorama/index.mdx:8` | `This is your complete digital manual for the Screenmate X.` (identical on all 11 EN index pages) | lite: `Questo è **il tuo manuale digitale completo per lo** Screenmate Lite.`<br>144hz: `Questo è **il manuale digitale completo del tuo** Screenmate Lite 144 Hz.`<br>panorama: `Questo è **il manuale digitale completo dello** Screenmate Panorama 15,6".` | Three different renderings of one EN sentence inside a single family. `lite-144hz` moves the possessive off the manual and onto the product — the **only** page in the whole 11-page IT corpus with that structure. `panorama` drops EN "your" entirely. Corpus-wide there are 4 shapes for 1 EN sentence. | §1.3 (possessive policy must be applied consistently, not per-page); §9.10 principle (recurring boilerplate = one target) |
| F2-02 | Medium | `it/manuals/lite-144hz/index.mdx:8` | `Use the navigation menu on the left to jump to each section.` | `…per passare **a ogni sezione**.` | **Calque.** `passare a ogni sezione` reads as "move on to every section (in turn)" — it describes visiting all of them, not navigating to whichever one you want. `lite` and `panorama` both correctly have `per passare **da una sezione all'altra**`; `lite-144hz` is the outlier *within its own family*. | §6 (literal-translation traps); §9.10 |
| F2-03 | Medium | `it/manuals/lite-144hz/installation.mdx:35, 57` | `…with video support **—** not every USB-C port…`<br>`…an HDMI device **—** such as a PC… **—** follow these steps` (U+2014, both) | `…con supporto video **–** non tutte…`<br>`…un dispositivo HDMI **–** come un PC… **–** segui…` (U+2013) | Em dash silently downgraded to en dash. The EN source is **byte-identical** to `lite/installation.mdx:35, 57`, and `it/manuals/lite/installation.mdx` correctly preserves U+2014 in both slots. Two sibling pages, same EN, different dash. Verified by full U+2014/U+2013 sweep of F2 (see Evidence E4). | §10 ("structural punctuation is preserved"); cross-product parity |
| F2-04 | Medium | `it/manuals/lite/osd.mdx` vs `it/manuals/lite-144hz/osd.mdx` : 17, 18, 32, 47, 49 | EN `lite/osd.mdx` and `lite-144hz/osd.mdx` are **byte-identical** for these five bullets | `:17` `più dettaglio` / `più dettagli`<br>`:18` `il dettaglio dell'immagine` / `i dettagli dell'immagine`<br>`:32` `**alterna** il rapporto d'aspetto tra **panoramico**` / `**cambia** il rapporto d'aspetto tra **formato panoramico**`<br>`:47` `scegli tra **12 lingue** disponibili` / `scegli tra **le 12 lingue** disponibili`<br>`:49` `per una **visione** migliore` / `per una **visualizzazione** migliore` | Five independent divergences on one checksum-identical page. `:32` also breaks the §7.3 gloss precedent — `alterna` is the glossary's own verb for ASPECT (`alterna tra 4:3 e WIDE`); `cambia` is an unforced synonym. | §9.10 principle; §7.3 (`alterna`) |
| F2-05 | Medium | `it/manuals/lite/installation.mdx` vs `it/manuals/lite-144hz/installation.mdx` : 9, 21, 35, 37, 41 | EN sources **byte-identical** | `:9` `ai cavi **che hai a disposizione**` / `ai cavi **disponibili**`<br>`:21` `**Serve** alimentazione aggiuntiva? **Usa il cavo**` / `**Ti serve** alimentazione aggiuntiva? **Usa allora il cavo**`<br>`:35` `collegare **il tuo telefono o tablet**` / `collegare **il telefono o il tablet**`<br>`:37, :41` alt `Collegamento USB-C **al telefono o al** tablet` / `Collegamento USB-C **a telefono o** tablet` | Four more divergences on a second checksum-identical page, including two `alt` strings. `:35` is also an internal contradiction: the same IT sentence then says `il **tuo** telefono o tablet deve avere una porta USB-C` — the possessive is dropped in the first clause and kept in the second. | §1.3; §9.10 principle; §10 (`alt` is user-visible) |
| F2-06 | Low | `it/manuals/lite-144hz/installation.mdx:21` | `Then use the USB-C to USB-A cable in combination with a power adapter:` | `**Usa allora** il cavo da USB-C a USB-A insieme a un alimentatore:` | Word-order calque of NL `Gebruik **dan** de…`. Italian does not place `allora` post-verbally in an imperative; natural is `Allora usa il cavo…`, or simply `Usa il cavo…` as `lite` already does. Suggests this page was rendered from the NL rather than the EN. | §6; §1.2 |
| F2-07 | Low | `it/manuals/lite/controls.mdx:33` vs `it/manuals/lite-144hz/controls.mdx:33` | `Rotate: navigate through menus and adjust settings` (identical) | `naviga **tra** i menu` / `naviga **nei** menu` | Same EN, two prepositions. (The neighbouring `Modalità OSD` vs `Modalità menu OSD` split at `:31`/`:41` is **correct** — EN itself says `OSD mode` vs `OSD menu mode`. Checked and cleared.) | Cross-product parity |
| F2-08 | Low | `it/manuals/panorama/index.mdx:15` | `A required display driver allows three independent screens to be driven through one cable.` | `Per gestire tre schermi indipendenti tramite un solo cavo **è necessario installare** il driver dello schermo.` | Meaning drift: a statement about what the driver *enables* is recast as an *installation instruction*. EN never says "install" here — the install step lives on `installation.mdx`. NL keeps the EN framing (`maakt het mogelijk om…`). Suggest `Un driver dello schermo, necessario, consente di gestire tre schermi indipendenti con un solo cavo.` | Meaning fidelity |
| F2-09 | Low | `it/manuals/panorama/controls.mdx:28` | `Opens the OSD menu (On-Screen Display) for the **currently** selected screen.` | `apre il menu OSD (On-Screen Display) dello schermo selezionato.` | `currently` dropped. The nuance is load-bearing here: `osd.mdx:14` explains that repeated short presses **cycle** which screen is selected, so "currently" is what tells the reader the target changes. Suggest `dello schermo attualmente selezionato`. | Meaning fidelity |
| F2-10 | Low | `it/manuals/panorama/installation.mdx:28` vs `it/manuals/panorama/safety.mdx:26` | `Watch your fingers when folding the screens to avoid pinching.` / `…when folding the screens in or out to avoid pinching.` | installation: `**Attenzione:** quando pieghi gli schermi, **fai attenzione** alle dita per evitare di **schiacciartele**.`<br>safety: `Fai attenzione alle dita quando richiudi o apri gli schermi, per evitare di **schiacciarle**.` | (a) `Attenzione: … fai attenzione` repeats the word twice in ten words — EN has no such echo; drop the second (`fai attenzione alle dita` → `bada alle dita`) or reorder. (b) `schiacciartele` vs `schiacciarle` for the same warning on the same product. EN differs only by `in or out`, so the verb form should still match. | §10 (no added redundancy); intra-product parity |
| F2-11 | Low | `it/manuals/panorama/safety.mdx:14` vs `it/manuals/lite/safety.mdx:12` + `lite-144hz/safety.mdx:12` | `**Only** use an AC/DC adapter as power supply.` / `**Only** use the included AC/DC adapter as power supply.` | panorama: `Usa **solo** un alimentatore AC/DC…`<br>lite / 144hz: `Usa **esclusivamente** l'alimentatore AC/DC in dotazione…` | The restrictive operator in *safety* copy renders two ways for the same EN `Only`. Not a negation weakening (both are exclusive), but safety register should be uniform across the corpus; `esclusivamente` is the stronger and is used 2:1. | §1.4 (safety copy); cross-product parity |
| F2-12 | Medium | all 16 F2 files (frontmatter) — and all 62 `it/` pages | EN pages carry `nl_link:`; NL pages carry `en_link:` | *(absent)* | **Structural, not linguistic.** No `it/` page carries `nl_link` / `en_link` / `it_link` (0 of 62). Per the language-switcher architecture (ab10152) these are required on every page or the switcher cannot resolve the sibling page. Confirmed this is the *sole* structural delta vs EN: every IT file is exactly 1 line shorter than its EN counterpart, headings/`<img>`/list counts all match (Evidence E1). `de/` and `fr/` are also at 0, so this is a branch-wide pending step rather than an IT-F2 regression — flagged so it is not lost. | MEMORY: language-switcher architecture |
| F2-13 | Info | `it/manuals/panorama/osd.mdx:45` | `…150% for larger text and **UI** elements.` | `…su 150% per testo ed elementi più grandi.` | `UI` is dropped. The page is **compliant** — §9.10's locked target drops it too, and this is the corpus's only `UI elements` instance. Raised against the **glossary**, not the page: consider `elementi dell'interfaccia` in the lock. | §9.10 (glossary-side) |
| F2-14 | Info | `it/manuals/panorama/osd.mdx:3` | `Per-screen display settings via the on-screen menu` | `Impostazioni schermo per singolo schermo dal menu a schermo` | Three `schermo` in eight words. Page is **compliant** — string is locked verbatim in §9.2. Raised against the glossary: `Impostazioni per singolo schermo dal menu a schermo` reads cleanly and loses nothing. | §9.2 (glossary-side) |

**Totals — Medium 6 · Low 6 · Info 2 · High/Critical 0.**

---

## Scrutiny evidence

Every category in the brief was actively probed. The checks below **passed**; they are recorded so the empty
result is auditable rather than assumed.

### E1 — Structural parity, EN ↔ IT, all 15 product pages
Compared heading ladder (`^#+` sequence), `<img>` count, and list-item count per file pair.
All 15 pairs: **heading ladder identical, image count identical, list count identical.** Line-count delta is
exactly `-1` on every single file — accounted for entirely by the missing `nl_link` frontmatter line (F2-12).
No dropped paragraph, no dropped bullet, no dropped image anywhere in F2.

### E2 — Register (§1.5), full defect grep
Ran the §1.5 courtesy-form regex and the 26-verb formal-imperative regex over all 16 F2 files.

- Courtesy pronouns/phrases (`Lei|Suo|Sua|Suoi|Sue|Vostr*|La preghiamo|Le consigliamo|Si prega di|Per favore|voglia`): **0 hits.**
- `può` / `deve`: 4 hits, **all whitelisted** — subject is a thing, not the reader:
  `lite/installation.mdx:16` + `lite-144hz/installation.mdx:16` `il monitor **deve** essere alimentato`;
  `lite/installation.mdx:35` + `lite-144hz/installation.mdx:35` `il telefono o tablet **deve** avere una porta USB-C`.
  (`panorama/installation.mdx:62` `**può** causare interferenze` — subject is `Collegare un caricabatterie`, a thing. Correct.)
- Formal-imperative verbs: 4 hits, **all false positives** — `usi` in `come **usi** il monitor` (2nd-sg indicative,
  `lite/osd.mdx:24`, `lite-144hz/osd.mdx:24`), `pieghi` in `quando **pieghi** gli schermi`
  (`panorama/installation.mdx:28`), `usi` in `quando non lo **usi**` (`panorama/safety.mdx:22`).
- Negative imperatives all use `non` + infinitive per §1.2: `Non usare`, `Non toccare`, `Non far cadere`,
  `Non ostruire`, `Non usare oggetti appuntiti`. **0 violations.**
- Irregular `tu` imperatives correct throughout: `Vai su`, `Fai clic su`, `Assicurati`, `Scegli`, `Rimuovi`,
  `Spegni`, `Estrai`, `Appoggia`, `Abbi` — no `Vada`/`Faccia`/`Prema` anywhere.

**Verdict: register clean.**

### E3 — Numbers, units, measurement (§4)
- `\d,\d\d\d` (English comma-thousands surviving into IT — the §4.2 "1000× error"): **0 hits.**
- `\d\.\d` (English decimal period surviving into IT): **0 hits.**
- Decimal commas correctly applied everywhere they belong: `15,6"` (×6), `35,4 × 22,1 × 1,1 cm` (×2),
  `42 × 36 × 2,8 cm`, `3,5 mm` (×2), `1,2 m`, `0,5 m`.
- Thousands correctly **un**separated: `1920×1080`, `1000:1`, `609 grammi`, `3000 grammi`.
- SI spacing per §4.1/§11.1-5: `5 V`, `20 V`, `±2 V`, `10 ms`, `60 Hz`, `144 Hz`, `65 W`, `300 cd/m²`,
  `350 cd/m²`, `609 grammi`. Closed-up per rule: `99%`, `100%`, `150%`, `172°`, `360°`.
  Temperature spaced per rule: `-20 °C`, `60 °C` (EN has `-20°C`; the IT space is the deliberate §11.1-5 divergence). **All correct.**
- §4.3 protected strings intact: `144 Hz` in the product name, `1000:1`, `16:9`, `4:3`, `PlayStation 4/5`, `USB 2.0`.
- `(×3)` in the panorama size row preserved from EN. Quantity prefixes converted per §4.1:
  EN `1x USB-C to USB-C cable` → `1 cavo da USB-C a USB-C` (the `x` is dropped, correct).

**Verdict: numbers clean.**

### E4 — Dash inventory (full U+2014 / U+2013 sweep of F2 IT)
- U+2014 (em): 4 occurrences — `lite/installation.mdx:35, 57`; `panorama/installation.mdx:46, 67` (the two
  `### Opzione N — …` headings, correctly preserved per §9.5).
- U+2013 (en): 20 occurrences — 18 are OSD numeric ranges (`0–100`, `0–4`, `10–60 secondi`), correct per §4.1;
  the remaining 2 are the F2-03 defect.

### E5 — Compounds, cable chain, connectors (§2)
- `cavo da X a Y` chain: 22 instances across F2, **all conform**. Zero hits for any §2.5 rejected variant
  (`cavo USB-C a USB-C`, `cavo USB-C-USB-C`, `cavo USB-C/USB-C`, `verso`, `su`, `dall'USB-C all'USB-C`).
- `ad` before a connector acronym (§2.5 locked off): **0 hits** for `ad USB`/`ad HDMI`/`ad Mini`.
- `Mini HDMI` unhyphenated (§2.2 requires `Mini-HDMI` in IT even where EN writes `Mini HDMI`): **0 hits** —
  every one of the 7 instances is `Mini-HDMI`, including in the `### 3 × porte Mini-HDMI` heading where EN
  writes `3 × Mini HDMI Ports`. Correctly *not* mirroring the EN inconsistency.
- Head-initial order throughout: `porta USB-C`, `cavo HDMI`, `menu OSD`, `Timer OSD`, `monitor DP`,
  `alimentatore da 65 W`, `jack per cuffie da 3,5 mm`. No Dutch/German hyphen chains. **0 violations.**
- §2.6 bare acronyms never articled: no `l'USB-C`, `la USB-C`, `il HDMI`. **0 hits.**

### E6 — Gender, articles, elision (§3)
- `lo Screenmate` / `dello Screenmate` / `allo Screenmate` / `sullo Screenmate` used correctly (18 instances);
  `il Screenmate` / `del Screenmate`: **0 hits.**
- §3.1 next-word sub-rule honoured: `lo Screenmate` but `il tuo laptop`, `gli schermi` but `i piedini`,
  `lo schermo` but `il monitor`.
- `la porta` (f.) throughout, never `il porta`. `i driver` never `i drivers`. `menu` never `menù`.
- Elision without space: `dell'immagine`, `l'alimentazione`, `all'angolo`, `dell'aria`, `un'immagine` — correct.
  `un alimentatore` (m., no apostrophe) correct.
- Typographic apostrophe U+2019: **0 hits** — straight ASCII throughout per §3.3.
- Accented vowels are real characters (`è`, `più`, `può`, `luminosità`, `nitidezza`); no `e'`/`perche'` hacks.

### E7 — Safety-negation integrity
Every negation and restriction in the three `safety.mdx` files plus the four `<Note>`/`<Warning>` blocks was
read against EN. **No weakening, no polarity inversion, no dropped restriction.** Spot list:

| EN | IT | |
|---|---|---|
| `Keep ventilation openings clear` | `**Non ostruire** le aperture di ventilazione` | correct per §6 (the literal `Tieni … chiare` trap avoided) |
| `Do not drop the monitor` | `**Non far cadere** il monitor` | correct per §1.2 (not `Non lasciare cadere giù`) |
| `Do not use liquids or aggressive cleaning agents` | `**Non usare** liquidi o detergenti aggressivi` | intact |
| `Do not touch the device with wet hands and do not use it in humid environments` | `**Non** toccare … e **non** usarlo in ambienti umidi` | both negations preserved |
| `Do not use sharp objects on or around the screen` | `**Non usare** oggetti appuntiti sullo schermo o attorno a esso` | intact |
| `A laptop's USB-C port does **not** supply enough power on its own … **Always** connect the 65 W adapter` | `La porta USB-C di un laptop **da sola non** fornisce abbastanza alimentazione … **Collega sempre** l'alimentatore da 65 W` | negation + "always" both intact |
| `If the connected device doesn't supply enough power, the monitor **needs to be** powered separately` | `se il dispositivo collegato **non** fornisce alimentazione sufficiente, il monitor **deve essere** alimentato separatamente` | obligation preserved, not softened to `può` |
| `**not** every USB-C port can output video` | `**non** tutte le porte USB-C possono trasmettere il video` | intact |
| `Connecting a separate charger … **may** cause interference` | `Collegare un caricabatterie separato … **può** causare interferenze` | hedge preserved, not upgraded or dropped |
| `Only use the device with a 5V power source` | `Usa il dispositivo **esclusivamente** con una fonte di alimentazione da 5 V` | restriction intact |

Numbered safety list is 14 items in EN and 14 in IT on both Lite pages; panorama's bulleted list is 10 in EN and
10 in IT. `lite/safety.mdx` and `lite-144hz/safety.mdx` are **byte-identical in IT** — correct, since their EN
sources are byte-identical. (This is the counter-example that makes F2-04 and F2-05 defects rather than noise:
the same pipeline *did* produce parity where it mattered on `safety.mdx`, and failed to on `osd.mdx`/`installation.mdx`.)

### E8 — Run-in colon casing (§7.3 policy; `it/lite` set the precedent)
Enumerated **all 56 bold run-in colons** and **9 bullet run-in colons** across F2 and inspected the first character
after each `:**`.

- Bold run-ins: 25 in `lite`, 25 in `lite-144hz`, 6 in `panorama`. **56/56 lowercase.** Includes the OSD glosses
  (`**Luminosità (0–100):** regola…`), the preset values (`**Standard:** modalità…`, `**Movie:** ideale…`), the
  callout lead-ins (`**Importante:** se…`, `**Attenzione:** quando…`), the installation run-ins
  (`**Alimentazione:** collega…`, `**Collegamento della console:** usa…`), the panorama control run-ins
  (`**Pressione prolungata (1 secondo):** spegne…`), and the panorama display-settings run-in
  (`**Estendi lo spazio di lavoro:** apri…`).
- Bullet run-ins in `lite`/`lite-144hz` `controls.mdx` (`- Pressione breve: accende…`, `- Rotazione: naviga…`):
  **8/8 lowercase**, matching. `panorama/safety.mdx:21` `- Temperatura ambiente consigliata: tra…` lowercase.
- Capitals after a bold prompt occur only where the prompt ends in `?` and a new sentence begins
  (`**Schermo capovolto?** Seleziona…`, `**Vuoi più spazio a schermo?** Fai clic…`) — correct, not an exception.

**Verdict: `lite-144hz` and `panorama` match the `lite` precedent exactly. No defect.**

### E9 — Alt-text completeness (R9)
All **40** `alt` attributes in F2 enumerated. **40/40 present, 40/40 Italian, 0 English, 0 Dutch, 0 empty,
0 copy-pasted-from-EN.** Alts are genuinely re-authored against page context rather than mechanically mirrored
(e.g. `panorama/installation.mdx:13` `Appoggia lo Screenmate chiuso sulla scrivania`;
`panorama/osd.mdx:58` `Immagine 2: finestra Disponi schermi di macOS con gli schermi nell'ordine corretto`).
Two alt strings drift between `lite` and `lite-144hz` — counted under F2-05, not here.
`src` / `className` / `href` / `icon` correctly left untouched; the URL-encoded `…Handleiding images/` paths are
intact on all 40 (breaking one would 404 the image).

### E10 — §9 heading and frontmatter lock check
Every `title`, `description`, `##` and `###` in F2 checked against §9.1/§9.2/§9.3/§9.4/§9.5/§9.6. **All conform.** Sampled:

`Manuale Screenmate Lite 144 Hz` · `Manuale d'uso completo del tuo monitor portatile a tre schermi Screenmate
Panorama 15,6"` (decimal comma **and** frontmatter-escaped `\"`, both correct) · `Impostazioni schermo per singolo
schermo dal menu a schermo` · `Porte e pulsanti` · `Panoramica delle porte e dei pulsanti di comando` ·
`Che cos'è lo Screenmate Panorama?` · `Contenuto della confezione` · `Specifiche tecniche` · `Montaggio` ·
`Installa il driver dello schermo` · `Opzioni di collegamento` · `Impostazioni per singolo schermo` ·
`Configurazione dello schermo (a livello di sistema operativo)` · `Istruzioni di sicurezza` ·
`Apertura del menu OSD` · `Regolazione della luminosità` · `Regolazione del volume` · `Prima dell'uso` ·
`Attenzione durante la chiusura` · `Opzione 1 — USB-C (cavo singolo)` · `Pulsante Giù (−)` · `Pulsante Su (+)` ·
`Pulsante Conferma / Esci` · `3 × porte Mini-HDMI` · `Jack per cuffie da 3,5 mm` · `1. Luminosità` ·
`2. Modalità immagine` · `3. Impostazioni colore` · `4. Impostazioni OSD`.

Sentence case (§9) observed throughout — no title-case carryover. Numbering and em dashes in headings preserved.
Spec-table column headers `Caratteristica` / `Specifica` correct on all three index pages, and every field label
matches §5.4 (`Rapporto d'aspetto`, `Tempo di risposta`, `Dimensioni schermo`, `Rapporto di contrasto`,
`Tipo di pannello`, `Tipo di schermo`, `Angolo di visione`, `Frequenza di aggiornamento`, `Precisione cromatica`,
`Gamma cromatica`, `Retroilluminazione`, `Peso`, `Dimensioni (da chiuso)`, `Sistemi operativi supportati`).
`Backlight` → `Retroilluminazione` in the spec-table position per ruling R1 — **correct**, and note NL leaves it
as `Backlight` here, so IT is right and NL is the one that drifts.

### E11 — OSD verbatim scope (§7)
- ALL-CAPS device tokens preserved character-for-character: `ON/OFF`, `DCR`, `RTS`, `FPS`. **0 translated.**
- Preset values kept EN per §7.2: `Standard`, `Text`, `Movie`, `Game`, `User`, `Warm`, `Cool`. **0 translated.**
  (NL localises `User`/`Cool` to `Gebruikersinstelling`/`Koel`; IT correctly does not — pre-ruled non-defect,
  confirmed present as expected on both Lite pages.)
- Chapter headings translated per R1: `1. Luminosità`, `2. Modalità immagine`, `3. Impostazioni colore`,
  `4. Impostazioni OSD`. **0 left in English.**
- Gloss vocabulary per §7.3.1: `Luminosità`, `Contrasto`, `Livello del nero`, `Nitidezza`, `Temperatura colore`,
  `Rosso`, `Verde`, `Blu`, `Lingua`, `Timer OSD`, `Trasparenza`, `Modalità ECO`, `Rapporto d'aspetto`. All correct.
- §7.3 "no invented gloss" rule: EN `**Brightness (0–100):**` carries no separate CAPS token here, and IT correctly
  does **not** manufacture one (`**Luminosità (0–100):**`, not `**Luminosità (BRIGHTNESS) (0–100):**`).
  Structural parity with EN respected.
- Expansions `(Dynamic Contrast Ratio)`, `(Real-Time Strategy (RTS))`, `(First-Person Shooter (FPS))`,
  `(On-Screen Display)`, `(DisplayPort Alt Mode)` left in English — correct, these are the standards' own names.

### E12 — OS UI labels (§8) and the §9.10 recurring prompts
`panorama/osd.mdx` is the only F2 page with OS-level UI strings. All match §8:
`Impostazioni schermo` · `Estendi il desktop a questo schermo` · `Identifica` · `Orientamento dello schermo` ·
`Capovolto` · `Ridimensionamento` · `Impostazioni di Sistema` · `Schermi` · `Disponi`. **No Dutch string survives**
on the Italian page (§8 note) — checked explicitly against NL's `Beeldscherminstellingen` / `Gespiegeld` / `Ordenen`.

§9.10 prompt counts across the **whole** `it/` corpus were tallied and match the glossary's stated EN occurrence
counts exactly: `Schermo capovolto?` **11** (glossary: 11) · `Uno schermo è capovolto?` **3** (3) ·
`Vuoi estendere lo spazio di lavoro?` **7** (7) · `Vuoi più spazio a schermo?` **8** (6+1+1). The three-way EN
collapse (`Need more overview?` / `Want more on-screen space?` / `Need more room?` → one target) is applied
correctly, including panorama's `Need more room?`.

Quote/bold markup on `panorama/osd.mdx:41, 43` uses **bold + double quotes** (`**"Capovolto"**`) rather than the
single quotes §10 names — but this **mirrors its own EN and NL sources**, which both use `**"Flipped"**` /
`**"Gespiegeld"**`, whereas the `display-settings.mdx` pages that use single quotes mirror an EN that uses single
quotes. Structural parity, which §10 makes decisive, is satisfied. **Not a defect** — checked and cleared, recorded
here because it is the kind of thing a byte-comparison against §9.10 would false-positive on.

### E13 — Literal-translation traps (§6), targeted
Each §6 trap was searched for by its wrong form. **0 hits.** The right forms are present where the source triggers them:
`Assicurati che` (not `Fai sicuro che`) · `Leggi attentamente le indicazioni seguenti` (not `Per favore leggi le
seguenti linee guida`) · `Fai clic su` (not `clicca`) · `Segui le istruzioni visualizzate sullo schermo`
(not `istruzioni sullo-schermo`) · `Quando entrambi i collegamenti sono stati effettuati` (not `Una volta che
entrambe le connessioni sono fatte`) · `ovunque ti trovi` for `on the go` (not `sull'andare`) ·
`aumentare la tua produttività` for `boost your productivity` · `Vuoi più spazio a schermo?` ·
`ideale per guardare film` for `Suited for watching films` (not `adatto per`) · `Non ostruire le aperture di
ventilazione` · `durata` for `lifespan` (not `durata della vita`) · `Hai scansionato un codice QR?` ·
`Scegli quello adatto al tuo dispositivo` for `Pick the one that matches` · `estrai l'archivio` ·
`Riavvia`-family verbs never rendered as `ricominciare`.
`connessione` (the network false friend, §6): **0 hits** in F2 — `collegamento` used throughout, including the
locked `Opzioni di collegamento`.

### E14 — JSX-embedded strings (§9.9) and DNT
`it/manuals-index.mdx`: all 11 `<Card title>` follow the `Manuale {Product}` pattern (§9.8); the three help cards
and their body text match §9.8 (`Contatta l'assistenza` / `Ricevi aiuto dal nostro team di assistenza` ·
`Acquista i prodotti` / `Sfoglia tutti i prodotti Screenmate` · `Informazioni sulla garanzia` /
`Scopri le garanzie sui prodotti`); the `<Tip>` matches `Hai scansionato un codice QR?`; `href` values correctly
repointed to `/it/…`; `icon` values untouched. The commented-out `<Card>` template
(`[Product Name] Manual` / `Brief product description`) is correctly left **verbatim in English** per §9.10's
ruled-DNT table, and the `{/* Add future products here */}` comment likewise.
`panorama/installation.mdx:40` — the Silicon Motion URL is left verbatim as both link text and target, per the same table.
No `<Tab>` / `<video>` elements exist in F2, so §9.9's `&quot;` hazard and the `Your browser does not support the
video tag.` boilerplate are out of scope here.

### E15 — Product-name and DNT integrity
`Screenmate`, `Lite`, `Lite 144 Hz`, `Panorama`, `OneCable`, `Dual Flip`, `Flip`, `Expand`, `Infinity`,
`Infinity Lite`, `One 4K`, `One 4K OLED`, `USB-C`, `USB-A`, `HDMI`, `Mini-HDMI`, `Power Delivery`,
`DisplayPort Alt Mode`, `Windows`, `macOS`, `Linux`, `Xbox`, `PlayStation 4/5`, `Nintendo Charging Dock`,
`Nintendo Switch`, `Silicon Motion`, `Full HD`, `IPS`, `LCD`, `LED`, `sRGB`, `cd/m²`, `ms`, `Hz`, `AC/DC`, `DC`, `HDR`
— all present unchanged, brand never inflected (no `Screenmates`). `Screenmate Lite 144 Hz` keeps `144 Hz` with the
space per §4.3.

---

## Root cause and recommended fix order

Findings 01–07 are one problem wearing seven hats: **`lite` and `lite-144hz` were translated as two independent
documents when their English sources are byte-identical apart from the product name and the `Refresh Rate` value.**
`safety.mdx` came out byte-identical in Italian; `installation.mdx`, `osd.mdx`, `controls.mdx` and `index.mdx` did not.

1. **Normalise the Lite pair first.** Pick `lite` as the reference (it holds the em dashes, the §7.3 `alterna`
   verb, and the idiomatic `da una sezione all'altra`), then regenerate `lite-144hz` from it by substituting only
   the product name and `60 Hz` → `144 Hz`. That closes F2-02, F2-03, F2-04, F2-05, F2-06, F2-07 in one edit and
   makes the pair diffable forever after.
2. **Lock the `Welcome!` banner** into §9.10 as a single template — `Questo è il tuo manuale digitale completo per
   lo Screenmate {Prodotto}. Usa il menu di navigazione a sinistra per passare da una sezione all'altra.` — and
   apply it to all 11 IT index pages (F2-01). It is currently 4 shapes for 1 English sentence, so this is
   corpus-wide work, not F2 work.
3. **Panorama touch-ups** (F2-08, F2-09, F2-10) are independent one-line edits.
4. **F2-11** is a two-word safety-register alignment.
5. **F2-12** is a pipeline step for the whole `lang-expansion-de-fr-it` branch, not an IT fix — route it with the
   `de` and `fr` families rather than patching 62 files by hand.
6. **F2-13 / F2-14** are glossary amendments, not page edits. No action on the pages.
