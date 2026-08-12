# Round 4 — Italian safety-chapter line alignment audit (IT vs EN)

**Date:** 2026-08-12
**Scope:** 6 file pairs (5 safety chapters + the canonical display-settings chapter), Italian vs
its English structural counterpart.
**Mode:** read-only. No `.mdx` file was modified by this audit.
**Method:** every content line (frontmatter `title` / `description`, heading, sentence, list item,
callout, image `alt`, video fallback string) was back-rendered from Italian into literal English and
compared against the aligned English line, checking meaning, severity/modality, restriction scope
(`solo` / `esclusivamente` attachment), negation scope, safety-bearing adverbs, numbers and units,
omissions/additions, and order of warnings.

**Reference authority:** `translations/glossary-it.md` is declared **binding** for every Italian
translation pass. Several renderings flagged below are glossary-locked; those are marked and the
remediation target is named (page vs. glossary).

---

## Headline result

| Severity | Count |
|---|---|
| **Critical** | **0** |
| **Major** | **1** |
| **Minor** | **4** |

No Italian line in any of the five safety chapters instructs the reader differently from the English.
The single Major finding is in `display-settings.mdx`, which is not a safety chapter.

---

## 1. `it/manuals/onecable/safety.mdx` vs `en/manuals/onecable/safety.mdx`

*(canonical body — byte-identical body shared by 7 products, see §7 propagation check)*

### Flagged lines

| EN line | IT line | Literal back-rendering of IT | Divergence | Severity |
|---|---|---|---|---|
| 11. `Keep ventilation openings clear and ensure sufficient air circulation to prevent overheating.` | 11. `Non ostruire le aperture di ventilazione e garantisci una circolazione dell'aria sufficiente per evitare il surriscaldamento.` | "Do **not obstruct** the ventilation openings and ensure sufficient air circulation to prevent overheating." | Positive requirement (`keep clear`) restated as a negative prohibition (`do not obstruct`). Truth-conditionally equivalent; no change to what the reader must do. **Glossary-locked** — `glossary-it.md` §6 line 676 lists `Keep ventilation openings clear` → `Non ostruire le aperture di ventilazione` as the ✓ correct rendering and rejects the literal `Tieni le aperture di ventilazione chiare`. Deliberate, not drift. | Minor |

### Coverage

**All 18 content lines of `it/manuals/onecable/safety.mdx` checked** (2 frontmatter strings + H2 +
2-sentence intro + 14 numbered items). The 4 cross-language link keys were verified structurally
(`de_link`/`en_link`/`fr_link`/`nl_link` present, all pointing to `…/onecable/safety`; no self-
referential `it_link` — correct per the language-switcher architecture).

Line-by-line notes on the items that carry the most weight:

- **Item 2** `Only use the included AC/DC adapter as power supply.` → `Usa esclusivamente
  l'alimentatore AC/DC in dotazione come alimentazione.` — `esclusivamente` sits immediately after
  the verb and governs the direct object; it restricts *which adapter*, exactly as EN `only` does.
  ✓
- **Item 8** `Clean the screen only with a dry, soft cloth.` → `Pulisci lo schermo solo con un panno
  asciutto e morbido.` — `solo` precedes `con`, restricting the instrument, matching EN `only with`.
  The following prohibition `Non usare liquidi o detergenti aggressivi` carries negation across both
  disjuncts. ✓
- **Item 9** — both conjuncts independently negated (`Non toccare… e non usarlo…`); EN's double
  negation preserved, no scope leak. ✓
- **Item 10** — `Non far cadere il monitor **e proteggi** lo schermo…`: the negation does *not* bleed
  into the second, affirmative imperative. ✓ (Matches glossary §6 line 664 locked form
  `Non far cadere il monitor`.)
- **Item 12** `Limit exposure to…` → `Limita l'esposizione a…` — modality preserved (limit, not
  prohibit). ✓
- **Item 14** `when not in use` → `quando non è in uso` (impersonal, matching EN). ✓

