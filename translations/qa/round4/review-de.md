# Round 4 — German fix wave: independent review

**Reviewed:** `git diff ebbda95..HEAD -- de/ translations/glossary-de.md` on `round4-fixes`
**DE commits in scope:** `fd77217`, `1cf7bbf`, `bd2b490` (commits touching `fr/` and `it/` excluded)
**Scope:** 41 files under `de/**` (80 changed lines) + `translations/glossary-de.md`
**Review basis:** every changed line re-derived from `en/...`; `nl/...` consulted as tiebreaker.
The fixlog was treated as unverified claims throughout.

**Verdict: NEEDS FIXES** — 0 Critical, 3 Important, 16 Minor.
The translation work itself is sound and the highest-severity risk is clear (see §0). All three
Important items are documentation/escalation defects, not mistranslations, and all three are
cheap to fix. No German body line needs re-translating.

---

## 0. The highest-severity check: was any target defect wrongly flagged as source-inherited?

**No. This review found zero such cases.**

15 items from `source-flags-de.md` and `fixlog-de.md` §C were re-verified by opening the aligned
`en/` line independently: **13 confirmed, 2 partial, 0 wrong.** In every case where the fixlog
claims "the EN says this too, the German is faithful", the EN literally says it. Spot evidence:

| Claim | EN line opened | Verdict |
|---|---|---|
| Safety 5 V vs 5–20 V is EN's | `en/manuals/onecable/safety.mdx:19` `…DC input between 5V and 20V…` + `:20` `Only use the device with a 5V power source…` | CONFIRMED — DE:19–20 render both exactly, incl. `ausschließlich` for "only" |
| "the screen automatically charges" is EN's | `en/manuals/one-4k/installation.mdx:17` (identical at `one-4k-oled:17`) | CONFIRMED — EN really says *screen* |
| infinity-lite "both extension screens" on a 1-screen product | `en/manuals/infinity-lite/installation.mdx:13` | CONFIRMED |
| infinity-lite "the **third** port" undefined | `en/…/installation.mdx:91`; `controls.mdx:17,21` document two | CONFIRMED |
| panorama "the HDMI port" vs `3 × Mini HDMI Ports` | `en/manuals/panorama/installation.mdx:77`; `controls.mdx:25` | CONFIRMED |
| motherboard LED blocks first FAQ answer | `en/manuals/onecable/troubleshooting.mdx:15` | CONFIRMED |
| expand `≡ Menu button` vs `M (Menu)` is EN's | `en/…/controls.mdx:21` vs `en/…/osd.mdx:13` | CONFIRMED |
| lite scroll wheel powers device, "Power" button does not | `en/manuals/lite/controls.mdx:29-33` vs `:39-42` | CONFIRMED |
| panorama `Viewing Angle 360°` | `en/manuals/panorama/index.mdx:43` | CONFIRMED |
| "brightness of the red RGB value" | `en/manuals/lite/osd.mdx:43` | CONFIRMED |
| §C7 `im normalen Gebrauch` renders `in general use`, not `General mode` | `en/manuals/dual-flip/controls.mdx:35` `Increases brightness **in general use**…` | CONFIRMED — rejection sound |
| §C30 flip `um` = "clips **around**", expand `an` = "clips **onto**" | `en/manuals/flip/index.mdx:19` / `en/manuals/expand/index.mdx:19` | CONFIRMED |
| §C25 flip description differs because EN differs | `en/manuals/flip/display-settings.mdx:3` vs `onecable:3` | CONFIRMED |

Two partials, both wording-level in `source-flags-de.md`, not translation defects — see Minor 8 and 9.

---

## 1. Meaning fidelity — PASS (with Minor drift, itemised)

Every one of the 80 changed lines was checked against its EN counterpart. **No dropped negation,
no changed quantity, no changed instruction outcome, no reversed modality in any procedural step.**
Verified spot-checks include `en/manuals/onecable/installation.mdx:17`
(`use the button to extend or retract it` → `fahre ihn mit der Taste aus oder ein` ✓),
`en/manuals/lite/osd.mdx:51` (✓), `en/manuals/panorama/installation.mdx:23`
(`Grip the screens and pull them upwards` ✓), `en/manuals/expand/installation.mdx:42`
(`supports three connection scenarios` → `unterstützt drei Anschlussvarianten` ✓ — in fact *more*
faithful than the `lässt sich auf drei Arten anschließen` it replaced).

Residual drift, all Minor, all in non-procedural product prose — see Minor 1–5.

## 2. The scaling-prompt split — PASS mechanically, Important gap on escalation

Grepped `en/` directly. The correspondence is exact, **line for line**:

| EN prompt | EN occurrences | DE result | Match |
|---|---|---|---|
| `Need more overview?` | `{onecable,dual-flip,flip,expand}/display-settings:34`, `infinity-lite/display-settings:23` and `:59` | `Brauchst du mehr Übersicht?` at the **same six file:line** | ✓ |
| `Want more on-screen space?` | `infinity/display-settings:30` | `Brauchst du mehr Platz?` at `de/…:30` | ✓ |
| `Need more room?` | `panorama/osd:49` | `Brauchst du mehr Platz?` at `de/…:49` | ✓ |

