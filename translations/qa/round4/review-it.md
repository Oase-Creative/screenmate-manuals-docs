# Round 4 — Italian fix wave: independent review

**Date:** 2026-08-12 · **Branch:** `round4-fixes` · **Reviewer scope:** `it/**`,
`translations/glossary-it.md` (commits `605570c`, `ed87722`, `290c8b4`) · **Base:** `ebbda95`

**Method:** the diff was verified against `en/` line by line, with `nl/` consulted as tiebreaker.
`fixlog-it.md` and `source-flags-it.md` were treated as unverified claims throughout. 16
"rejected" / "source-flagged" items were re-checked against the English pages directly.

**Verdict: APPROVED** *(as of fix commit `f66e287` — see §12)*. The original verdict on
`bd2b490` was **NEEDS FIXES** — 1 Critical, 2 Important, 4 Minor; §§1–11 below are that review,
left unedited as the record. All six actionable findings were resolved in `f66e287`; one residual
Minor (a bookkeeping count) is recorded in §12 and does not block merge.

The wave is, on the whole, careful and well-evidenced work: structure is untouched, safety is
frozen, the shared bodies still match, the twins are in step, and the great majority of the
"source-inherited" classifications hold up under direct inspection. Three findings need action
before merge; the Critical one is a fix that stopped two pages short of finishing and then locked
the shortfall into the glossary.

---

## 1. Verdict per check

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Meaning fidelity of changed lines | **PASS with 1 Minor** | 51 changed lines in `it/`, each compared to its `en/` line; see §2 |
| 2 | Scaling-prompt split | **FAIL** | Under-inclusive; see F-1 |
| 3 | Structure (headings/steps/lists/rows/components/images) | **PASS** | §3 |
| 4 | Frozen safety | **PASS** | `git diff a0525eb..HEAD -- 'it/manuals/*/safety.mdx'` → empty |
| 5 | Shared display-settings bodies | **PASS** | 4 identical md5s; §5 |
| 6 | Twins (lite pair, one-4k pair) | **PASS** | §6 |
| 7 | Register `tu`, DNT, number/SI formats | **PASS with 1 Minor** | §7 |
| 8 | Glossary edits justified; pages and glossary agree | **PASS with 1 Important** | §8 |
| 9 | Italian quality of new strings | **PASS with 1 Important** | §9 |

`python scripts/verify_translation.py --base en --targets it --include-nl` → **0 FAIL, 0 WARN**,
reproducing the fixlog's claim.

---

## 2. Meaning fidelity

Every one of the 51 changed lines in `it/` was diffed against its English counterpart. No dropped
negation, no dropped quantity, no changed instruction semantics except where noted in F-2.

**The `…? Allora` rewrites.** The brief anticipated 11 sites; there were only ever **4** literal
`Allora` occurrences in `it/` (`git grep -ni allora ebbda95 -- it/`), all 4 fixed, **0** remaining
at HEAD. The fixlog's account — reviewer A counted 11 line references, of which 4 were literal
`Allora` and 7 were plain question-headers — matches the repository. Each of the 4 preserves the
source's question-then-answer structure and its modality:

| Site | EN | NL | IT after | Modality |
|---|---|---|---|---|
| `it/manuals/infinity/installation.mdx:42` | `Then you can connect…` | `Dan kun je…` | `Puoi collegare…` | *can* kept in `Puoi` ✔ |
| `it/manuals/onecable/installation.mdx:30` | `Then additional power supply is needed` | `Dan is een extra stroomvoorziening nodig` | `Serve un'alimentazione aggiuntiva` | necessity kept ✔ |
| `it/manuals/onecable/installation.mdx:44` | `Then connect the other USB cable…` | `Sluit dan de andere USB-kabel aan` | `Collega l'altro cavo USB…` | imperative kept ✔ |
| `it/manuals/onecable/troubleshooting.mdx:41` | `Then use a PD charger of at least 45W` | — | `Usa un caricabatterie PD da almeno 45 W` | quantity + `almeno` kept ✔ |

