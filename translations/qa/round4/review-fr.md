# Round 4 — French fix wave: independent review

**Date:** 2026-08-12 · **Branch:** `round4-fixes` · **Reviewer:** FR round-4 verification pass
**Diff under review:** `git diff ebbda95..HEAD -- fr/ translations/glossary-fr.md`
**Commits in FR scope:** `aea5af3` (fix), `6c3cf8c` (docs). `bd2b490`, `290c8b4`, `1cf7bbf`, `ed87722`,
`605570c`, `fd77217` touch `de/`/`it/` only — out of scope, not reviewed.

**Verdict: NEEDS FIXES — 1 required change.** Everything else passes. The fix log is
substantially accurate: every "fixed" claim maps to a real hunk, and 18 of 18 sampled
"rejected"/"source-flagged" classifications were confirmed correct against `en/` (and `nl/` where it
disambiguates). No target defect was found misattributed to the source — the highest-severity miss
this review was chartered to catch did not occur.

| Severity | Count |
|---|---|
| Critical | 0 |
| Important | 1 |
| Minor | 8 |

---

## 1 · Verdict per check

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Meaning fidelity of every changed line | **PASS with 1 Important** | 59 changed lines read against `en/` line-by-line; NL consulted on 12 of them. Sole regression: I-1 below. |
| 1a | The 9 `… ? … alors` sites | **8 PASS / 1 FAIL** | 8 are intra-sentence and idiomatic without `alors`. Site #2 (`onecable/installation.mdx:44`) is cross-paragraph → I-1. |
| 1b | `l'entrée S6-R` → `l'option` | **PASS** | `en/manuals/infinity/display-settings.mdx:78` and `en/manuals/infinity-lite/display-settings.mdx:104` both read "choose the **S6-R / Screenmate** entry". `l'option` is the right call. |
| 2 | Glossary §5.2 interference split, both sides | **PASS** (see M-5) | EM sense correct and untouched ×8; power sense changed ×1 in the right place. |
| 3 | Structure — headings / steps / list items / table rows / components / images | **PASS** | Skeleton identical in all 31 files; 59 added / 59 deleted, no net line change anywhere. |
| 4 | Frozen `safety.mdx` | **PASS** | `git diff a0525eb..HEAD -- 'fr/manuals/*/safety.mdx'` → empty. |
| 5 | Shared `display-settings` bodies | **PASS** | 4 FR bodies all `ec24415c0551ca0628b4f8b22c7a6bdc`; 4 EN bodies all `467551f5a59279929d98a427fcdce9d0`. Sharing groups still congruent. |
| 6 | Twin parity | **PASS** | FR twin divergences exactly mirror EN twin divergences in both pairs. |
| 7 | Conventions — register, DNT, numbers, SI spacing, `&nbsp;` | **PASS** | No tutoiement; all 42 DNT token counts unchanged; no bare space before `? : ; !` or inside `« »` in any added line. |
| 8 | Glossary edits justified; §12 proposals unapplied | **PASS with 2 Minor** | All 5 edits traceable to a proven error or a documented split. R4-P1…P7 verified still present verbatim in `fr/` — no page edits behind them. |
| 9 | French quality of the new strings | **PASS** | 33 new strings read; all idiomatic. No new translationese introduced. |
| — | Gate + tests (fixlog §6.1/§6.2 claims) | **PASS, reproduced** | `verify_translation.py --base en --targets fr --include-nl` → `0 FAIL, 0 WARN`; `pytest tests/test_verify_translation.py -q` → 20 passed. |
| — | Residual greps (fixlog §6.6) | **PASS, reproduced** | `alors` → 1 hit (`panorama/installation.mdx:66`, the conjunction `alors que`); `Vérifiez si`, `transfert vidéo`, `rétablir tous les réglages`, `Cela se fait`, `prend en charge la charge`, `recevoir de l'alimentation`, `l'entrée` → 0 hits each. |
| — | Counts in fixlog header | **ACCURATE** | 31 files, 59 changed lines / 60 replacements (one line in `onecable/troubleshooting.mdx` carries two). |

### Detail: check 3 (structure)

Per-file structural skeleton (heading levels, list markers, ordered-step markers, table pipes, JSX
component and `<img>` openers, with indentation preserved) extracted at `ebbda95` and at `HEAD` and
compared: **identical in all 31 files.** Heading *text* also byte-identical in all 31 — no heading was
reworded. No frontmatter key was touched (`title`, `description`, `en_link`, `nl_link`, `de_link`,
`it_link` all unchanged), so the cross-language link graph is intact. `git diff --numstat` shows
**59 added / 59 deleted** with every file balanced 1:1, 2:2, 3:3 or 4:4 — arithmetic proof that no
line was added or removed, only replaced.