`glossary-de.md` now carries one row per EN prompt (`:1207-1209`) plus an occurrence table. No
`Anzeigeausrichtung` survives anywhere in `de/` (0 hits); `Bildschirmausrichtung` appears 9 times
= 8 body + 1 `alt`, exactly as claimed.

**But see Important 3** — NL, the designated tiebreaker, says *overview* in all eight.

## 3. Structure — PASS

Zero headings, list items, numbered steps, table rows, components (`<Card>/<Tab>/<Note>/<Warning>`)
or images added, removed, or reordered in any of the 41 files. Verified by per-file structural-token
count parity between `ebbda95` and `HEAD`, and by diffing the heading sequence of every changed file.

The heading sequence diff surfaces exactly **two renames**, both intentional, both at the same
ordinal position, both twins edited identically:
`de/manuals/lite/controls.mdx:39` and `de/manuals/lite-144hz/controls.mdx:39`,
`### Power- und Zurück-Taste` → `### Power-/Zurück-Taste`.
Anchor safety checked: no `](#…)` link anywhere in `de/` targets that slug (the corpus has exactly
one intra-page anchor, `de/manuals/infinity/controls.mdx:23` → `#bildschirmmenü-osd`, whose target
`## Bildschirmmenü (OSD)` at `:33` is intact).

## 4. Frozen safety — PASS

```
$ git diff a0525eb..HEAD -- 'de/manuals/*/safety.mdx'   →  0 bytes
```
No safety body was touched. The `safety.mdx` style observations were correctly deferred
(`fixlog-de.md` §D1) rather than applied.

## 5. Shared display-settings bodies — PASS

After frontmatter strip, all four are byte-identical and match the checksum the fixlog claims:

```
onecable / dual-flip / flip / expand  →  23c155f4861fc970c03a1d1f0838886a
```
Cross-checked that the four **EN** bodies are likewise identical (`467551f5…`), so the invariant is
genuine and not an artefact of the German.

## 6. Twins — PASS

`lite` / `lite-144hz` and `one-4k` / `one-4k-oled` received identical edits on every page where the
EN pages agree. Per-page edit counts are equal across each pair (index 1/1, installation 2/2 and 3/3,
controls 1/1 and 0/0, osd 2/2 and 0/0), and the number of product-normalised differing lines is
identical in EN and DE for all four `lite` pages (16/16, 16/16, 26/26, 22/22).

The shared EN sentence `It connects via USB-C or HDMI and supports both video and power over a
single USB-C cable on compatible devices.` (`en/manuals/one-4k/index.mdx:19`, identical at
`one-4k-oled:19`) produced the identical German in both files. Divergence elsewhere on those two
pages tracks a real EN divergence (the OLED panel sentence).

## 7. Conventions — PASS

- **Register:** no `Sie`/`Ihr`/`Ihnen` anywhere in the added lines. `du`/`dein` and the
  non-apocopated imperative (`Drücke`, `Klicke`, `Wähle`, `Greife`, `Stelle`) intact.
- **DNT (`translations/dnt.json`):** every occurrence preserved verbatim in the added lines —
  `Screenmate`, `USB-C`, `USB-A`, `HDMI`, `Power Delivery`, `OSD`, and the OSD literal `LANGUAGE`
  (kept in `dual-flip/osd.mdx:47` and `flip/osd.mdx:47` while the *list contents* around it changed).
- **Numbers / SI:** German decimal comma (`15,6`), thousands dot (`100.000`), spaced multiplication
  (`2560 × 1600`), DIN 5008 unit spacing (`5 V`, `3 A`, `144 Hz`, `609 Gramm`, `150 %`) all intact.
- **Frontmatter:** `nl_link:` and `en_link:` present on all 41 changed pages.
- **Verifier:** `python scripts/verify_translation.py --base en --targets de --include-nl` →
  `0 FAIL, 0 WARN`, reproducing the fixlog's claim.
- **Commit hygiene:** DE commits touch only `de/` + `translations/`; the five FR/IT commits touch
  0 files under `de/`. The glossary meaning fix and the pages it governs did ship in the *same*
  commit (`fd77217` contains both `translations/glossary-de.md` and the display-settings pages).

## 8. Glossary edits — PASS on substance, Important defects in bookkeeping

All five amendments are justified by a demonstrated meaning error, independently confirmed:

| Amendment | Evidence it is a meaning error, not taste |
|---|---|
| `Display orientation` → `Bildschirmausrichtung` | `Anzeigeausrichtung` is not a German Windows string; swept to 0 occurrences, 9 sites updated |
| `Need more overview?` → `Brauchst du mehr Übersicht?` | NL tiebreaker `nl/…:34` `Behoefte aan meer overzicht?` confirms *overview*; `mehr Platz` inverted it |
| `durchsuchen` → `entdecken` | `durchsuchen` = search through/rummage; also contradicted its own card title `Produkte ansehen` (`de/manuals-index.mdx:97`) |
| `Power- und Zurück-Taste` → `Power-/Zurück-Taste` | `en/manuals/lite/controls.mdx:39` `Power & Return **Button**` (singular); house slash-suspension precedent already locked at `glossary-de.md:836` `Menü-/Auswahl-/Bestätigungstaste` |
| OS-label gloss order | German label leading is right — but the execution is half-applied, see Important 2 |