Dropping the resumptive `Allora` is a legitimate register call: Italian technical prose does not
carry the Dutch `Dan` / English `Then` pick-up adverb after a rhetorical question, and
`one-4k/installation.mdx` already used the bare pattern. Meaning is unaffected in all four.

**Other reworded sentences, spot-verified against EN and NL:**

- `it/manuals/panorama/index.mdx:19` — EN `A required display driver allows three independent
  screens to be driven through one cable.` / NL `Een vereiste display-driver maakt het mogelijk…`.
  The recast (`Per gestire tre schermi indipendenti con un solo cavo è necessario un apposito
  driver dello schermo.`) keeps both the requirement (`è necessario`) and the cable count. ✔
- `it/manuals/expand/index.mdx:19` — EN `unfolds two Full HD displays`; `dispiega` is accurate and
  better than the previous `apre`. ✔
- `it/manuals/dual-flip/index.mdx:19` — EN `unfolds into two extra 16" displays`; `si apre a
  formare` renders `into` without the "cracks open" reading of `si apre in`. ✔
- `it/manuals/dual-flip/controls.mdx:34,38` — EN `Increases brightness in general use, and
  navigates / increases values inside the OSD menu.` Both verbs, both scopes and the descriptive
  third-person voice survive; fronting `all'interno del menu OSD` removes a real scope ambiguity
  (the old ending could be read as governing only `aumenta i valori`). ✔
- `it/manuals/onecable/troubleshooting.mdx:38` — `L'alimentazione` → `L'alimentatore` for EN `The
  power supply is PD-compatible.` NL has the abstract `De stroomvoorziening`, so this is a small
  abstract→device shift, but PD compatibility genuinely attaches to the unit and the glossary
  exception is scoped to this one line. Acceptable. ✔
- `it/manuals/expand/installation.mdx:20` and `it/manuals/infinity/installation.mdx:35` — the
  `1 USB` left unqualified is correct: `en/manuals/infinity/installation.mdx:35` reads
  `1× USB-C & 1× USB & 1× HDMI`, with no `-A`. The fixlog's note is accurate. ✔

---

## 3. Structure — PASS

For all 29 changed files, the count of headings, list items, ordered steps, JSX components, images
and table rows is identical at `ebbda95` and `HEAD`, and so is the total line count. No changed
line is a heading, table row, component or image tag:

```
git diff -U0 ebbda95..HEAD -- it/ | grep -E "^[+-][^+-]" \
  | grep -E "^[+-]\s*(#{1,6} |\||<[A-Za-z]|!\[)"   → no output
```

Five changed lines are list items or numbered steps, all edited **in place** with their markers and
numbering intact (`- 1 USB-C, 1 USB-A e 1 HDMI`; steps `1.`, `5.`, `6.`). Nothing added, removed or
reordered.

---

## 4. Frozen safety — PASS

```
git diff a0525eb..HEAD -- 'it/manuals/*/safety.mdx'   → empty
```

---

## 5. Shared display-settings bodies — PASS

Frontmatter-stripped body hashes, `onecable` / `expand` / `flip` / `dual-flip`:

```
9a7b67c0a2662cc94be8774d99299a9a   (all four, IT)
467551f5a59279929d98a427fcdce9d0   (all four, EN — also mutually identical)
```

Both round-4 edits that land in this body (the `Identify` sentence and the scaling prompt) were
propagated to all four. `infinity` and `infinity-lite` have their own bodies, as expected.

---

## 6. Twins — PASS

- **`one-4k` / `one-4k-oled`** — `en/manuals/one-4k/index.mdx:19` and
  `en/manuals/one-4k-oled/index.mdx:19` carry the identical clause `supports both video and power
  over a single USB-C cable on compatible devices`. Both Italian pages received the identical edit
  to `…tramite un solo cavo USB-C sui dispositivi compatibili`. ✔
