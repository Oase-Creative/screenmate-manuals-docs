# Adversarial review — Italian, family F4 (expand, one-4k, one-4k-oled)

**Branch:** `lang-expansion-de-fr-it` · **Scope:** 16 pages — `it/manuals/expand/` (6), `it/manuals/one-4k/` (5), `it/manuals/one-4k-oled/` (5), each read against its `en/` and `nl/` counterpart.

**Posture:** adversarial. The mechanical gate (`scripts/verify_translation.py --targets it`) reports **0 FAIL, 0 WARN** on this tree, and the glossary greps of §1.5, §2.5, §4.2 and §4.3 are all clean. Every finding below is something that gate structurally cannot see: it compares each target page against **en**, never sibling IT pages against each other, and its `DEDUPE_GROUPS` covers only `safety.mdx` and `display-settings.mdx`. The dominant defect class in F4 is exactly what falls through that hole — **EN-identical chapters that the Italian re-translated twice**.

Known non-defects listed in the brief (expand `alt="…steps 1 through 6"`, the EN Color Gamut/Accuracy split, EN-verbatim `{/* TODO */}` comments per §10, bodyless `### Porta USB-A`, Dutch screenshots) were checked and are excluded from the table.

---

## Findings

| # | Sev | Page(s) : line | Class | Finding |
|---|---|---|---|---|
| F4-01 | **High** | `it/manuals/one-4k/installation.mdx:9,11,15` vs `it/manuals/one-4k-oled/installation.mdx:9,11,15` | shared-chapter divergence / consistency | The `## Per iniziare` chapter is **byte-identical in EN** between the two products (verified by diff after frontmatter strip) but Italian ships **3 of 7 bullets in two versions**: `con i cavi corretti` / `con i cavi giusti`; `…e regola le impostazioni schermo` / `…e adatta le impostazioni schermo`; `Quando viene ricevuto un segnale tramite la porta USB-C` / `Quando riceve un segnale dalla porta USB-C`. The heading itself is consistent — the body is not. `nl` and `fr` keep this chapter identical across the two products; `de` diverges too (out of F4 scope, but same root cause). The third variant also shifts voice: EN is impersonal passive ("When a signal is received via…"), the OLED page promotes `lo Screenmate` to subject. |
| F4-02 | **High** | `it/manuals/one-4k/controls.mdx:13,15,23,39` vs `it/manuals/one-4k-oled/controls.mdx:13,15,23,39` | shared-chapter divergence | EN `controls.mdx` for the two products differs in **exactly one line** (the `USB-A Port` body, replaced by the TODO comment on OLED). Italian diverges in **five further places**: `Questo unico collegamento … su un solo cavo` / `Questo singolo collegamento … con un solo cavo`; `per trasportare il segnale video` / `per trasmettere il segnale video`; `Usala insieme al cavo USB-C e all'alimentatore in dotazione.` / `Usala con il cavo USB-C e l'alimentatore in dotazione.`; `Spia LED che indica lo stato dell'alimentazione e del segnale.` / `Spia LED di stato per l'alimentazione e il segnale.`; plus the `+ / −` bullets (F4-03). Machine diff: EN 2 changed lines, IT 14. |
| F4-03 | Medium | `it/manuals/one-4k/controls.mdx:47-48` | meaning drift (omission) | EN: "opens the **brightness shortcut menu** in general mode". IT one-4k: `apre la scorciatoia per la luminosità in modalità generale` — the *menu* is dropped, so the reader is told the button applies a shortcut rather than opening a menu of them. `one-4k-oled/controls.mdx:47-48` has the correct `apre il menu delle scorciatoie per la luminosità`. **one-4k is the defective side**; align it to OLED (this also resolves part of F4-02). |
| F4-04 | Medium | `it/manuals/one-4k/osd.mdx:30` vs `it/manuals/one-4k-oled/osd.mdx:30` | shared-chapter divergence | EN `### OSD Lock` body is identical across the two products; Italian ships three differences in one sentence: `pulsanti anteriori` / `pulsanti frontali`, `l'OSD potrebbe essere bloccato` / `il menu OSD potrebbe essere bloccato`, and `Tieni premuto per **10 secondi** il pulsante sopra…` / `Tieni premuto il pulsante sopra … per **10 secondi**`. §3.2 prefers `il menu OSD` over bare `l'OSD`, so the OLED wording is the one to keep. |
| F4-05 | Medium | `it/manuals/one-4k/index.mdx:15` vs `it/manuals/one-4k-oled/index.mdx:15` | consistency + register/style | Two problems on the same EN-identical closing sentence ("It connects via USB-C or HDMI and supports both video and power over a single USB-C cable on compatible devices"): (a) rendered `supporta … su un solo cavo USB-C con i dispositivi compatibili` on one-4k but `trasporta … con un solo cavo USB-C`, with `sui dispositivi compatibili` fronted, on OLED; (b) the product gloss inverts head order — `monitor portatile 4K UHD da 15,6"` (one-4k) vs `monitor portatile da 15,6" 4K UHD` (OLED). The OLED order makes `da` appear to govern `15,6" 4K UHD` as one spec and reads worse; §2.4 attaches `da` to the measurement alone. |
| F4-06 | Medium | `it/manuals/expand/installation.mdx:59, 74` | typography consistency | `**Nota:** La porta HDMI…` capitalises the first word after the bold run-in colon. These are the **only 2 such instances in the entire `it/manuals/**` tree — the other 156 bold run-ins all lowercase** after the colon, including `**Importante:** assicurati` at line 45 of this very file. The §7.3 glossing pattern is lowercase. Two-character fix, but it is a visible in-page inconsistency. |
| F4-07 | Medium | `it/manuals/expand/display-settings.mdx:28, 32, 48` | glossary §9.10 lock violation | §9.10 declares these bodies locked and byte-identical corpus-wide, and gives `…per correggerlo.` and `…per visualizzare testo ed elementi più grandi.`. The shipped pages instead read `…per correggere il problema.` (×2) and `…per una visualizzazione più grande di testo ed elementi.`. The pages *are* internally consistent (all four IT display-settings share body hash `24c9126006`), so this is a glossary-vs-shipped mismatch, not page drift — but one of the two must move before sign-off, or §9.10 stops being a usable lock. (The EN-label-plus-IT-gloss slot form, `'Scale' ('Ridimensionamento')`, is correct per §8 and is **not** part of this finding.) |
| F4-08 | Low | `it/manuals/expand/index.mdx:15`; `expand/installation.mdx:74`; `one-4k/installation.mdx:45,67`; `one-4k-oled/index.mdx:15`, `installation.mdx:61` | typography consistency (§10) | The EN body em dash gets **three different treatments inside one family**: converted to en dash `–` (expand/index), replaced by a comma (expand/installation), and preserved as `—` (both One 4K pages, 5×). §10 says to avoid the em dash in body copy and use `–` with spaces or a comma, so the One 4K pages are the outliers, but the real defect is that F4 does not pick one rule. Counts: EN `expand/index` 2 em → IT 0 em / 4 en; EN `one-4k/installation` 3 em → IT 3 em. |
| F4-09 | Low | `it/manuals/expand/safety.mdx:14` (shared chapter — all 7 IT safety pages) | safety-text weakening (adverb drop) | EN item 4: "Make sure the power outlet is **properly** grounded and suitable for the correct amperage." IT: `Assicurati che la presa di corrente sia dotata di messa a terra e adatta all'amperaggio corretto.` — `properly` is dropped, turning a quality requirement into a presence check. NL retains it (`goed geaard`). Negation structure elsewhere in the chapter is intact (items 8–11 all carry `Non …` + infinitive per §1.2), so this is the only weakening in the safety text. Fix propagates to all 7 pages — re-verify the group hash afterwards. |
| F4-10 | Low | `it/manuals/expand/controls.mdx:9` vs `one-4k/controls.mdx:9`, `one-4k-oled/controls.mdx:9` | consistency | Identical EN opener ("This section provides an overview of all physical ports and control buttons on the Screenmate X.") yields `…di tutte le porte fisiche e **di tutti i** pulsanti di comando…` on expand but `…di tutte le porte fisiche e **dei** pulsanti di comando…` on both One 4K pages. Boilerplate; pick one. |
| F4-11 | Low | `it/manuals/expand/osd.mdx:61` | style (echo) | `riduce la quantità di luce blu emessa dallo schermo per **ridurre** l'affaticamento degli occhi` — `riduce … ridurre` in eleven words. §6 locks the tail (`per ridurre l'affaticamento degli occhi`), so the head verb is what should change (`attenua` / `limita`). Cosmetic, but it is the one sentence in the F4 OSD chapter that reads translated. |
| F4-12 | Info (out of F4 scope) | all 62 `it/**/*.mdx` | build / language switcher | **0 of 62** Italian pages carry a `*_link` frontmatter key (nor do any `de/` or `fr/` pages). `python scripts/generate_language_links.py --check` reports pending edits branch-wide, including `en/` and `nl/`, so this is a branch-level mechanical step that has not been run, not an Italian translation defect. Recorded here only because the switcher cannot reach the IT pages until it is. |