Pages and glossary agree on all five. **But the glossary now contradicts itself, and three
corpus-wide harmonisations went unrecorded — Important 1 and Minor 6.**

## 9. German quality of the new strings — PASS

The round is clearly net positive. Unambiguous wins, each fixing a real defect:

- `Chinesisch (vereinfacht)` — the German language-list convention (matches CLDR / Microsoft
  German). `Vereinfachtes Chinesisch` additionally had a wrongly capitalised attributive adjective
  mid-list. Now consistent across all three OSD pages.
- `Power-/Zurück-Taste` — slash-suspension with hanging hyphen is correct per the amtliches
  Regelwerk (cf. `Ein-/Ausschalter`), and it removes a real ambiguity against EN's singular
  "Button". No collision with the genuinely separate `Power-Taste` on `one-4k` / `panorama`.
- `Drücke die Taste nach links, um die Hintergrundbeleuchtung (Helligkeit) einzustellen.` — the old
  `Nach links drücken – stellt … ein.` was genuinely broken (`stellt` had no subject).
- `Dieser Anschluss nimmt ausschließlich Strom auf und wird **für Folgendes** verwendet:` — correct
  substantivised `Folgendes`; removes a stranded English preposition before a list.
- `etwas Strom` — natural; `eine geringe Menge Strom` was stiff translationese.
- `deines Macs` — correct per Duden (*der Mac, des Macs*).
- `Damit bietet er Gamern und Power-Usern einen zweiten Bildschirm mit flüssiger Darstellung – …` —
  correct dative plurals, correct `Damit` anaphora to the 144 Hz rate, and it genuinely fixes the
  bad collocation `ein flüssiger Bildschirm`.
- `Stelle den Abstand … so ein, wie es für dich am angenehmsten ist.` — correct `so … wie`
  correlative; a large improvement on a 17-word Satzklammer plus the `Nutzungserlebnis` anglicism.
- `Er **bietet** dir …`, `Anschlussvarianten`, `fahre ihn mit der Taste aus oder ein` — all
  idiomatic and on-register.

No new string is ungrammatical and none is a mistranslation. The residual quality issues are
Minor 6–16 below; the recurring pattern is that a few edits replaced correct German with something
no better (M11, M13, M15) or fixed one awkwardness by introducing another (M4, M8, M10).

One point worth stating plainly, because the fixlog overstates it: **`Brauchst du mehr Übersicht?`
is the right target, but not for the reason given.** It is right because it restores fidelity to
the source — `nl/…:34` `Behoefte aan meer overzicht?`. It does **not** make the passage logical:
setting scaling to 150 % shows *less* on screen at once, so "more overview" is as much of a
non-sequitur in German as `mehr Platz` was. The fixlog's framing ("the German reader was being
promised the opposite of what the setting delivers") implies the German is now sound; it is not.
The underlying defect is in the source, exists identically in NL, survives in all eight
occurrences, and is source-flagged in none of them. See Important 3.

---

# Findings

## Important

### I1 — `glossary-de.md` now contradicts itself about the display-settings freeze
`translations/glossary-de.md:1397-1404` (added this round) states the display-settings chapter is
**"no longer byte-frozen at `4792819`"**. The very next paragraph, `:1406`, is unedited and still
reads:

> `Frozen chapters (shipped 4792819): **safety** and **display-settings**, all 17 files.`

Two directly opposed statements, three lines apart, in the file that governs what a future
translator may touch. Whichever a later round reads first decides whether it treats the chapter as
editable or "restores" round 4's corrections. **Fix:** amend `:1406` to name **safety** only, and
point the canonical-body sentence at the new `round4-fixes` body.

### I2 — the OS-label gloss rewrite keeps the one string its own rationale calls useless
The new §9 note argues that on a German page the English label "is not on the screenshot *and* not
in the reader's OS — it is the one label that is guaranteed to help nobody." The fix then places
that exact string in the parentheses:

- `en/manuals/onecable/display-settings.mdx:13` — `**Display settings** ('Beeldscherminstellingen')` — English label + **Dutch** gloss, because the screenshot is Dutch.
- `nl/manuals/onecable/display-settings.mdx:13` — `kies **Beeldscherminstellingen**` — **no gloss at all**; the cited NL precedent drops it when the leading label is the reader's own.
- `de/manuals/onecable/display-settings.mdx:13` (new) — `wähle **Anzeigeeinstellungen** („Display settings“)` — German label + **English** gloss, matching neither the screenshot nor the reader's OS.

This is now the **only** English OS label left anywhere in `de/` (4 hits, all this one line in the
shared body). Every other page — `infinity`, `infinity-lite`, `installation-mac` — was correctly
made German-only in the same round.

The rule is also not swept across the page it governs. `en/manuals/onecable/display-settings.mdx:23`
carries two Dutch glosses (`'Bureaublad uitbreiden naar dit beeldscherm'`, `'Identificeren'`);
`de/…:31` carries none. So within one file, line 13 now adds a gloss the EN has and line 31 omits
two glosses the EN has — the opposite treatment of the same situation.

**Fix (either is defensible, but pick one):** drop the parenthetical entirely, following the NL
precedent the note cites; or keep a gloss and make it the **Dutch** string that is actually visible
in the screenshot. Then apply the choice to line 31 as well.

