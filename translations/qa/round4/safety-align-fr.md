# Round 4 — FR↔EN line-aligned audit of the safety chapters

**Scope:** 6 file pairs (5 safety chapters + the canonical display-settings chapter)
**Direction:** FR fidelity against `en/` as structural base. Dutch origin noted only where it explains an EN artefact.
**Mode:** READ-ONLY. No `.mdx` file was modified by this audit.
**Date:** 2026-08-12 · **Branch:** `main` (post-merge `a0525eb`)
**Auditor stance:** fresh eyes, prior passes treated as unproven.

---

## 0 · Headline

| | |
|---|---|
| **Critical** | **0** |
| **Major** | **0** |
| **Minor** | **5** (4 distinct defect classes; 2 of them sit on `translations/glossary-fr.md` §10 **locked** strings) |
| **EN-source observations** (not counted against FR) | 7 |
| **Verdict** | **PASS — clear for client handoff.** No line in the six FR files would lead a French reader to take a different physical action, accept a different limit, or perform a different negated instruction than an English reader. |

Independent machine gates run alongside the manual pass:

| Gate | Result |
|---|---|
| `python scripts/verify_translation.py --base en --targets fr` | `0 FAIL, 0 WARN` (exit 0) |
| Group-A `safety.mdx` FR body md5 (onecable, lite, lite-144hz, flip, expand, one-4k, one-4k-oled) | `252d38c7` — byte-identical ×7 |
| Same 7 products, EN body md5 | `b709f7d9` ×7 — **FR sharing group == EN sharing group** |
| `dual-flip/safety.mdx` FR body md5 | `cffcd1c8` (own EN group `7b08b090`) — correctly *not* pooled with Group A |
| `display-settings` FR body md5 (onecable, flip, dual-flip, expand) | `ec24415c` ×4, EN `467551f5` ×4 — groups match |
| `img`/`video` `src` tokens, FR vs EN display-settings | byte-identical (0-line diff) |
| Line counts FR vs EN, all 5 safety pairs | equal (28/28, 28/28, 26/26, 26/26, 30/30) |

The md5 grouping matters for this audit's reach: auditing the canonical `onecable/safety.mdx`
provably covers the other six Group-A products, because the FR bodies are byte-identical and their
EN counterparts are byte-identical too. No product-specific drift can hide inside the group.

---

## 1 · `fr/manuals/onecable/safety.mdx` vs `en/manuals/onecable/safety.mdx`

Canonical. Body shared byte-identically with `lite`, `lite-144hz`, `flip`, `expand`, `one-4k`, `one-4k-oled`.

### Flagged lines

| # | EN line | FR line | Literal back-rendering of the FR | Divergence | Severity |
|---|---|---|---|---|---|
| 1.1 | *(L13)* "They **ensure** safe **operation** and extend the lifespan of your Screenmate." | "Elles **garantissent** une **utilisation** sûre et prolongent la durée de vie de votre Screenmate." | "They **guarantee** safe **use** and extend the lifespan of your Screenmate." | `garantir` is a stronger commitment verb than *ensure* — in a safety/warranty-adjacent sentence it reads as a promise rather than a consequence. `operation` (how the device runs) → `utilisation` (how the user uses it) shifts the subject of the safety claim slightly. Instruction to the reader is unchanged (both say: read these first). | Minor |
| 1.2 | *(L18)* "…suitable for the **correct** amperage." | "…adaptée à l'**ampérage requis**." | "…suited to the **required** amperage." | *correct* → *requis*. Same operational meaning (match the amperage the device needs); FR is marginally more determinate than the vaguer EN. No change to what the reader must check. | Minor |

### Cleared explicitly (highest-risk lines, checked and found faithful)

