# Round 4 — German Safety Chapter Line-Alignment Audit (DE vs EN)

**Scope:** the highest-stakes translated content on the site — the German safety chapters plus
the canonical display-settings chapter — audited line-by-line against their English counterparts.
**Method:** every content line (frontmatter string, heading, sentence, list item, callout,
image alt text, video fallback) was rendered back into literal English and compared against the
aligned English line. Checked for divergence in meaning, severity/modality, scope of
restrictions, negation scope, safety-bearing adverbs, numbers/units/voltages/temperatures,
omitted or added content, and order of warnings.
**Posture:** fresh eyes, assume nothing. Prior rounds passed; nothing was taken on trust.
**Mode:** READ-ONLY. No `.mdx` file was modified.

**Auditor's note on authority.** `translations/glossary-de.md` locks a number of the renderings
below (§9, §10.1, §10.2, §11.0 — safety and display-settings are declared *frozen chapters*,
shipped `4792819`, with `de/manuals/onecable/{safety,display-settings}.mdx` canonical). A locked
rendering is evidence of *intent*, not proof of *correctness*, so every such line was still
audited on its merits and is flagged where it diverges from its English source. Where a flag
collides with a lock, that is stated in the row.

---

## Summary

| Severity | Count |
|---|---|
| **Critical** (a German reader would understand a different safety instruction) | **0** |
| **Major** (meaning shade or emphasis differs) | **1** |
| **Minor** (stylistic / normalisation / no practical divergence) | **7** |

**Zero Critical findings.** No German safety instruction differs in substance from its English
source. Every restriction keeps its scope, every negation keeps its full reach, every
safety-bearing adverb survives, and every number, unit, voltage and temperature matches.

The single **Major** is in the display-settings chapter, is **not safety content**, and is a
documented house lock (glossary §10.1). It is raised because the audit brief asks for meaning
shades regardless of provenance.

---

## Shared-body verification (done first, so coverage is provable)

Auditing 6 files covers 17 shipped files. Body checksums (`md5` of each file below the
frontmatter) confirm the sharing is real and identical on **both** sides:

| Body | EN checksum | DE checksum | Products sharing it |
|---|---|---|---|
| safety (canonical) | `c19ed425` | `82f2a1d9` | onecable, expand, flip, lite, lite-144hz, one-4k, one-4k-oled — **7** |
| safety (dual-flip) | `9150ec5a` | `ee4b9738` | dual-flip — 1 (differs from canonical only in list marker `-` vs `1.`, identically on both sides) |
| safety (infinity) | `780f6941` | `afa020c9` | infinity — 1 |
| safety (infinity-lite) | `e8e86327` | `9ef08114` | infinity-lite — 1 |
| safety (panorama) | `437296ba` | `9dda138e` | panorama — 1 |
| display-settings (canonical) | `e63d5d0a` | `076187e1` | onecable, dual-flip, expand, flip — **4** |

The EN grouping and the DE grouping are **identical partitions**. No product has drifted off its
shared body on one side only — the failure mode where auditing the canonical file would give
false assurance for its siblings. Glossary §7.3 requires the display-settings chapter to stay
checksum-identical across its four products in DE; it is.

`de/manuals/{infinity,infinity-lite}/display-settings.mdx` carry their own bodies
(`2be2e728`, `e3be2e18`) and are **outside this audit's scope** — see Residual Risk.

---

## File 1 — `de/manuals/onecable/safety.mdx` vs `en/manuals/onecable/safety.mdx`

**Canonical. Body shared by 7 products.** Highest-blast-radius file in the audit.

### Flagged lines