### I3 — the two surviving `mehr Platz` prompts keep the documented inversion and were never source-flagged
The round's central finding is that `Brauchst du mehr Platz?` followed by "set scaling to 150 % so
text and elements are displayed larger" promises the reader the opposite of what the setting does.
Six occurrences were fixed. The two where the EN wording differs were correctly left alone **per the
letter of the split rule** — but they carry the identical instruction and therefore the identical
inversion:

```
de/manuals/infinity/display-settings.mdx:30  **Brauchst du mehr Platz?**
                                        :31  Klicke auf **Skalierung** und stelle sie auf **150 %** ein, damit Text und Elemente größer dargestellt werden.
de/manuals/panorama/osd.mdx:49               **Brauchst du mehr Platz?** Klicke auf **Skalierung** und stelle sie auf 150 % ein, …
```

And the tiebreaker language contradicts the EN on both:

| Page | EN | **NL (tiebreaker)** | DE |
|---|---|---|---|
| `infinity/display-settings:30` | `Want more on-screen space?` | `Heb je behoefte aan meer **overzicht**?` | `mehr Platz` |
| `panorama/osd:49` | `Need more room?` | `Meer **overzicht** nodig?` | `mehr Platz` |

NL says *overview* in **all eight** occurrences. The EN corpus's three-way variation is EN-side
drift from a Dutch original that never varied. Two consequences:

1. Neither occurrence appears in `source-flags-de.md`. The round diagnosed a meaning inversion,
   fixed it where the EN wording permitted, and then **did not register the two places it could not
   fix** — so a defect the team has already characterised in writing is now invisible to the client
   and to the other four languages.
2. `fixlog-de.md:18-20` claims `nl/` "was consulted wherever the EN wording was itself ambiguous
   (the `Need more overview?` … rows in particular)". Had NL been opened on these two rows, the
   EN/NL divergence would have been unmissable. The verification claim is overstated.

Note also that the *logical* defect is not repaired anywhere, including on the six pages that were
changed: "more overview" does not follow from enlarging text either (see §9). All eight occurrences
inherit a source-side non-sequitur.

**Italian has already diverged from German on exactly these two lines.** Commit `f66e287`
(`fix(it): round-4 review follow-up — resolve scaling prompt against NL`) landed on this branch
while this review was in progress and harmonised **all eight** Italian occurrences to
`Vuoi una visione d'insieme migliore?` — including `it/manuals/infinity/display-settings.mdx:30`
and `it/manuals/panorama/osd.mdx:49`, the two the German kept as `mehr Platz`. Italian resolved
against NL; German resolved against EN. Both are defensible in isolation, but the branch cannot ship
with two sister languages rendering the same source line on opposite principles. This now needs one
owner decision applied across all five languages, which raises the priority of this item.

**Fix:** add all eight occurrences to `source-flags-de.md` with the NL evidence — the two
`mehr Platz` ones for the EN/NL wording divergence, and the family as a whole for the prompt→
instruction mismatch. Recommend EN be harmonised to `Need more overview?` and the wording
reconsidered (e.g. "Is everything too small?"), propagated to all five languages at once. Do not
change the German unilaterally — that would break EN parity.

## Minor

**M1 — "designed to / built to" flattened to plain assertion on five product intros.** EN hedges
these as design intent; the German now asserts them as fact. `en/manuals/onecable/index.mdx:19`
`designed to boost your productivity` → `der deine Produktivität steigert`; likewise
`lite/index.mdx:19`, `lite-144hz/index.mdx:19` (`built to give gamers…` → `Damit bietet er…`),
`panorama/index.mdx:19` (`is designed to massively expand` → `Damit erweiterst du…`). Defensible as
de-translationese — German product copy does assert — and confined to non-procedural prose, so
Minor. Worth a conscious client sign-off since it recurs five times.

**M2 — `infinity-lite/index.mdx:19` upgrades a design claim to a capability claim.**
`en/…:19` `is designed for plug-and-play use with laptops, phones, tablets and game consoles` →
`funktioniert per Plug-and-Play mit Laptops, Smartphones, Tablets und Spielkonsolen`. This is the
strongest member of the M1 family: "designed for" is intent, "funktioniert" is a promise that it
works. The German now guarantees more than the source. Suggest `ist für den Plug-and-Play-Betrieb
mit … ausgelegt` or `ist auf Plug-and-Play-Betrieb ausgelegt`.

