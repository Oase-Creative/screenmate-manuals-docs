# Adversarial translation review — Italian, family F3 (`flip` + `dual-flip`)

**Branch:** `lang-expansion-de-fr-it` · **Reviewer stance:** adversarial (hunting defects, not confirming quality)
**Scope:** 12 pages — `it/manuals/flip/{index,installation,controls,osd,display-settings,safety}.mdx`
and `it/manuals/dual-flip/{index,installation,controls,osd,display-settings,safety}.mdx`,
each read against its EN source and NL sibling.
**References:** `translations/glossary-it.md`, `translations/dnt.json`,
`it/manuals/onecable/display-settings.mdx` (canonical shared body).

**Known non-defects excluded by brief** (verified present, deliberately not filed): the `×`/`x`
quantity-prefix drop in package-contents and connection lists (§4.1/§9.5); the EN-side
`Color Gamut` / `Color Accuracy` split on the two Flip spec tabs; `Please note:` → `Nota:`
collapse (§5.5/§9.9); Dutch-language screenshots.

---

## Findings

| # | File | Line / quote | Problem | Severity | Proposed fix |
|---|---|---|---|---|---|
| 1 | `it/manuals/flip/safety.mdx` (also `dual-flip/safety.mdx:14` and the whole byte-identical IT safety group) | `14:` `Assicurati che la presa di corrente sia dotata di messa a terra e adatta all'amperaggio corretto.` | **Safety-requirement weakening.** EN reads *"Make sure the power outlet is **properly** grounded"*; NL reads *"goed geaard"*. The IT drops the qualifier entirely, downgrading the instruction from "correctly earthed" to merely "has an earth connection" — a mains-electrical clause where the adverb is the load-bearing word. The glossary's own §5.2 example (`assicurati che la presa sia dotata di messa a terra`) also omits it, so the omission is inherited, not accidental — which makes it systemic rather than harmless. | **moderate** | `…sia correttamente dotata di messa a terra e adatta all'amperaggio corretto.` Frozen shared chapter: apply to all 8 IT pages in the numbered group (md5 `30cbd8e47a`) **and** the bullet variant in `dual-flip`, then re-verify group byte-identity. Update the §5.2 glossary example in the same commit. |
| 2 | `it/manuals/flip/installation.mdx` | `80:` `Ruota lo schermo sinistro di 180° all'indietro nella direzione **mostrata** nell'immagine 1.` | **Glossary violation + intra-file inconsistency.** §5.5 locks `in the direction shown` → `nella direzione indicata`. Line 47 of the *same file* renders the identical EN phrase (`in the direction shown in image 2`) correctly as `nella direzione indicata nell'immagine 2`; line 80 switches to `mostrata`. The page also (correctly) reserves `come mostrato` for EN `as shown` on lines 48 and 81, so the `indicata`/`mostrato` split is otherwise clean — line 80 is the single break. | cosmetic | `…nella direzione indicata nell'immagine 1.` |
| 3 | `it/manuals/flip/index.mdx` vs `it/manuals/dual-flip/index.mdx` | `8:` `Questo è il manuale digitale completo **dello** Screenmate Flip…` vs `8:` `Questo è **il tuo** manuale digitale completo **per lo** Screenmate Dual Flip 16"…` | **Boilerplate drift inside F3.** Both render the byte-identical EN string `This is your complete digital manual for the Screenmate {X}`. Two different possessive/preposition treatments on adjacent product families. Corpus-wide the IT `index` pages carry **three** variants (`il tuo … per lo` ×6, `il manuale … dello` ×4, `il manuale … del tuo` ×1), so F3 straddles the two majority forms. Recurring UI boilerplate must read identically. | cosmetic | Normalise F3 (and ideally all 11 IT index pages) onto the corpus-majority form: `Questo è il tuo manuale digitale completo per lo Screenmate {X}.` Also reconcile the tail (`per passare a ogni sezione` ×5 vs `per passare da una sezione all'altra` ×6). |
| 4 | `it/manuals/flip/installation.mdx` vs `it/manuals/dual-flip/installation.mdx` | `46:` `Estrai **con attenzione** lo Screenmate dalla confezione.` vs `20:` `Estrai **con cura** lo Screenmate dalla confezione.` | Identical EN step (`Carefully remove the Screenmate from the packaging.`) rendered two ways within F3. Corpus vote is 2:1 for `con cura` (`dual-flip`, `onecable`). | cosmetic | Use `con cura` in `flip/installation.mdx:46`. |
| 5 | `it/manuals/dual-flip/osd.mdx` | `11:` `Premi il pulsante **M** (Menu) per confermare **la tua** scelta.` | Identical EN step (`to confirm your choice`) is rendered `per confermare la scelta` in `flip/osd.mdx:11` and `expand/osd.mdx:11`. §1.3 explicitly instructs *not* to mechanically carry every English "your"; the choice is not reader-owned in the §1.3 sense. `dual-flip` is the 1-of-3 outlier. | cosmetic | `…per confermare la scelta.` |
| 6 | `it/manuals/flip/controls.mdx` | `24:` `- **+** — aumenta la luminosità.` / `25:` `- **−** — riduce la luminosità.` | **Sentence-initial casing.** These bullets are full-stop-terminated fragments; EN (`— Increase brightness.`) and NL (`— Helderheid verhogen.`) both capitalise, and the F3 sibling `dual-flip/controls.mdx:31,35` capitalises the same content (`Aumenta la luminosità nell'uso normale…`). No glossary rule licenses lowercase here — §7.3's lowercase-after-colon applies to `**Gloss (CAPS):**` run-ins, and §9's sentence-case rule applies to headings, neither of which this is. Lower confidence than the rest: after an em-dash apposition, lowercase is defensible for the noun phrase on line 23. | cosmetic | Capitalise the two verb-phrase bullets — `Aumenta la luminosità.` / `Riduce la luminosità.` — or capitalise all three for internal list consistency. Decide once and mirror onto the other IT `controls` pages. |
| 7 | `it/manuals/flip/display-settings.mdx` (and the whole frozen group) vs `translations/glossary-it.md` | `28,48:` `…per correggere il problema.` and `32:` `…per una visualizzazione più grande di testo ed elementi.` | **Glossary/shipped divergence in §9.10 body rows.** `glossary-it.md:1270-1271` lock `…per correggerlo.` and `:1267` locks `…per visualizzare testo ed elementi più grandi.`. Shipped IT uses the other wording — but does so with **100 % consistency across all six IT `display-settings` pages**, so the pages are self-coherent and the glossary rows are the stale side. Meaning is unaffected either way. (The §9.10 *question* strings were already back-derived from shipped per the review brief; the body rows evidently were not.) | cosmetic | Reconcile `glossary-it.md:1267,1270,1271` to the shipped wording. **Do not** edit the frozen chapter — a text change there must be applied to all six pages atomically and re-checksummed. |
| 8 | `it/manuals/flip/installation.mdx` and `it/manuals/dual-flip/installation.mdx` | `12:` `- **1 USB-C e 1 USB-A e 1 HDMI**` | **Calque of the EN `&` chain.** Doubled coordinating `e … e` is unidiomatic in an Italian enumeration. §9.5 renders the analogous EN list (`2. 1x USB-C, 1x HDMI and 1x USB-A`) as `1 USB-C, 1 HDMI e 1 USB-A` — comma-separated with a single final `e`. §10's `&` → `e` rule governs the *character*, not the repetition. | cosmetic | `- **1 USB-C, 1 USB-A e 1 HDMI**` on both pages. Note this trades a literal `&`-for-`e` mapping against readability; if strict separator parity with EN is preferred, close as won't-fix and record the ruling in §10. |
| 9 | `it/manuals/flip/index.mdx` | `20:` `- **1 cavo USB-C con adattatore USB-A (90 cm)**` | **Addition not in source.** This page's EN reads `1× USB-C with USB-A **Adapter** (90 cm)` and NL `1× USB-C met USB-A **Adapter** (90 cm)` — neither carries a head noun for "cable". IT inserts `cavo`. It matches §2.5's mapping of the *dual-flip* string (`USB-C with USB-A adapter **cable**`) and is factually correct (the part is a cable), so it reads as a silent EN-side correction rather than a translation error. | cosmetic | No IT change recommended. Route the EN inconsistency (`flip` says "Adapter", `dual-flip` says "adapter cable" for the same part) to EN editorial; if EN is normalised, IT is already aligned. |