| # | EN line | DE line | Literal back-rendering | Divergence | Severity |
|---|---|---|---|---|---|
| 7 | Prevent exposure to moisture, dust and static electricity to prevent damage to the electronics. | Vermeide die Einwirkung von Feuchtigkeit, Staub und statischer Elektrizität, um Schäden an der Elektronik zu verhindern. | **Avoid** exposure to moisture, dust and static electricity, in order to prevent damage to the electronics. | `Prevent` → `Vermeide` (avoid). The German de-duplicates the EN's clumsy "Prevent … to prevent" by using *vermeiden* then *verhindern*. `Vermeide` is a shade weaker than a literal `Verhindere`, but as a user-directed instruction ("keep it away from X") the two are operationally identical, and the purpose clause keeps the full-strength `verhindern`. No change to what the reader must do. | Minor |
| intro | Please read the following **guidelines** carefully … | Lies die folgenden **Hinweise** sorgfältig durch … | Read the following **notices/instructions** carefully … | `guidelines` → `Hinweise` (notices) rather than `Richtlinien`. Same referent — the numbered list that follows. Also drops "Please" per the locked house rule (glossary §2.2, §10.1: German instructions drop it exactly as Dutch drops "alstublieft"). Neither changes modality: the EN is not a modal "should", and the DE imperative `Lies` is no stronger or weaker than the EN imperative `read`. | Minor |

### Lines cleared (no divergence) — the ones that matter

- **Item 2 — restriction scope.** EN `Only use the included AC/DC adapter as power supply.` → DE
  `Verwende ausschließlich das mitgelieferte AC/DC-Netzteil als Stromversorgung.` `ausschließlich`
  sits immediately before the object NP, so it restricts **the adapter** — exactly what EN's
  `only` restricts. It does *not* read as "use it only as a power supply" or "only use it".
  Correct attachment.
- **Item 4 — grounding adverb.** `properly grounded` → `ordnungsgemäß geerdet`. The adverb is
  present and attaches to `geerdet`, not to the amperage clause. Both predicates share the
  final `ist`, mirroring the EN coordination exactly.
- **Item 5 — voltages.** `between 5V and 20V (with a tolerance of ±2V)` → `zwischen 5 V und 20 V
  (mit einer Toleranz von ±2 V)`. All three figures correct; DIN 5008 unit spacing is a
  deliberate, signed-off divergence from NL (glossary §4, §11) and not a defect.
- **Item 6 — the 5 V restriction.** See regression checks below. Correct, and it *disambiguates*
  the EN in the intended direction.
- **Item 8 — negation over a coordinated object.** `Do not use liquids or aggressive cleaning
  agents.` → `Verwende keine Flüssigkeiten oder aggressiven Reinigungsmittel.` The weak plural
  adjective ending `aggressiv**en**` (not `aggressive`) proves the second conjunct is governed by
  `keine`. Both conjuncts are negated. Had it read `aggressive Reinigungsmittel`, the negation
  would have leaked and only liquids would be prohibited — that defect is **not** present.
  Separately, `Reinige den Bildschirm **nur** mit einem trockenen, weichen Tuch` places `nur`
  before the instrument PP, restricting the cloth — same as EN `only with`.
- **Item 9 — double negation.** `Do not touch … and do not use it …` → `Berühre … **nicht** … und
  verwende es **nicht** …`. Both negations survive. The German carries the same
  constituent-vs-sentential ambiguity the EN has; no scope shift was introduced.
- **Items 10, 11, 12, 13, 14** — exact. `Lass … nicht fallen`, `Halte die Lüftungsöffnungen frei`,
  `Begrenze die Einwirkung`, `−20 °C und 60 °C`, `Schalte den Bildschirm aus, wenn du ihn nicht
  verwendest`.
- **Order of warnings** — items 1–14 appear in identical order. Nothing reordered, nothing
  omitted, nothing added.

**Coverage: all 18 content lines of `de/manuals/onecable/safety.mdx` checked**
(2 frontmatter strings, 1 `##` heading, 1 intro paragraph, 14 numbered list items comprising
15 sentences), against all 18 aligned EN lines.

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor. Safe to hand off as-is.

---

## File 2 — `de/manuals/dual-flip/safety.mdx` vs `en/manuals/dual-flip/safety.mdx`

Prose is **word-for-word identical** to File 1 on both the EN and the DE side; the only
difference is the list marker (`-` bullets instead of `1.` numbering), and that difference is
present identically in EN and DE. Structural parity preserved.

### Flagged lines