**M3 — `panorama/index.mdx:19` loses the driver's enabling modality.** EN: `A required display
driver **allows** three independent screens **to be driven** through one cable.` DE: `Dafür ist ein
Displaytreiber erforderlich: **Er steuert** drei unabhängige Bildschirme über ein einziges Kabel
**an**.` The driver becomes the agent that drives the screens rather than the thing that makes
driving them possible. Suggest `… erforderlich: Erst er macht es möglich, drei unabhängige
Bildschirme über ein einziges Kabel anzusteuern.`

**M4 — `onecable/controls.mdx:17-19`: the two rewrites in this paragraph are the weakest in the round.**
(a) `:19` `en/…:19` `This **is** the main port for connecting your laptop via USB-C.` → `An diesem
**Hauptanschluss** schließt du deinen Laptop über USB-C an.` The sentence's job is to *assert* that
this port is "the main port", because `en/…:53` later says `The main port is for data/video, the
Power port is for power only.` The rewrite demotes that into a presupposition and asserts the action
instead — an action already given two lines above (`Schließe hier das Kabel deines Laptops an.`).
The paragraph now states the connection twice and never tells the reader this is the main port.
Suggest `Das ist der Hauptanschluss für die Verbindung zu deinem Laptop über USB-C.`
(b) `:17` `Über diesen Anschluss empfängt **der Monitor** … und kann **darüber** auch mit Strom
versorgt werden.` — grammatical (`der Monitor` is nominative in both conjuncts), but `Über diesen
Anschluss` already scopes over both, so `darüber` is redundant; and the active/passive diathesis
clash on one subject is the kind of thing the round elsewhere set out to remove. It also introduces
an inconsistency *within the same file*: `:34` retains port-as-subject (`Dieser Anschluss nimmt
ausschließlich Strom auf`), so one paragraph says the monitor receives and the next says the port
does. The `-` line (`Dieser Anschluss empfängt … und kann auch Strom aufnehmen`) was idiomatic —
`Strom aufnehmen` is standard German. At minimum drop `darüber`.

**M5 — two small content shifts.**
(a) `de/manuals/infinity-lite/installation.mdx:58` drops one of EN's two adjuncts:
`en/…:58` `…to suit your preferences **for a better user experience**` → `…so ein, wie es für dich
am angenehmsten ist.` Natural German, but one source element is gone.
(b) `de/manuals/onecable/troubleshooting.mdx:23` explicitates: `en/…:23` `the **dual** USB-A to
USB-C cable` → `das USB-A-auf-USB-C-Kabel **mit zwei USB-A-Steckern**`. The added detail is correct
(EN states it at `:25`) but is not in the line being rendered.
(c) `de/manuals/one-4k/installation.mdx:18` (and `one-4k-oled:18`): `en/…:18` `switches to
fast-charge **mode**` → `schaltet … die Schnellladefunktion **ein**`. The fixlog's stated reason
("you switch to fast charging, not to a function") does not hold — EN says *mode*. `umschalten`
(switch over) became `einschalten` (switch on). Harmless in practice; `schaltet automatisch in den
Schnelllademodus um` would have been closer had the glossary not locked `Schnellladefunktion`.

**M6 — three corpus-wide harmonisations were applied but not recorded in the glossary.**
`Anschlussvarianten` (6 files), `etwas Strom` (4 files) and `Chinesisch (vereinfacht)` (3 files)
have **no row** in `glossary-de.md` (greps return nothing for any of them, nor for `connection
scenarios` as a sentence-level phrase — `:768` locks only the `Connection Options` heading and
`:856` only the numbered option labels). Two other round-4 harmonisations *were* recorded
(`Power-/Zurück-Taste`, `entdecken`). Nothing now prevents round 5 from drifting these back.
Scoping was verified **complete and correct**, so this should not be re-litigated: `connection
scenarios` occurs in exactly six EN files (`expand:42`, `flip:59`, `lite:13`, `lite-144hz:13`,
`one-4k:23`, `one-4k-oled:23`) and all six German pages now read `Anschlussvarianten`. The pages
that still say `lässt sich auf … Arten anschließen` render *different* EN strings and were rightly
left alone — `en/manuals/infinity-lite/installation.mdx:73` `supports two main connection
**methods**`, and `dual-flip:13` / `expand:18` / `infinity:33` `can be connected in the following
ways`.

**M7 — `entdecken` overshoots "browse".** `de/manuals-index.mdx:101`. `durchsuchen` was genuinely
wrong, but NL renders it `Bekijk alle Screenmate producten` (view) and EN is `Browse`. `entdecken`
(discover) is a marketing register the source does not have. `durchstöbern` is the exact German for
"browse" and avoids both problems.

**M8 — voice switch inside one entry.** `de/manuals/dual-flip/controls.mdx:35` and `:39`:
`Erhöht im normalen Gebrauch die Helligkeit. Im OSD-Menü navigier**st du** damit und erhöh**st**
Werte.` The first sentence keeps EN's implicit third-person subject (the button); the second
switches to `du`. The underlying fix was necessary (`navigiert / erhöht Werte` was ungrammatical —
`navigieren` cannot govern `Werte`), but a same-voice rendering would be cleaner, e.g.
`Im OSD-Menü dient die Taste zum Navigieren und zum Erhöhen von Werten.`

Also `de/manuals/panorama/osd.mdx:41`: `Vielleicht möchtest du die Anordnung des Desktops **daher**
in deinem Betriebssystem anpassen.` — `vielleicht` and a mid-sentence `daher` sit awkwardly together;
`Daher möchtest du die Anordnung des Desktops vielleicht … anpassen.` reads better. The modality
restoration itself is correct against `en/manuals/panorama/osd.mdx:41` `you may want to`.

**M9 — two inaccuracies in the claim documents (no translation impact).**
(a) `fixlog-de.md:43` says `Need extra power?` covers "4 installation pages". It is **3** — `lite`,
`lite-144hz`, `one-4k`; `en/manuals/one-4k-oled/installation.mdx` carries no such prompt.
(b) `source-flags-de.md` §2 says EN uses `Color Gamut` and `Color Accuracy` "for the *same* row
(`45% NTSC`, `72% NTSC`, `100% sRGB`)". Only `en/manuals/flip/index.mdx:47` vs `:66` is a true
same-value split; in `expand/index.mdx` the two rows hold different values (72 % vs 45 %), and
`onecable`/`lite`/`dual-flip` use `Color Accuracy` only, so there is no in-file split there.
(c) `source-flags-de.md` §7 says of the duplicated infinity-lite instruction set that "structural
parity forbids collapsing it in German only" — but the German *has* collapsed the one substantive
divergence: `en/manuals/infinity-lite/display-settings.mdx:57` `'Mirrored'` (the sole occurrence in
the whole EN corpus; all eight others say `Flipped`) is rendered with the `Flipped` target. That is
in fact **correct and locked** — `glossary-de.md` carries the row
`| Windows | Mirrored *(superseded — EN now says "Flipped")* | Querformat (gedreht) |` — so the flag
text is simply describing the file inaccurately. Reword the flag; do not change the page.

**M10 — one added comma is a misapplication of the coordinate-adjective rule.**
`de/manuals/lite/index.mdx:19` and `de/manuals/lite-144hz/index.mdx:19`:
`ein leichter**,** tragbarer 15,6"-Full-HD-Monitor`. This pair is hierarchical, not coordinate:
`tragbarer …-Monitor` is the Gesamtbegriff the whole corpus uses as the product class
(`ein tragbarer 15,6"-4K-UHD-Monitor`, `ein tragbarer Monitor mit drei Bildschirmen`), and `leicht`
scopes over that unit — the §71 E1 no-comma case (cf. `die neue englische Literatur`). Semantically
`leicht` is also the *reason* for `tragbar`, not a co-equal property. The `-` line was correct;
recommend reverting these two commas. The sibling change `ein faltbarer, tragbarer Doppelmonitor`
(`de/manuals/infinity/index.mdx:19`) is fine — those two *are* equal-rank and pass the und-Probe.