### Verdict

**PASS.** 1 Minor, glossary-sanctioned. No action required on the page.

---

## 2. `it/manuals/dual-flip/safety.mdx` vs `en/manuals/dual-flip/safety.mdx`

The EN body is textually identical to `onecable/safety.mdx` except that the 14 items are rendered as
a bulleted list instead of a numbered list; the IT body mirrors that difference exactly and is
otherwise textually identical to the IT OneCable body.

### Flagged lines

| EN line | IT line | Literal back-rendering of IT | Divergence | Severity |
|---|---|---|---|---|
| `Keep ventilation openings clear and ensure sufficient air circulation to prevent overheating.` | `Non ostruire le aperture di ventilazione e garantisci una circolazione dell'aria sufficiente per evitare il surriscaldamento.` | "Do not obstruct the ventilation openings and ensure sufficient air circulation to prevent overheating." | Same glossary-locked polarity reformulation as §1. | Minor |

### Coverage

**All 18 content lines of `it/manuals/dual-flip/safety.mdx` checked.** List markers (`-` vs `1.`)
align 1:1 with the EN counterpart; no item was merged, split, added, dropped or reordered.

### Verdict

**PASS.** 1 Minor (inherited, glossary-sanctioned).

---

## 3. `it/manuals/infinity/safety.mdx` vs `en/manuals/infinity/safety.mdx`

### Flagged lines

*None.*

### Coverage

**All 15 content lines of `it/manuals/infinity/safety.mdx` checked** (2 frontmatter strings + H2 +
2-sentence intro + H3 + 10 bullets).

Notes:

- Intro: `Always use this product in a safe and responsible way.` → `Usa sempre questo prodotto in
  modo sicuro e responsabile.` — `sempre` retained; `risks such as electric shock or fire` →
  `rischi come scosse elettriche o incendi` (both hazards, same order). ✓
- H3 `Check before use` → `Controlla prima dell'uso` (glossary §9 line 1082, locked). ✓
- Bullet 2 `Use only an AC/DC adapter as power supply.` → `Usa solo un alimentatore AC/DC come
  alimentazione.` — `solo` immediately precedes the object; scope identical. ✓
- Bullet 7 `Do not use sharp objects on or around the screen.` → `Non usare oggetti appuntiti sullo
  schermo o attorno a esso.` — negation covers both locative disjuncts. ✓
- Bullet 8 `Suitable for both home and business use.` → `Adatto sia all'uso domestico sia a quello
  aziendale.` — the `sia…sia` correlative preserves EN `both…and`. ✓
- Bullet 10 `Turn the screen off when not in use.` → `Spegni lo schermo quando non è in uso.` —
  impersonal, correctly distinguished from the 2nd-person variant used in Infinity Lite and
  Panorama (see §4, §5). ✓

### Verdict

**PASS.** Clean.

---

## 4. `it/manuals/infinity-lite/safety.mdx` vs `en/manuals/infinity-lite/safety.mdx`

### Flagged lines

*None.*

### Coverage

**All 15 content lines of `it/manuals/infinity-lite/safety.mdx` checked** (2 frontmatter strings +
H2 + 2-sentence intro + H3 + 10 numbered items).

Notes:

- H3 `Read this before use` → `Leggi prima dell'uso` (glossary §9 line 1081, locked) — correctly
  distinguished from Infinity's `Check before use` → `Controlla prima dell'uso`. ✓
- Item 5 `dust accumulation` → `l'accumulo di polvere`; Infinity's `dust build-up` → the same
  Italian. Both EN variants map to one Italian target; no meaning change. ✓
- Item 10 `Turn the screen off when you are not using it.` → `Spegni lo schermo quando non lo usi.`
  — 2nd person preserved, correctly *not* collapsed into the impersonal form used by Infinity. ✓
  (`usi` here is `tu usi`, the informal present indicative — it is a documented false positive of
  the glossary §1.5 courtesy-form grep, not the courtesy imperative. Confirmed in context.)