**Counts:** 0 Critical · 2 High · 5 Medium · 4 Low · 1 Info.

---

## Scrutiny evidence

Everything below was run or read; each item states what would have counted as a defect and what was actually observed.

### 1. Shared-chapter checksums — expand vs the group (onecable canonical) — PASS

`body_hash()` from `scripts/verify_translation.py` (frontmatter stripped, trailing whitespace normalised) over both dedupe groups, in all five languages:

| Chapter | Group | IT hash | Result |
|---|---|---|---|
| `safety.mdx` | onecable, lite, lite-144hz, flip, **expand**, one-4k, one-4k-oled | `afeef247c5` × 7 | identical — expand matches onecable |
| `display-settings.mdx` | onecable, dual-flip, flip, **expand** | `24c9126006` × 4 | identical — expand matches onecable |

`en` (`b7fdd138bd` / `739ae20927`), `nl`, `de`, `fr` are each internally identical too. **No divergence — the critical-severity condition named in the brief does not occur.** Note that this is precisely the pair of chapters the mechanical verifier does police; the divergences that *were* found (F4-01, F4-02, F4-04) are all in chapters absent from `DEDUPE_GROUPS`.

### 2. Cross-product body comparison — where the High findings came from

Normalised diff (frontmatter stripped, `<img …>` collapsed, product name and slug folded to a token) of one-4k against one-4k-oled, per page, in EN and IT. A page where IT diverges materially more than EN is by construction a translation-side defect:

| Page | EN diff lines | IT diff lines | Verdict |
|---|---|---|---|
| `index.mdx` | 16 | 16 | equal count, but two of the changed lines are EN-identical sentences translated twice → **F4-05** |
| `installation.mdx` | 10 | 16 | 6 excess; 3 are the `## Per iniziare` bullets → **F4-01** (remainder are legitimate, EN-driven) |
| `controls.mdx` | **2** | **14** | 12 excess → **F4-02 / F4-03** |
| `osd.mdx` | 2 | 4 | 2 excess (EN's 2 are the differing TODO comments, correctly mirrored) → **F4-04** |
| `safety.mdx` | 0 | 0 | clean |

Cross-checked against the other languages: `nl` and `fr` keep the `## Getting Started` bullets identical across the two products, `de` does not. Italian is not alone, but it is defective.

### 3. The nine sentences one-4k-oled reuses from `it/lite/installation.mdx` — VERIFIED (claim understates)

Paragraph-block set comparison of `one-4k-oled/installation.mdx` against `lite/installation.mdx`, run in EN and IT and compared:

- EN: 15 blocks on the OLED page, **11 shared verbatim** with lite; 4 not shared.
- IT: 15 blocks, **11 shared verbatim**; 4 not shared.
- The 4 non-shared blocks are the **same 4 in both languages** (the `Per iniziare` bullet list, the product-name sentence, the §3 opener where EN OLED omits lite's `Nota:` sentence, and the additional-power sentence where EN OLED ends in `.` and lite in `:` — IT mirrors both punctuation marks correctly).

At sentence granularity: 17 EN strings shared verbatim, 18 IT (the extra is a heading-split artefact of the tokenizer, not a real difference). Spot-verified verbatim, including `**Alimentazione:** collega l'alimentatore in dotazione a una presa di corrente e collegalo al monitor con il cavo da USB-C a USB-A.` (×2), `**Collegamento del dispositivo HDMI:** usa il cavo da Mini-HDMI a HDMI…`, and `Quando entrambi i collegamenti sono stati effettuati…` (×2). **Every EN-shared string is IT-shared verbatim. The "nine" figure understates the reuse; nothing is broken.** Contrast with F4-01: reuse discipline against `it/lite` is perfect, while reuse discipline against the sibling `it/one-4k` is not.

### 4. Numbers and units — PASS

| Target | Check | Result |
|---|---|---|
| `100.000:1` in OLED **prose and spec row** | grep `100[.,]000` | 2 hits, both `100.000` — `one-4k-oled/index.mdx:15` (prose) and `:27` (Rapporto di contrasto row). §4.1 six-digit period form, §11.1 ruling 4. ✓ |
| `3,5 mm` jack heading | grep `3[.,]5\s?mm` | `one-4k/controls.mdx:29` and `one-4k-oled/controls.mdx:29`, both `### Jack per cuffie da 3,5 mm` — matches §9.4 including the `da`. ✓ |
| `15,6"` internal consistency (divergence itself LOCKED per §4.5, so only inconsistency is in scope) | all size tokens in F4 | 11 occurrences, **every one comma-form**: frontmatter descriptions, `<Note>` welcome lines, prose, the `Dimensioni schermo` rows and the `Nome del prodotto` row (`Screenmate One 4K 15,6"`), plus `<Tab title="Expand 15,6&quot;">` / `14&quot;`. No mixed `15.6`/`15,6` anywhere. **No inconsistency to flag.** ✓ |
| English comma-thousands surviving (§4.2, the 1000× error) | `\d,\d\d\d` | 0 hits. `1750 grammi`, `1450 grammi`, `860 grammi`, `1920 × 1080`, `3840 × 2160` all unseparated. ✓ |
| Period-decimal surviving (§4.2) | `\d\.\d` | 20 hits, **all inside `src=` image paths** (`Expand%2015.6`), which §4.3 forbids localising. 0 in body copy. ✓ |
| SI spacing (§4.1) | manual | `5 V/2 A`, `±2 V`, `-20 °C`, `60 °C`, `300 cd/m²`, `25 ms`, `60 Hz`, `6 mm`, `10 secondi` all spaced; `150%`, `178°`, `0° – 235°` per the closed-up/spaced rules. ✓ |
| Quantity prefix (§4.1) | manual | `2 cavi da USB-C a USB-C`, `6 clip protettive`, `2 USB-A e 2 HDMI` — `x`/`×` correctly dropped. ✓ |

### 5. Register §1.5 — PASS (all grep hits are documented false positives)

| Grep | Hits | Adjudication |
|---|---|---|
| `Lei\|Suo\|Sua\|Suoi\|Sue\|Vostr…\|La preghiamo\|Si prega di\|Per favore` | **0** | clean |
| courtesy imperatives (`prema\|colleghi\|vada\|faccia\|…`) | 4 × `colleghi` | all are `non appena lo colleghi` / `non appena colleghi il caricabatterie` — 2nd-person-singular **present indicative**, the correct `tu` form. False positive, exactly as §1.5 anticipates. |
| `può\|deve\|voglia` | 7 | every one has a **thing** as subject — `lo Screenmate Expand si può collegare`, `la porta HDMI … lo Screenmate deve essere collegato`, `il cavo USB-A può`, `il monitor deve essere alimentato`, `il tuo telefono o tablet deve avere`. §1.5 whitelist. |
| §1.2 irregular imperatives | manual | `Estrai`, `Apri`, `Appoggia`, `Solleva`, `Premi`, `Tieni premuto`, `Scegli`, `Vai`, `Fai clic`, `Assicurati`, `Abbi cura`, `Rimuovi`, `Spegni`, `Pulisci` — all correct `tu`; no infinitive-instruction style anywhere. |
| §1.2 negative imperative = `non` + infinitive | manual | `Non premere`, `Non ruotare`, `Non usare`, `Non toccare`, `Non far cadere`, `Non ostruire` — 6/6 correct. |

### 6. Safety negation integrity — PASS except F4-09

All 14 numbered items read line-by-line against EN and NL. Items 8, 9, 10 preserve their negations one-for-one; item 11 correctly converts EN's positive "Keep ventilation openings clear" into the §6-locked negative `Non ostruire le aperture di ventilazione`; item 7's `Evita … per evitare` echoes EN's own "Prevent … to prevent". The intro uses the §6-locked `Leggi attentamente le indicazioni seguenti` and `prolungano la durata` (not the §6-flagged calque `durata della vita`). The **only** weakening found is the dropped `properly` in item 4 — F4-09.

### 7. `## Per iniziare` consistency between one-4k and one-4k-oled — HEADING PASS, BODY FAIL

Heading string is identical on both pages (`one-4k/installation.mdx:7`, `one-4k-oled/installation.mdx:7`) and matches the §9.3 lock `Getting Started → Per iniziare`. The chapter **body** does not — see F4-01.

### 8. Glossary term compliance — PASS

| §  | Grep / check | Result |
|---|---|---|
| §2.5 | every `cav[oi] …` occurrence in F4 (62 hits) enumerated | all use the locked `cavo da X a Y` chain — `cavo da USB-C a USB-C`, `cavo da USB-C a USB-A`, `cavo da Mini-HDMI a HDMI`, `2 cavi da USB-C a USB-C`. **0** rejected variants (`cavo USB-C a USB-C`, `cavo USB-C/USB-C`, `verso`, hyphen chains). |
| §2.5 | `\bad (USB\|HDMI)` — the euphonic-`d` lock | 0 hits |
| §2.2 | `Mini HDMI` unhyphenated | 0 hits; all 6 occurrences are `Mini-HDMI` even where EN writes `Mini HDMI` — correct per the §2.2 note |
| §3.1 | `il\|del\|al\|sul\|nel Screenmate`, `il schermo`, `i schermi` | 0 hits; `lo Screenmate` / `dello Screenmate` / `allo Screenmate` / `gli schermi` throughout, and `il tuo Screenmate` correctly switches allomorph before `tuo` |
| §3.2 | `i drivers`, `menù`, `il porta`, `bottone` | 0 hits each |
| §6 | `connession…`, `clicc…` | 0 hits; `collegamento` / `fare clic su` used throughout |
| §3.3 | typographic apostrophe `’`, `qual'è`, `perche'`/`piu'`/`puo'` | 0 hits; straight ASCII `'` everywhere (`dell'OSD`, `l'alimentazione`, `un'opzione`) |
| §10 | sentence-final double space, NBSP | 0 hits |
| — | Dutch leakage (`scherm`, `kabel`, `knop`, `instellingen`, `Beeldscherm…`) | 0 hits in IT prose; the OS-label glosses are Italian per §8 (`('Impostazioni schermo')`, `('Identifica')`, `('Ridimensionamento e layout')`) |

### 9. Headings, frontmatter and JSX strings — PASS

All 70 headings in F4 listed and checked against §9.3–§9.6: every one is sentence case and matches its locked target (`Uso dell'OSD`, `Impostazioni OSD`, `1. Retroilluminazione` … `6. Altro`, `Comandi e menu OSD`, `Blocco dell'OSD`, `Scorciatoie per volume e luminosità`, `Porta USB-C (alimentazione e video)`, `Pulsante Menu (accensione / OSD)`, `Jack per cuffie da 3,5 mm`, `Fasi di installazione`, `Cappuccio protettivo`, `Scegli i cavi`, `Opzioni di collegamento`, `2. 1 USB-C, 1 HDMI e 1 USB-A`, `3. 2 USB-A e 2 HDMI`). All 16 frontmatter `title`/`description` pairs match §9.1/§9.2 verbatim, including the `{Prodotto}` patterns. `icon` values untranslated. `<Tab title="Expand 15,6&quot;">` keeps the `&quot;` escape per §9.9 (a literal `"` would break the build). §7.3 OSD glosses match the glossary row-for-row, including `**DCR (Dynamic Contrast Ratio):** attiva o disattiva il contrasto dinamico (ON / OFF).` and the §7.4 lowercase language list. `Your browser does not support the video tag.` → `Il tuo browser non supporta il tag video.` in both display-settings `<video>` blocks. OSD `alt` text uses one shape corpus-wide (`Menu OSD {Sezione}`, 6/6) — the fr R9 fix has no IT equivalent to make. Internal links all carry the `/it/` prefix (3/3).

### 10. Mechanical gate

```
$ python scripts/verify_translation.py --base en --targets it
0 FAIL, 0 WARN
```

Reproduced clean before and after this review; no file was modified by it.