- **L16 item 2** — "Only use the included AC/DC adapter as power supply" → `Utilisez uniquement l'adaptateur CA/CC fourni comme alimentation.` `uniquement` follows the verb and governs the noun phrase `l'adaptateur CA/CC fourni`: the restriction lands on *which adapter*, exactly as EN. `fourni` (= included) is present — the restriction is to the **supplied** adapter, not to AC/DC adapters generally.
- **L19 item 5** — `5&nbsp;V`/`20&nbsp;V`/`±2&nbsp;V` — all three figures, both bounds and the tolerance sign, match EN character-for-character. `entre … et …` is inclusive-range, as EN "between … and …".
- **L20 item 6** — see §7 regression check R1.
- **L22 item 8** — "Do not use liquids **or** aggressive cleaning agents" → `N'utilisez pas de liquides **ni** de produits de nettoyage agressifs.` The `ne … pas … ni …` frame negates **both** conjuncts. A `ou` here would have been readable as "not (A or B) — but one of them is fine"; `ni` is unambiguous. Correct. Adjective order `doux et sec` for EN "dry, soft" is French-obligatory ordering, not a meaning change — not flagged.
- **L23 item 9** — both clauses carry their own full `ne … pas`; neither instruction rides on the other's negation.
- **L24 item 10** — negation is correctly confined to the first clause (`Ne faites pas tomber`), with `protégez` positive, mirroring EN "Do not drop … **and** protect …". A French reader is not told "do not protect the screen".
- **L25 item 11** — "Keep ventilation openings clear" → `Maintenez les ouvertures de ventilation dégagées` (keep them *unobstructed*, not "clean") — correct sense of *clear*.
- **L27 item 13** — `-20&nbsp;°C` / `60&nbsp;°C`, sign and both bounds correct.
- **L28 item 14** — EN impersonal "when not in use" → FR impersonal `lorsqu'il n'est pas utilisé`. (Contrast infinity-lite/panorama, where EN switches to "when you are not using it" and FR correctly switches to `lorsque vous ne l'utilisez pas` — the EN person-shift is mirrored, not flattened.)
- **Frontmatter** — `title`/`description` translated; `icon` unchanged; the four sibling link keys (`de_link`, `en_link`, `it_link`, `nl_link`) present and all pointing at the same product+page.

**Coverage: all 18 content lines of `fr/manuals/onecable/safety.mdx` checked** (2 translatable frontmatter values + 1 H2 + 1 intro paragraph + 14 numbered items). Ordered list `1.`–`14.`; EN is also ordered `1.`–`14.` — numbering style and warning order match, no item reordered, none added, none dropped.

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor (1.1 is a §10-locked string; 1.2 is stylistic-determinate).

---

## 2 · `fr/manuals/dual-flip/safety.mdx` vs `en/manuals/dual-flip/safety.mdx`

Same 14 instructions as §1, but **bulleted** in EN and **bulleted** in FR — list style matches its own EN base, and this file is correctly *not* pooled into Group A.

### Flagged lines

| # | EN line | FR line | Literal back-rendering of the FR | Divergence | Severity |
|---|---|---|---|---|---|
| 2.1 | *(L13)* "They ensure safe operation…" | "Elles garantissent une utilisation sûre…" | as 1.1 | Same instance of finding 1.1 (locked §10 string, propagated). | Minor |
| 2.2 | *(L18)* "…suitable for the correct amperage." | "…adaptée à l'ampérage requis." | as 1.2 | Same instance of finding 1.2. | Minor |

All other lines are character-for-character the same French as the audited canonical text (verified by reading, not assumed), so every clearance in §1 applies here identically, including the `ni` double-negation at L22 and the confined negation at L24.

**Coverage: all 18 content lines of `fr/manuals/dual-flip/safety.mdx` checked.** Bullet count 14 = EN bullet count 14; order identical.

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor (both are the §1 findings recurring — not new defects).

---

## 3 · `fr/manuals/infinity/safety.mdx` vs `en/manuals/infinity/safety.mdx`

### Flagged lines

| # | EN line | FR line | Literal back-rendering of the FR | Divergence | Severity |
|---|---|---|---|---|---|
| 3.1 | *(L13)* "…to avoid risks **such as** electric shock or fire." | "…afin d'éviter tout risque d'électrocution ou d'incendie." | "…in order to avoid **any risk of** electrocution or fire." | EN presents shock/fire as **examples** of a larger risk set (open list); FR presents them as **the** risks (closed list). The action demanded is identical ("read the guidelines carefully"), so no reader acts differently; the loss is the open-endedness of the hazard set. Note the internal tension: glossary §6 lists `such as → tel qu'un… / par exemple`, while §10 **locks** the shipped closed-list form. §0 rule 3 (shipped wins) resolves in favour of the current text. | Minor |
| 3.2 | *(L19)* "…suitable for the correct amperage." | "…adaptée à l'ampérage requis." | as 1.2 | Same instance of finding 1.2. | Minor |