**Counts:** critical **0** · moderate **1** · cosmetic **8**.

---

## Scrutiny evidence — checks run, and what they proved

### Frozen shared chapters

- **`display-settings` body byte-identity.** md5 of every IT page from line 6 down:
  `dual-flip`, `expand`, `flip`, `onecable` all = `a82c96c61a45`. Group is intact and matches
  the OneCable canonical exactly, including all three `alt` strings and both
  `Il tuo browser non supporta il tag video.` fallbacks. `infinity` / `infinity-lite` sit
  outside the group in IT (`15c979170c57`, `3ff4d2af461f`) — correctly, because their EN
  sources also diverge (`a44bc8469386`, `6818a40603eb`). No divergence to report.
- **`safety` body parity.** IT `flip` = `30cbd8e47a`, in the numbered-list group with `expand`,
  `lite`, `lite-144hz`, `one-4k`, `one-4k-oled`, `onecable`. IT `dual-flip` uses `-` bullets and
  sits alone — **this mirrors EN exactly**: `en/manuals/dual-flip/safety.mdx` is bulleted while
  `en/manuals/flip/safety.mdx` is numbered, and the same split appears in NL, DE and FR. Verified
  mechanically: `diff` of IT flip (markers rewritten `^N.` → `- `) against IT dual-flip returns
  **rc=0**, and the identical diff on the EN pair also returns **rc=0**. Not a defect.
