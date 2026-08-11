# Adversarial review — Italian, family F1 (OneCable · Infinity · Infinity Lite)

**Branch:** `lang-expansion-de-fr-it` · **Date:** 2026-08-11
**Scope:** 18 Italian pages read side by side with their EN and NL twins
(`it|en|nl /manuals/onecable/` ×8, `/manuals/infinity/` ×5, `/manuals/infinity-lite/` ×5 = 54 files).
**Binding reference:** `translations/glossary-it.md` (all sections), `translations/dnt.json`.

Posture: hostile. The pass hunts for meaning drift against **both** sources, register breaches,
glossary-lock violations, calques, number/unit corruption, weakened safety negations and broken
anchors. Items the brief lists as known non-defects were checked and deliberately **not** filed;
they are itemised in the scrutiny-evidence section so the exclusion is auditable.

---

## Findings

| # | File : line | Quote | Problem | Severity | Proposed fix |
|---|---|---|---|---|---|
| 1 | all 18 F1 pages, frontmatter — e.g. `it/manuals/onecable/index.mdx:1-5` | `---`<br>`title: "Manuale Screenmate OneCable"`<br>`description: …`<br>`icon: "book-open"`<br>`---` | **No cross-language `<lang>_link` key on any Italian page**, and no `it_link` on the EN/NL twins. `scripts/generate_language_links.py` documents that every product tab in `docs.json` is `hidden: true`, so Mintlify **cannot infer** a page's counterpart — the explicit key is load-bearing. Verified: `python scripts/generate_language_links.py --check` → `310 file(s) would change: 1116 added`. The Italian pages ship unreachable from the switcher and offer no way back to EN/NL. (Branch-wide: DE and FR have the same gap; it still blocks IT delivery.) | **High** | Run `python scripts/generate_language_links.py` from the repo root and commit the 310-file diff; add `--check` to CI so the gap cannot recur. |
| 2 | `it/manuals/onecable/display-settings.mdx:32`<br>`it/manuals/infinity-lite/display-settings.mdx:57` | `Fai clic su 'Ridimensionamento' e impostalo su 150% per una visualizzazione più grande di testo ed elementi.` | Deviates from the **§9.10 locked** body string for the quoted EN variant (`Click on 'Scale' and set it to 150% for a larger display of text and elements.`), whose target is `… per visualizzare testo ed elementi più grandi.` The shipped wording is also a word-for-word calque of the NL `voor een grotere weergave van tekst en elementen` — nominalised where Italian prefers the verb. §9.10 exists precisely to keep this checksum-identical chapter identical across products. | **Medium** | Replace with the locked string: `Fai clic su 'Ridimensionamento' e impostalo su 150% per visualizzare testo ed elementi più grandi.` (2 occurrences). |
| 3 | `it/manuals/onecable/display-settings.mdx:28,48`<br>`it/manuals/infinity/display-settings.mdx:24,47`<br>`it/manuals/infinity-lite/display-settings.mdx:17,53,72` | `… e scegli 'Capovolto' per correggere il problema.` | 7 occurrences of `per correggere il problema` where §9.10 locks `per correggerlo` (both the `Display orientation`/`Flipped` row and the `Rotation`/`Standard` row). Internally consistent, meaning intact — but it is a locked string, and the lock is binding per the glossary preamble. | **Medium** | Either normalise all 7 to `… per correggerlo.`, or amend §9.10 to the shipped wording and record the change in §11. Do not leave glossary and corpus disagreeing. |
| 4 | `it/manuals/infinity-lite/index.mdx:15` | `Si collega tramite USB-C o HDMI ed è pensata per l'uso plug-and-play …` | Gender-agreement drift. The implicit subject of the second sentence is `lo Screenmate Infinity Lite` (m., §3.2); `è pensata` agrees instead with `un'estensione` from the previous sentence, so the paragraph switches gender mid-flow. EN: "It connects … and is designed for …". | **Low** | `… ed è pensato per l'uso plug-and-play …`, or recast: `… ed è progettato per l'uso plug-and-play …`. |
| 5 | `it/manuals/infinity/index.mdx:15` | `… si aggancia dietro il tuo laptop e ti dà due schermi in più in una sola volta.` | Calque of EN "at once". Italian `in una sola volta` = "in one go / in a single operation" (an action count), whereas EN/NL mean *simultaneously* ("twee extra schermen tegelijk"). Slight meaning drift against both sources. | **Low** | `… e ti dà due schermi in più contemporaneamente.` (or drop the adverbial — `ti dà subito due schermi in più`). |
| 6 | `it/manuals/onecable/index.mdx:15` | `… progettato per aumentare la tua produttività aggiungendo due schermi aggiuntivi al tuo laptop …` | `aggiungendo … aggiuntivi` — same root twice in four words; EN "adding two extra screens" has no such echo. Reads as machine output in the product's first descriptive sentence (highest-visibility copy on the page). | **Low** | `… aggiungendo due schermi in più al tuo laptop …`. |
| 7 | `it/manuals/onecable/installation-windows.mdx:47` vs `it/manuals/infinity/display-settings.mdx:68,74` and `it/manuals/infinity-lite/display-settings.mdx:93,100` | `… della tua versione di Windows – per Windows 10 o 11 …` (en dash) vs `… dispositivo di output **Screenmate** — è indicato come …` (em dash) | §10 dash policy applied two different ways to the *same* input: an EN **body-copy** em dash is downgraded to an en dash in one file and preserved as an em dash in four others. One of the two treatments is wrong whichever reading of §10 wins. | **Low** | Pick one and sweep F1: either preserve EN body em dashes everywhere (structural parity, matches 4 of 5 sites) — i.e. restore `—` at `installation-windows.mdx:47` — or downgrade all five to ` – `. Record the ruling in §10. |
| 8 | `it/manuals/onecable/display-settings.mdx:28` | `… vai su 'Display orientation' ('Orientamento dello schermo') e scegli 'Capovolto' per correggere il problema.` | Mixed label treatment inside a single sentence: the setting name keeps the EN token with an Italian gloss (§8 pattern, matching the English-language screenshots directly above), but its *value* is given in Italian only. A reader following the English-UI screenshots looks for `Flipped` and finds no such word. Not a translator error — §9.10 currently prescribes the bare Italian — but the page is internally incoherent. | **Low** (glossary-level question) | Extend the §8 parenthetical pattern to the value: `… e scegli 'Flipped' ('Capovolto') …`. Needs a §9.10 amendment, so route with finding 3. |