### Cleared explicitly

- **L13** — "Always use this product in a safe and responsible way" → `Utilisez toujours ce produit de manière sûre et responsable.` `toujours` retained (EN "Always"); modality is imperative in both.
- **L15 H3** — EN "Check before use" → `À vérifier avant utilisation` ("what to check before use"). EN's *check* sense is preserved, and it is distinct from the sibling files' EN headings (see §4, §5) — the FR mirrors the EN heading variation instead of harmonising it away.
- **L18** — "Use **only** an AC/DC adapter as power supply" → `Utilisez uniquement un adaptateur CA/CC comme alimentation.` `uniquement` governs `un adaptateur CA/CC`. Note the deliberate contrast with the onecable text: onecable says *the included* adapter (`l'adaptateur … fourni`), infinity/infinity-lite/panorama say *an* adapter (`un adaptateur`) — the FR reproduces the EN definite/indefinite split rather than levelling it. Second sentence ("Place it in a well-ventilated area, away from heat sources") kept in the same item, same order.
- **L19** — `correctement mise à la terre` — the *properly* adverb is present (see R3).
- **L20** — "The **required** DC input is between 5V and 20V (±2V)" → `L'entrée CC **requise** est comprise entre 5&nbsp;V et 20&nbsp;V (…±2&nbsp;V)`. Both bounds, tolerance and the *required* modality preserved.
- **L21** — "Avoid humid spaces and dust build-up" → `Évitez les espaces humides et l'accumulation de poussière` — `Évitez` governs both conjuncts.
- **L22** — "Protect the screen against impact and external pressure" → `contre les chocs et la pression extérieure` — *external* correctly attaches to *pressure* only, as in EN.
- **L23** — "Do not use sharp objects **on or around** the screen" → `N'utilisez pas d'objets tranchants sur l'écran **ou à proximité**.` The negation covers both locations; `à proximité` = *around/nearby*, not a weaker "near-ish". No partial-negation leak.
- **L24** — "Suitable for both home and business use" → `Convient à un usage domestique comme professionnel.` `A comme B` carries EN's *both … and* (inclusive, not alternative). §10-locked string.
- **L25, L26** — temperature figures and the "turn off when not in use" impersonal form both match EN.

**Coverage: all 15 content lines of `fr/manuals/infinity/safety.mdx` checked** (2 frontmatter + H2 + intro + H3 + 10 bullets).

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor (both recurrences of locked/known classes).

---

## 4 · `fr/manuals/infinity-lite/safety.mdx` vs `en/manuals/infinity-lite/safety.mdx`

### Flagged lines

| # | EN line | FR line | Literal back-rendering of the FR | Divergence | Severity |
|---|---|---|---|---|---|
| 4.1 | *(L13)* "…to avoid risks **such as** electric shock or fire." | "…afin d'éviter tout risque d'électrocution ou d'incendie." | as 3.1 | Same instance of finding 3.1 (locked §10 string). | Minor |
| 4.2 | *(L19)* "…suitable for the correct amperage." | "…adaptée à l'ampérage requis." | as 1.2 | Same instance of finding 1.2. | Minor |

### Cleared explicitly

- **L13** — EN here says "in a safe and responsible **manner**" where infinity says "**way**"; FR renders both `de manière sûre et responsable`. The EN variance is cosmetic and carries no meaning, so harmonising it is not a fidelity loss (recorded as EN-source observation E2).
- **L15 H3** — EN "Read this before use" → `À lire avant utilisation` (*to be read*), distinct from infinity's `À vérifier` (*to be checked*) and panorama's `Avant utilisation`. The three-way EN heading split is faithfully reproduced three ways.
- **L17–L25** — identical French to §3 items 1–9; all §3 clearances apply, including the `uniquement` scope at item 2, the grounding adverb at item 3, the 5–20 V / ±2 V figures at item 4, the both-locations negation at item 7 and the *both … and* at item 8.
- **L21 item 5** — EN says "dust **accumulation**" here vs "dust **build-up**" in infinity/panorama; FR uses `l'accumulation de poussière` for all three. Same referent; no divergence.
- **L26 item 10** — EN switches to the personal "when **you are not using it**"; FR correctly switches with it: `lorsque vous ne l'utilisez pas` (vs `lorsqu'il n'est pas utilisé` where EN is impersonal). Person-shift mirrored, negation intact, `vous` register per glossary §2.