Identical to File 1: the `Prevent` → `Vermeide` row and the `guidelines` → `Hinweise` row
(both **Minor**, already counted once in the summary — not double-counted).

**Coverage: all 18 content lines of `de/manuals/dual-flip/safety.mdx` checked.**

**Verdict: PASS.** 0 Critical, 0 Major, 0 new findings.

---

## File 3 — `de/manuals/infinity/safety.mdx` vs `en/manuals/infinity/safety.mdx`

### Flagged lines

| # | EN line | DE line | Literal back-rendering | Divergence | Severity |
|---|---|---|---|---|---|
| 8 | Suitable for **both** home **and** business use. | Für den privaten und gewerblichen Gebrauch geeignet. | Suitable for private and commercial use. | `both … and` → plain `und`. German `sowohl … als auch` is not used; the bare coordination already covers both cases and adds no restriction. No scope change. | Minor |

### Lines cleared — the ones that matter

- **Bullet 2 — indefinite article preserved.** EN here reads `Use only **an** AC/DC adapter`
  (indefinite), *not* "the included adapter" as in the canonical file. DE reads `Verwende
  ausschließlich **ein** AC/DC-Netzteil` — indefinite. This is the trap where a translator
  imports the canonical file's `das mitgelieferte` and silently narrows the permitted hardware to
  the in-box unit. **It was not imported.** Correct.
- **Bullet 3 — grounding adverb.** `ordnungsgemäß geerdet` present.
- **Bullet 4 — voltages.** `Der erforderliche DC-Eingang liegt zwischen 5 V und 20 V (mit einer
  Toleranz von ±2 V)`. Note the EN here says *required DC input* (not "the monitor operates on"),
  and the DE tracks that with `erforderlich` + `liegt` rather than reusing the canonical
  `arbeitet mit`. Correctly differentiated from File 1.
- **Bullet 7 — negation.** `Do not use sharp objects **on or around** the screen.` → `Verwende
  **keine** scharfen Gegenstände **auf dem Bildschirm oder in seiner Umgebung**.` Negation intact;
  both locative alternatives ("on" and "around") preserved — neither dropped.
- **Bullet 6.** `impact and external pressure` → `Stößen und Druck von außen`. EN singular
  `impact` → DE plural `Stößen` is idiomatic German and carries the same coverage.
- **Intro.** `Always use this product in a safe and responsible way. Read the following
  guidelines carefully to avoid risks such as electric shock or fire.` → `Verwende dieses Produkt
  immer auf sichere und verantwortungsvolle Weise. Lies die folgenden Hinweise sorgfältig durch,
  um Risiken wie Stromschlag oder Brand zu vermeiden.` `immer` retained; both named hazards
  (electric shock, fire) retained in order.
- **Heading.** `### Check before use` → `### Vor der Verwendung prüfen` — EN imperative rendered
  as a German infinitive heading (glossary §10.4). Same instruction.

**Coverage: all 15 content lines of `de/manuals/infinity/safety.mdx` checked**
(2 frontmatter strings, 1 `##` heading, 1 two-sentence intro, 1 `###` heading, 10 bullets).

**Verdict: PASS.** 0 Critical, 0 Major, 1 Minor.

---

## File 4 — `de/manuals/infinity-lite/safety.mdx` vs `en/manuals/infinity-lite/safety.mdx`

Same content as File 3 with a numbered list, the heading `Read this before use`, and EN wording
variants (`manner` for `way`, `accumulation` for `build-up`, `impacts` for `impact`).

### Flagged lines

| # | EN line | DE line | Literal back-rendering | Divergence | Severity |
|---|---|---|---|---|---|
| 8 | Suitable for **both** home **and** business use. | Für den privaten und gewerblichen Gebrauch geeignet. | Suitable for private and commercial use. | Same `both … and` → `und` as File 3. Not double-counted. | Minor |

### Lines cleared

- `### Read this before use` → `### Vor der Verwendung lesen` — correct, and correctly *different*
  from File 3's `… prüfen` (EN says "read" here, "check" there). The two headings were not
  collapsed onto one German target.