**Counts:** 1 High · 2 Medium · 5 Low. No Critical.

### Source-side observations (no Italian defect — do not "fix" in IT)

| File : line | Observation |
|---|---|
| `it/manuals/infinity-lite/installation.mdx:9` | `… per posizionare in sicurezza entrambi gli schermi aggiuntivi dietro il laptop.` The Infinity Lite ships **one** screen (`index.mdx`: "un display portatile in più"). EN says "both extension screens", NL "beide uitbreidingsschermen" — the Italian mirrors both sources faithfully. Fix belongs on the EN/NL side. |
| `it/manuals/infinity-lite/controls.mdx:19` | `… oppure serve per l'alimentazione quando è la porta HDMI a trasportare il segnale video.` The Lite has no HDMI port — video arrives on the third USB-C via the HDMI→USB-C cable. Mirrors EN verbatim. EN-side correction. |
| `it/manuals/infinity/controls.mdx:9` | EN "The layout is mirrored" vs NL "De indeling is identiek" — the sources disagree. Italian follows EN with `speculare`, which is the ruling under R10. Correct as shipped. |

---

## Scrutiny evidence

### Coverage

All 54 files read in full, IT against EN and NL line by line:

- `onecable/`: `index`, `installation`, `installation-windows`, `installation-mac`, `display-settings`, `controls`, `troubleshooting`, `safety`
- `infinity/`: `index`, `installation` (174 lines), `display-settings`, `controls`, `safety`
- `infinity-lite/`: `index`, `installation`, `display-settings`, `controls`, `safety`