### Verdict

**PASS.** Clean.

---

## 5. `it/manuals/panorama/safety.mdx` vs `en/manuals/panorama/safety.mdx`

### Flagged lines

| EN line | IT line | Literal back-rendering of IT | Divergence | Severity |
|---|---|---|---|---|
| `### Folding caution` | `### Attenzione durante la chiusura` | "Caution during closing / folding-in" | EN heading is scope-neutral over folding **in and out**; the Italian heading names only the folding-**in** direction. The body line directly beneath restores full scope (`quando richiudi o apri gli schermi`), so no instruction is lost. **Glossary-locked** (`glossary-it.md` §9 line 1052) and it matches the Dutch source heading `Let op bij inklappen` ("caution when folding in") more closely than the EN does — the EN heading is the broadened one. | Minor |

### Coverage

**All 17 content lines of `it/manuals/panorama/safety.mdx` checked** (2 frontmatter strings + H2 +
2-sentence intro + H3 `Before use` + 10 bullets + H3 `Folding caution` + 1 caution paragraph).

Notes:

- H3 `Before use` → `Prima dell'uso` (glossary §9 line 1083, locked). ✓
- Bullet 2 `Only use an AC/DC adapter as power supply.` → `Usa esclusivamente un alimentatore AC/DC
  come alimentazione.` — restriction scope identical to EN. (Panorama uses `esclusivamente` where
  Infinity/Infinity Lite use `solo` for near-identical EN lines; both are correct renderings of
  `only` in this position, so this is register variation, not divergence.) ✓
- Bullet 8 `Suitable for both home and professional use.` → `Adatto sia all'uso domestico sia a
  quello professionale.` — faithful to *its* EN counterpart. See EN-source observation E1. ✓
- **Order of warnings preserved:** the `Folding caution` block sits after the `Before use` list in
  both languages; no warning was promoted or demoted. ✓
- Caution body: `Watch your fingers when folding the screens in or out to avoid pinching.` → `Fai
  attenzione alle dita quando richiudi o apri gli schermi, per evitare di schiacciarle.` = "Pay
  attention to your fingers when you close or open the screens, to avoid crushing them."
  Direction order (in → out) preserved as (close → open); `richiudere` / `aprire` are the
  glossary-locked verbs (§5.5 lines 597–598). `schiacciare` is the correct Italian pinch/crush
  hazard verb. Dropping the possessive (`alle dita`, not `alle tue dita`) is mandated by glossary
  §1.3. ✓

### Verdict

**PASS.** 1 Minor, glossary-sanctioned and closer to the Dutch source than the EN is.

---

## 6. `it/manuals/onecable/display-settings.mdx` vs `en/manuals/onecable/display-settings.mdx`

*(canonical body — shared by 4 products, see §7)*

### Flagged lines

| EN line | IT line | Literal back-rendering of IT | Divergence | Severity |
|---|---|---|---|---|
| `**Need more overview?**` (L34) | `**Vuoi più spazio a schermo?**` (L34) | "**Do you want more space on screen?**" | **Meaning change, and it points the opposite way from the instruction it introduces.** EN/NL (`Behoefte aan meer overzicht?`) ask about *legibility / getting a better overview*; the answer given is "set Scale to 150%", which enlarges text and therefore yields **less** usable screen space. An Italian reader who wants *more space* and follows the instruction gets the opposite of what the heading promised. **Glossary-locked** — `glossary-it.md` §6 line 669 lists this exact string as the ✓ correct rendering, so the defect is in the glossary, not in the page; fixing the page alone would be reverted by the next pass. Suggested replacement (glossary + all 4 pages): `**Testo troppo piccolo?**` or `**Vuoi una visione d'insieme migliore?**`. Cross-language note: DE carries the same error (`Brauchst du mehr Platz?`); FR is correct (`Besoin d'une meilleure vue d'ensemble ?`). | **Major** |
| `…and choose 'Flipped' to correct this.` (L32) | `…e scegli 'Capovolto' per correggerlo.` (L32) | "…and choose 'Capovolto' to correct this." | The English UI token is replaced rather than glossed, breaking the convention the *same sentence* uses two clauses earlier (`'Display orientation' ('Orientamento dello schermo')` keeps EN primary + IT gloss). A reader on an English-language Windows cannot match `'Capovolto'` to anything on screen. Glossary §8 line 812 does map `Flipped` → `Capovolto`, so the rendering is sanctioned; only the *presentation* (gloss vs. replacement) is inconsistent. Note also that the Italian Windows option is `Orizzontale capovolto` / `Verticale capovolto` — bare `Capovolto` is not a complete on-screen label (DE and FR both use the fuller form: `Querformat (gedreht)`, `Paysage (inversé)`). | Minor |
| `Go to Display Settings and choose…` (L23) | `Vai su Impostazioni schermo e scegli…` (L23) | "Go to Impostazioni schermo and choose…" | Same class as above: the English UI label is replaced rather than glossed, where L13 of the same file keeps `**Display settings** ('Impostazioni schermo')`. Low impact — L13 already taught the mapping. | Minor |