**Coverage: all 15 content lines of `fr/manuals/infinity-lite/safety.mdx` checked.** Ordered list `1.`–`10.` in both languages; order identical.

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor (recurrences).

---

## 5 · `fr/manuals/panorama/safety.mdx` vs `en/manuals/panorama/safety.mdx`

### Flagged lines

| # | EN line | FR line | Literal back-rendering of the FR | Divergence | Severity |
|---|---|---|---|---|---|
| 5.1 | *(L13)* "…to avoid risks **such as** electric shock or fire." | "…afin d'éviter tout risque d'électrocution ou d'incendie." | as 3.1 | Same instance of finding 3.1 (locked §10 string). | Minor |
| 5.2 | *(L19)* "…suitable for the correct amperage." | "…adaptée à l'ampérage requis." | as 1.2 | Same instance of finding 1.2. | Minor |

### Cleared explicitly

- **L15 H3** — "Before use" → `Avant utilisation` — the bare EN heading, rendered bare.
- **L17–L26** — identical French to §3/§4 for the shared ten items; all clearances carry over. EN "Protect the screen **from** impacts" (vs infinity's "**against** impact") is a null EN variance; FR `contre les chocs` in both.
- **L24** — EN here says "home and **professional** use" where infinity/infinity-lite say "home and **business** use"; FR uses `domestique comme professionnel` for all three. `professionnel` covers both EN words in this register; the §10 lock is on the "business" wording and the shipped FR satisfies both (EN-source observation E3).
- **L28 H3** — "Folding caution" → `Précaution lors du pliage` — *caution* as a precaution heading, not as an "Attention!" alarm; matches EN's neutral heading severity. No severity inflation (EN has no `<Warning>`/`<Note>` component here and FR adds none).
- **L30 pinch hazard** — "Watch your fingers when folding the screens **in or out** to avoid pinching." → `Attention à vos doigts lorsque vous **repliez ou dépliez** les écrans, afin d'éviter tout pincement.` Back-renders as "Mind your fingers when you fold the screens in or unfold them, so as to avoid any pinching." **Both directions of the hazard are present** (`repliez` = fold in, `dépliez` = fold out), matching EN's "in or out". Severity marker matches: EN uses a bare imperative sentence, FR uses the §6-locked `Attention à vos doigts` with no added bold/callout. This is the one in-scope line whose scope was narrowed on the *installation* page in a prior round (deliberately, because that EN line says only "when folding"); the **safety** page correctly keeps the two-direction scope. Verified as correct here.

**Coverage: all 17 content lines of `fr/manuals/panorama/safety.mdx` checked** (2 frontmatter + H2 + intro + H3 + 10 bullets + H3 + 1 paragraph). Both H3 sections present, in EN order.

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor (recurrences).

---

## 6 · `fr/manuals/onecable/display-settings.mdx` vs `en/manuals/onecable/display-settings.mdx`

Canonical. Body shared byte-identically with `flip`, `dual-flip`, `expand`.

### Flagged lines

| # | EN line | FR line | Literal back-rendering of the FR | Divergence | Severity |
|---|---|---|---|---|---|
| 6.1 | *(L32)* "…go to 'Display orientation' ('Beeldschermstand') and choose **'Flipped'** to correct this." | "…allez dans «&nbsp;Orientation de l'affichage&nbsp;» et choisissez «&nbsp;**Paysage (inversé)**&nbsp;» pour corriger cela." | "…go to 'Display orientation' and choose **'Landscape (flipped)'** to correct this." | FR adds the `Paysage` qualifier that bare EN 'Flipped' lacks — an **addition** relative to EN, but a correcting one: 'Flipped' is not a Windows option label, whereas `Paysage (inversé)` is the label a French user actually sees. Cross-checked against siblings: DE does the same (`Querformat (gedreht)`), IT keeps the literal (`Capovolto`), NL source says `Gespiegeld` (= *mirrored*, wrong feature). Already adjudicated in `backtranslation-review-fr.md` row 3 as an EN-source quirk; FR is the more actionable text. **No FR action** — fix `en/`. | Minor (informational; FR is the correct side) |
| 6.2 | *(L13, L16–L18, L23 — 6 sites)* Dutch UI glosses in parentheses: `('Beeldscherminstellingen')`, `(Identificeren)`, `(Bureaublad uitbreiden naar dit beeldscherm)`, `(Schaal en indeling)`, `(Schaal)` | FR carries **no** parenthetical gloss; the French UI label alone. | e.g. "Right-click on your desktop and choose **Display settings** to open the display configuration." | Content present in EN is **omitted** in FR. Deliberate and uniform localisation: the glosses exist to help a Dutch-UI reader map English labels, and are noise for a French-UI reader. Adjudicated previously (fixes-fr S-06, BT row 10) as correct localisation. Recorded here for completeness because it is, strictly, an omission. **No FR action.** | Minor (informational) |

### Cleared explicitly — UI strings (the load-bearing part of this file)

Every French UI label was checked against the French Windows/macOS interface, not just against the English words:

| EN label | FR label | Assessment |
|---|---|---|
| **Display settings** | **Paramètres d'affichage** | correct FR Windows label; bold preserved |
| 'Extend desktop to this display' | «&nbsp;Étendre le Bureau à cet écran&nbsp;» | matches the EN wording literally and the FR Windows wording |
| 'Identify' | «&nbsp;Identifier&nbsp;» | correct |
| 'Display orientation' | «&nbsp;Orientation de l'affichage&nbsp;» | correct |
| 'Scale and layout' / 'Scale' | «&nbsp;Échelle et disposition&nbsp;» / «&nbsp;Échelle&nbsp;» | correct; `150&nbsp;%` figure unchanged |
| System Settings | Réglages Système | correct FR macOS pane name |
| Displays | Moniteurs | correct FR macOS pane name (previously adjudicated, S-04) |
| Arrangement | Disposition | correct FR macOS control |
| 'Rotation' / 'Standard' | «&nbsp;Rotation&nbsp;» / «&nbsp;Standard&nbsp;» | correct; unchanged where FR macOS keeps the English-identical term |

Also cleared: all three `alt=` texts (instruction content preserved, same step order, Dutch glosses dropped per 6.2); both video fallback strings (`Votre navigateur ne prend pas en charge la balise vidéo.` — §10-locked); the four macOS steps in EN order with no step added or dropped; both "Screen upside down?" prompts (`Écran à l'envers&nbsp;?`) present, in EN positions; "Want to extend your workspace?"; "Need more overview?" (§6-locked shipped form); "Select the relevant screen" → `Sélectionnez l'écran concerné`; H2 headings for Windows and macOS; guillemets + `&nbsp;` typography per glossary §3/§4 (deliberate FR divergence from EN's straight quotes, not a content change). `img`/`video` `src` URLs and query tokens are byte-identical to EN (verified by diff).

**Coverage: all 22 content lines of `fr/manuals/onecable/display-settings.mdx` checked** (2 frontmatter + 2 H2 + 3 `alt` texts + 3 bold prompts + 4 prose paragraphs + 4 macOS steps + 2 video fallbacks + the 2 upside-down fix paragraphs). Non-content JSX (`className`, `controls`, `type`) and media URLs verified unchanged.

**Verdict: PASS.** 0 Critical, 0 Major, 2 Minor — both informational, both with the corrective action on the **EN** side.

---

## 7 · Regression checks (explicitly requested)

### R1 — the 5 V power-restriction sentence: `uniquement` scope

**Checked. Correct.**

- EN: `Only use the device **with** a 5V power source via the appropriate cable.` The restriction attaches to the prepositional phrase — *what you may power it from* — not to the device.
- FR as shipped (`fr/manuals/onecable/safety.mdx:20`, `fr/manuals/dual-flip/safety.mdx:20`):
  `Utilisez l'appareil **uniquement avec** une source d'alimentation de 5&nbsp;V via le câble approprié.`
  `uniquement` sits **after** the direct object `l'appareil` and immediately **before** `avec …`, so it scopes the prepositional phrase. Back-renders as "Use the device only with a 5 V power source" — same restricted constituent as EN.
- The previously defective form `Utilisez **uniquement l'appareil** avec…` ("use only the device with…") is **absent** from the corpus — grep for it returns nothing; every Group-A file carries the fixed sentence.
- **Propagation verified, not assumed:** the sentence exists in 8 FR files (7 Group-A + `dual-flip`); Group-A bodies are byte-identical (`252d38c7` ×7) so the fix cannot have landed on some and not others, and `dual-flip` was read line-by-line. The 3 remaining in-scope products (`infinity`, `infinity-lite`, `panorama`) correctly do **not** carry this EN item at all — their EN sources have no such line, so its absence in FR is fidelity, not omission.
- Consistency cross-check: the same `uniquement`-after-verb pattern is used correctly at item 2 (`Utilisez uniquement l'adaptateur … fourni` — restricting *which adapter*) and item 8 (`Nettoyez l'écran uniquement avec un chiffon doux et sec` — restricting *what you clean with*). All three restrictions land on the constituent EN restricts. No `ne … que` variant was introduced anywhere, so there is no second, differently-scoped pattern in play.

### R2 — partial negations: EN negation scope preserved

**Checked. Correct; no regression.**

- The four sites fixed in the prior round (`tous les X ne … pas` → `les X ne … pas tous`) are all in `installation.mdx` files (`infinity`, `one-4k`, `lite`, `lite-144hz`) — outside this file set. A corpus-wide sweep of `fr/` for `tous les … ne` / `toutes les … ne` returns **0 hits**, so the fix has not regressed anywhere, in scope or out.
- Within the six audited files, **every** negated instruction was scope-checked individually:
  - `N'utilisez pas de liquides **ni** de produits de nettoyage agressifs.` — `ne … pas … ni …` negates both conjuncts; EN "or" under negation is correctly rendered as `ni`, not `ou`. **No partial negation.**
  - `Ne touchez pas l'appareil avec les mains mouillées **et ne** l'utilisez pas dans des environnements humides.` — two independent full negations; the second does not depend on the first.
  - `**Ne** faites **pas** tomber le moniteur **et protégez** l'écran contre les chocs, la pression ou les objets tranchants.` — negation confined to clause 1; clause 2 positive, as EN. The three-item list under `protégez` is affirmative in both languages.
  - `N'utilisez pas d'objets tranchants sur l'écran **ou à proximité**.` (×3 files) — negation covers both locations; the reader is not left thinking "near the screen is fine".
  - `lorsqu'il **n'**est **pas** utilisé` / `lorsque vous **ne** l'utilisez **pas**` — full `ne … pas` in both variants, each matching its EN person.
- No dropped `ne` (informal spoken-French elision) anywhere in the six files; no negation added where EN has none; no EN negation dropped.

### R3 — grounding / earthing clause keeps the "properly" adverb

**Checked. Correct.**

`Assurez-vous que la prise de courant est **correctement** mise à la terre et adaptée à l'ampérage requis.`
The adverb `correctement` is present and attaches to `mise à la terre`, exactly as EN "properly grounded". Verified present in all five in-scope files (`onecable:18`, `dual-flip:18`, `infinity:19`, `infinity-lite:19`, `panorama:19`) and, for completeness, in all eleven FR `safety.mdx` files corpus-wide. The second conjunct (`et adaptée à l'ampérage requis`) is intact in every instance — the clause was not truncated to the grounding half. Matches the glossary §5 lock `grounded → mis à la terre`, example `une prise de courant correctement mise à la terre`.

---

## 8 · EN-source observations (not counted against the French)

| # | Where | Observation |
|---|---|---|
| E1 | `en/manuals/onecable/safety.mdx` items 5 & 6 (+ 7 Group-A products + dual-flip) | Item 5 states the monitor "operates on a DC input **between 5V and 20V**"; item 6 states "Only use the device with a **5V** power source". As written, item 6 forbids most of the range item 5 permits. FR mirrors both faithfully, so the tension is inherited, not introduced. Worth a client ruling — this is the highest-value EN fix in the safety set. |
| E2 | `infinity` vs `infinity-lite`/`panorama`, L13 | EN alternates "in a safe and responsible **way**" / "…**manner**" for the same sentence. Null variance; FR renders both `de manière sûre et responsable`. |
| E3 | `infinity`/`infinity-lite` vs `panorama`, item 8 | EN alternates "home and **business** use" / "home and **professional** use". FR renders both `domestique comme professionnel`. |
| E4 | all `display-settings` pages | **'Flipped' is not a Windows option label**; the English UI string is "Landscape (flipped)". Already on the client list; FR (and DE) silently supply the correct label. |
| E5 | `infinity` item 6 | EN "impact" (singular) vs siblings' "impacts". Null variance; FR uses `les chocs` throughout. |
| E6 | `en/manuals/onecable/display-settings.mdx` | File ends without a trailing newline (FR has one) — hence the 52-vs-51 line count. Cosmetic, non-content. |
| E7 | `infinity` / `infinity-lite` / `panorama` H3 | Three different EN headings for the same ten-item list ("Check before use" / "Read this before use" / "Before use"). FR mirrors all three distinctly rather than harmonising — correct behaviour, but the EN inconsistency is worth a client note. |

---

## 9 · Coverage statement

| File | Content lines checked | Method |
|---|---|---|
| `fr/manuals/onecable/safety.mdx` | **all 18** | line-aligned against EN, each line back-rendered |
| `fr/manuals/dual-flip/safety.mdx` | **all 18** | line-aligned against EN |
| `fr/manuals/infinity/safety.mdx` | **all 15** | line-aligned against EN |
| `fr/manuals/infinity-lite/safety.mdx` | **all 15** | line-aligned against EN |
| `fr/manuals/panorama/safety.mdx` | **all 17** | line-aligned against EN |
| `fr/manuals/onecable/display-settings.mdx` | **all 22** | line-aligned against EN + FR OS-UI label verification |
| **Total** | **105 content lines** | plus frontmatter link-key integrity, list numbering/order, media URLs, `alt` texts, callout severity |

By byte-identity of the shared bodies, this also covers `lite`, `lite-144hz`, `flip`, `expand`,
`one-4k`, `one-4k-oled` safety chapters and `flip`, `dual-flip`, `expand` display-settings chapters.
Out of scope and not audited here: `infinity` and `infinity-lite` `display-settings.mdx`, which have
their own distinct bodies.

Checked and found clean across all six files: numbers, units and signs (5 V, 20 V, ±2 V, −20 °C,
60 °C, 150 %); modality (every EN imperative is a FR imperative; no *must* → *should* or
*should* → *may* slippage; no *devrait*/*peut* introduced where EN commands); warning order (no item
moved); component severity (no `<Note>`/`<Warning>` added, removed or changed — none of the six files
uses one); added content (none beyond finding 6.1); omitted content (none beyond finding 6.2);
frontmatter link keys (4 sibling languages on every FR page, all paths product- and page-correct).

---

## 10 · Verdicts

| File | Critical | Major | Minor | Verdict |
|---|---|---|---|---|
| `fr/manuals/onecable/safety.mdx` | 0 | 0 | 2 | **PASS** |
| `fr/manuals/dual-flip/safety.mdx` | 0 | 0 | 2 (recurrences) | **PASS** |
| `fr/manuals/infinity/safety.mdx` | 0 | 0 | 2 (recurrences) | **PASS** |
| `fr/manuals/infinity-lite/safety.mdx` | 0 | 0 | 2 (recurrences) | **PASS** |
| `fr/manuals/panorama/safety.mdx` | 0 | 0 | 2 (recurrences) | **PASS** |
| `fr/manuals/onecable/display-settings.mdx` | 0 | 0 | 2 (informational) | **PASS** |

**Distinct defect classes: 5** — (1.1) `garantissent` for *ensure*; (1.2) `requis` for *correct* amperage;
(3.1) closed-list rendering of *risks such as*; (6.1) FR supplies a Windows label EN lacks;
(6.2) Dutch UI glosses dropped. Findings 1.1, 3.1 and 6.2 sit on locked/adjudicated text.

**Recommended follow-ups (none blocking, none unilateral):**

1. **EN-side, worth raising with the client:** E1 (5 V vs 5–20 V contradiction) and E4 ('Flipped').
   Both are English defects that FR either mirrors faithfully or silently corrects.
2. **Optional glossary §12 proposals**, if the client wants the last shade of fidelity:
   `Elles **assurent un fonctionnement** sûr…` for 1.1 — note the prior round already downgraded a
   guarantee-flavoured verb elsewhere for exactly this reason (F3-06, `gage de` → plain benefit
   statement), so this would be consistent with an established precedent; and
   `…afin d'éviter tout risque, **tel qu'une électrocution ou un incendie**` for 3.1, which would also
   resolve the §6-vs-§10 tension on *such as*. Both touch §10-locked strings and frozen byte-identical
   groups (7 files and 3 files respectively), so neither should be applied without sign-off and a
   full-group re-propagation.
3. **Nothing to fix in the French for handoff.** The safety chapters are semantically faithful.