- **`lite` / `lite-144hz`** — both received the shared index boilerplate edit. The second
  `lite-144hz` edit (`frequenza di aggiornamento rapida` → `un'elevata frequenza di
  aggiornamento`) has no counterpart in `lite` because the English `lite/index.mdx` has no
  refresh-rate sentence at all. Correct asymmetry. ✔

---

## 7. Conventions — PASS (1 Minor)

- **Register.** Every changed line keeps the `tu` register: `Vuoi…`, `usa`, `Premi`, `Scarica`,
  `Collega`, `riavvia`, `presta attenzione`, `del tuo Screenmate`. One exception, F-4 below.
- **DNT.** No hunk in the entire diff contains the string `DC` (`git diff … | grep DC` → empty), so
  `ingresso DC` and the AC/DC safety strings are untouched. `USB-C`, `USB-A`, `HDMI`, `OSD`,
  `Power Delivery (PD)` all survive the changed lines verbatim.
- **Numbers and SI.** Every numeral in a `+` line is well-formed Italian: `15,6"`, `14"`, `16"`,
  `144 Hz`, `10 W`, `45 W`, `65 W`, `6 mm`, `609 grammi`, `2560 × 1600`, `100.000:1`. Decimal
  comma, thousands point and the space before the unit are all correct and unchanged.

---

## 8. Cross-check of "rejected" / "source-flagged" classifications

16 items re-checked directly against `en/`. **15 confirmed correct, 1 rests on a false premise.**

### Confirmed correct

| Item | Claim | Verified |
|---|---|---|
| §1.4 `Duplicato` | EN page stale, says `Mirrored` | ✔ `en/manuals/infinity-lite/display-settings.mdx:57` = `'Mirrored'`, `:21` = `**Flipped**`. IT renders both glossary-locked targets (§8 line 812–813, which already marks `Mirrored` *superseded*). NL says `Gespiegeld` at **both** lines — so EN is the outlier. Classification correct. See F-5. |
| §2.4 mount hardware | EN/NL divergence, not IT drift | ✔ `en/manuals/expand/index.mdx:29` = `6x protective clips`; `en/manuals/expand/installation.mdx:26` = `protective cap`; NL says `beschermkap` in **both**. IT maps EN 1:1 (`6 clip protettive` / `cappuccio protettivo`). EN is the outlier exactly as claimed. |
| rej #6 `Formato` / `Rapporto d'aspetto` | EN-faithful | ✔ `en/manuals/expand/osd.mdx:34` = `Aspect (ASPECT)`; `en/manuals/flip/osd.mdx:32` = `Aspect Ratio (ASPECT)`. Harmonising IT would flatten a real EN distinction. |
| §1.2 Infinity Lite port map | verbatim EN | ✔ `en/.../controls.mdx:19` `The leftmost bottom port.`; `en/.../installation.mdx:91` `the **third** port` |
| §1.5 Flip ports contradiction | verbatim EN | ✔ `en/manuals/flip/installation.mdx:20` vs `:26` |
| §1.6 "two sources", three listed | verbatim EN | ✔ `en/manuals/flip/osd.mdx:62`, `en/manuals/expand/osd.mdx:64` |
| §1.7 245° annotated 180° | verbatim EN | ✔ `en/manuals/dual-flip/index.mdx:56` |
| §1.8 Panorama HDMI/Mini-HDMI | verbatim EN | ✔ `en/manuals/panorama/installation.mdx:77` |
| §2.1 Color Gamut / Color Accuracy | EN inconsistency | ✔ `en/manuals/flip/index.mdx:47` vs `:66` — same 45% NTSC value, two labels |
| §2.6 speaker count | EN inconsistency | ✔ `en/manuals/infinity/index.mdx:19` plural vs `controls.mdx:19` singular |
| rej #7 `spia della scheda madre` | EN says it | ✔ `en/manuals/onecable/troubleshooting.mdx:15` `motherboard indicator light` |
| rej #19 `gesti` | EN says it | ✔ `en/manuals/infinity/controls.mdx:23` `full gesture reference` |
| rej #20 `pulsante girevole` | EN says it | ✔ same line, `A rotatable button` |
| rej #21 `pagina` / `menu precedente` | EN splits | ✔ `previous page` on dual-flip/expand/flip; `previous menu` on one-4k/one-4k-oled |
| rej #16 `modalità generale` | EN label | ✔ `**General mode**` on lite/lite-144hz `controls.mdx:31,41`; `in general mode` on one-4k |