### Coverage

**All 22 content lines of `it/manuals/onecable/display-settings.mdx` checked** (2 frontmatter
strings + 2 H2 headings + Windows intro + 3 image `alt` texts + 3 bold question lines + 3 answer
paragraphs + 4 numbered macOS steps + 1 macOS bold question + 1 macOS answer + 2 video fallback
strings).

Notes on the unflagged lines:

- All three `alt` texts translated, none dropped, none left in Dutch; the EN pattern
  `English UI term (Dutch gloss)` becomes `English UI term (Italian gloss)` throughout, which is
  exactly what glossary §8 (note on the NL parenthetical pattern) prescribes. ✓
- `Identify` → `('Identifica')`, `Extend desktop to this display` → `('Estendi il desktop a questo
  schermo')`, `Scale` → `('Ridimensionamento')`, `Scale and layout` → `('Ridimensionamento e
  layout')` — all match glossary §8 lines 808–815. ✓
- macOS chain: `System Settings` → `Impostazioni di Sistema`, `Displays` → `Schermi`,
  `Arrangement` → `Disposizione`, `Rotation` → `Rotazione`, `Standard` → `Standard` (kept EN, as
  the label is identical in the Italian OS) — all match glossary §8 lines 820–829. Step order 1-2-3-4
  identical. ✓
- `set it to 150%` → `impostalo su 150%` — value preserved, and `150%` is written without a space,
  which is the glossary §4.1 Italian percent rule. ✓
- Both video fallback strings translated (`Il tuo browser non supporta il tag video.`). ✓
- `Right-click on your desktop` → `Fai clic con il pulsante destro del mouse sul desktop` — the
  glossary-locked long form (§5.3 line 546). ✓

### Verdict

**PASS WITH ONE MAJOR.** The Major is a content defect inherited from the binding glossary and
affects 4 Italian pages plus the German set; it is not a safety instruction. Recommend fixing
`glossary-it.md` §6 line 669 first, then the 4 `it/manuals/*/display-settings.mdx` pages carrying
the string, then re-checking `de`.

---

## 7. Regression checks — explicitly performed

These were verified individually in every file in scope, not sampled.

### R1 — The grounding / earthing clause and its "properly" adverb

The clause appears in **all five safety files**. In every one it reads:

> `Assicurati che la presa di corrente sia **correttamente** dotata di messa a terra e adatta
> all'amperaggio corretto.`

against EN `Make sure the power outlet is **properly** grounded and suitable for the correct
amperage.`

| File | `correttamente` present | Scoped to the grounding predicate | Second `corretto` on amperage | Result |
|---|---|---|---|---|
| `it/manuals/onecable/safety.mdx` (item 4) | ✓ | ✓ | ✓ | PASS |
| `it/manuals/dual-flip/safety.mdx` | ✓ | ✓ | ✓ | PASS |
| `it/manuals/infinity/safety.mdx` | ✓ | ✓ | ✓ | PASS |
| `it/manuals/infinity-lite/safety.mdx` (item 3) | ✓ | ✓ | ✓ | PASS |
| `it/manuals/panorama/safety.mdx` | ✓ | ✓ | ✓ | PASS |

