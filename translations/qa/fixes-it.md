# Italian fix log — Task 10 adversarial + back-translation findings

**Branch:** `lang-expansion-de-fr-it` · **Date:** 2026-08-11
**Sources:** `adversarial-it-F1.md`, `-F2.md`, `-F3.md`, `-F4.md`, `backtranslation-review-it.md`
**Binding reference:** `translations/glossary-it.md`

**Gate after fixes:** `python scripts/verify_translation.py --base en --targets it` → **0 FAIL, 0 WARN (exit 0)**
**Group-A `safety.mdx` body hash (onecable, lite, lite-144hz, flip, expand, one-4k, one-4k-oled):** `3819445a96d21842` ×7 — byte-identical
**`display-settings.mdx` dedupe group (onecable, dual-flip, flip, expand):** `0a5c2885f7ef3360` ×4 — byte-identical

**Totals:** 83 string edits across 45 files (44 `it/` pages + `glossary-it.md`). **Applied: 27 findings. Skipped: 11** (all with reason below).

---

## 1. SAFETY — grounding clause (F3-01 / F4-09) — **highest priority, applied**

EN `Make sure the power outlet is **properly** grounded…` / NL `goed geaard` — the Italian dropped the
adverb, downgrading a mains-electrical quality requirement to a presence check.

| Item | Change |
|---|---|
| Fix, per F3's proposal | `Assicurati che la presa di corrente sia dotata di messa a terra e adatta all'amperaggio corretto.` → `Assicurati che la presa di corrente sia **correttamente** dotata di messa a terra e adatta all'amperaggio corretto.` |
| Group-A re-propagation (byte-identical, dedupe-enforced) | `it/manuals/{onecable,lite,lite-144hz,flip,expand,one-4k,one-4k-oled}/safety.mdx:14` |
| Non-group pages carrying the same EN sentence | `it/manuals/dual-flip/safety.mdx:14` (bullet variant), `it/manuals/infinity/safety.mdx:15`, `it/manuals/infinity-lite/safety.mdx:15`, `it/manuals/panorama/safety.mdx:15` |
| **Systemic glossary amendment** (explicitly authorised — chapter and glossary example must agree) | `translations/glossary-it.md:500` §5.2 `grounded` row: example changed to `assicurati che la presa sia **correttamente** dotata di messa a terra`, with a note that EN `properly` / NL `goed` is load-bearing and `correttamente` must never be dropped. Without this the omission would be re-inherited by the next translator. |

11 IT pages carry the corrected sentence; group-A re-verified byte-identical (hash above).

---

## 2. §9.10 lock deviations (F1-02, F1-03, F3-07, F4-07) — applied

The glossary rows are the lock; the shipped pages were moved onto them (not the reverse).

| Finding → locked target | file:line | Change |
|---|---|---|
| F1-02 — `…per una visualizzazione più grande di testo ed elementi.` (calque of NL `voor een grotere weergave van`) → §9.10 `…per visualizzare testo ed elementi più grandi.` | `it/manuals/{onecable,dual-flip,flip,expand}/display-settings.mdx:32`, `it/manuals/infinity-lite/display-settings.mdx:57` | 5 occurrences replaced (F1 filed 2; corpus sweep found 5 — the lock is corpus-wide) |
| F1-03 — `…per correggere il problema.` → §9.10 `…per correggerlo.` | `it/manuals/{onecable,dual-flip,flip,expand}/display-settings.mdx:28,48`; `it/manuals/infinity/display-settings.mdx:24,47`; `it/manuals/infinity-lite/display-settings.mdx:17,53,72` | 13 occurrences replaced (F1 filed 7; swept corpus-wide) |

F3-07 and F4-07 report the same divergence and proposed reconciling the glossary to the shipped text
instead. **Ruling applied: pages move to the glossary**, per the brief's priority-2 instruction. No
§9.10 edit was made — the rows already read as shipped now. The `display-settings.mdx` dedupe group
was re-verified byte-identical after the edits.

---