### Not correct

**rej #17** — see **F-2**.

---

## 9. Findings

### CRITICAL

#### F-1 · The scaling-prompt split is under-inclusive, and the glossary now locks the shortfall

*Files:* `it/manuals/panorama/osd.mdx:49`, `it/manuals/infinity/display-settings.mdx:30`,
`translations/glossary-it.md` §9.10

The mechanical part of the split is exactly as specified and I confirm it:

- EN `Need more overview?` — **6** occurrences (`dual-flip`, `expand`, `flip`, `onecable`
  display-settings L34; `infinity-lite` L23 and L59). All 6 Italian sites now read
  `**Vuoi una visione d'insieme migliore?**`, and no seventh site was touched.
- EN `Want more on-screen space?` — 1 (`en/manuals/infinity/display-settings.mdx:30`).
- EN `Need more room?` — 1 (`en/manuals/panorama/osd.mdx:49`).
- The glossary has one row per EN prompt.

**But the Dutch source contradicts the split.** All eight sites say the same thing in NL:

```
nl/manuals/dual-flip/display-settings.mdx:34      **Behoefte aan meer overzicht?**
nl/manuals/expand/display-settings.mdx:34         **Behoefte aan meer overzicht?**
nl/manuals/flip/display-settings.mdx:34           **Behoefte aan meer overzicht?**
nl/manuals/onecable/display-settings.mdx:34       **Behoefte aan meer overzicht?**
nl/manuals/infinity-lite/display-settings.mdx:23  **Heb je behoefte aan meer overzicht?**
nl/manuals/infinity-lite/display-settings.mdx:59  **Behoefte aan meer overzicht?**
nl/manuals/infinity/display-settings.mdx:30       **Heb je behoefte aan meer overzicht?**
nl/manuals/panorama/osd.mdx:49                    **Meer overzicht nodig?**
```

The body that follows is the same 150%-scaling instruction at all eight sites, in all three
languages. So the original §9.10 collapse was *right* that the three EN prompts say one thing — it
was wrong only about **which** thing. The correct outcome is one row and one target,
`Vuoi una visione d'insieme migliore?`, at all eight sites; instead the wave produced two rows and
left the condemned string on two pages.

`panorama/osd.mdx:49` is the sharp end. EN `Need more room?` does **not** mean "more on-screen
space" — `room` here is room to take things in, which is precisely what NL `Meer overzicht nodig?`
disambiguates. Rendering it `Vuoi più spazio a schermo?` is a target-side narrowing that reproduces
the very inversion §2.1 of the fixlog exists to remove: the reader is promised more screen space and
handed an instruction that gives them less. This is a **target defect classified as
source-inherited** (`source-flags-it.md` §3.1).

`infinity/display-settings.mdx:30` is the softer case — EN literally reads `Want more on-screen
space?`, so the Italian is faithful and the defect is genuinely English's. Flagging it is right.
What is not right is the glossary row that brackets it with `panorama` and declares both
*"faithful to these two EN variants"*: half of that row is a real EN flag, the other half is an
untranslated NL meaning.

The lock is what makes this Critical rather than Important. `translations/glossary-it.md` §9.10 now
records `Vuoi più spazio a schermo?` as the **locked** target for those two prompts, so the next
pass will not correct it — the same failure mode §2.1 identified when it noted the page fix alone
"would have been reverted by the next pass".