- Indefinite `an AC/DC adapter` → `ein AC/DC-Netzteil` — preserved, same as File 3.
- `ordnungsgemäß geerdet` present. `5 V`/`20 V`/`±2 V` correct. `−20 °C`/`60 °C` correct.
- `Do not use sharp objects on or around the screen` → `keine …, auf dem Bildschirm oder in seiner
  Umgebung` — negation and both locatives intact.
- `Turn the screen off when you are not using it.` → `Schalte den Bildschirm aus, wenn du ihn
  nicht verwendest.` — negation intact.
- EN's own sibling variance (`manner`/`way`, `accumulation`/`build-up`, `impacts`/`impact`) is
  normalised to one German rendering each. This is deliberate and harmless — see EN-source
  observation **EN3**.

**Coverage: all 15 content lines of `de/manuals/infinity-lite/safety.mdx` checked**
(2 frontmatter strings, 1 `##` heading, 1 two-sentence intro, 1 `###` heading, 10 numbered items).

**Verdict: PASS.** 0 Critical, 0 Major, 0 new findings.

---

## File 5 — `de/manuals/panorama/safety.mdx` vs `en/manuals/panorama/safety.mdx`

The only safety file with a second section (`Folding caution`) — a physical-injury warning, so
it got extra scrutiny.

### Flagged lines

| # | EN line | DE line | Literal back-rendering | Divergence | Severity |
|---|---|---|---|---|---|
| 8 | Suitable for both home and **professional** use. | Für den privaten und **gewerblichen** Gebrauch geeignet. | Suitable for private and **commercial** use. | `professional` → `gewerblich` (commercial / trade), not `professionell`. The two EN sibling files say *business* use, which `gewerblich` renders exactly; the German has normalised panorama onto the sibling target. Near-synonymous in a suitability statement, imposes no restriction the EN does not, and arguably repairs an EN inconsistency (see **EN3**). Raised for completeness. | Minor |
| 8 | Suitable for **both** home and professional use. | Für den privaten und gewerblichen Gebrauch geeignet. | — | `both … and` → `und`, as Files 3–4. Not double-counted. | Minor |
| 30 | Watch your fingers when folding the screens **in or out** to avoid pinching. | Achte beim **Ein- und Ausklappen** der Bildschirme auf deine Finger, um Quetschungen zu vermeiden. | Watch out for your fingers when folding the screens **in and out**, to avoid crush injuries. | `in **or** out` → `Ein- **und** Ausklappen`. German's suspended-hyphen construction takes `und`; `Ein- oder Ausklappen` would be unidiomatic. Coverage is **identical or wider** — the warning applies to both operations either way. No safety scope is lost; a reader cannot conclude that only one direction is hazardous. | Minor |

### Lines cleared — the folding warning in detail

This is the one line in the corpus warning about a **physical injury**, so it was checked
element by element:

- Hazard action — `folding the screens in or out` → `beim Ein- und Ausklappen der Bildschirme` ✔
- Body part at risk — `your fingers` → `auf deine Finger` ✔ (`achten` correctly governs `auf`)
- Instruction — `Watch` → `Achte … auf` ✔ imperative, same force
- Consequence avoided — `pinching` → `Quetschungen` ✔ (crush/pinch injuries)
- Purpose clause — `to avoid` → `um … zu vermeiden` ✔
- Heading — `### Folding caution` → `### Vorsicht beim Klappen` ✔ (`Vorsicht` = caution;
  glossary §10.1 maps `Caution:` → `Achtung:` for the *callout lead-in*, a different construction
  — `Vorsicht` is correct for a heading and is the shipped form)

Nothing about the hazard is softened, narrowed or reordered. The warning is the last block on the
page in both languages.

Also cleared: `Only use an AC/DC adapter` → `Verwende ausschließlich ein AC/DC-Netzteil`
(indefinite preserved); `ordnungsgemäß geerdet`; `5 V`/`20 V`/`±2 V`; `−20 °C`/`60 °C`;
`Do not use sharp objects on or around the screen` → full negation + both locatives;
`### Before use` → `### Vor der Verwendung`.