## 3. Twin harmonisation — applied

### 3a. `lite` ↔ `lite-144hz` (F2-02 … F2-07)

EN sources are byte-identical apart from product name and refresh rate. `lite` taken as reference
except where the glossary makes `lite-144hz` the compliant side (dash policy, §5).

| # | file:line | Change |
|---|---|---|
| F2-05 | `lite-144hz/installation.mdx:9` | `ai cavi disponibili` → `ai cavi che hai a disposizione` |
| F2-05/06 | `lite-144hz/installation.mdx:21` | `Ti serve alimentazione aggiuntiva? **Usa allora** il cavo…` → `Serve alimentazione aggiuntiva? **Usa** il cavo…` (NL word-order calque `Gebruik dan`) |
| F2-05 | `lite-144hz/installation.mdx:35` | `collegare il telefono o il tablet` → `collegare il tuo telefono o tablet` (§1.3; removes the in-sentence possessive contradiction) |
| F2-05 | `lite-144hz/installation.mdx:37,41` | `alt="Collegamento USB-C a telefono o tablet…"` → `…al telefono o al tablet…` |
| F2-03 | `lite/installation.mdx:35,57` | em dash → ` – ` (see §5 dash ruling); this closes the twin split **and** brings both onto §10 |
| F2-04 | `lite-144hz/osd.mdx:17` | `più dettagli nelle scene scure` → `più dettaglio` (EN `more detail`) |
| F2-04 | `lite-144hz/osd.mdx:18` | `i dettagli dell'immagine` → `il dettaglio dell'immagine` |
| F2-04 | `lite-144hz/osd.mdx:32` | `**cambia** … tra **formato panoramico**` → `**alterna** … tra **panoramico**` (§7.3 locks `alterna` for ASPECT) |
| F2-04 | `lite-144hz/osd.mdx:47` | `scegli tra **le** 12 lingue` → `scegli tra 12 lingue` (EN `Choose from 12 available languages`) |
| F2-04 | `lite-144hz/osd.mdx:49` | `per una **visualizzazione** migliore` → `per una **visione** migliore` |
| F2-07 | `lite-144hz/controls.mdx:33` | `naviga **nei** menu` → `naviga **tra** i menu` (EN `navigate through menus`) |

**Post-check:** the only remaining IT differences between the pair are EN-driven (the `index.mdx:15`
product description, which differs in EN, and `**Modalità OSD**` vs `**Modalità menu OSD**`, which
mirrors EN `OSD mode` / `OSD menu mode`). `safety.mdx` remains byte-identical.

### 3b. `one-4k` ↔ `one-4k-oled` (F4-01 … F4-05)