**Required fix**
1. `it/manuals/panorama/osd.mdx:49` → `**Vuoi una visione d'insieme migliore?**`.
2. Glossary §9.10: fold `Need more room?` into the `Vuoi una visione d'insieme migliore?` row,
   citing NL `Meer overzicht nodig?`.
3. Leave `infinity/display-settings.mdx:30` as-is but re-word its glossary note so it reads as a
   *pending EN defect* (EN drifted from NL `meer overzicht`), not as a settled faithful rendering.
4. `source-flags-it.md` §3.1: keep the EN recommendation, drop `panorama` from it, and record that
   NL already has the correct prompt at all eight sites — which makes the suggested EN fix a
   revert-to-Dutch rather than an open question.

---

### IMPORTANT

#### F-2 · Rejection #17 rests on an English string that does not exist

*File:* `translations/qa/round4/fixlog-it.md:210-211`; affects `it/manuals/panorama/controls.mdx:38,44`

The fixlog rejects the reviewer's `menu delle scorciatoie` / `menu rapido` harmonisation with:

> EN says `shortcut menu` on one-4k and `quick menu` on panorama; the Italian tracks each.

`quick menu` does not occur anywhere in `en/` — `grep -rn "quick" en/manuals/` returns **nothing**.
The English is the *same term on both products*:

```
en/manuals/one-4k/controls.mdx:51    opens the brightness shortcut menu in general mode.
en/manuals/panorama/controls.mdx:38  Opens the brightness shortcut menu.
en/manuals/panorama/controls.mdx:44  Opens the volume shortcut menu.
```

while the Italian splits it in two:

```
it/manuals/one-4k/controls.mdx:51    apre il menu delle scorciatoie per la luminosità
it/manuals/panorama/controls.mdx:38  Apre il menu rapido della luminosità
```

One EN term, two Italian terms, no source warrant — the reviewer's MAJOR-02 was correct and the
rejection is invalid. (NL is a third variant again, `het helderheidsmenu` / `het volumemenu`, with
no "shortcut" element at all, so `menu rapido` is not traceable to the Dutch either.)

Not a meaning error and not safety-relevant, hence Important rather than Critical — but the
justification is verifiably fabricated, which is the part that matters for a log that exists to be
trusted. The other 15 items I sampled were sound, so I read this as an isolated slip rather than a
pattern; it should still be corrected in the log even if the wording change is deferred.

**Required fix:** pick one target for EN `shortcut menu`, apply it to `one-4k`, `one-4k-oled` and
`panorama` `controls.mdx`, add the glossary row, and correct the rejection entry. (If the change is
deferred, the log entry must still be rewritten — leaving the false EN citation in place would let
a future pass "re-verify" it and reject the finding again.)

#### F-3 · `Toggle` → `Premi` changes the documented hardware gesture, and is now glossary-locked

*Files:* `it/manuals/infinity-lite/controls.mdx:50,54`; `translations/glossary-it.md` §9.9

```
en/manuals/infinity-lite/controls.mdx:50   Toggle left – adjusts the backlight (brightness).
nl/manuals/infinity-lite/controls.mdx:50   Naar links schakelen – aanpassing van de achtergrondverlichting
it/manuals/infinity-lite/controls.mdx:50   Premi verso sinistra – regola la retroilluminazione (luminosità).
```

The grammatical objection to the old `Sposta verso sinistra` is fair — bare `sposta` is a transitive
imperative with no object. But the replacement swaps the physical action: EN `Toggle` and NL
`schakelen` describe flicking a switch sideways, `Premi` describes pressing. English keeps
`Press` (Infinity) and `Toggle` (Infinity Lite) deliberately distinct across the two products, and
NL follows; the Italian now says `Premi` on both, collapsing a distinction the source makes. That is
the opposite of the reasoning applied — correctly — in rejections #17 and #21, where the log's own
rule is "EN splits, the Italian tracks each".

