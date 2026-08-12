# Round 4 — German fix log

**Branch:** `round4-fixes`
**Commits:** `fd77217` (glossary + display-settings OS-label pass), `1cf7bbf` (fluency wave)
**Inputs triaged:** `fluency-de-a.md`, `fluency-de-b.md`, `safety-align-de.md`
**Files touched:** 41 under `de/**` + `translations/glossary-de.md`. **No `safety.mdx` body was
edited** (`git diff --stat HEAD~2 -- 'de/**/safety.mdx'` is empty).

**Triage totals**

| Outcome | Count |
|---|---|
| Fixed (real German defects) | **58** distinct edits across 41 files |
| Rejected (locked convention / faithful to source / taste) | **34** |
| Source-flagged (EN/NL defect, German faithful) | **45** rows, logged in `source-flags-de.md` |
| Deferred (worth a native reviewer's eye, not fixed here) | **6** |

Every finding was checked against the aligned `en/` line before a verdict; `nl/` was consulted
wherever the EN wording was itself ambiguous (the `Need more overview?` / `Display orientation`
rows in particular).

---

## A. Glossary amendments — locked strings that carried meaning errors

Four locked strings were fixed **together with every affected page in the same commit**, as the
brief requires. These are the highest-consequence changes in this round.

| § | Was | Now | Why it is a meaning error, not a preference |
|---|---|---|---|
| §9 | `Display orientation → Anzeigeausrichtung` | **`Bildschirmausrichtung`** | `Anzeigeausrichtung` is a coined string. German Windows labels the field **`Bildschirmausrichtung`** under *Skalierung und Layout*. The reader is sent looking for something that is not on their screen. 8 body occurrences + 1 `alt` text updated. |
| §10.1 | `Need more room? / Need more overview? → Brauchst du mehr Platz?` — a **three-way collapse**: the EN corpus has three distinct run-in labels here | split into **one row per EN prompt** (see table below) | The single target inverted the meaning of the `overview` variant: the instruction under it sets scaling to 150 %, which *reduces* usable desktop area. 6 occurrences fixed; the 2 genuine `room`/`space` occurrences were checked against EN and **left alone** — `mehr Platz` is faithful there. |

**The three-way split (§10.1), verified occurrence by occurrence against the aligned EN line:**

| EN prompt | German | Occurrences | Action |
|---|---|---|---|
| `Need more overview?` | **`Brauchst du mehr Übersicht?`** | 6 — `{onecable,dual-flip,flip,expand}/display-settings` (shared body) + `infinity-lite/display-settings` ×2 | **fixed** (meaning inversion) |
| `Want more on-screen space?` | `Brauchst du mehr Platz?` | 1 — `infinity/display-settings` L30 | **left alone** — faithful |
| `Need more room?` | `Brauchst du mehr Platz?` | 1 — `panorama/osd` L49 | **left alone** — faithful |

This matches the split the Italian fixer made on the same glossary defect. Not part of this
family and already correct: `Need extra power?` → `Brauchst du mehr Strom?` (4 installation pages).
| §9 note | English OS label first, German gloss in parentheses | **German label leads**; English goes in the parentheses *only where the EN line carries a gloss at all* | The analogy to the NL pages does not hold: the screenshots in this chapter are **Dutch**, so on a German page the English string is on neither the screenshot nor the reader's OS. Where EN has no gloss (`infinity`, `infinity-lite`, `installation-mac`), the German now has none either — parity restored. |
| §7.5 | `Browse all Screenmate products → Alle Screenmate-Produkte durchsuchen` | **`… entdecken`** | `durchsuchen` = to search through / rummage (the police *durchsuchen* a flat). It also contradicted its own card title `Produkte ansehen` directly above it. |
| §7.4 | `Power & Return Button → Power- und Zurück-Taste` | **`Power-/Zurück-Taste`** | EN says "Button" (singular) and "Press the … button" — it is **one** button. The suspended-hyphen + `und` form reads as two, so `Drücke die Power- und Zurück-Taste` instructed the reader to press both. §3.5 already establishes slash-suspension (`Menü-/Auswahl-/Bestätigungstaste`) as the house form for a multi-function single button. 4 occurrences (lite, lite-144hz × controls, osd). |

§11.0 was updated to record that the **display-settings** chapter is no longer byte-frozen at
`4792819`; its new canonical body is `de/manuals/onecable/display-settings.mdx` on this branch.
The **safety** chapter remains frozen.

---

## B. Accepted fixes (before → after)

### B1 — display-settings chapter (shared body, 4 products + 2 own-body products)

| File(s) | Before | After |
|---|---|---|
| `{onecable,dual-flip,flip,expand}/display-settings.mdx` | `wähle **Display settings** („Anzeigeeinstellungen“)` | `wähle **Anzeigeeinstellungen** („Display settings“)` |
| idem | `gehe zu „Anzeigeausrichtung“` | `gehe zu „Bildschirmausrichtung“` |
| idem | `**Brauchst du mehr Platz?**` | `**Brauchst du mehr Übersicht?**` |
| `infinity/display-settings.mdx` | `Öffne die **Display settings** („Anzeigeeinstellungen“) und wähle …` | `Öffne die **Anzeigeeinstellungen** und wähle …` *(EN carries no gloss here)* |
| idem | `gehe zu **Anzeigeausrichtung**` | `gehe zu **Bildschirmausrichtung**` |
| `infinity-lite/display-settings.mdx` | `Gehe zu den **Display settings** („Anzeigeeinstellungen“)` | `Gehe zu den **Anzeigeeinstellungen**` — this also removes the page's self-contradiction with line 48, which already said `Anzeigeeinstellungen` |
| idem | `Anzeigeausrichtung` ×2 body + ×1 `alt` | `Bildschirmausrichtung` |
| idem | `**Brauchst du mehr Platz?**` ×2 | `**Brauchst du mehr Übersicht?**` ×2 |
| `panorama/osd.mdx` | `gehe zu **Anzeigeausrichtung**` | `gehe zu **Bildschirmausrichtung**` |

### B2 — English sentence architecture (the Majors both reviewers converged on)

| File | Before | After |
|---|---|---|
| `onecable/index.mdx` | `… ein tragbarer Monitor, der darauf ausgelegt ist, deine Produktivität zu steigern, indem er deinen Laptop mit nur einer Kabelverbindung um zwei zusätzliche Bildschirme erweitert.` | `… ein tragbarer Monitor, der deine Produktivität steigert: Er erweitert deinen Laptop mit nur einer Kabelverbindung um zwei zusätzliche Bildschirme.` |
| `lite/index.mdx` | `… der darauf ausgelegt ist, … zu steigern, indem er deinem Laptop … einen zusätzlichen Bildschirm **hinzufügt**.` | `… der deine Produktivität steigert: Er **erweitert** deinen Laptop, dein Smartphone, dein Tablet oder deine Spielkonsole **um** einen zusätzlichen Bildschirm.` (German extends a device *um* a screen; it does not *add* one *to* it) |
| `lite-144hz/index.mdx` | `Er ist dafür gemacht, Gamern … einen **flüssigen** zweiten Bildschirm … zu bieten.` | `Damit bietet er Gamern und Power-Usern einen zweiten Bildschirm **mit flüssiger Darstellung** …` (a screen is not *flüssig*; its rendering is) |
| `one-4k/index.mdx`, `one-4k-oled/index.mdx` *(twins, edited identically)* | `Er wird über USB-C oder HDMI angeschlossen **und überträgt** auf kompatiblen Geräten Video und Strom …` | `Du schließt ihn über USB-C oder HDMI an. Auf kompatiblen Geräten laufen Video und Strom über ein einziges USB-C-Kabel.` (zeugma: passive + active on one subject, and it made the monitor transmit power) |
| `one-4k/index.mdx` | `Er **gibt** dir einen hochauflösenden zweiten Bildschirm` | `Er **bietet** dir …` |
| `onecable/controls.mdx` | `Dieser Anschluss empfängt Daten und Video von deinem Laptop und kann auch Strom aufnehmen.` | `Über diesen Anschluss empfängt der Monitor Daten und Video von deinem Laptop und kann darüber auch mit Strom versorgt werden.` |
| `onecable/controls.mdx` | `Das ist der Hauptanschluss, **um** deinen Laptop über USB-C **anzuschließen**.` | `An diesem Hauptanschluss schließt du deinen Laptop über USB-C an.` (German does not hang a purpose-infinitive off a bare predicate noun) |
| `onecable/controls.mdx` | `… und **wird verwendet für:**` | `… und wird **für Folgendes** verwendet:` (stranded preposition before a bullet list is English) |
| `expand/index.mdx` | `… den du an deinen Laptop klemmst und **zu zwei Full-HD-Bildschirmen aufklappst – einer auf jeder Seite**.` | `… den du an deinen Laptop klemmst und aufklappst: Du bekommst zwei Full-HD-Bildschirme, **je einen** auf jeder Seite.` |
| `dual-flip/index.mdx` | `… aufklappst – **einer** auf jeder Seite.` | `… aufklappst – **je einer** auf jeder Seite.` |
| `panorama/index.mdx` | `… der dir drei Full-HD-Bildschirme mit 15,6" **aus einem einzigen Gerät liefert**. … **Er ist dafür gemacht**, deine Arbeitsfläche unterwegs enorm zu erweitern. **Ein erforderlicher Displaytreiber macht es möglich**, drei unabhängige Bildschirme … anzusteuern.` | `… der dir **in einem einzigen Gerät** drei Full-HD-Bildschirme mit 15,6" **bietet**. … **Damit erweiterst du** deine Arbeitsfläche auch unterwegs enorm. **Dafür ist ein Displaytreiber erforderlich: Er steuert** drei unabhängige Bildschirme über ein einziges Kabel **an**.` |
| `infinity/index.mdx` | `… und hast damit zwei zusätzliche Bildschirme **auf einmal**.` | `… und hast damit **gleich zwei** zusätzliche Bildschirme.` (`auf einmal` = suddenly / in one go, not "simultaneously") |
| `infinity-lite/index.mdx` | `… und **ist auf Plug-and-Play mit** Laptops … **ausgelegt**.` | `… und **funktioniert per Plug-and-Play mit** Laptops …` (`auf X ausgelegt sein` needs a purpose, not a feature name) |
| `infinity-lite/index.mdx` | `einen zusätzlichen tragbaren Bildschirm **und** mehr Bildschirmfläche` | `… **und damit** mehr Bildschirmfläche` (EN has a purpose relation, not two separate things) |
| `infinity/controls.mdx` | `… mit der du **das Ein- und Ausschalten**, das Bildschirmmenü, die Helligkeit und die Lautstärke **steuerst**.` | `… mit der du **den Bildschirm ein- und ausschaltest sowie** Bildschirmmenü, Helligkeit und Lautstärke steuerst.` |
| `infinity/installation.mdx` | `Der Ständer **öffnet sich** bis zu einem maximalen Winkel von 235°.` | `Der Ständer **lässt sich** bis zu einem maximalen Winkel von 235° **öffnen**.` |
| `infinity/installation.mdx` | `… muss sauber in die Aussparung am Ständer **fallen**, damit alles fest sitzt.` | `… muss sauber in die Aussparung am Ständer **greifen**, …` (calque of "fall into place"; `fallen` + `fest sitzen` in one sentence is self-contradictory. `greifen` chosen over `einrasten` so as not to claim a click-lock the EN does not) |
| `infinity-lite/controls.mdx` | `Nach links drücken – **stellt** die Hintergrundbeleuchtung (Helligkeit) **ein**.` (+ the „Plus" twin) | `Drücke die Taste nach links, um die Hintergrundbeleuchtung (Helligkeit) einzustellen.` (infinitive phrase + dash + subjectless finite verb: neither half can govern the other) |
| `infinity-lite/installation.mdx` | `Passe den Abstand zwischen dem tragbaren Bildschirm und dem Computerbildschirm **für ein angenehmeres Nutzungserlebnis** nach deinen Vorlieben **an**.` | `Stelle den Abstand zwischen dem tragbaren Bildschirm und dem Computerbildschirm so ein, wie es für dich am angenehmsten ist.` (corporate anglicism + 17 words inside the Satzklammer) |
| `flip/index.mdx` | `Beide seitlichen Bildschirme **klappen** flach an das mittlere Gehäuse` | `Beide seitlichen Bildschirme **lassen sich** flach an das mittlere Gehäuse **klappen**` |
| `flip/installation.mdx` ×2, `expand/installation.mdx` ×1 | `Klappe den rechten Bildschirm **in die in Abbildung 2 gezeigte** Richtung auf.` | `Klappe den rechten Bildschirm **in die Richtung auf, die in Abbildung 2 gezeigt wird**.` (stacked extended attribute; the very next step already used the natural form) |
| `panorama/installation.mdx` | `**Fasse** die Bildschirme **an** und ziehe sie nach oben` | `**Greife** die Bildschirme und ziehe sie nach oben` (`anfassen` = to touch) |
| `panorama/installation.mdx` | `führe **die Schritte oben** in umgekehrter Reihenfolge aus` | `führe **die oben beschriebenen Schritte** in umgekehrter Reihenfolge aus` |
| `panorama/installation.mdx` | `Lade den Treiber **von** der Download-Seite **von** Silicon Motion herunter` | `Lade den Treiber **auf** der Download-Seite von Silicon Motion herunter` |
| `panorama/osd.mdx` | `Der Panorama steuert drei unabhängige Bildschirme an. **Deshalb kannst du** die Anordnung des Desktops … anpassen.` | `… **Vielleicht möchtest du** die Anordnung des Desktops **daher** … anpassen.` (restores EN's `you may want to`; the bare `Deshalb kannst du` read as a non-sequitur) |
| `dual-flip/controls.mdx` ×2 | `Erhöht im normalen Gebrauch die Helligkeit und **navigiert / erhöht Werte** im OSD-Menü.` | `Erhöht im normalen Gebrauch die Helligkeit. Im OSD-Menü navigierst du damit und erhöhst Werte.` (`navigieren` is intransitive and cannot govern `Werte`) |
| `onecable/installation.mdx` | `Hebe den Ständer an und **ziehe ihn mit der Taste aus oder schiebe ihn ein**, um mehr Stabilität zu erhalten.` | `Hebe den Ständer an und **fahre ihn mit der Taste aus oder ein**, um mehr Stabilität zu erhalten.` (a button does not *ausziehen*) |
| `lite/osd.mdx`, `lite-144hz/osd.mdx` | `**Sprache:** Wähle aus 12 verfügbaren Sprachen **für die Anzeige des OSD-Menüs**.` | `**Sprache:** Wähle **die Sprache des OSD-Menüs** aus 12 verfügbaren Sprachen.` (dangling English word order) |
| `manuals-index.mdx` | `Alle Screenmate-Produkte **durchsuchen**` | `Alle Screenmate-Produkte **entdecken**` |

### B3 — Grammar, orthography and punctuation

| File | Before | After |
|---|---|---|
| `onecable/troubleshooting.mdx` ×2 | `in der Menüleiste deines **Mac**` / `das Launchpad deines **Mac**` | `deines **Macs**` (Duden: *der Mac, des Macs*) |
| `onecable/troubleshooting.mdx` | `Schließe falls nötig eine externe Stromversorgung an` | `Schließe**,** falls nötig**,** eine externe Stromversorgung an` |
| `onecable/troubleshooting.mdx` | `Verwende das **doppelte** USB-A-auf-USB-C-Kabel:` | `Verwende das USB-A-auf-USB-C-Kabel **mit zwei USB-A-Steckern**:` (`das doppelte Kabel` is not a German noun phrase; the locked chain `USB-A-auf-USB-C-Kabel` per §3.3 is preserved, and the two plugs are named in the next sentence anyway) |
| `flip/osd.mdx`, `dual-flip/osd.mdx` | `**Vereinfachtes** Chinesisch` | `Chinesisch (vereinfacht)` (English title-case bleed; also harmonises with `expand/osd.mdx`, which already had the correct German form) |
| `lite/index.mdx`, `lite-144hz/index.mdx`, `infinity/index.mdx` | `ein leichter tragbarer …` / `ein faltbarer tragbarer Doppelmonitor` | comma between the coordinate adjectives |
| `infinity/controls.mdx` | `Der Anschluss ist **auf** jedem Bildschirm **auf** der Rückseite … markiert.` | `… ist **an** jedem Bildschirm auf der Rückseite … markiert.` |
| `infinity-lite/controls.mdx` | `Der **äußerste linke** Anschluss an der Unterseite.` | `Der **ganz linke** Anschluss an der Unterseite.` |

### B4 — Terminology drift where EN uses one term and German used several

These are German-internal defects: the EN source is consistent, the German was not.

| EN term | Was (German) | Now |
|---|---|---|
| `connection scenarios` | `Anschlussszenarien` (lite, lite-144hz) / `Anschlussvarianten` (flip) / `lässt sich auf N Arten anschließen` (expand, one-4k, one-4k-oled) | **`Anschlussvarianten`** in all six. Chosen over `Anschlussszenarien` for register (a consumer manual does not have *Szenarien*) and legibility (triple `s`), and it chains cleanly into the following `Wähle die Variante, die …`. |
| `a small amount of power` | `eine geringe Menge Strom` (flip, dual-flip) / `etwas Strom` (onecable, expand) | **`etwas Strom`** in all four. |
| `Power & Return Button` | `Power- und Zurück-Taste` | **`Power-/Zurück-Taste`** — see §A. |
| macOS path glossing on one page | step 4 English-first with gloss, the same path German-only 14 lines later | **German-only in both places**, matching EN which carries no gloss at all on that page (`onecable/installation-mac.mdx`) |
| `Simplified Chinese` | `Vereinfachtes Chinesisch` / `Chinesisch (vereinfacht)` | **`Chinesisch (vereinfacht)`** in all three OSD pages |

### B5 — Modality / collocation fixes

| File | Before | After |
|---|---|---|
| `one-4k/installation.mdx`, `one-4k-oled/installation.mdx` *(twins, edited identically)* | `Bei Unterstützung von Power Delivery (PD) schaltet der Screenmate automatisch **auf die Schnellladefunktion um**.` | `Wenn Power Delivery (PD) unterstützt wird, schaltet der Screenmate automatisch **die Schnellladefunktion ein**.` (you switch *to fast charging*, not *to a function*; the glossary-locked noun `Schnellladefunktion` is kept) |
| `lite`, `lite-144hz`, `one-4k`, `one-4k-oled` `/installation.mdx` | `Um den Screenmate **mit** einer Spielkonsole **mit** USB-C-Anschluss zu verwenden` | `Um den Screenmate mit einer Spielkonsole zu verwenden, **die einen USB-C-Anschluss hat**` (matches EN's relative clause) |

---

## C. Rejected — one line each

**Glossary-locked, and the lock is correct:**

1. `## Bildschirmkonfiguration Windows` → "unter Windows" — locked §7.3 / §11.0, EN heading is `Display Configuration Windows`.
2. `Gewicht | 1820 Gramm` → `1820 g` — §4 locks `Gramm` spelled out, matching EN "grams". (Same for 609/860/1450/1552/1565/1750/1900/2390/3000.)
3. `Blickwinkel` / `Größe` vs `Bildschirmgröße` — §8; EN itself uses `Viewing Angle`, `Size` and `Screen Size` in different products.
4. `Farbgenauigkeit` for sRGB/NTSC coverage — §8; the term error is EN's (`Color Accuracy`). Source-flagged.
5. `das Netzkabel abziehen` — §5 locks it for EN `disconnect the power cable`.
6. `Dedizierter Stromeingang` — §5 locks it for EN `dedicated power input`.
7. `im allgemeinen Modus` — §10.5 locks `General mode → Allgemeiner Modus`. dual-flip's `im normalen Gebrauch` renders a *different* EN string (`in general use`).
8. `Kontrollleuchte der Hauptplatine` — §1.1 locks it; the customer-visibility problem is EN's. Source-flagged.
9. `6× Schutzclips` → `6× Schutzclip` — §1.1 locks the plural form.
10. `Verriegelungsfüße` — §1.1 locks it for `locking legs`.
11. `Ständer für einen Bildschirm` — §1.1 explicitly forbids `Einzelbildschirmständer`.
12. `Taste Ab (−)` / `Taste Auf (+)` — §7.4 locks both.
13. `3 × Mini-HDMI-Anschlüsse` (spaced) → `3×` — §7.4 locks the spaced form, matching EN `3 × Mini HDMI Ports`.
14. `Geh sorgsam mit deinem Screenmate um` → `Gehe` — §10.1 locks the apocopated form.
15. `Option 1 – USB-C (nur ein Kabel)` — §7.4 locked; the one-cable/two-cable contradiction is EN's. Source-flagged.
16. `Achtung:` + `Achte … auf deine Finger` root echo — both halves locked (§10.1, §10.2).
17. `(DP-Monitor)` → spelled-out `DisplayPort` — §5 locks `DP`.
18. `Bildschirmkonfiguration (Betriebssystem)` — §7.3 locks it for `Display Configuration (OS-Level)`.
19. `Warnungen` → `Warnhinweise` in the safety `description` — §7.2 locks it, and `Warnungen` renders EN `warnings` faithfully.
20. `„15,6"-Full-HD-Monitor` → `15,6-Zoll-` — §4: do not expand the inch mark to `Zoll`.
21. Number ranges `0° – 245°` (spaced) → unspaced — §3.6 locks spaced ranges, and EN is spaced too.
22. `- **Helligkeit - (linker Bildschirm)**` ASCII hyphen → `−` (U+2212) — §3.6 says keep the source character, and the EN source uses the ASCII hyphen here.
23. `**OSD-Modus**` (lite) vs `**OSD-Menü-Modus**` (lite-144hz) — §10.5 locks both separately; EN differs the same way.

**Faithful to the source — changing the German would break parity:**

24. macOS block missing quotation marks around UI labels — EN has none either.
25. `display-settings` frontmatter `description` differs on flip — because the **EN** description differs on flip.
26. `am Monitor Screenmate OneCable` → drop `Monitor` — EN says "the Screenmate OneCable monitor", and §7.2 uses exactly this apposition pattern.
27. `die Bildschirmhelligkeit … zu verbessern` vs `Optimierung` elsewhere — EN says `improve` in one place and `optimization` in the other.
28. `HDMI-Verbindung mit … einer Kamera` (alt text) — the camera is in the EN alt text. Source-flagged.
29. `nicht in Gebrauch ist` → `wenn du den Monitor nicht benutzt` — faithful to `when the monitor is not in use`; no meaning gap.
30. `den du **um** deinen Laptop klemmst` (flip) — EN says "clips **around** your laptop", and the Flip does wrap around. Expand's `an` renders EN's "clips **onto**".
31. `montierst` (infinity-lite) vs `befestigst` (infinity) — EN says `mounts` and `clips` respectively.
32. `senkrecht`/`waagerecht` → `Hochformat`/`Querformat` — EN says `vertical`/`horizontal` there and `Landscape/Portrait view` in the captions; two EN vocabularies, faithfully rendered.
33. `<Warning>` callouts containing neutral instructions — component choice is structural parity; changing it in German only is forbidden. Source-flagged.
34. `wähle es oben aus der Liste aus` → "aus" — EN says "from the list above"; the grid-vs-list mismatch is the source's.

---

## D. Deferred — for the native reviewer / client, not fixed here

1. **`safety.mdx` style suggestions (frozen bodies, logged as instructed).**
   (a) Item 12 `Begrenze die Einwirkung von starken Magnetfeldern oder Sendeanlagen` — `Begrenze die
   Einwirkung von` is *limit exposure to* word-for-word, and `Sendeanlagen` is not something a
   consumer meets; a native would write `Halte das Gerät von starken Magnetfeldern und Funksendern
   fern`. (b) The device is called `Monitor` / `Bildschirm` / `Gerät` / `Screenmate` inside one
   14-item list, twice within item 10 — worth fixing `Monitor` for the device and reserving
   `Bildschirm` for the panel, but only in a round that is allowed to reopen the frozen chapter,
   and only alongside EN. Both were verified as *faithful* renderings in `safety-align-de.md`;
   neither changes what the reader must do.
2. **`Anschlussszenarien` register was fixed, but `Szenarien` also appears nowhere else** — if the
   client prefers `Anschlussmöglichkeiten` in the body as well as the heading, that is a one-line
   sweep across six files.
3. **Alt texts on the display-settings chapter carry German OS labels while the screenshots are
   Dutch.** A German screen-reader user is given a label that is not in the image. Consistent with
   §9 and with all four products, so left as-is; worth an accessibility decision.
4. **`die gesamte Farbintensität`** (lite, lite-144hz osd) — literal rendering of EN's "the overall
   color intensity"; the concept error under *Farbtemperatur* is EN's, so the German was left
   faithful. If EN is corrected, correct German with it.
5. **`Verwende das lange weiße Kabel für den Strom und das kurze schwarze Kabel, um … zu verbinden`**
   (panorama/installation) — non-parallel coordination mirroring EN's own non-parallel sentence.
6. **`versorgt werden` without `mit Strom`** (lite, lite-144hz, one-4k, one-4k-oled installation) —
   flagged by reviewer B as ungrammatical. Rejected as a defect: `Das Gerät wird über USB versorgt`
   is standard German engineering usage. Recorded here in case a native reviewer disagrees.

---

## E. Verification (run after the final edit)

```
$ python scripts/verify_translation.py --base en --targets de --include-nl
0 FAIL, 0 WARN

$ python -m pytest tests/test_verify_translation.py -q
....................                                                     [100%]
20 passed in 0.19s

$ git diff --stat HEAD -- 'de/**/safety.mdx'
(no output — safety bodies unchanged)

$ for f in onecable dual-flip flip expand; do
    awk 'BEGIN{c=0} /^---$/{c++; next} c>=2{print}' de/manuals/$f/display-settings.mdx | md5sum
  done
onecable     23c155f4861fc970c03a1d1f0838886a
dual-flip    23c155f4861fc970c03a1d1f0838886a
flip         23c155f4861fc970c03a1d1f0838886a
expand       23c155f4861fc970c03a1d1f0838886a
```

0 FAIL, 0 WARN — and **no new warn classes**: the run was clean before this round and is clean
after it. The four display-settings bodies remain byte-identical after propagation. The twin
products (`lite` / `lite-144hz` and `one-4k` / `one-4k-oled`) received identical edits wherever
their EN pages are identical apart from product name and specs.