### Mechanical sweeps run (all over the 18 IT pages)

| Check | Regex / method | Result |
|---|---|---|
| Courtesy pronouns & set phrases (§1.5) | `\bLei\b\|\bSuo\b\|\bSua\b\|\bSuoi\b\|\bSue\b\|\bVostr[oaie]\b\|La preghiamo\|Le consigliamo\|Si prega di\|Per favore\|\bvoglia\b` | **0 hits** — clean |
| Courtesy imperatives (§1.5) | `\b(prema\|colleghi\|selezioni\|scelga\|vada\|faccia\|apra\|inserisca\|rimuova\|verifichi\|controlli\|scarichi\|installi\|riavvii\|tenga\|prenda\|segua\|posizioni\|sollevi\|ruoti\|pieghi\|spenga\|accenda\|utilizzi)\b` | 1 hit, **false positive**: `installation-windows.mdx:31` `non appena colleghi lo Screenmate` = `tu` indicative, whitelisted by §1.5 |
| `può` / `deve` / `usi` (§1.5 whitelist) | `\b(può\|deve\|usi)\b` | 10 hits, **all whitelisted**: thing-subjects (`Questa porta … può ricevere`, `lo Screenmate può essere usato`, `La striscia di silicone … deve combaciare`, `lo schermo e il supporto devono restare paralleli`) or `usi` as 2nd-person indicative (`quando usi Power Delivery`). No reader-as-subject modal anywhere. |
| Thousands-comma corruption (§4.2 — the 1000× error) | `[0-9],[0-9]{3}` | **0 hits**. `1820 grammi`, `1552 grammi`, `2390 grammi`, `1261 grammi`, `1920×1200`, `1920×1080`, `1000:1` all separator-free as locked |
| Period-as-decimal survival (§4.2) | `[0-9]\.[0-9]` | 5 hits, **all §4.3-whitelisted or non-prose**: `RacerDisplayDriver-2024.9.13-en` (protected filename) and 4 inline `<svg>` path coordinates |
| Decimal commas converted | manual diff of every spec table | `39 × 24 × 2,5 cm`, `34,5 × 22 × 2,5 cm`, `36,1 × 21,6 × 4,5 cm`, `36,2 × 20,9 × 1,6 cm`, `15,6"`, `3,5 mm` — all correct; `x` → `×` per §4.1 |
| SI spacing & closed-up forms (§4.1) | manual | `10 W`, `45 W`, `5 V/2 A`, `DC 5 V/3 A`, `±2 V`, `-20 °C`, `60 °C`, `60 Hz`, `25 ms`, `350 cd/m²` spaced; `150%`, `100% sRGB`, `72% NTSC`, `120% sRGB`, `90°`, `235°`, `360°`, `178°`, `172°` closed up. Divergence from NL is the accepted §11.1(5) per-language ruling — not filed. |
| Cable-chain lock (§2.5) | `cavo (USB\|HDMI\|Mini)\S* a \|ad (USB\|HDMI)\|verso USB\|cavo da \S+ su ` | **0 violations**. Every chain reads `cavo da X a Y`: `cavo da USB-C a USB-C`, `2 cavi da USB-A a USB-C`, `cavo da HDMI a USB-C`, `cavo doppio da USB-A a USB-C`, `cavo da USB-A o USB-C a USB-C`. No `ad USB-C`, no hyphen chains, no `verso`. |
| §6 trap terms | `connessione\|clicca\|menù\|i drivers\|il Screenmate\|del Screenmate\|al Screenmate\|sul schermo\|il schermo` | **0 hits**. `collegamento` throughout, `fai clic su` throughout, `il driver`/`i driver` invariable, `lo/dello/allo Screenmate` correct everywhere |
| Typography (§3.3, §10) | `’\|qual'è\|perche'\|\be' \b` | **0 hits** — straight ASCII apostrophes only; `è`, `più`, `può`, `luminosità`, `nitidezza`, `perché` all real accented characters |
| Untranslated leftovers | English-function-word sweep over prose, `alt`, `<p>`, `<Tab title>` | **0 leftovers**. Residual English is all DNT: `Power Delivery`, `System Settings`/`Privacy & Security`/`Screen & System Audio Recording`, `UsbDisplay`, `RacerUSB`, `DRIVERS (D:)`, `Win10&11`, `S6-L`/`S6-R`, `Speaker (Realtek(R) Audio)`, `HD Audio Driver for Display Audio`, `DisplayPort` |
| Anchors | `](#…)` in IT vs heading slugs | 1 anchor in F1: `infinity/controls.mdx:19` → `#menu-a-schermo-osd`; target `## Menu a schermo (OSD)` at line 29 → slug `menu-a-schermo-osd`. **Resolves.** (EN twin `#on-screen-menu-osd` likewise.) |
| Heading inventory | all 91 `##`/`###` headings extracted and matched 1:1 against EN | **No structural drift, no missing/extra heading, no title-case leakage.** Every heading matches its §9.1/§9.3/§9.4/§9.5 locked target, incl. `Porte e pulsanti`, `Porte e comandi`, `Menu a schermo (OSD)`, `Menu / Selezione / Conferma`, `Pulsante sinistro "Min"`, `Jack per cuffie da 3,5 mm`, `Scegli i cavi`, `Come riporre il prodotto`, `Come richiudere lo schermo`, `Apertura degli schermi`, `Configurazioni possibili`, `Doppio schermo — davanti e dietro in orizzontale`, `Fasi di installazione`, `Scarica i driver` (R3), `Se il driver non funziona`, and all 5 FAQ questions from §9.7 verbatim |
| JSX-embedded strings (§9.9) | every `<Tab title>`, `<Card>`, `<p>`, `<a>`, `<video>` fallback | `<Tab title="OneCable 16&quot;">` / `14&quot;` preserved escaped; `Scarica i driver per Windows`, `Scarica per macOS`, `Custodia protettiva`, `2 cavi da USB-A a USB-C`, `Cavo da USB-C a USB-C`, `Chiavetta USB (con driver)`, `Il tuo browser non supporta il tag video.` (×5 in F1), `Vista orizzontale`/`Vista verticale`/`Combinazione verticale e orizzontale`/`Vista separata`/`Appoggia lo schermo sul supporto singolo`/`Il supporto ruota di 360°` — **all match the locked renderings**. `className`/`href`/`src`/`icon` untouched. |
| Callout lead-ins (§9.9) | `\*\*(Nota\|Importante\|Attenzione\|Suggerimento\|Benvenuto!\|Informazioni importanti)` | 11 hits, all correct against their EN twins (`Note:`→`Nota:`, `Important:`→`Importante:`, `Tip:`→`Suggerimento:`, `Important Information:`→`Informazioni importanti:`, `Welcome!`→`Benvenuto!`); bold markers and colons carried over position-for-position |
| Recurring display-settings prompts (§9.10) | all 11 sites | Prompts themselves **all conform**: `Schermo capovolto?` ×4, `Uno schermo è capovolto?` ×3, `Vuoi estendere lo spazio di lavoro?` ×4, `Vuoi più spazio a schermo?` ×4 (collapsing "Need more overview?" / "Want more on-screen space?"), `Lavori con tre schermi?` ×1. Only the two **bodies** drift → findings 2 and 3. |