**M11 — the `von`-stacking fix does not remove the stacking.**
`de/manuals/panorama/installation.mdx:43`. The stated purpose was to break `von der Download-Seite
**von** Silicon Motion`, but `von Silicon Motion` is still there: `Lade den Treiber **auf** der
Download-Seite **von** Silicon Motion herunter`. Both `von …herunterladen` (directional, the default
collocation) and `auf …herunterladen` (locative) are correct German, so nothing is broken — the edit
simply did not achieve its goal. `Lade den Treiber von der Silicon-Motion-Downloadseite herunter:`
removes the doubled `von` and keeps the natural collocation.

**M12 — the round split the voice on four sibling index pages that share one EN pattern.**
`en` renders all four identically as `It connects via USB-C or HDMI…`. After this round:
`de/manuals/one-4k/index.mdx:19` and `one-4k-oled/index.mdx:19` read active `Du schließt ihn über
USB-C oder HDMI an.`, while `lite/index.mdx:19`, `lite-144hz/index.mdx:19` and
`infinity-lite/index.mdx:19` still read passive `Er wird über USB-C oder HDMI angeschlossen`. The
zeugma fix on the One 4K pair was justified; the harmonisation it implies was not carried through.

**M13 — `greifen` overstates the EN action in one of its three uses.**
`de/manuals/infinity/installation.mdx:174` renders `en/…:174` `must **drop neatly into** the groove
on the stand for a snug fit` as `muss sauber in die Aussparung am Ständer **greifen**`. EN describes
passive seating; `greifen` claims active mechanical engagement — close to the `einrasten` the
fixlog deliberately rejected as over-claiming. `…muss genau in die Aussparung am Ständer **passen**`
is both natural and faithful. Related: the fixlog's justification for
`de/manuals/panorama/installation.mdx:23` (`anfassen` = "to touch") is not right — Duden gives
`anfassen` = *mit der Hand berühren, ergreifen*, so `Fasse die Bildschirme an` was already correct
for EN `Grip the screens`. `Greife die Bildschirme` is grammatical but bare and slightly literary
for an instruction. Net effect: `greifen` now carries three senses across `de/` (human grasping
`panorama:23`, bracket gripping `expand:34`, lug engagement `infinity:174`), each individually
faithful but collectively muddier than before.

**M14 — `Sprache … Sprache … Sprachen` in eleven words.**
`de/manuals/lite/osd.mdx:51` and `lite-144hz/osd.mdx:51`: `**Sprache:** Wähle die Sprache des
OSD-Menüs aus 12 verfügbaren Sprachen.` The dangling word order is fixed, but the repetition is new.
`Wähle eine von 12 verfügbaren Sprachen für das OSD-Menü.` reads better.

**M15 — the added commas around `falls nötig` were optional, not a correction.**
`de/manuals/onecable/troubleshooting.mdx:17`. Per amtliches Regelwerk §77 E1, formelhafte verkürzte
Nebensätze such as `falls nötig` may stand without commas, so the `-` line was already correct. The
result is comma-dense. If touched again, `Schließe bei Bedarf eine externe Stromversorgung an, …`
is lighter. No defect either way — logged so it is not re-flagged as a fix next round.