- **Frozen-chapter safety net.** Finding #1 and #7 both land inside frozen bodies; both proposed
  fixes are written as all-or-nothing group operations for exactly that reason.

### Register (§1)

- Courtesy-form grep (§1.5 regex, all 12 pages): 2 hits, both `deve` — `flip/installation.mdx:72`
  and `dual-flip/installation.mdx:46`, subject `lo Screenmate` in both. Documented false positive
  per §1.5 ("`può`/`deve` are legitimate when the subject is a **thing**"). Clean.
- Formal-imperative grep (§1.5 verb list): 2 hits, both documented false positives —
  `usi` as the plural noun in `per usi diversi` (`flip/osd.mdx:20`) and `selezioni` as the plural
  noun in `per confermare le selezioni` (`dual-flip/controls.mdx:27`). Clean.
- Impersonal-infinitive instruction style (`Collegare…`, `Assicurarsi…` at step-start): 0 hits.
- Negative imperatives are `non` + infinitive throughout: `non premere sugli schermi`,
  `Non ruotare gli schermi`, `Non usare liquidi`, `Non toccare il dispositivo`,
  `Non far cadere il monitor`, `Non ostruire le aperture di ventilazione`. All §1.2-conformant.
- `Ti consigliamo di scollegare…` (both index pages) — correct informal plural-of-modesty per §1.1.

### Safety-negation integrity (`safety.mdx`, both pages, item by item)

All 14 items read against EN and NL. Every negation survives, including the two double negations
(`Non toccare … e non usarlo in ambienti umidi`; `Non usare liquidi o detergenti aggressivi`).
`Keep ventilation openings clear` → `Non ostruire le aperture di ventilazione` inverts polarity
**as §6 explicitly locks it** — verified against the glossary, not assumed. Electrical values
carried intact: `5 V`–`20 V`, `±2 V`, `5 V`, `-20 °C`/`60 °C`. Only finding #1 breaks the set.

### Numbers, units, measurements (§4)

- `\d,\d\d\d` (English thousands separator surviving into IT) — **0 hits** across all 12 pages.
  The two four-digit weights are correct: `1565 grammi`, `1875 grammi`, `1900 grammi`.
- `\d\.\d` — 21 hits, **all** inside `src="…Flip%2015.6…"` URL paths or the whitelisted
  `USB-A 2.0` token (§4.3). Zero in body copy.
- Decimal commas applied where they must be and nowhere else: `34,5 × 22 × 3,5 cm`,
  `39 × 23 × 3,5 cm`, `39 × 24 × 3,5 cm`, `15,6"`.
- Spec values cross-checked cell-by-cell against EN for both Flip tabs and the Dual Flip table —
  no transposition between the 14" and 15.6" columns (`1920×1200`/`16:10`/`1565` vs
  `1920×1080`/`16:9`/`1875`), and no swap of the asymmetric rotation limits
  (`sinistro` 245°, `destro` 205°) on either index page.
- `×` audit: EN 21, NL 17, IT 10. Every dropped instance is a quantity prefix (the sanctioned
  §4.1 drop); **every** dimension and resolution `×` survives — enumerated and confirmed at
  `flip/index.mdx:33,46,52,65` and `dual-flip/index.mdx:15,31,44`.
- SI spacing per §4.1/§11.1-5: `250 cd/m²`, `25 ms`, `60 Hz`, `5 V/2 A`, `178°` (closed up),
  `150%` (closed up), `-20 °C` (spaced). All conformant.
- `10–60 secondi`, `0–100`, `0–4` — en-dash ranges mirrored from EN, `secondi` spelled out (§4.4).

### Glossary term compliance (§2, §3, §5, §6)