### Detail: check 2 (the §5.2 interference split)

Both sides verified independently.

**EM side — correct and untouched.** `en/manuals/*/safety.mdx:26` ×8 (`onecable`, `lite`,
`lite-144hz`, `flip`, `expand`, `one-4k`, `one-4k-oled`, `dual-flip`): *"Limit exposure to strong
magnetic fields or transmitting equipment to prevent interference."* This is unambiguously EM
interference and `interférences` is the correct French. All 8 FR lines still read
`…afin d'éviter les interférences.` and all 8 files are inside the frozen set — confirmed unchanged
by check 4. The glossary's "×8 safety files" figure is exact.

**Power side — the only site.** `en/manuals/panorama/installation.mdx:66` is the sole non-safety
`interference` in the EN corpus, and it describes a second charger and the Panorama both feeding the
laptop. `interférences` there did point the French reader at the wrong phenomenon. The change is
correctly scoped to one line. See M-5 for a reservation about the *replacement* wording.

### Detail: check 6 (twins)

`lite` / `lite-144hz` — after normalising the product name and image-path tokens, the FR pair differs
in exactly the places the EN pair differs: image path segments, `index.mdx:19` (the 144 Hz intro
sentence) and `index.mdx:34` (`60 Hz` vs `144 Hz`). `installation.mdx` and `osd.mdx` bodies are
otherwise identical, and both received the identical edit. The `taux de rafraîchissement rapide →
élevé` fix landing only in `lite-144hz` is correct: `lite/index.mdx` has no refresh-rate sentence,
matching `en/manuals/lite/index.mdx:19`.

`one-4k` / `one-4k-oled` — same result. The `osd.mdx` edits (`apparaît en surbrillance jaune`,
`Maintenez enfoncé le bouton…`) landed identically in both. The `alors` fix being `one-4k`-only is
correct and not drift: `en/manuals/one-4k-oled/installation.mdx` genuinely has no *"Need extra
power?"* paragraph — the EN pair diverges at exactly the same offset (EN lines 33–37 vs 33).

### Detail: check 7 (conventions)

- **Register.** `\b(tu|ton|ta|tes|toi)\b` → 0 hits across all 31 changed files. `vous` intact.
- **DNT.** All 42 tokens from `translations/dnt.json` counted across `fr/` at `ebbda95` and at
  `HEAD`: **every count identical.** No DNT term was translated, dropped, or introduced. Spot-checked
  in-hunk: `Mini-HDMI`, `RESET`, `ASPECT`, `WIDE`, `HDR`, `Power Delivery`, `DisplayPort`,
  `Lite 144 Hz`, `USB-C`, `USB-A`, `HDMI`, `Screenmate`, `OSD` all survive the rewrites verbatim.