### Safety-negation audit (line by line, all three `safety.mdx` + every `<Warning>`)

Every prohibition survives translation with the negation intact and in the §1.2 form
(`non` + infinitive):

- `Non toccare il dispositivo con le mani bagnate e non usarlo in ambienti umidi.` — both negations preserved (EN doubles them too)
- `Non far cadere il monitor` (not the calque `non lasciare cadere giù`), `Non usare liquidi o detergenti aggressivi`, `Non usare oggetti appuntiti sullo schermo o attorno a esso`, `non premere sugli schermi`, `Non ruotare gli schermi oltre l'angolo massimo`
- EN's positive `Keep ventilation openings clear` correctly inverts to the §6-mandated
  `Non ostruire le aperture di ventilazione` — stronger, not weaker
- No modal softening: `deve`/`devono` appear only with thing-subjects; no `dovresti`, no
  `si consiglia di non`, no dropped `mai`
- Electrical limits transferred exactly: `tra 5 V e 20 V (con una tolleranza di ±2 V)`,
  `fonte di alimentazione da 5 V`, `alimentatore da almeno 45 W`, `-20 °C` / `60 °C`
- `<Warning>` / `<Note>` component choice matches EN 1:1 on every page (Infinity Lite
  installation: 5 `<Warning>`, 2 `<Note>` on both sides)