Scope analysis: `correttamente` is positioned immediately before the participle `dotata`, so it
modifies the earthing predicate alone — it cannot be misread as modifying the whole conjunction. The
second conjunct carries its own adjective (`adatta all'amperaggio **corretto**`), matching EN
`the correct amperage`. Neither adverb has been dropped, merged or duplicated.

This is exactly the rendering mandated by `glossary-it.md` §5.2 line 500, which states the EN
`properly` / NL `goed` "is load-bearing in a mains-electrical clause — never drop `correttamente`".
**The prior round's fix is intact in all five files. No regression.**

### R2 — The 5 V power-restriction sentence and restrictive-word placement

Present in the OneCable/Dual Flip family only (item 6 / bullet 6):

> EN: `Only use the device with a 5V power source via the appropriate cable.`
> IT: `Usa il dispositivo esclusivamente con una fonte di alimentazione da 5 V tramite il cavo
> appropriato.`

- `esclusivamente` is placed after the direct object and immediately before the `con` phrase, so it
  restricts **the power source**, not the act of using. This is the same thing EN `only` restricts
  on its idiomatic reading. **PASS** in both `it/manuals/onecable/safety.mdx` and
  `it/manuals/dual-flip/safety.mdx`.
- The Italian is in fact *less* ambiguous than the English here (see EN-source observation E3).
- `5 V` preserved; `da 5 V` is the glossary §2.4 spec-attachment form. `the appropriate cable` →
  `il cavo appropriato`, definite article preserved (not weakened to `un cavo`).

Adjacent voltage line (item 5, all five files) also re-verified:
EN `a DC input between 5V and 20V (with a tolerance of ±2V)` /
`The required DC input is between 5V and 20V (with a tolerance of ±2V)` →
IT `un ingresso DC compreso tra 5 V e 20 V (con una tolleranza di ±2 V)` /
`L'ingresso DC necessario è compreso tra 5 V e 20 V (con una tolleranza di ±2 V)`.
Values, unit symbols, the `±` sign and the inclusive `tra…e` range are all correct in all five
files. **PASS.**

### R3 — Full negation scope on every negated safety instruction

Every negated instruction in scope, back-rendered and scope-tested:

| File(s) | EN | IT | Negation scope |
|---|---|---|---|
| OneCable / Dual Flip | `Do not use liquids or aggressive cleaning agents.` | `Non usare liquidi o detergenti aggressivi.` | Covers both disjuncts ✓ |
| OneCable / Dual Flip | `Do not touch the device with wet hands and do not use it in humid environments.` | `Non toccare il dispositivo con le mani bagnate e non usarlo in ambienti umidi.` | Both conjuncts independently negated; the second `non` is present, not elided ✓ |
| OneCable / Dual Flip | `Do not drop the monitor and protect the screen from impacts, pressure or sharp objects.` | `Non far cadere il monitor e proteggi lo schermo da urti, pressione o oggetti appuntiti.` | Negation stops at the conjunction; the affirmative imperative `proteggi` is **not** dragged under it ✓ (this is the highest-risk scope boundary in the corpus and it is correct) |
| OneCable / Dual Flip | `Keep ventilation openings clear…` | `Non ostruire le aperture di ventilazione…` | Added negation is the glossary-locked equivalent restatement, semantics unchanged — see §1 Minor ✓ |
| Infinity / Infinity Lite / Panorama | `Do not use sharp objects on or around the screen.` | `Non usare oggetti appuntiti sullo schermo o attorno a esso.` | Covers both locative disjuncts ✓ |
| All five | `when not in use` / `when you are not using it` | `quando non è in uso` / `quando non lo usi` | Negation intact; person correctly tracked per EN variant ✓ |