- **Numbers / SI.** Added lines carry `5&nbsp;V/2&nbsp;A`, `5&nbsp;V/3&nbsp;A`, `10&nbsp;W`,
  `45&nbsp;W`, `144&nbsp;Hz`, `étape&nbsp;5` — `&nbsp;` before every unit *symbol*, per §4.
  `**10 secondes**` and `609 grammes` keep a plain space, correct because the unit is spelled out
  (consistent with the fixlog's own rejected items 9 and 17). `15,6"` keeps the French decimal comma.
- **Double punctuation.** Every added line uses `&nbsp;` before `?`, `:` and `;` and inside `«&nbsp;…&nbsp;»`.
  Grep for a bare space before `? : ; ! »` or after `«` in added lines → **0 hits.** Bare colons that
  do appear are ratio separators (`4:3`, `16:9`), which is correct.

### Detail: check 8 (glossary)

Five edits, all justified:

1. **§5.2 row split, `interference`** — justified by a proven meaning error, correctly scoped.
2. **§5.2 row added, `receive power (a port)` → `recevoir du courant`** — justified and, better than
   the fixlog claims, corroborated by the NL source: `nl/manuals/onecable/controls.mdx:17,47` read
   `kan ook stroom ontvangen` / `ontvangt alleen stroom` (`stroom` = *courant*). The row is right.
3. **§6 row corrected, `Then proceed to step 5`** — legitimate under §0 precedence rule 3. Note the
   table's ✗ column now holds the *previously locked* form; the original ✗ example
   (`Alors procédez à l'étape 5`) is gone. Acceptable table maintenance, flagged only so nobody
   later mistakes the old locked string for a wrong-from-the-start example.
4. **§6.1 new ruling** — well-argued and matches what shipped, but its defect grep is defective (M-2).
5. **§6.2 new ruling** — all three bans check out. `vérifier si` = *find out whether*; `rétablir X à Y`
   has no French preposition; `basculer` in the *switch between modes* sense is intransitive. All
   three shipped rewrites conform.

**§12 proposals R4-P1…R4-P7 — verified as proposals only.** Every locked string named in the
proposals table was grepped in `fr/` at `HEAD` and found **present, verbatim, unchanged**:
`Pour une utilisation économe en énergie…` ×4 (`dual-flip`, `expand`, `flip`, `onecable` `index.mdx`);
`devrait vous avoir mené` ×1 (`fr/manuals-index.mdx:114`); `écran portable triple` ×4
(`expand/index.mdx:3,19`, `panorama/index.mdx:3,19`); `Lumière bleue faible` ×2
(`expand/osd.mdx:65`, `flip/osd.mdx:63`); `Évitez … afin d'éviter` ×10, `comme alimentation` ×10,
`garantissent une utilisation sûre` / `ampérage` ×10 across `*/safety.mdx`. **No page edit sits behind
any proposal.** The one `afin d'éviter` duplicate that *was* rewritten (fix #33) is in
`infinity-lite/installation.mdx:66`, not in a `safety.mdx` — correctly outside the R4-P5 scope.

---

## 2 · Findings

### Critical — none.

### Important

#### I-1 · `fr/manuals/onecable/installation.mdx:44` — dropping `alors` severed a conditional that spans a paragraph break

This is the one site of the nine where "keep the question, drop `alors`" does not hold, because the
question and its answer are **separate paragraphs**, not one sentence.

Shipped now (lines 42–44):

```
Vous n'avez qu'un seul port USB sur votre ordinateur portable&nbsp;?

Branchez l'autre câble USB sur une prise de courant.
```

Both source languages carry an explicit connector across that break:

- `en/manuals/onecable/installation.mdx:44` — *"**Then** connect the other USB cable to a power outlet."*
- `nl/manuals/onecable/installation.mdx:44` — *"Sluit **dan** de andere USB-kabel aan op het netstroom."*

`alors` was the only thing scoping the imperative to the one-USB-port case. As a free-standing
paragraph, `Branchez l'autre câble USB sur une prise de courant.` reads as an unconditional
instruction — a reader with two USB ports, who has already followed the two-cable instructions above,
is now told to plug a cable into the mains as well. That is a change in instruction semantics, not a
style change, and it is the reverse of the pass's stated principle that restructuring "would change
the sentence type the EN source uses".

The §6.1 model the ruling cites as precedent does not license this case: at
`fr/manuals/onecable/installation.mdx:62`, `Pas de chargeur USB-C&nbsp;? Utilisez un adaptateur
secteur approprié.` is a **same-sentence** pairing, where adjacency alone carries the condition.

**Required fix** (restores the conditional without reintroducing the banned `alors` rhythm):

```
Dans ce cas, branchez l'autre câble USB sur une prise de courant.
```

`Dans ce cas, …` is idiomatic French, is not the `alors` calque, and is the standard French device for
exactly this cross-paragraph question-answer pattern. Merging the two paragraphs into one and keeping
the bare imperative would also work, but that changes the paragraph structure and would trip check 3.

If this fix is applied, §6.1 should gain a one-line carve-out: *the rule applies within a sentence;
across a paragraph break, replace `alors` with `Dans ce cas`, do not delete it.*

### Minor

#### M-2 · The §6.1 defect grep cannot catch the form in I-1, and half of it is dead code

The regression guard published in the glossary is:

```
grep -rnE '\?\*{0,2}&nbsp;\? [^.]*\balors\b|&nbsp;\?[^|]*\balors\b' fr/
```

Reproduced against `ebbda95` (pre-fix): the full expression finds **8** lines; the **first alternative
alone finds 0**. It requires a literal `?` immediately before optional asterisks before `&nbsp;?`,
which never occurs in the corpus — it is dead. Only the second alternative does any work.

More importantly the pattern is single-line, so it never saw site #2 — the very site that turned out
to be I-1. The guard will not catch a regression of it either. Suggested replacement, run with
`-z`/multiline or as a two-pass grep, so the paragraph-break form is covered:

```
grep -rnzE '&nbsp;\?[^|]*\balors\b|&nbsp;\?\n\n[^\n]*\balors\b' fr/
```

#### M-3 · `flip/installation.mdx:76`, `dual-flip/installation.mdx:50` — the null-variance collapse went against the NL tiebreaker

Fixlog §1.3 #13 justifies rewriting `Cela se fait facilement via le port USB-A…` as
`Le port USB-A de votre ordinateur portable convient parfaitement pour cela.` on the grounds that EN's
two variants are null variance. EN's variance is real —
`en/…/dual-flip/installation.mdx:50` and `en/…/flip/installation.mdx:76` say *"This can easily be done
via your laptop's USB-A port"*, `en/…/expand/installation.mdx:63` says *"The USB-A port on your laptop
works well for this"* — but **NL is uniform and says "easily" in all three**:

- `nl/manuals/dual-flip/installation.mdx:50` — *"Dit kan **gemakkelijk** via de USB-A-poort van je laptop."*
- `nl/manuals/flip/installation.mdx:76` — *"Dit kan **gemakkelijk** via de USB-A-poort van je laptop."*
- `nl/manuals/expand/installation.mdx:63` — *"…dit kan **gemakkelijk** via de USB-A-poort van je laptop."*

So the EN-expand wording is itself the drifted variant, and the collapse target was taken from it.
`convient parfaitement` (*is perfectly suited*) drops `gemakkelijk`/*easily* on two more pages. The
prescriptive content of the Note is unaffected, so this is Minor. A drift-free collapse that still
kills the impersonal-passive-plus-`via` translationese:

```
Le port USB-A de votre ordinateur portable permet de le faire facilement.
```

Not required for merge, but if `expand` is ever retouched, the three should collapse onto *that*
sentence rather than the current one.

#### M-4 · `panorama/installation.mdx:66` — `conflit d'alimentation` specifies a mechanism neither source states

The change is a net improvement — French `interférences` genuinely reads as EMI and the old line
misdirected the reader. But the new wording is more specific than either source:

- EN:66 — *"may cause **interference**"* (vague)
- NL:66 — *"kan dit **storingen** veroorzaken"* (= *disturbances / malfunctions*, generic)

`un conflit d'alimentation` names a power-negotiation conflict, which is the plausible physics but is
an editorial inference, and the glossary now locks that inference as a term. A rendering that keeps
the source's vagueness while still avoiding the EMI reading would be
`peut provoquer des perturbations` or `…des dysfonctionnements`. Recommend either softening the FR to
one of those, or raising it to the client as an EN/NL wording defect (the sources should say what they
mean) rather than resolving it inside the French. Flagged for the record; not blocking.

#### M-5 · `infinity-lite/installation.mdx:50` — `angle d'inclinaison` renames the property

EN:50 *"set it to the correct **support angle**"*; NL:50 *"stel deze af op de juiste
**ondersteuningshoek**"*. Both name a *support* angle; the FR now names a *tilt* angle. `angle d'appui`
was correctly identified as a non-collocation, and no French phrasing of "support angle" is idiomatic,
so this is the pragmatic repair and it does not mislead — the stand's adjustable property *is* its
inclination. Recorded so the substitution is visible, not to reverse it.

#### M-6 · `panorama/controls.mdx:27` — `écran précis` shifts *individual* to *specific*

EN:27 *"connect your laptop to an **individual** screen"*; NL:27 *"…met een **los** beeldscherm"*
(= *a separate screen*). `écran individuel` was rightly rejected (it reads *personal/private*), but
`précis` means *specific* rather than *separate/one of the three*. `l'un des écrans` or `un écran
donné` would sit closer to the source. Low impact — in context the reader is looking at three
Mini-HDMI ports and the meaning lands either way.

#### M-7 · Fixlog §1.3 #18 documents a dash that the shipped edit removed

The row claims *"The `–` was left as U+2013 because EN uses U+2013 here."* The shipped edit at
`infinity-lite/controls.mdx:51,55` drops the dash entirely
(`Basculement vers la gauche – règle…` → `Basculez vers la gauche pour régler…`). The edit itself is
correct and faithful to `en/manuals/infinity-lite/controls.mdx:51,55`; only the log entry is stale.
Correct the fixlog row so a later reader does not go looking for a dash that is not there.

#### M-8 · Two further intentional collapses, recorded for traceability

Neither is a defect; both are places where the FR now stops mirroring an EN per-file wording, and
both should be visible to whoever maintains EN↔FR parity.

- **`RESET` bullet, 3 files.** `en/…/flip/osd.mdx:55` says *"return all settings to **their** factory
  defaults"* while `en/…/dual-flip/osd.mdx:55` and `en/…/expand/osd.mdx:57` say *"restore all settings
  to factory defaults"*. FR now ships one form for all three. No meaning change.
- **`transmission vidéo`, 6 hunks.** EN alternates *video transfer* (`dual-flip/controls.mdx:19,23,27`,
  `expand/controls.mdx:25,26,27`) and *video transmission* (`flip/controls.mdx:19,20,21`). FR now
  ships `transmission vidéo` everywhere. Correct French, and the right direction — but it is a
  harmonisation, not a mirror.

#### M-9 · `onecable/index.mdx:19` drops the "connection" node

EN:19 *"with just one **cable connection**"*; NL:19 *"met slechts één **kabelaansluiting**"*. FR now
reads `à l'aide d'un seul câble`. `connexion par câble` was a genuine calque and the replacement is
the right register for a product one-liner; the dropped noun carries no information the sentence
needs. Recorded only because it is a §5.2-adjacent locked-phrase area.

---

## 3 · Sampled "rejected" / "source-flagged" items — all classifications confirmed

18 items checked directly against `en/` (13 source-flagged, 5 rejected). **All 18 correct. No target
defect found misattributed to the source.**

| Item | Claim | EN evidence | Verdict |
|---|---|---|---|
| **S1** | 5 V vs 5–20 V contradiction is EN's | `en/…/onecable/safety.mdx` item 5 *"operates on a DC input between 5V and 20V"* vs item 6 *"Only use the device with a 5V power source"* | **Correct** — genuine EN self-contradiction, correctly the corpus's only Critical |
| **P1** | infinity button mapping incomplete in EN | `en/…/infinity/controls.mdx:45-46` documents only *right = increase backlight* / *left = decrease volume* | **Correct** — no way to lower brightness or raise volume, in EN |
| **P4** | infinity-lite plural screens is EN's | `en/…/infinity-lite/installation.mdx:13` *"both extension screens"* vs `index.mdx:19` *"one extra portable display"* | **Correct** |
| **P9** | `l'écran se recharge` referent is EN's | `en/…/one-4k/installation.mdx:16`, `one-4k-oled:17` *"the screen automatically charges"*; NL:17 *"wordt het scherm automatisch opgeladen"* | **Correct**, and stronger than claimed — the defect is in NL too |
| **H1** | reverse-charging under a "Charging the OneCable" heading | `en/…/onecable/installation.mdx:51` heading vs `:60` *"Your laptop is now being charged"* | **Correct** |
| **H2** | *Color Accuracy* mislabels a gamut figure | `en/…/onecable/index.mdx:102,122`, `lite:35`, `lite-144hz:35`, `dual-flip:45` — all `Color Accuracy | % sRGB` | **Correct** |
| **H3** | the flip/expand tab split runs opposite ways | `en/…/flip/index.mdx:47` `Color Gamut` / `:66` `Color Accuracy`; `en/…/expand/index.mdx:50` `Color Accuracy` / `:69` `Color Gamut` | **Correct** — the inversion is real |
| **H8** | "clamped tightly" is EN's | `en/…/expand/installation.mdx:34` *"so your screen is clamped tightly"* | **Correct** |
| **H11** | speakers plural/singular split is EN's | `en/…/infinity/index.mdx:19` *"built-in speakers"* vs `controls.mdx:19` *"a built-in speaker"* | **Correct** |
| **H12** | panorama documents off but not on | `en/…/panorama/controls.mdx:31` *"Long press (1 second): Switch the monitor off"*, no on | **Correct** |
| **D3** | `Day Mode` / `Night Mode` leaked into alt text in EN | `en/…/onecable/installation-windows.mdx:40-41` | **Correct** — FR faithfully renders `mode jour` |
| **D6** | colour temperature described as intensity in EN | `en/…/lite/osd.mdx:42`, `lite-144hz:42` *"adjust the overall color intensity"*; FR `l'intensité globale des couleurs` | **Correct**, FR faithful |
| **D16** | `1× USB` is not a port type, in EN | `en/…/infinity/installation.mdx:36` *"1× USB-C & 1× USB & 1× HDMI"*; FR:36 `1 USB-C, 1 USB et 1 HDMI` | **Correct**, FR faithful |
| **Rej. 2** | `Paysage (inversé)` — FR is the correct side | `en/…/onecable/display-settings.mdx:32` *"choose 'Flipped'"*; FR:32 `«&nbsp;Paysage (inversé)&nbsp;»` | **Correct** — already adjudicated, FR supplies the real Windows label |
| **Rej. 6** | RTS/FPS stay English | `en/…/lite/osd.mdx:30-31`; FR:30-31 keeps `Real-Time Strategy (RTS)` / `First-Person Shooter (FPS)` | **Correct** per §7.1 and `dnt.json` |
| **Rej. 19** | `### 3 × ports Mini-HDMI` | `en/…/panorama/controls.mdx:25` `### 3 × Mini HDMI Ports` | **Correct** |
| **Rej. 29** | ASCII hyphen in `**Luminosité -**` | `en/…/onecable/controls.mdx:60` `**Brightness - (Left screen)**` — ASCII hyphen in EN | **Correct** |
| **Rej. 30** | `Attention&nbsp;:` + `prenez garde à vos doigts` | `en/…/panorama/installation.mdx:32` *"**Caution:** Watch your fingers…"* — both elements present, so the doubled "Attention" was rightly avoided | **Correct** |

Two additional coverage checks on the source-flag boundary:

- `grep -rn "\bentry\b" en/` returns **exactly 2** hits, and both received the `l'option` fix. No
  `l'entrée` remains anywhere in `fr/`. Coverage complete, no half-applied fix.
- The `interference` classification is complete in both directions: 9 EN occurrences total, 8 EM
  (safety, unchanged) + 1 power (panorama, changed). Nothing was missed and nothing was over-applied.

---

## 4 · Required before merge

1. **I-1** — `fr/manuals/onecable/installation.mdx:44`: restore the conditional across the paragraph
   break. `Branchez l'autre câble USB sur une prise de courant.` →
   `Dans ce cas, branchez l'autre câble USB sur une prise de courant.`
   Add the one-line carve-out to glossary §6.1 in the same commit.

Everything else in this review is advisory. Recommended but not blocking, in priority order:
**M-2** (fix the §6.1 defect grep so the paragraph-break form is guarded), **M-7** (correct the stale
dash claim in fixlog §1.3 #18), **M-4** (decide whether `conflit d'alimentation` stands or the client
is asked to fix EN/NL), **M-3** (note the preferred collapse target for the USB-A Note).

Re-run after the I-1 edit: `python scripts/verify_translation.py --base en --targets fr --include-nl`
and the two structural checks in §1 (skeleton compare, `--numstat` balance).

---

## 5 · Read-only attestation

This review mutated exactly one path: `translations/qa/round4/review-fr.md` (this file). No commit, no
index change, no branch or HEAD movement, no edit to any `fr/`, `en/`, `nl/` or `translations/` source
file. All comparisons against `ebbda95` and `a0525eb` were made with `git show` / `git grep` /
`git diff` against those revisions, never by checking them out.

---

# 6 · Fix-round verification — commit `8eab711`

**Scope:** re-review of `git show 8eab711` only, against the 9 findings raised above. Read-only, as before.

**Verdict: APPROVED.** All 9 findings correctly resolved. No remaining issues, no new drift.
The required change I-1 is applied exactly as specified; two Minors were resolved *better* than
proposed (M-2, M-3); one of my own recommendations was wrong and the fixer was right to reject it.

| Finding | Disposition claimed | Verified | Result |
|---|---|---|---|
| **I-1** | `Dans ce cas, branchez…`, paragraphs separate, §6.1 carve-out, other 8 sites untouched | yes | **RESOLVED** |
| **M-2** | my suggested single-expression grep rejected as unworkable; replaced by a two-pass guard | yes, reproduced both ways | **RESOLVED — fixer correct, reviewer was wrong** |
| **M-3** | flip/dual-flip follow NL; expand keeps its own EN; EN drift logged as D19 | yes | **RESOLVED — better than proposed** |
| **M-4** | `conflit d'alimentation` stands; client-flag F1 added | yes | **RESOLVED** |
| **M-5** | recorded only (fixlog §7.7) | yes | **Defensible** |
| **M-6** | `écran précis` → `l'un des écrans` | yes | **RESOLVED** |
| **M-7** | fixlog §1.3 #18 dash claim corrected | yes | **RESOLVED** |
| **M-8** | recorded only (fixlog §7.7) | yes | **Defensible** |
| **M-9** | recorded only (fixlog §7.7) | yes | **Defensible** |

## 6.1 · I-1 — resolved

`fr/manuals/onecable/installation.mdx:44` now reads
`Dans ce cas, branchez l'autre câble USB sur une prise de courant.`

Byte-level check with `cat -A` confirms the **paragraphs stay separate** — blank lines at 41, 43 and
45, so line 42 (the question) and line 44 (the answer) remain distinct blocks and block parity with
`en/manuals/onecable/installation.mdx:42,44` holds. The conditional is restored, and the banned
`alors` rhythm is not reintroduced.

`grep -rn "Dans ce cas" fr/` returns **exactly 1 hit**, the intended line. The phrase was not
sprayed across the corpus.

**§6.1 carve-out present** (`translations/glossary-fr.md`, new subsection *"The carve-out: the rule
applies inside a sentence only"*). It states the rule, gives the EN:44 / NL:44 evidence, gives a
✗/✓ pair with the paragraph break marked, and records the 8-intra-sentence / 1-cross-paragraph
split. It also correctly rejects merging the two paragraphs as an alternative repair, on
block-parity grounds — the same reason I gave.

**The other 8 sites are untouched and still correct.** Re-read all 8 at `HEAD`:
`onecable/installation.mdx:30`, `onecable/installation-mac.mdx:51`, `onecable/troubleshooting.mdx:41`,
`lite/installation.mdx:25`, `lite-144hz/installation.mdx:25`, `one-4k/installation.mdx:35`,
`infinity/installation.mdx:42`, `infinity/installation.mdx:48` — all intra-sentence, all still in the
round-1 form. `grep -rn "alors" fr/` returns 1 hit, `panorama/installation.mdx:66`, the conjunction
`alors que`. Unchanged.

## 6.2 · M-2 — resolved; the fixer's rebuttal is correct and my suggestion was wrong

**I reproduced the fixer's claim and it holds. My M-2 replacement expression was broken; theirs is not.**

Proof that GNU grep's POSIX ERE reads `\n` as a literal `n`:

```
$ printf 'ann\n'    | grep -cE 'a\n\n'   → 1     # matches the literal string "ann"
$ printf 'a\n\nb\n' | grep -czE 'a\n\n'  → 0     # does NOT match a real blank-line break
```

Proof that my suggested cross-paragraph alternative is inert, run against the pre-fix tree
(`ebbda95`, extracted read-only to a scratch dir via `git archive`):

```
$ grep -rlzE '&nbsp;\?\n\n[^\n]*\balors\b' fr/           → 0 files
$ grep -rlzE '<first alt>|&nbsp;\?\n\n[^\n]*\balors\b' fr/ → 7 files, incl. onecable/installation.mdx
```

The 7-file result is exactly the false confidence the fixer describes: with `-z` the *first*
alternative's `[^|]*` spans newlines and matches site #1 in the same file, so
`onecable/installation.mdx` appears in the output for the wrong reason. The diagnosis in the commit
message is precisely right.

The shipped two-pass guard validates cleanly in both directions:

| Pass | On `ebbda95` (pre-fix) | On `HEAD` (post-fix) |
|---|---|---|
| 1 · same-sentence, `grep -rnE` | **8** lines — the 8 intra-sentence sites | **0** |
| 2 · cross-paragraph, `LC_ALL=C.UTF-8 grep -rlzP` | **`fr/manuals/onecable/installation.mdx`** — exactly I-1 | **0** |

Pass 2 **would have caught I-1**, which was the whole point of the finding. The
"do not simplify these back into one expression" warning in the glossary is warranted and should stay.

## 6.3 · M-3 — resolved, and the split is the right reading

The fixer did not apply my proposed three-way collapse; they **un-collapsed** instead, restoring the
per-file EN split. Verified against both sources at `HEAD`:

| Product | NL | EN | FR now |
|---|---|---|---|
| `flip:76` | *"Dit kan **gemakkelijk**…"* | *"This can **easily** be done…"* | `permet de le faire facilement` |
| `dual-flip:50` | *"Dit kan **gemakkelijk**…"* | *"This can **easily** be done…"* | `permet de le faire facilement` |
| `expand:63` | *"…dit kan **gemakkelijk**…"* | *"…**works well** for this."* | `convient parfaitement pour cela` |

**This is the better resolution and I withdraw my proposed collapse.** My M-3 assumed the three
should end up identical; that was wrong. Because EN-expand genuinely differs, collapsing all three
would have flattened a real EN variance — the opposite of what the corpus does everywhere else it
mirrors a genuine per-file EN split (H2/H3 the Color Accuracy/Gamut inversion, H4 the two "first
check which ports" headings, D9 the two-vs-three sources count). The E2/E3 "null variance" precedent
does not apply, because the variance is not null. The fixer's reading of EN/NL is exactly correct.

`source-flags-fr.md` **D19** is present and accurate: it names EN-expand as the drifted side, cites
all three NL lines, and carries the forward instruction — *if EN-expand is repaired to say "easily",
collapse the three French sentences onto the `facilement` form.* That leaves the eventual cleanup
unambiguous. `grep -rn "convient parfaitement pour cela" fr/` returns **1 hit**,
`expand/installation.mdx:63`, the intended deliberate survivor.

## 6.4 · M-4, M-6, M-7 — resolved

- **M-4.** `source-flags-fr.md` gains section **F** (*"French is more specific than both sources"*)
  with **F1** on `panorama/installation.mdx:66`. It quotes EN *"interference"* and NL *"storingen"*,
  states plainly that `conflit d'alimentation` is an editorial inference rather than a source claim,
  notes the glossary now locks that inference, and offers the client both exits (repair EN/NL, or
  soften to `des perturbations` / `des dysfonctionnements`). That is exactly the disposition I asked
  for. The page and glossary are correctly left as-is pending the ruling.
- **M-6.** `panorama/controls.mdx:27` now reads `…pour connecter votre ordinateur portable à **l'un
  des écrans**.` against EN:27 *"an **individual** screen"* and NL:27 *"een **los** beeldscherm"*.
  Both sources mean *one of the three panels*, which is what `l'un des écrans` says — closer to
  source than `précis` and idiomatic French. `grep -rn "écran précis" fr/` returns 0.
- **M-7.** Fixlog §1.3 row #18 now states the dash is removed entirely and that this is faithful to
  `en/manuals/infinity-lite/controls.mdx:51,55`. Documentation-only, correctly scoped — no page edit
  rode along with it.

## 6.5 · M-5, M-8, M-9 — recorded-only dispositions are defensible

All three are logged in fixlog **§7.7** with the reasoning, and in each case the disposition matches
the conclusion I reached myself:

- **M-5** (`angle d'inclinaison`) — kept, because `angle d'appui` is a non-collocation and no
  idiomatic French rendering of *support angle* exists. Recorded rather than reversed. Correct.
- **M-8** (the `RESET` bullet and `transmission vidéo`) — kept as harmonisations of genuinely null
  EN variance, with an explicit note flagging them to whoever maintains EN↔FR parity. Correct, and
  the note is the right artefact.
- **M-9** (`à l'aide d'un seul câble`) — kept. Correct.

None of the three was quietly dropped; each is traceable in the log.

## 6.6 · Scope and no-new-drift

**Files touched — 7, all in scope:** `fr/manuals/dual-flip/installation.mdx`,
`fr/manuals/flip/installation.mdx`, `fr/manuals/onecable/installation.mdx`,
`fr/manuals/panorama/controls.mdx`, `translations/glossary-fr.md`,
`translations/qa/round4/fixlog-fr.md`, `translations/qa/round4/source-flags-fr.md`.
**Nothing outside `fr/` + `glossary-fr.md` + `qa/round4/*-fr.md`.** No `en/`, `nl/`, `de/`, `it/`,
`docs.json`, `dnt.json` or script was touched.

**All 4 changed lines re-checked against EN and NL** (§6.1, §6.3, §6.4 above) — every one now sits
closer to its source than before. **No new meaning drift.**

Mechanical re-checks, all reproduced independently:

| Check | Result |
|---|---|
| `git diff --numstat 8eab711^..8eab711 -- fr/` | **1 added / 1 deleted in each of 4 files** — replacements only |
| Structural skeleton + heading text, 4 files | **identical** before/after |
| Heading-count parity FR↔EN | **62 of 62 pages match** (61 under `fr/manuals` + `fr/manuals-index.mdx`), 0 mismatches |
| `git diff a0525eb..HEAD -- 'fr/manuals/*/safety.mdx'` | **empty** — frozen safety still frozen |
| `display-settings` 4-group body md5 | `ec24415c0551ca0628b4f8b22c7a6bdc` ×4, still congruent with EN `467551f5…` ×4 |
| Register / DNT / `&nbsp;` before double punctuation, added lines | **clean** — no tutoiement, no bare space before `? : ; ! »` |
| `verify_translation.py --base en --targets fr --include-nl` | **0 FAIL, 0 WARN** |
| `pytest tests/test_verify_translation.py -q` | **20 passed** |
| Both new defect greps, current tree | **0 hits each** |

The fixlog's revised counts in §7.8 are arithmetically consistent with the diff: 60 + 4 = **64
replacements**, still across the same **31 files** (all four round-2 files were already in the
round-1 set), and the §7 supersession banner at the top of the file resolves the round-1/round-2
count ambiguity cleanly.

## 6.7 · Read-only attestation (fix round)

This re-review mutated exactly one path: `translations/qa/round4/review-fr.md` (this file). `HEAD`
is `8eab711` on `round4-fixes`, unmoved; no commit, no index change, no branch operation, no
`git worktree`. The pre-fix tree was inspected by extracting `git archive ebbda95 fr/` into the
session scratchpad, which does not touch the repository. `git status` for the review scope
(`fr/`, `translations/glossary-fr.md`) is **clean**; the untracked `review-de.md` / `review-it.md`
and the modified `glossary-de.md` in the working tree belong to the concurrent DE and IT reviewers
and were neither read for this verdict nor altered.