| # | file:line | Change |
|---|---|---|
| F4-01 | `one-4k-oled/installation.mdx:9` | `con i cavi giusti` → `con i cavi corretti` (EN `correct cables`) |
| F4-01 | `one-4k-oled/installation.mdx:11` | `adatta le impostazioni schermo` → `regola le impostazioni schermo` (EN `adjusts`) |
| F4-01 | `one-4k-oled/installation.mdx:15` | `Quando riceve un segnale dalla porta USB-C, lo Screenmate…` → `Quando viene ricevuto un segnale tramite la porta USB-C, lo Screenmate…` (restores EN's impersonal passive) |
| F4-02 | `one-4k/controls.mdx:13` | `Questo **unico** collegamento … **su** un solo cavo.` → `Questo **singolo** collegamento … **con** un solo cavo.` |
| F4-02 | `one-4k-oled/controls.mdx:15` | `per **trasmettere** il segnale video` → `per **trasportare** il segnale video` (matches `trasporta` for EN `carries` two lines above) |
| F4-02 | `one-4k/controls.mdx:23` | `Usala **insieme al** cavo USB-C e **all'**alimentatore in dotazione.` → `Usala **con il** cavo USB-C e **l'**alimentatore in dotazione.` (EN `Use with the supplied…`) |
| F4-02 | `one-4k-oled/controls.mdx:39` | `Spia LED di stato per l'alimentazione e il segnale.` → `Spia LED che indica lo stato dell'alimentazione e del segnale.` (EN `Status LED indicating power and signal state`) |
| F4-03 | `one-4k/controls.mdx:47,48` | `apre la **scorciatoia** per la luminosità/il volume in modalità generale` → `in modalità generale apre il **menu delle scorciatoie** per la luminosità/il volume` (EN `opens the … shortcut menu`; one-4k was the defective side) |
| F4-04 | `one-4k/osd.mdx:30` | adopted the OLED wording wholesale: `pulsanti **frontali**`, `il **menu OSD** potrebbe essere bloccato` (§3.2), and EN's clause order `Tieni premuto il pulsante sopra … per **10 secondi**` |
| F4-05 | `one-4k-oled/index.mdx:15` | gloss head order `monitor portatile **da 15,6" 4K UHD**` → `monitor portatile **4K UHD da 15,6"**` (§2.4 — `da` governs the measurement only); closing sentence normalised onto one-4k's faithful `supporta …` shape; em dash → ` – ` |

**Post-check (normalised diff, one-4k vs one-4k-oled):** IT divergent-line count is now ≤ EN's on every
page (`index` EN 20 / IT 18, `installation` 22/20, `controls` 8/6, `osd` 4/2, `safety` 2/0 — the
constant −2 is the `nl_link` frontmatter line present on both EN sides only). Before the fix,
`controls` was EN 2 / IT 14.

---

## 4. `Welcome!` harmonisation (F2-01, F3-03) — applied

One EN sentence (`This is your complete digital manual for the Screenmate X. Use the navigation menu on
the left to jump to each section.`) had **4 Italian shapes** across 11 index pages, plus 2 tail shapes.

Single locked target chosen (corpus-majority, §1.3-compliant — possessive on the manual, not the
product; §3.1 `per lo Screenmate`; idiomatic tail, not the `passare a ogni sezione` calque flagged as
F2-02):

> `**Benvenuto!** Questo è il tuo manuale digitale completo per lo Screenmate {Prodotto}. Usa il menu di navigazione a sinistra per passare da una sezione all'altra.`

Applied at `:8` on all 11 `it/manuals/*/index.mdx`. 7 pages changed
(`dual-flip`, `expand`, `flip`, `infinity`, `lite-144hz`, `onecable`, `panorama`); 4 already conformed.
`flip` keeps its EN-sourced extra clause (`, valido sia per il modello da 14" sia per quello da 15,6"`).

---

## 5. Remaining concrete lows — applied

| # | file:line | Change |
|---|---|---|
| F1-04 | `infinity-lite/index.mdx:15` | `ed è **pensata** per l'uso plug-and-play` → `ed è **pensato**` (subject is `lo Screenmate Infinity Lite`, m., §3.2 — gender was agreeing with `un'estensione` from the previous sentence) |
| F1-05 | `infinity/index.mdx:15` | `due schermi in più **in una sola volta**` → `**contemporaneamente**` (EN/NL `at once` = simultaneously, not "in one go") |
| F1-06 | `onecable/index.mdx:15` | `**aggiungendo** due schermi **aggiuntivi**` → `aggiungendo due schermi **in più**` (same-root echo in the page's highest-visibility sentence) |
| F1-07 / F2-03 / F4-08 | 10 sites, 14 dashes | **Dash policy unified**, see ruling below |
| F3-02 | `flip/installation.mdx:80` | `nella direzione **mostrata**` → `nella direzione **indicata**` (§5.5 lock; line 47 of the same file already had it right) |
| F3-04 | `flip/installation.mdx:46` | `Estrai **con attenzione**` → `Estrai **con cura**` (corpus vote 2:1) |
| F3-05 | `dual-flip/osd.mdx:11` | `per confermare **la tua** scelta` → `per confermare **la** scelta` (§1.3; matches `flip` and `expand`) |
| F3-06 | `flip/controls.mdx:23,24,25` | Sentence-initial capitals restored on all three em-dash label bullets (`Pulsante del menu OSD.` / `Aumenta la luminosità.` / `Riduce la luminosità.`) — EN, NL and the `dual-flip` sibling all capitalise; all three capitalised for internal list consistency, as F3 recommended |
| F3-08 | `flip/installation.mdx:12`, `dual-flip/installation.mdx:12` | `- **1 USB-C e 1 USB-A e 1 HDMI**` → `- **1 USB-C, 1 USB-A e 1 HDMI**` (§9.5 enumeration pattern; §10's `&`→`e` rule governs the character, not the repetition) |
| F2-08 | `panorama/index.mdx:15` | `Per gestire tre schermi indipendenti … **è necessario installare** il driver dello schermo.` → `Il driver dello schermo **necessario consente** di gestire tre schermi indipendenti con un solo cavo.` (EN states what the driver enables; it never says "install" here) |
| F2-09 | `panorama/controls.mdx:28` | `dello schermo selezionato` → `dello schermo **attualmente** selezionato` (load-bearing: short presses cycle the selected screen) |
| F2-10 | `panorama/installation.mdx:28` | `**Attenzione:** quando pieghi gli schermi, **fai attenzione** alle dita … di **schiacciartele**.` → `**Attenzione:** **bada** alle dita quando pieghi gli schermi, per evitare di **schiacciarle**.` (removes the `attenzione`×2 echo EN does not have; aligns the verb form with `safety.mdx:26`) |
| F2-11 | `panorama/safety.mdx:14` | `Usa **solo** un alimentatore AC/DC` → `Usa **esclusivamente**` (safety restrictive operator uniform corpus-wide; `esclusivamente` used 2:1 and is the stronger) |
| F4-06 | `expand/installation.mdx:59,74` | `**Nota:** **L**a porta HDMI` → `**Nota:** **l**a porta HDMI` (the only 2 capitalised bold run-ins in the whole `it/` tree; 156 others lowercase) |
| F4-10 | `expand/controls.mdx:9` | `e **di tutti i** pulsanti di comando` → `e **dei** pulsanti di comando` (matches both One 4K pages) |
| F4-11 | `expand/osd.mdx:61` | `**riduce** la quantità di luce blu … per **ridurre** l'affaticamento` → `**limita** la quantità …` (§6 locks the tail, so the head verb moved) |

### Dash ruling (F1-07, F2-03, F4-08) — the §10 reading applied

§10 states: *em dash — preserve it where an EN **heading** already has one; avoid introducing it into
body copy; use `–` (en dash) with spaces, or a comma.* Applied literally and corpus-wide:

- **Em dash kept** in: `##`/`###` headings, frontmatter `description` values, MDX comments (never
  rendered, §10), and label-apposition list items of the form `- **X** — gloss` (structurally the
  bullet twin of `dual-flip`'s `### M — pulsante del menu OSD` heading).
- **Em dash → ` – `** in running prose, 14 occurrences across 10 sites:
  `dual-flip/index.mdx:15` · `infinity/display-settings.mdx:68 (×2), :74` ·
  `infinity-lite/display-settings.mdx:93 (×2), :100` · `lite/installation.mdx:35, :57 (×2)` ·
  `one-4k/installation.mdx:45, :67 (×2)` · `one-4k-oled/index.mdx:15` ·
  `one-4k-oled/installation.mdx:61 (×2)`.

This resolves all three reports at once: `onecable/installation-windows.mdx:47` (F1-07's en-dash site)
was already compliant, `lite-144hz` (F2-03) was already compliant, and `expand` (F4-08) was already
compliant — the outliers moved to them rather than the reverse. Post-check: 12 em dashes remain in
`it/`, all in the four permitted positions.

---

## Skipped — with reason

| # | Finding | Reason |
|---|---|---|
| F1-01, F2-12, F3 (out-of-scope note), F4-12, backtranslation structural note | No `*_link` frontmatter key on any `it/` page | **FALSE POSITIVE for this task.** Branch-wide mechanical step (`de/` and `fr/` are also at 0) owned by the later cross-language link-generator task, not an Italian translation defect. |
| F1-08 | `scegli 'Capovolto'` — value given in Italian only while the setting name keeps the EN token with a gloss | Requires a **§9.10 amendment** (extending the §8 parenthetical pattern to setting *values*), which is outside the single glossary edit authorised for this pass. Routed to the glossary owner; would also touch the frozen `display-settings` chapter corpus-wide. |
| F2-13 | `UI` dropped from `for larger text and UI elements` | Raised by its own author against the **glossary**, not the page — the page is §9.10-compliant as shipped. |
| F2-14 | `Impostazioni schermo per singolo schermo dal menu a schermo` — three `schermo` in eight words | Same: string is locked verbatim in §9.2; glossary-side proposal, page is compliant. |
| F3-09 | `1 cavo USB-C con adattatore USB-A (90 cm)` adds a head noun EN lacks | **EN-source issue** — `flip` says "Adapter", `dual-flip` says "adapter cable" for the same part. F3's own recommendation is "no IT change"; the IT is already aligned with whichever way EN normalises. |
| F1 source-side ×3 (`infinity-lite` "both extension screens", `infinity-lite` HDMI port, `infinity` mirrored/identical) | EN/NL source defects faithfully mirrored | **EN-source issues** — client list. |
| Backtranslation §2 items 1–23 | Contradictory instructions, framing defects, cosmetic EN inconsistencies | **EN-source issues** — client list. Fixing them means editing EN and IT together. |
| Backtranslation table rows 5–12 | Heading levels, gloss duplication, `Ridimensionamento`, decimal commas, `blocco anteriore`, numbered-vs-bulleted safety, image placement, `COLOR TEMP` split | **Loop artifacts** — adjudicated as non-divergences by the review itself. |
| Backtranslation drift #2 | `Vuoi più spazio a schermo?` collapsing three EN prompts | Deliberate and **§9.10-locked** (one target for `Need more overview?` / `Want more on-screen space?` / `Need more room?`). Correct as shipped. |
| Backtranslation drift #3 | Added Italian glosses on the macOS `System Settings` path | Beneficial and matches the §8 parenthetical pattern. No meaning change. |
| Backtranslation drift #4 | `/en/…` href inside the commented-out `<Card>` template in `it/manuals-index.mdx` | §10 and §9.10's ruled-DNT table **explicitly lock MDX comment contents verbatim**, naming this template. Not reader-visible. |

---

## Verification performed

| Check | Result |
|---|---|
| `python scripts/verify_translation.py --base en --targets it` | **0 FAIL, 0 WARN — exit 0** |
| `safety.mdx` group-A byte-identity (dedupe-enforced) | 1 hash for 7 slugs: `3819445a96d21842` |
| `display-settings.mdx` dedupe group byte-identity | 1 hash for 4 slugs: `0a5c2885f7ef3360` |
| §1.5 courtesy pronouns / set phrases (`Lei|Suo|Sua|Suoi|Sue|Vostr*|La preghiamo|Le consigliamo|Si prega di|Per favore|voglia`) | **0 hits** |
| §1.5 courtesy imperatives (26-verb regex) | 7 hits, **all documented false positives** — `colleghi` / `pieghi` as 2nd-sg present indicative (5), `selezioni` as a plural noun (1), `pieghi` in `quando pieghi gli schermi` (1) |
| Residual lock deviations (`correggere il problema`, `visualizzazione più grande`, `Usa allora`, `in una sola volta`, `è pensata per l'uso`, `passare a ogni sezione`) | **0 hits** |
| Grounding clause present with `correttamente` | 11/11 `it/manuals/*/safety.mdx` |
| `Welcome!` shape | 11/11 index pages on one template |
| Em dash inventory | 12 remaining, all in headings / frontmatter descriptions / MDX comments / label bullets |
| Twin parity | `lite` pair: residual diffs are EN-driven only. `one-4k` pair: IT divergent lines ≤ EN on every page. |