All negations use `non` + infinitive, the correct Italian `tu` negative imperative (glossary §1.2
line 60). **No partial negation, no dropped negation, no over-extended negation. PASS.**

### R4 — Numbers, units and symbols

Byte-level check of every numeric line across the five safety files:

- Voltages `5 V`, `20 V`, `±2 V`; temperatures `-20 °C`, `60 °C`; scale value `150%`.
- All values identical to EN. No transposition, no unit substitution, no sign loss.
- `°` is U+00B0 and `±` is U+00B1 in every occurrence (10 and 5 occurrences respectively).
- The minus in `-20` is the same ASCII hyphen-minus the EN uses — no character swap.
- Spacing follows glossary §4.1: space before `V` and `°C`, no space before `%`. Confirmed as
  ordinary U+0020, not a non-breaking space (the FR pages use `&nbsp;`; the IT glossary specifies a
  plain space, so IT is compliant — noted only for typography awareness, not a defect).
- Glossary §4.2 defect greps run on all six files: `\d,\d\d\d` → **0 hits**; `\d\.\d` → **0 hits**.
  No English thousands separator and no English decimal point survived into the Italian.

### R5 — Additional checks run (not requested, cheap to run, all clean)

- **Structural parity:** non-blank line counts match exactly for all six pairs
  (25/25, 25/25, 22/22, 22/22, 24/24, 37/37). No line added or dropped anywhere.
- **Canonical-body propagation.** The EN and IT canonical groupings are identical, so no sibling has
  drifted from the audited canonical text:
  - `safety.mdx` — one shared body across **7** products in EN *and* in IT: `expand`, `flip`,
    `lite`, `lite-144hz`, `one-4k`, `one-4k-oled`, `onecable`. `dual-flip`, `infinity`,
    `infinity-lite`, `panorama` are distinct in both languages.
  - `display-settings.mdx` — one shared body across **4** products in EN *and* in IT: `dual-flip`,
    `expand`, `flip`, `onecable`. `infinity` and `infinity-lite` are distinct in both.
  - Consequence: the OneCable verdict below transfers verbatim to the 6 other safety pages and the
    3 other display-settings pages.
- **Register:** glossary §1.5 courtesy-form grep run on all six files → the only hits are `usi` in
  `infinity-lite` and `panorama` (`quando non lo usi`), which is the informal `tu` present
  indicative and a documented false positive of that grep. **No `Lei`/`Suo`/`Voi`, no courtesy
  imperative, no impersonal infinitive, no `Per favore` / `Si prega di`.** Register is uniformly
  informal `tu`, as required.
- **Orthography:** no typographic apostrophes (U+2019), no curly quotes, no non-breaking spaces, no
  en/em dashes, no apostrophe-hack accents. The complete non-ASCII inventory across the six files is
  `°` ×10, `±` ×5, `à` ×4 (`umidità`, `elettricità`), `è` ×6, `ù` ×2 (`più`) — every one correct in
  context, and `è` (is) is never confused with `e` (and).
- **Frontmatter link keys:** every Italian file carries `de_link`, `en_link`, `fr_link`, `nl_link`
  and no `it_link`; every English counterpart carries `de_link`, `fr_link`, `it_link`, `nl_link` and
  no `en_link`. All targets resolve to the same product slug and page. Consistent with the
  language-first routing architecture.

---

## 8. EN-source observations (not counted against the Italian)

**E1 — `en/manuals/panorama/safety.mdx` line 24.** EN reads `Suitable for both home and
**professional** use`, while `en/manuals/infinity/safety.mdx` and
`en/manuals/infinity-lite/safety.mdx` read `home and **business** use` for the same source bullet,
and the Dutch original for all three is `zowel thuis als **zakelijk** gebruik` ("business"). The EN
Panorama page is the outlier. The Italian faithfully mirrors whichever EN variant it was given
(`professionale` on Panorama, `aziendale` on the other two), so the Italian is correct as a
translation — but if the client wants the family to read consistently, the fix belongs on the EN
Panorama page (and would then need to propagate to `de`, `fr`, `it`).