**Coverage: all 17 content lines of `de/manuals/panorama/safety.mdx` checked**
(2 frontmatter strings, 1 `##` heading, 1 two-sentence intro, 2 `###` headings, 10 bullets,
1 folding-warning sentence).

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor (1 new: `professional` → `gewerblich`).

---

## File 6 — `de/manuals/onecable/display-settings.mdx` vs `en/manuals/onecable/display-settings.mdx`

**Canonical. Body shared by 4 products.** Not safety content; graded on the same scale.

### Flagged lines

| # | EN line | DE line | Literal back-rendering | Divergence | Severity |
|---|---|---|---|---|---|
| 34 | **Need more overview?** | **Brauchst du mehr Platz?** | **Need more room / space?** | Meaning shade differs: *overview* → *room*. Compounding it, the instruction that follows sets scaling to **150 %**, which enlarges text and UI elements and therefore **reduces** usable desktop area — so `mehr Platz` reads as the opposite of what the setting delivers, while `Überblick`/`Übersicht` is what the source means and what the setting actually gives. **Glossary-locked** (§10.1 collapses both EN variants `Need more room?` / `Need more overview?` onto `Brauchst du mehr Platz?`), and the chapter is declared frozen (§11.0) — so this is a deliberate house decision, not translator drift. Non-safety. Recommend the client consider `Brauchst du mehr Übersicht?` for the `Need more overview?` occurrences and keep `mehr Platz` only for panorama/osd's `Need more room?`. | **Major** |
| 32 | … choose **'Flipped'** to correct this. | … wähle **„Querformat (gedreht)"**, um das zu korrigieren. | … choose **'Landscape (flipped)'** to correct this. | Scope narrowed: EN's generic `Flipped` covers any flipped orientation; the German names the specific landscape-flipped dropdown entry. Deliberate and documented (glossary §9 note: German Windows has no standalone *Gedreht* entry — the options are `Querformat`, `Hochformat`, `Querformat (gedreht)`, `Hochformat (gedreht)`), and it is arguably *more* actionable than the EN, which names no real Windows option (see **EN2**). Residual narrowing: a user whose screen is in **portrait** and upside down needs `Hochformat (gedreht)`. Glossary §11 already lists this as "worth the client's eye — verify against a real German Windows install before the pages ship"; that verification is **still open**. | Minor |
| 16–18 | alt: "Right-click the desktop and choose **Display settings** (Beeldscherminstellingen)" / "… use **Identify** (Identificeren) and **Extend desktop to this display** (…)" / "**Scale and layout** (Schaal en indeling): adjust **Scale** (Schaal)" | alt: "… und **Anzeigeeinstellungen** wählen" / "… dann **Identifizieren** und **Desktop auf diese Anzeige erweitern** verwenden" / "**Skalierung und Anordnung**: die **Skalierung** anpassen" | (German UI labels only) | The EN alt texts pair the **English** label (which is what the screenshot actually shows) with a local gloss; the German alt texts carry the German label **only**. Per glossary §9 the screenshots stay English on every language page, so a German screen-reader user is given a label that does not appear in the image they cannot see. Consistent across all three alt texts and consistent with the §9 body-copy rule ("German label alone" after first mention). Accessibility-parity nit, no instructional content lost. | Minor |
| 23 | Go to Display Settings and choose 'Extend desktop to this display' ('Bureaublad uitbreiden…'). | Gehe zu den Anzeigeeinstellungen und wähle „Desktop auf diese Anzeige erweitern". | Go to the Display Settings and choose 'Extend desktop to this display'. | Second-mention gloss dropped — correct per §9 ("then the German label alone"). Listed only to record that the drop was checked and is intentional, not an omission. | Minor (informational) |

### Lines cleared

- **Line 13.** `Right-click on your desktop and choose **Display settings**
  ('Beeldscherminstellingen') to open the display configuration.` → `Klicke mit der rechten
  Maustaste auf deinen Desktop und wähle **Display settings** („Anzeigeeinstellungen"), um die
  Bildschirmkonfiguration zu öffnen.` Structurally parallel: bold English label (matching the
  English screenshot) + localised parenthetical. Exactly the §9 first-mention pattern.