### Register audit (§1)

Uniform informal `tu` across all 18 pages. Imperatives are the irregular `tu` forms the glossary
demands — `Vai`, `Fai clic`, `Apri`, `Estrai`, `Tieni premuto`, `Abbi cura`, `Rimuovi`, `Spegni`,
`Sgancia`, `Riponi`, `Appoggia`, `Scegli`, `Assicurati`. `Please` is dropped everywhere
(`Leggi attentamente le indicazioni seguenti`, never `La preghiamo` / `Per favore`).
Possessives follow §1.3: `il tuo laptop` kept, `lo schermo` / `la confezione` / `le specifiche del
dispositivo` de-possessivised. No impersonal-infinitive appliance style anywhere.

### Known non-defects — checked and deliberately not filed

| Item | Where seen | Why not filed |
|---|---|---|
| `**This PC** ('Questo PC')` over Dutch-Windows screenshots | `onecable/installation-windows.mdx:46,53` | Brief-listed non-defect; matches the §8 parenthetical pattern |
| `ricarica inversa (reverse charging)` gloss | `onecable/controls.mdx:30,45`, `installation.mdx:49`, `troubleshooting.mdx:37` | Locked with client sign-off (§11.1(3)) |
| `'Duplicato'` (EN `Mirrored`) beside `'Capovolto'` (EN `Flipped`) on one page | `infinity-lite/display-settings.mdx:53` vs `:17` | Infinity Lite mirrored quirk, client-flagged; IT follows the §8 `Mirrored → Duplicato` row and mirrors EN's own drift |
| SI spacing divergence from NL (`45 W` vs `45W`) | corpus-wide | Accepted per-language ruling §11.1(5) |
| `Pulsante di accensione e ritorno` (R8) | not present in F1; verified absent | n/a for this family |
| `speculare` for EN "mirrored" | `infinity/controls.mdx:9` | R10 — correct as shipped |
| 3rd-person descriptive verbs in button lists (`riduce`/`aumenta la luminosità`) | `onecable/controls.mdx:56-57` | Matches the §9.4 locked pattern `Pulsante + (aumenta la luminosità)`, even though EN/NL use imperatives |
| Double quotes around UI strings where EN uses them (`**"Capovolto"**`) | `infinity/display-settings.mdx:24,47` | §10 gives structural parity with EN precedence over the single-quote default |

### Verdict

The Italian F1 set is terminologically and numerically sound — the high-risk classes (thousands
separators, decimal commas, cable chains, courtesy register, safety negations, heading locks,
JSX-embedded strings, anchors) are **clean under both manual and mechanical inspection**. What it
is missing is the cross-language plumbing (finding 1, a delivery blocker) and byte-fidelity to two
§9.10 locked strings (findings 2–3). The remaining five are low-severity polish and one glossary
question routed back to the glossary owner.