The fixlog's stated rationale ("`premere verso` matches the glossary-locked `Premi a destra /
a sinistra` on the sibling `infinity/controls.mdx`") is a harmonisation argument, but those sibling
strings render EN `Press right ("Plus")` — a genuinely different English verb.

A user told to *press towards the left* on a side-toggle may press it inward rather than flick it.
Now locked in §9.9, so it will propagate.

**Required fix:** keep an object-bearing form that preserves the toggle gesture — e.g.
`Sposta il pulsante verso sinistra –`, `Aziona verso sinistra –`, or the NL-style nominalisation
`Spostamento verso sinistra –` — and amend the §9.9 row accordingly.

---

### MINOR

#### F-4 · `tu` register dropped in the `panorama/osd` rewrite

`it/manuals/panorama/osd.mdx:41`. EN `so you may want to adjust the desktop layout in your
operating system` / NL `dus mogelijk wil je de bureaubladindeling in je besturingssysteem
aanpassen` — both address the reader directly and both carry a possessive. The new Italian
(`quindi può essere utile modificare la disposizione del desktop nel sistema operativo`) drops
both: `you may want` becomes impersonal usefulness, and `your operating system` becomes `il sistema
operativo`. Removing the `potresti voler` calque was right, but glossary §1 mandates the informal
`tu` register and a form that keeps it is available, e.g. `quindi potresti dover modificare la
disposizione del desktop nel tuo sistema operativo`. Meaning is otherwise intact.

#### F-5 · `Duplicato` collides with a real Windows-IT control name — escalate beyond "EN is stale"

`it/manuals/infinity-lite/display-settings.mdx:57`. The classification in `source-flags-it.md` §1.4
is correct as far as it goes (EN is stale; NL says `Gespiegeld` at both sites). But the Italian
lands worse than its English: `Mirrored` is merely a label that does not exist in the Windows
orientation dropdown, whereas `Duplicato` **is** a real Windows Italian control — the multi-monitor
mode *Duplica questi schermi* — so the Italian sends the reader to an existing setting that does the
wrong thing. Pre-existing, not introduced by this wave, and correctly out of scope for a
target-only fix; it deserves flagging to the client at a higher priority than the neighbouring EN
tidy-ups. Note that adopting `Capovolto` here would match NL, glossary §8's own *superseded* note,
and the sibling line 21 — so the EN fix is a revert-to-Dutch, not an open design question.

#### F-6 · Fixlog edit counts do not match the repository

`fixlog-it.md:22` claims *"43 edits across 30 Italian pages + 5 glossary rows"*. The diff contains
**29** changed files under `it/` and **51** changed lines. The glossary row count (5) is right.
Bookkeeping only, but the fixlog is the audit record for this wave.

#### F-7 · `A e B e C` → `A, B e C` diverges from the EN separator

`it/manuals/expand/installation.mdx:20`, `it/manuals/infinity/installation.mdx:35`. EN uses a
uniform `&` between all three items (`1× USB-C & 1× USB & 1× HDMI`). The comma-series is correct
Italian coordination and matches `flip` / `dual-flip`, so I would keep it — recording it only
because it is the one place the wave chose idiom over a mechanical EN separator match, and a future
parity sweep may query it. No action needed.

---

## 10. Things the wave got right, worth recording

- The 6-site `Need more overview?` correction is real, correctly scoped, and correctly propagated
  through the shared 4-product body without breaking its checksum.
- `quale schermo ha quale numero` → `quale numero corrisponde a ciascuno schermo`: exactly 7
  occurrences claimed, exactly 7 present, **0** of the old form left, and the glossary row matches
  the string on the page.
- Index boilerplate: exactly 11 `index.mdx` pages, all carrying the identical new sentence, **0**
  instances of the old calque left, and the §9.9 row matches.
- `spesso` → `ha uno spessore inferiore a` (`expand/installation.mdx:25`) removes a genuine garden
  path (`spesso` = "often" on first reading) with no meaning cost.
- `abbastanza alimentazione` → `potenza sufficiente` (`panorama/installation.mdx:63`) correctly
  applies the existing §5.2 `power (output capability)` → `potenza` mapping.
- `bada alle dita` → `presta attenzione alle dita` (`panorama/installation.mdx:33`) — the old form
  meant "look after your fingers"; the new one matches the frozen `panorama/safety.mdx` without
  echoing the `Attenzione:` lead-in.
- Scope discipline is clean: no `de/`, `fr/`, `nl/` or `en/` file was touched by the two Italian
  commits.

---

## 11. Required before merge

1. **[Critical]** `it/manuals/panorama/osd.mdx:49` → `**Vuoi una visione d'insieme migliore?**`;
   re-fold the `Need more room?` glossary row; re-word the `infinity` note as a pending EN defect;
   update `source-flags-it.md` §3.1 with the NL evidence.