- **Line 23, remainder.** `Use the 'Identify' button …` → `Verwende die **Schaltfläche**
  „Identifizieren" …` — `Schaltfläche` (on-screen UI button), not `Taste` (physical device
  button). Correct per glossary §1.1/§10.4; the wrong choice here would have pointed the reader at
  the monitor's hardware buttons. `Then you can easily drag …` → `Danach kannst du die Bildschirme
  einfach in die richtige Reihenfolge ziehen.` ✔
- **Line 36.** `set it to 150% for a larger display of text and elements` → `stelle sie auf 150 %
  ein, damit Text und Elemente größer dargestellt werden` — value and effect both correct.
- **Lines 40–43 (macOS steps).** `System Settings` → `Systemeinstellungen`, `Displays` →
  `Displays`, `Arrangement` → `Anordnen`, `Arrange the displays in the desired order` → `Ordne die
  Bildschirme in der gewünschten Reihenfolge an`. All four match the German macOS UI (§9) and are
  in the same order.
- **Line 52.** `go to 'Rotation' and choose 'Standard'` → `gehe zu „Drehung" und wähle „Standard"`
  — both are the real German macOS labels; `Standard` correctly left untranslated.
- **Headings.** `Display Configuration Windows` / `macOS` → `Bildschirmkonfiguration Windows` /
  `macOS` under frontmatter title `Anzeigeeinstellungen` — the locked split (§7.3, §11.0).
- **Video fallbacks (×2).** `Your browser does not support the video tag.` → `Dein Browser
  unterstützt das Video-Tag nicht.` — negation intact, both occurrences.
- **Media integrity.** Both `<img>` `src` paths and both Firebase `<source>` URLs (including
  query strings and access tokens) are **byte-identical** between EN and DE. No broken or
  substituted asset.
- **Section order** — Windows block then macOS block, identical.

**Coverage: all 22 content lines of `de/manuals/onecable/display-settings.mdx` checked**
(2 frontmatter strings, 2 `##` headings, 3 image alt texts, 4 bold callout lead-ins, 4 macOS
numbered steps, 5 body paragraphs, 2 video fallbacks).