**M16 — the display-settings pages now mix two Windows generations (worth client verification).**
`Bildschirmausrichtung` is the Windows **11** German label (`Anzeigeausrichtung` was Windows 10), so
the §9 amendment does point most readers at a string they will see. But the same paragraphs still
carry Windows 10-era strings — `Desktop auf diese Anzeige erweitern` — so one page now mixes
vintages. The fix is an improvement regardless; flagging so someone confirms the full set against a
live German Windows 11 install before this ships.

---

## Fix list for approval

1. **I1** — reconcile `glossary-de.md:1406` with the new note at `:1397-1404`; **safety** only in the
   frozen-chapters line.
2. **I2** — resolve the gloss inconsistency in the shared display-settings body: drop the
   `(„Display settings“)` parenthetical (NL precedent) or replace it with the Dutch on-screenshot
   string, and apply the same rule to line 31 of the same page.
3. **I3** — escalate the scaling prompt to a single cross-language decision. German and Italian
   currently disagree on `…/infinity/display-settings:30` and `…/panorama/osd:49` (DE followed EN and
   kept `mehr Platz`; IT followed NL and harmonised to "overview" in `f66e287`). Record both German
   occurrences in `source-flags-de.md` with the NL `overzicht` evidence, then apply one ruling to all
   five languages. Leave the German unchanged until that ruling exists — changing it unilaterally
   breaks EN parity, and leaving it silently breaks DE/IT parity.

Minors are advisory. The four most worth taking in this round: **M2** (capability over-claim),
**M4** (the OneCable port paragraph, the weakest German in the diff), **M6** (record the three
unrecorded harmonisations before they drift back), and **M10** (revert the two `leichter,`
commas — a rule misapplication, cheap to undo).

Everything else — meaning fidelity, the scaling-prompt split as specified, structure, the frozen
safety chapter, the shared bodies, the twins, register, DNT, number formats, and the source-flag
classifications — passes.

---

# Fix-round verification — commit `1082d1b`

**Scope of this pass:** verify only that the findings above were correctly resolved, and that
nothing new broke. Read-only; this appendix is the only write.

**Verdict: APPROVED.** All 3 Important and all accepted Minors are correctly resolved. The 7
rejections are defensible — one of them (M11) is a correct rebuttal of my own suggestion. No new
meaning drift, no structural change, no scope leakage.

## Scope

`git show --name-only 1082d1b` touches **only** `de/**` (17 files), `translations/glossary-de.md`,
and `translations/qa/round4/{fixlog,source-flags}-de.md`. Nothing under `en/`, `nl/`, `fr/`, `it/`,
`docs.json` or images. ✓

## The three Important findings

**I1 — RESOLVED.** §11.0 now carries a single freeze-status table (`glossary-de.md:1434-1440`):
**safety = FROZEN** (with the `git diff a0525eb..HEAD` verification command), **display-settings =
NOT frozen**, its invariant restated as byte-identity across the four products enforced by the
`awk` + `md5sum` check rather than by a freeze. The contradictory "Frozen chapters … safety **and
display-settings**, all 17 files" sentence is gone. Grepping `frozen|freeze` across the file returns
only the new table plus two descriptive provenance mentions.
*Trivial residue:* `:94` still reads `*(as shipped in the frozen display-settings chapter)*`. It
describes provenance, not editability, and the governing table is unambiguous — but "frozen" is now
the wrong adjective there. One-word fix whenever the file is next opened; not a blocker.

**I2 — RESOLVED, and resolved the right way.** The note was rewritten to one rule with no
exceptions — *German label only, no parenthetical gloss in any language, on any mention* — and
correctly grounds it in the NL precedent it had previously misapplied (`nl/…:13` carries no gloss).
Grepping `de/` for `Display settings`, `System Settings`, `Privacy & Security` and `Applications`
returns **0 hits**. The file list in the note is accurate
(`de/manuals/onecable/installation-windows.mdx` does exist). The new glossary table also covers the
`Extend desktop to this display` line, closing the line-13-vs-31 inconsistency I raised.

*The critical sub-check — the sweep edited the shared body:*

```
onecable / dual-flip / flip / expand  →  77cfed71bc3e4b0b63e9ea963e4c44aa   (×4, byte-identical)
```

matching the hash claimed in the commit message. The edit is **gloss-only**: the full diff of the
shared body across this commit is a single line, removing `(„Display settings“)` and nothing else.
Meaning-safe, and now structurally identical to the Dutch:

| | |
|---|---|
| NL `:13` | `Klik met de rechtermuisknop op je bureaublad en kies **Beeldscherminstellingen** om de beeldschermconfiguratie te openen.` |
| DE `:13` | `Klicke mit der rechten Maustaste auf deinen Desktop und wähle **Anzeigeeinstellungen**, um die Bildschirmkonfiguration zu öffnen.` |

**I3 — RESOLVED, root cause identified.** `Brauchst du mehr Übersicht?` now at **8/8** sites
(dual-flip, expand, flip, onecable, infinity ×1 each; infinity-lite ×2; panorama/osd ×1); grepping
`de/` for `mehr Platz` returns **0 hits**. The commit message names the actual root cause — the
round-4 NL check was case-sensitive and missed `nl/manuals/panorama/osd.mdx:49` `**M**eer overzicht
nodig?` — which is the right kind of disclosure.