2. **[Important]** Correct fixlog rejection #17 — `quick menu` does not exist in `en/`. Unify the
   Italian for EN `shortcut menu` across `one-4k`, `one-4k-oled` and `panorama`, or defer the
   wording change but fix the log either way.
3. **[Important]** Restore the toggle gesture at `it/manuals/infinity-lite/controls.mdx:50,54` with
   an object-bearing form, and amend glossary §9.9.
4. **[Minor]** Restore `tu` at `it/manuals/panorama/osd.mdx:41`.
5. **[Minor]** Re-file `Duplicato` (§1.4) as a target-affecting client escalation, not a routine EN
   staleness item.
6. **[Minor]** Correct the edit counts at `fixlog-it.md:22` (29 files, 51 lines).

Checks 1, 3, 4, 5, 6 and 7 pass as they stand and need no rework.

---

## 12. Fix-round verification — commit `f66e287`

Scoped re-review of `f66e287` ("fix(it): round-4 review follow-up"), read-only. Verified only that
the findings in §9 were correctly resolved.

**Result: APPROVED.** All six actionable findings resolved; 1 residual Minor (V-1).

### 12.1 Findings resolved

| Finding | Verdict | Evidence |
|---|---|---|
| **F-1** Critical | **RESOLVED** | `grep -rn "Vuoi più spazio a schermo" it/` → **0**. `Vuoi una visione d'insieme migliore?` now at **8** sites: `dual-flip`/`expand`/`flip`/`onecable` display-settings L34, `infinity-lite` L23+L59, `infinity/display-settings.mdx:30`, `panorama/osd.mdx:49`. Glossary §9.10 folded back to **one** row with an NL column and a standing "resolve against the Dutch" ruling plus an explicit *"Do not re-split this row per EN variant"*; §6 lists all three EN strings on the one target. `source-flags-it.md` §3.1 rewritten as the EN finding, with the full 8-site NL/EN table and the revert-to-Dutch recommendation. |
| **F-2** Important | **RESOLVED** | `menu delle scorciatoie` → **0** occurrences; `menu rapido` now uniform across `one-4k/controls.mdx:51-52`, `one-4k-oled/controls.mdx:51-52`, `panorama/controls.mdx:38,44`. Glossary §5.3 row added. The §9.3 heading `Scorciatoie per volume e luminosità` is correctly *retained*: EN itself splits the noun (`### Volume and Brightness Shortcuts`, `en/manuals/one-4k/osd.mdx:25`) from the inline term (`shortcut menu`), so tracking each is the log's own rule, and both rows now cross-reference each other. Rejection #17 struck through with the false `quick menu` citation named. |
| **F-3** Important | **RESOLVED** | `it/manuals/infinity-lite/controls.mdx:51,55` → `Sposta il pulsante verso sinistra/destra –`. Object-bearing (fixing the original grammatical defect) while `spostare` preserves the sideways-flick gesture of EN `Toggle` / NL `Naar links schakelen`. The Press/Toggle split survives: `it/manuals/infinity/controls.mdx:45-46` still reads `Premi a destra/sinistra ("Plus"/"Min")` for EN `Press`. Glossary §9.9 carries an explicit ⚠ against collapsing the two. |
| **F-4** Minor | **RESOLVED** | `panorama/osd.mdx:41` → `può esserti utile … nel tuo sistema operativo`. `esserti` restores the `tu` clitic, `nel tuo` the possessive, matching EN `you may want … your operating system` / NL `wil je … je besturingssysteem`. |
| **F-5** Minor | **RESOLVED** | `source-flags-it.md` §1.4 re-titled **CLIENT ESCALATION**, NL row added (`Gespiegeld` at both lines), and the escalation rationale recorded — `Duplicato` is a real Windows-IT control (*Duplica questi schermi*), so the Italian sends the reader to an existing setting that does the wrong thing, unlike EN `Mirrored` which simply does not exist. EN fix named as a revert-to-Dutch at `en/manuals/infinity-lite/display-settings.mdx:57`. |
| **F-6** Minor | **PARTIALLY RESOLVED** | First-wave figures corrected to **29 files / 51 lines**, which matches the repository exactly. The new cumulative headline is wrong — see V-1. |
| **F-7** | **N/A** | Correctly recorded as "no action needed" and kept. |