**E2 — `en/manuals/onecable/display-settings.mdx` line 32.** EN glosses `Display orientation` with
its Dutch original (`'Beeldschermstand'`) but gives `'Flipped'` with no Dutch gloss, even though the
Dutch source says `'Gespiegeld'`. The convention is applied asymmetrically inside a single sentence,
which is what leaves the translated pages without a clear pattern to follow (see the two Minor
findings in §6). Worth normalising on the EN side. The glossary already records the churn here:
§8 line 813 marks `Mirrored` as "superseded — EN pages now say 'Flipped'".

**E3 — `en/manuals/onecable/safety.mdx` item 6.** `Only use the device with a 5V power source via
the appropriate cable.` Sentence-initial `only` in an English imperative is scopally ambiguous — it
can be parsed as restricting the act (`the only thing you should do is use it…`) rather than the
power source. The Italian `Usa il dispositivo esclusivamente con…` is unambiguous. No action needed;
recorded so that a future reviewer does not "correct" the Italian toward the looser English.

**E4 — line-ending / trailing-newline nit.** `en/manuals/onecable/display-settings.mdx` has no
trailing newline; the Italian counterpart does. Cosmetic only, no rendered difference.

---

## 9. Per-file verdicts

| # | File | Content lines checked | Critical | Major | Minor | Verdict |
|---|---|---|---|---|---|---|
| 1 | `it/manuals/onecable/safety.mdx` | 18 | 0 | 0 | 1 | **PASS** |
| 2 | `it/manuals/dual-flip/safety.mdx` | 18 | 0 | 0 | 1 | **PASS** |
| 3 | `it/manuals/infinity/safety.mdx` | 15 | 0 | 0 | 0 | **PASS — clean** |
| 4 | `it/manuals/infinity-lite/safety.mdx` | 15 | 0 | 0 | 0 | **PASS — clean** |
| 5 | `it/manuals/panorama/safety.mdx` | 17 | 0 | 0 | 1 | **PASS** |
| 6 | `it/manuals/onecable/display-settings.mdx` | 22 | 0 | 1 | 2 | **PASS with one Major** |
| | **Total** | **105** | **0** | **1** | **4** | |

All 105 content lines across the six files were individually back-rendered and compared. Both
canonical bodies were additionally confirmed to be propagated byte-identically to their sibling
products, so the audited text is the text that ships on all 11 Italian safety pages and all 6
Italian display-settings pages.

---

## 10. Recommended actions

1. **(Major, non-safety)** Replace the locked rendering of `Need more overview?`. Fix
   `translations/glossary-it.md` §6 line 669 first (it is binding and will otherwise re-impose the
   current string), then the 4 Italian `display-settings.mdx` pages, then review the identical
   German string. Candidate: `**Testo troppo piccolo?**`.
2. **(Minor)** Decide one convention for Windows UI option values on Italian pages — either
   `'Flipped' ('Capovolto')` mirroring the file's own `'Display orientation' ('Orientamento dello
   schermo')` pattern, or the fuller Italian option label `'Orizzontale capovolto'` as DE/FR do.
   Record the decision in glossary §8 so it stops drifting.
3. **(No action)** The two remaining Minors (ventilation-opening polarity; `Attenzione durante la
   chiusura`) are deliberate, glossary-locked, and in the second case closer to the Dutch source
   than the English is. Listed for the record only.
4. **(Optional, EN side)** Normalise EN Panorama `professional` → `business` (E1) and the
   `'Flipped'` gloss asymmetry (E2). Both are English-source editorial calls, not translation
   defects.

**Bottom line for client handoff: the Italian safety chapters are cleared. Zero Critical findings,
zero Major findings in any safety file. The grounding/"properly" fix from the prior round is intact
in all five files, the 5 V restriction is correctly scoped, and every negation is complete.**