The glossary folded the three per-EN-variant rows back into **one NL-anchored row** carrying a
standing ruling (*"Do not re-split this row per EN variant"*) plus the five-site NL/EN/DE evidence
table. The EN drift is filed as `source-flags-de.md` **§8**, correctly split into **8a** (three EN
strings for one Dutch string) and **8b** (the prompt does not follow from its instruction *in any
language* — `mehr Übersicht` restores fidelity, not logic). §8 also flags FR to be checked against
the same principle before ship. Both the glossary note and §8 state the residual defect explicitly
rather than implying the German is now sound — the framing problem I raised in §9 is fixed.

**DE/IT alignment confirmed independently:** Italian's `visione d'insieme` occurs at exactly the
same 8 sites with the same per-file distribution (dual-flip 1, expand 1, flip 1, infinity-lite 2,
infinity 1, onecable 1, panorama/osd 1). The only other IT hit is `it/manuals/flip/index.mdx:19`,
an unrelated product-intro use of EN "for more overview and focus". The two languages now resolve
this family on the same principle, site for site.

## M4 and the other accepted Minors

**M4 — RESOLVED.** `de/manuals/onecable/controls.mdx:17-19` now reads
`Schließe hier das Kabel deines Laptops an. Dieser Anschluss empfängt Daten und Video von deinem
Laptop und kann auch Strom aufnehmen.` / `Das ist der Hauptanschluss für die Verbindung zu deinem
Laptop über USB-C.` The assertion `en/…:53` depends on is restored, the duplicated connection
statement and the redundant `darüber` are gone, and `:17` reverts to port-as-subject so the file no
longer switches referent between `:17` and `:34`. Faithful to `en/…:17-19`.

Also verified line-by-line against EN, all faithful: **M2** `ist für den Plug-and-Play-Betrieb …
ausgelegt` (design intent restored, `en/…:19` `is designed for`); **M3** `Erst er macht es möglich,
… anzusteuern` (enabling modality restored, `en/…:19` `allows … to be driven`); **M7**
`durchstöbern`; **M8a** `Im OSD-Menü dient die Taste zum Navigieren und zum Erhöhen von Werten`
(voice now consistent); **M8b** `Daher möchtest du … vielleicht …`; **M13a** `muss genau … passen`
(`en/…:174` `drop neatly into … for a snug fit`); **M14** `Wähle eine von 12 verfügbaren Sprachen
für das OSD-Menü`. **M6** added three harmonisation rows to the glossary *plus* a defensive row
naming the EN strings that must **not** be normalised onto `Anschlussvarianten` — the guard I asked
for. **M9** corrected all three claim-document inaccuracies (incl. `Need extra power?` → 3 sites).

**The two self-reverts are executed correctly and discriminatingly.**
**M10** removed the comma in `lite/index.mdx:19` and `lite-144hz/index.mdx:19`
(`ein leichter tragbarer …`) and — correctly — **left `infinity/index.mdx:19`
`ein faltbarer, tragbarer Doppelmonitor` alone**, which is the genuinely coordinate pair.
**M13b** restored `Fasse die Bildschirme an` at `panorama/installation.mdx:23`, and the fixlog
concedes the original Duden rationale was wrong. Reverting one's own prior edit on evidence is the
right behaviour.
*Trivial:* M13a's `sauber` → `genau` puts `genau` in two consecutive bullets at
`infinity/installation.mdx:173-174` where EN varies (`exactly` / `neatly`). Cosmetic only.

## The seven rejections

All defensible. **M11 is a correct rebuttal of my suggestion** — `glossary-de.md:344` forbids
coupling a multi-token product designation into a German compound, so `Silicon-Motion-Downloadseite`
would have violated §3.4; the stacking *was* reduced from two adjacent `von`-phrases to one. I
withdraw M11. **M5c** is kept but its §B5 rationale is explicitly corrected in the log (EN does say
*mode*; the rendering stands only because `Schnellladefunktion` is glossary-locked) — exactly the
resolution my finding asked for. **M1**, **M5a**, **M5b**, **M12** are reasoned trade-offs, not
dismissals. **M15** correctly logs a no-defect-either-way case so it is not re-flagged next round.
**M16** is deferred for verification against a live German Windows 11 install, as I recommended.

## Regression checks

| Check | Result |
|---|---|
| Frozen safety vs `a0525eb` | 0 bytes ✓ |
| Shared display-settings body | byte-identical ×4 at `77cfed71bc3e4b0b63e9ea963e4c44aa` ✓ |
| Structure (headings / lists / steps / rows / components / images) | no add, remove or reorder in any of the 17 files ✓ |
| Headings | none touched by this commit ✓ |
| Twins (`lite`/`lite-144hz`, `one-4k`/`one-4k-oled`) | edited in lockstep ✓ |
| Register | no `Sie`/`Ihr`/`Ihnen` in added lines ✓ |
| DNT + number/SI formats | intact (`144 Hz`, `150 %`, `609 Gramm`) ✓ |
| `nl_link` / `en_link` frontmatter | present on all changed pages ✓ |
| `verify_translation.py --base en --targets de --include-nl` | `0 FAIL, 0 WARN` ✓ |
| New meaning drift | none — every changed line re-checked against EN, NL consulted ✓ |

**Nothing outstanding. The German round-4 work is approved to merge.**