- Cable chain (§2.5): `cavo da USB-C a USB-C`, `cavo da Mini-HDMI a HDMI`, `cavo da USB-C a USB-A`,
  `2 cavi da USB-C a USB-C`. Zero rejected variants; grep for `ad USB|ad HDMI|ad Mini` → 0 hits.
  Directionality preserved from source (`USB-C to USB-A` stays `da USB-C a USB-A`).
- Compounds (§2.1–2.3): `porta USB-C`, `porta HDMI`, `menu OSD`, `cavo di alimentazione`,
  `pulsante di accensione`, `supporto regolabile`, `superficie piana`. No Dutch/German hyphen
  chains imported — `USB-C-kabel`-style forms: 0 hits.
- `Mini-HDMI` hyphenated in **all** IT positions (`controls.mdx:17,21`, `installation.mdx:16,18`
  alt) even where EN writes `Mini HDMI` — §2.2 note honoured deliberately, not accidentally.
- Article/gender traps (§3.1): grep for `il Screenmate|del Screenmate|al/sul/nel Screenmate|
  il schermo|i schermi|il smartphone` → **0 hits**. Shipped uses `lo Screenmate`, `dello Screenmate`,
  `allo Screenmate`, `gli schermi`, and correctly switches to `il tuo Screenmate` / `il monitor`
  when a `t`/`m`-initial word intervenes.
- Locked §6 renderings all present and correct: `Abbi cura del tuo Screenmate` (not
  `Prendi buona cura`), `Non far cadere il monitor`, `Assicurati che`, `Tieni premuto`,
  `Fai clic su`, `ovunque ti trovi`, `Scegli quello adatto`, `per ridurre l'affaticamento
  degli occhi`, `prolungano la durata`.
- `collegamento` not `connessione` throughout (`Opzioni di collegamento`, `scenari di
  collegamento`) — grep for `connessione` → 0 hits. `clicca` → 0 hits. `drivers` → 0 hits.
  `menù` → 0 hits.

### OSD policy (§7, R1 + §7.3 carve-out)

- `flip/osd.mdx` headings fully translated per R1: `Retroilluminazione` · `Immagine` · `Colore` ·
  `Impostazioni` · `Ripristino` · `Altro`. `dual-flip/osd.mdx` likewise with numbering preserved:
  `### 1. Retroilluminazione` … `### 6. Altro`, plus `### 3. Impostazioni colore` for EN
  `3. Color Settings` (§9.6). No untranslated `Backlight`/`Reset` heading anywhere.
- ALL-CAPS device tokens verbatim in every gloss: `BRIGHTNESS`, `CONTRAST`, `ECO`, `DCR`,
  `SHARPNESS`, `ASPECT`, `COLOR TEMP.` (trailing period preserved on `flip`, absent on
  `dual-flip` — matching each EN source exactly), `RED`, `GREEN`, `BLUE`, `LANGUAGE`,
  `OSD TIMER`, `TRANSPARENCY`, `RESET`, `HDR`/`HDR MODE`, `SOURCE`, `LOW BLUE LIGHT`.
- **§7.3 carve-out correctly applied:** `dual-flip/osd.mdx` uses bare CAPS run-ins
  (`- **BRIGHTNESS (0–100):** regola la luminosità dello schermo.`) because its EN has no gloss,
  while `flip/osd.mdx` uses the glossed form (`- **Luminosità (BRIGHTNESS):** …`) because its EN
  does. No Italian gloss was invented where EN lacks one. This is the exact trap §7.3's last
  paragraph warns about, and the pages pass it.
- Preset values kept English per §7.2: `Standard, Game, Movie, Text, FPS, RTS, Energy Saving`,
  `Warm, Cool, User`, `Off, Auto, 2084`, `Type-C1 / Type-C2`, `4:3`, `WIDE`, `ON`/`OFF`.
- §7.4 language list lowercased on both pages: `inglese, francese, tedesco, cinese semplificato,
  italiano, spagnolo, portoghese, turco, polacco, olandese, giapponese, coreano.`
- Source-count fidelity: `flip` = `due sorgenti del segnale: Type-C1 / Type-C2 e HDMI`;
  `dual-flip` = `tre sorgenti del segnale: Type-C1, Type-C2 e HDMI`. Not cross-contaminated.

### JSX-embedded strings and inch marks (§9.9, §4.5)

- `<Tab title="Flip 14&quot;">` and `<Tab title="Flip 15,6&quot;">` — `&quot;` escaping intact,
  decimal comma applied inside the escaped string. No literal `"` in any JSX attribute
  (would break the MDX build).
- Markdown-heading counterparts carry the **literal** prime: `### Flip 14"` / `### Flip 15,6"`
  (`installation.mdx:14,20`). The §9.9 two-context rule is honoured in both directions on the
  same page.