**Verdict: PASS WITH ONE OBSERVATION.** 0 Critical, 1 Major (`Need more overview?` →
`Brauchst du mehr Platz?` — non-safety, glossary-locked, client's call), 3 Minor. No blocker.

---

## Regression checks — explicit confirmations

The three risk patterns named in the audit brief were each checked in the **current** German text
of every file in which they occur. All three are **correct**.

### 1. The 5 V / power-restriction sentence and its restrictive adverb placement — ✅ CONFIRMED CORRECT

Occurs in the canonical safety body (7 products) and dual-flip — 8 shipped files.

> EN: `Only use the device with a 5V power source via the appropriate cable.`
> DE: `Verwende das Gerät ausschließlich mit einer 5-V-Stromquelle über das passende Kabel.`

`ausschließlich` sits **after the object** `das Gerät` and **immediately before the `mit`-PP**, so
it restricts **the power source** — which is what the sentence is for. The dangerous alternative
placements are absent:

- ✗ `Verwende ausschließlich das Gerät mit einer 5-V-Stromquelle` would restrict the *device*
  ("use only the device…") — **not present**.
- ✗ `Verwende das Gerät ausschließlich über das passende Kabel` would shift the restriction onto
  the *cable* — **not present**.

The German is in fact **less ambiguous than the English**, and resolves in the intended direction.
Adjacent numbers verified in the same sweep: `5-V-Stromquelle` (correct Durchkopplung per §3.2),
and in item 5 `zwischen 5 V und 20 V (mit einer Toleranz von ±2 V)`. The parallel restriction in
item 2 (`Verwende **ausschließlich** das mitgelieferte AC/DC-Netzteil`) correctly attaches to the
adapter, and in infinity / infinity-lite / panorama the indefinite `**ein** AC/DC-Netzteil` was
**not** silently upgraded to `das mitgelieferte`.

### 2. Grounding/earthing clauses retaining the "properly/ordnungsgemäß"-type adverb — ✅ CONFIRMED CORRECT

Occurs in **all five** safety files.

> EN: `Make sure the power outlet is properly grounded and suitable for the correct amperage.`
> DE: `Achte darauf, dass die Steckdose ordnungsgemäß geerdet und für die richtige Stromstärke geeignet ist.`

`ordnungsgemäß` is **present in all five files** and attaches to `geerdet`, not to the amperage
clause. The failure mode — dropping the adverb to leave a bare `geerdet` ("grounded"), which
would permit an improvised or partial earth — is **not present anywhere**. `richtige` (correct)
likewise survives on the amperage clause in all five. `Achte darauf, dass …` is the locked
rendering of `Make sure that …` (§10.1) and carries the same obligation force.

### 3. All negated safety instructions preserving full negation scope — ✅ CONFIRMED CORRECT

Every negation was matched 1:1 against its English source, and the token counts reconcile exactly
across all six files:

| File | EN negations | DE `nicht` | DE `kein*` | DE total | Reconciles |
|---|---|---|---|---|---|
| onecable/safety | 5 | 4 | 1 | 5 | ✅ |
| dual-flip/safety | 5 | 4 | 1 | 5 | ✅ |
| infinity/safety | 2 | 1 | 1 | 2 | ✅ |
| infinity-lite/safety | 2 | 1 | 1 | 2 | ✅ |
| panorama/safety | 2 | 1 | 1 | 2 | ✅ |
| onecable/display-settings | 2 | 2 | 0 | 2 | ✅ |

No negation is dropped, and none is added. The two partial-negation risks specifically named in
the brief were both examined:

- **Coordinated object under one negator** — `Do not use liquids or aggressive cleaning agents.` →
  `Verwende **keine** Flüssigkeiten oder **aggressiven** Reinigungsmittel.` The weak plural
  ending `aggressiv**en**` (not the strong `aggressive`) is positive proof the second conjunct is
  still governed by `keine`. Both are prohibited. ✅
- **Two coordinated clauses each needing its own negator** — `Do not touch the device with wet
  hands **and do not** use it in humid environments.` → `Berühre das Gerät **nicht** mit nassen
  Händen und verwende es **nicht** in feuchten Umgebungen.` Both `nicht` present; the second is
  not elided. ✅

Also verified: `Lass den Monitor **nicht** fallen` (separable verb, negator correctly placed
before `fallen`); `Verwende **keine** scharfen Gegenstände auf dem Bildschirm oder in seiner
Umgebung` (×3 files — negation plus **both** locatives `on` and `around`); `wenn du ihn **nicht**
verwendest` (×5 files); `Dein Browser unterstützt das Video-Tag **nicht**.` (×2 in
display-settings).

### Additional checks run (not requested, no findings)

- **Register.** Zero hits for `Sie`, `Ihnen`, `Ihre`, `Ihrem`, `Ihren`, `Ihrer`, `Ihres`, `Bitte`
  across all six DE files. Informal `du`/`dein` throughout, lowercase. Clean.
- **Cross-language link keys.** All six DE files carry exactly `en_link`, `fr_link`, `it_link`,
  `nl_link`; all six EN files carry exactly `nl_link`, `de_link`, `fr_link`, `it_link`. Complete
  4-key sets, no self-links, no missing keys, no stale slugs — the language switcher is intact on
  every audited page.
- **Numbers and units.** Every voltage, tolerance, temperature and percentage matched: `5 V`,
  `20 V`, `±2 V`, `−20 °C`, `60 °C`, `150 %`. Typographic minus `−` (U+2212) used in
  temperatures per §4; DIN 5008 unit spacing throughout, which is a signed-off deliberate
  divergence from the NL lock (§11) and must **not** be re-flagged as an nl↔de parity defect.
- **Content addition/omission.** No German file adds a sentence, a bullet, a heading or a caveat
  that its English counterpart lacks; none omits one. Block order is identical in all six pairs.

---

## EN-source observations (not counted against the German)

- **EN1 — internal contradiction in the canonical safety body (8 shipped files).** Item 5 states
  the monitor operates on a DC input **between 5 V and 20 V**; item 6 then says to use it
  **only with a 5 V power source**. As written, item 6 forbids most of the range item 5 permits.
  The German reproduces this faithfully and is therefore *correct as a translation* — but the
  contradiction is now shipped in five languages. Worth resolving with the client at source
  (Dutch), then propagating. This is the highest-value finding in the audit even though it is
  not a German defect.
- **EN2 — `'Flipped'` is not a Windows orientation option.** The Windows *Display orientation*
  dropdown offers Landscape / Portrait / Landscape (flipped) / Portrait (flipped). The EN
  instruction names none of them. The German picked the specific entry; FR and IT should be
  checked for how they resolved the same gap, and the EN should probably be tightened too.
- **EN3 — sibling inconsistencies in the EN safety pages**, normalised by the German:
  `business use` (infinity, infinity-lite) vs `professional use` (panorama);
  `in a safe and responsible **way**` (infinity) vs `**manner**` (infinity-lite, panorama);
  `against impact` (infinity) vs `against impacts` (infinity-lite); `dust build-up` (infinity,
  panorama) vs `dust accumulation` (infinity-lite). Each pair carries one German rendering. The
  normalisation is defensible; the EN variance is the thing to fix.
- **EN4 — Dutch strings on the English display-settings page.** The EN chapter carries Dutch
  parenthetical glosses (`'Beeldscherminstellingen'`, `'Identificeren'`, `'Schaal en indeling'`)
  in body copy *and* in image alt text. Intentional per §9 (the screenshots are Dutch/English),
  but an English-speaking client reading the EN page will notice it.

---

## Residual risk / out of scope

1. **`de/manuals/{infinity,infinity-lite}/display-settings.mdx` were not audited.** They carry
   their own bodies (`2be2e728`, `e3be2e18`), are not covered by the canonical file, and were not
   in the assigned file list. `en/manuals/infinity-lite/display-settings.mdx` contains a second
   `**Need more overview?**` occurrence (line 59), so the Major finding above **probably recurs
   there**. Recommend a follow-up pass on these two files before handoff.
2. **The `Querformat (gedreht)` verification is still open.** Glossary §11 asks for confirmation
   against a real German Windows install. This audit confirms the rendering is *internally
   consistent and documented*; it cannot confirm the dropdown label empirically.
3. **Screenshots remain English/Dutch on the German pages** (client decision per §9). Combined
   with German-only alt text, a German user matching prose to screenshot relies on the
   parenthetical gloss on first mention. Working as designed, flagged for visibility.

---

## Overall verdict

**PASS — cleared for client handoff.**

The German safety chapters are a faithful, careful rendering of the English. Across 105 content
lines in six file pairs — covering 17 shipped files — there is **not one line where a German
reader would come away with a different safety instruction than an English reader**. Restriction
scope, negation scope, safety-bearing adverbs, hazard warnings, numbers and units are all intact,
and several places where a translator would plausibly have drifted (importing `das mitgelieferte`
into the indefinite-article files, letting `keine` fail to distribute across a coordinated object,
attaching `ausschließlich` to the wrong constituent, dropping `ordnungsgemäß`) are demonstrably
correct.

The one Major finding is a non-safety UI heading in the display-settings chapter, is a documented
house lock rather than translator error, and is a judgement call for the client. The seven Minor
findings are stylistic or normalising and require no action.

The most consequential thing this audit surfaced is **not a German defect at all**: the EN source
contradiction between the 5–20 V operating range and the "only use a 5 V power source"
instruction (**EN1**), which is now faithfully shipped in every language.

---

*Round 4 final audit — read-only. No `.mdx` file was modified. 6 file pairs, 105 content lines,
17 shipped files covered via verified checksum-identical shared bodies.*