### 12.2 No new drift, no scope creep

All **9** changed lines under `it/` re-checked against `en/` and `nl/`; no meaning drift introduced.
The two prompt sites now diverge from their literal EN strings by design, under the §9.10
resolve-against-Dutch ruling, and match NL exactly. The four `menu rapido` lines and the two
`Sposta il pulsante` lines preserve every other element of their sentences (OSD navigation
direction, `in modalità generale`, `Tieni premuto per tornare al menu precedente`, the
`(luminosità)` gloss).

Scope is clean — the commit touches only `it/` (5 files), `translations/glossary-it.md`, and
`translations/qa/round4/{fixlog,source-flags}-it.md`. Nothing under `de/`, `fr/`, `nl/` or `en/`.

Invariants re-run at `f66e287`:

```
git diff a0525eb..HEAD -- 'it/manuals/*/safety.mdx'        → empty
display-settings 4-product body md5                        → 9a7b67c0a2662cc94be8774d99299a9a ×4
python scripts/verify_translation.py --base en --targets it --include-nl  → 0 FAIL, 0 WARN
python -m pytest tests/test_verify_translation.py -q        → 20 passed
```

Twin parity held: `one-4k/controls.mdx` and `one-4k-oled/controls.mdx` received identical edits.

### 12.3 Residual

#### V-1 · Minor — the corrected cumulative counts are themselves off by one

`fixlog-it.md` headline now reads *"59 changed lines across 32 Italian pages + 8 glossary rows"*,
and §7.6 states the fix round *"adds 3 files, 8 lines"*. Measured:

| | Claimed | Actual |
|---|---|---|
| Cumulative `it/` files (`ebbda95..HEAD`) | 32 | **31** |
| Cumulative `it/` changed lines | 59 | **57** |
| Fix round: files new to the round | 3 | **2** (`one-4k/controls.mdx`, `one-4k-oled/controls.mdx`) |
| Fix round: changed lines under `it/` | 8 | **9** |

The first-wave correction (29 files / 51 lines) is right; the arithmetic on top of it is not. Note
that cumulative lines are **not** 51 + 9 = 60 either: three lines were edited twice across the two
waves (`infinity-lite/controls.mdx:51,55` and `panorama/osd.mdx:41`), so the union is 57. The
`### 7.8` line *"none of the 8 edits lands in that body"* should likewise read 9.

Documentation-only, in a QA log rather than shipped content, and every substantive claim in the log
checks out. **Does not block merge** — correct on the next touch of the file.