- `<p className="…">` children swept: `USB-C`, `HDMI`, `USB-A 2.0` — DNT connector names,
  correctly left verbatim (§9.9).
- `<video>` fallbacks: `Il tuo browser non supporta il tag video.` ×2 per display-settings page.
- `className` / `src` / `icon` untouched; no image filename translated.

### `alt` text (R9)

All 30 unique `alt` strings enumerated. Every product-page alt is fully Italian
(`Porte laterali dello Screenmate Flip`, `Fasi per riporre lo Screenmate Flip`,
`Diagramma in tre passaggi per riporre il Dual Flip`, `Menu OSD Retroilluminazione`, …).
Zero Dutch residue. The three `display-settings` alts retain EN OS labels with Italian glosses
(`…scegli Display settings (Impostazioni schermo)`) — that is the §8 parenthetical pattern, is
required for byte-identity with the OneCable canonical, and matches the visible body copy on the
same page. Leakage grep for Dutch/English content words across all IT prose returned exactly one
hit: the word `and` inside `Scale and layout` — a Windows UI label, correct per §8.

### Structural parity (EN ↔ IT ↔ NL)

Per-file counts of headings / `-` bullets / `<img>` / `**bold**` runs / ordered-list items are
**identical in all three languages for all 12 pages** (e.g. `flip/osd` = 7/17/6/22/4 in EN, IT
and NL alike). No content dropped, none invented, no emphasis added or removed (§10). Singular/
plural distinctions tracked to source — EN `maximum angles` (flip) → `gli angoli massimi`
vs EN `maximum angle` (dual-flip) → `l'angolo massimo`; EN `tiltable` → `inclinabile`
vs EN `tilts` → `si inclina`; EN `connect the Screenmate as follows` (imperative, flip) →
`collega lo Screenmate come segue` vs EN `you can connect` (dual-flip) → `puoi collegare`.

### Typography (§3.3, §10)

- Typographic apostrophe `’` — **0 hits**; all elisions use straight ASCII `'`
  (`dell'OSD`, `l'alimentazione`, `un'estensione`, `d'aspetto`, `all'interno`).
- `un'` used feminine-only (`un'estensione`, `un'immagine`); no `un'alimentatore`.
- `qual'è` — 0 hits. Accented vowels are real characters throughout (`è`, `più`, `luminosità`,
  `nitidezza`, `perché`); no `e'`-style apostrophe hacks.
- Sentence-final double spaces — 0 hits.
- Straight single quotes around UI strings (`'Ridimensionamento'`, `'Capovolto'`, `'Standard'`);
  no caporali `«…»`.
- Em dash preserved only where the EN heading/body already had one
  (`### M — pulsante del menu OSD`, `— uno per lato`); none introduced. Special-character
  inventory matches EN exactly for `−` (4), `–` (12), `—` (6), `±` (2), `°` (21), `²` (3).
- Line endings CRLF and trailing newline present on all 12 IT pages, consistent with the tree.

### Frontmatter (§9.1, §9.2)

Every `title` and `description` matches its §9.1/§9.2 locked row against the correct EN source —
including the easily-crossed pair where `flip/display-settings` takes
`Configurazione degli schermi su Windows e macOS` (EN: *Configuring your displays…*) while
`dual-flip/display-settings` takes `Impostazioni schermo per Windows e macOS`
(EN: *Display settings for…*). Verified by extracting line 3 of all 18 EN/NL/IT
`display-settings` pages side by side; no crossover. `icon` values untranslated.

**Out of scope, noted not filed:** no IT page carries an `it_link`/`en_link` frontmatter key.
This is uniform across the entire branch (`it/`, `de/`, `fr/` = 0 pages with any `*_link` key),
was mandated by the expansion brief, and is already routed to the orchestrator in
`.superpowers/sdd/2026-08-11-it-de-fr-language-expansion/task-7-fr-manuals-index-report.md`.
Not an F3 translation defect.

### Headings audit (§9.3–§9.6)

All 50 IT headings across the 12 pages listed and checked individually against the §9 tables.
Sentence case everywhere (`Porte e pulsanti`, `Contenuto della confezione`, `Specifiche tecniche`,
`Opzioni di collegamento`, `Impostazioni colore`) — no title-case carry-over from EN.
The §11.3 two-target `Storage` split is applied correctly and not swapped:
`flip/installation.mdx:75` = `## Come riporre lo Screenmate` (EN *Storing the Screenmate*),
`dual-flip/installation.mdx:49` = `## Come riporre il prodotto` (EN *Storage*).
