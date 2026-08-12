# Fluency review — German (Reviewer A)

**Scope:** monolingual German fluency/naturalness review of the published DE manual copy for
OneCable, Lite, Lite 144 Hz, Flip and Expand, plus `de/manuals-index.mdx`.
No `en/` or `nl/` file was opened. The question answered here is the one structural and
meaning-fidelity checks cannot answer: *does this read as if it had been written in German, by a
German technical editor, for German customers?*

**Deliberate conventions honoured (not flagged):** informal *du*; English technical terms
(DisplayPort, HDMI, USB-C, OSD, DRIVERS (D:), product names, ALL-CAPS device labels); German
number/unit locale; title style `Screenmate X – Handbuch`; frontmatter `*_link` keys, slugs and
icons ignored; JSX component names/props ignored except human-visible strings (alt text, card
titles, callout text — those are reviewed in full).

**Register check:** no *Sie* leakage anywhere in `de/` (grep-verified across the whole tree). *du*
is applied consistently, including in callouts, alt text and card copy. This is genuinely well done.

**Body-identity check (verified by hash, not assumed):**
`onecable|lite|lite-144hz|flip|expand/safety.mdx` bodies are byte-identical (md5 `82f2a1…`), and
`onecable|flip|expand/display-settings.mdx` bodies are byte-identical (md5 `076187…`). Findings on
those two pages therefore publish on **five** and **three** product manuals respectively.

**Minor findings are capped** at the 20 most worthwhile, per brief. Additional lower-value polish
(pure preference rewrites, repeated instances of an already-listed pattern) was deliberately left
out — this is an error hunt, not a style rewrite.

---

## de/manuals-index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Alle Screenmate-Produkte durchsuchen" | Wrong collocation. *durchsuchen* = to search through / rummage (the police *durchsuchen* a flat). English "browse all products" taken literally. It also contradicts its own card title „Produkte ansehen" directly above it. | „Alle Screenmate-Produkte entdecken" (or „…ansehen", matching the card title) | **Major** |
| „wähle es oben aus der Liste aus" | The page shows a card grid, not a list — the reader looks for a list that isn't there. | „wähle es oben aus." | Minor |

Frontmatter („Screenmate-Produkthandbücher" / „Digitale Handbücher für alle Screenmate-Produkte")
and the remaining card copy are idiomatic. No further findings.

---

## de/manuals/onecable/index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „ist ein tragbarer Monitor, der darauf ausgelegt ist, deine Produktivität zu steigern, indem er deinen Laptop mit nur einer Kabelverbindung um zwei zusätzliche Bildschirme erweitert." | Textbook translationese: *designed to … by …ing* mapped 1:1 onto *darauf ausgelegt, … zu …, indem er …*. Two subordinate clauses stacked behind a copula; no German product writer builds this. „Kabelverbindung" is also a heavy stand-in for „Kabel". The same pattern recurs verbatim in `lite/index.mdx`. | „Der Screenmate OneCable ist ein tragbarer Monitor, der deine Produktivität steigert: Er erweitert deinen Laptop mit nur einem Kabel um zwei zusätzliche Bildschirme." | **Major** |
| „Gewicht \| 1820 Gramm" | Unit spelled out while every other row of the same table uses symbols (cd/m², ms, Hz, cm, %, °). Affects all six index pages (1820 / 1552 / 609 / 1565 / 1875 / 1750 / 1450 Gramm). | „1820 g" | Minor |
| „Der Screenmate verbraucht im Standby-Modus etwas Strom." | Correct here — but `flip/index.mdx` renders the identical boilerplate as „eine geringe Menge Strom". One sentence, two versions across sibling manuals. | Standardise on „etwas Strom" (2 of 3 pages already use it). | Minor |
| „empfehlen wir, das Netzkabel abzuziehen, wenn der Monitor nicht in Gebrauch ist." | Two problems: *Netzkabel abziehen* is a weak collocation (German pulls the *Stecker*, and this device is fed over USB-C, not a *Netzkabel*), and „nicht in Gebrauch ist" is Amtsdeutsch clashing with the du-voice used everywhere else. | „empfehlen wir, den Stecker zu ziehen, wenn du den Monitor nicht benutzt." | Minor |

„Farbgenauigkeit \| 100 % sRGB" is the wrong German label for a gamut figure — tracked as a Major
under `flip/index.mdx`, where the set contradicts itself inside a single table.

---

## de/manuals/onecable/controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Dieser Anschluss empfängt Daten und Video von deinem Laptop und kann auch Strom aufnehmen." | Two un-German collocations in one sentence: a port does not *empfangen* „Video" (German needs *Bild-* / *Videosignal*), and „Strom aufnehmen" as a port property reads as a literal *can also take power*. | „Über diesen Anschluss erhält der Monitor Daten und das Videosignal deines Laptops. Er kann darüber außerdem mit Strom versorgt werden." | **Major** |
| „Das ist der Hauptanschluss, um deinen Laptop über USB-C anzuschließen." | Calque of *This is the main port to connect your laptop via USB-C*. German does not hang a purpose-infinitive off a bare predicate noun this way. | „Über diesen Hauptanschluss schließt du deinen Laptop per USB-C an." | **Major** |
| „Dieser Anschluss nimmt ausschließlich Strom auf und wird verwendet für:" | „wird verwendet für:" with a stranded preposition in front of a bullet list is an English list stem transplanted into German. | „…und dient dazu:" / „…und wird für Folgendes verwendet:" | **Major** |
| „**Helligkeit - (linker Bildschirm)**" | ASCII hyphen used as a minus sign. `flip/controls.mdx` and `expand/controls.mdx` use „−" (U+2212) for the same button. As printed this reads as a hyphen, not a minus. | „**Helligkeit −** (linker Bildschirm)" | Minor |
| „Power-Anschluss" (here) / „Power-Anschluss des Screenmate" (installation) / „Power-USB-C-Anschluss" (troubleshooting) / heading „USB-C-Anschluss (nur Strom / Power Delivery)" | Four names for one socket inside one manual; the customer has to infer they are the same port. | Fix one term — e.g. „Power-Anschluss (USB-C)" — and use it in all three files. | Minor |
| „…alle physischen Anschlüsse und Bedientasten am **Monitor Screenmate OneCable**." | The three sibling pages all say „am Screenmate Lite / Flip / Expand". Only OneCable inserts „Monitor", producing a stiff apposition. | „…am Screenmate OneCable." | Minor |

---

## de/manuals/onecable/display-settings.mdx
*(body byte-identical in `flip/` and `expand/` — every finding publishes three times)*

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „wähle **Display settings** („Anzeigeeinstellungen")" — then „wähle „Desktop auf diese Anzeige erweitern"", „die Schaltfläche „Identifizieren"", „gehe zu „Anzeigeausrichtung"", „wähle „Querformat (gedreht)"" | Page-internal inconsistency in UI-label policy: the *first* label is English-first with a German gloss, every later label is German-only. A German reader concludes the first dialog is English and the rest German. | Pick one policy. For a German audience: German first, English in parentheses only where the screenshot shows English — „wähle **Anzeigeeinstellungen** („Display settings")" — then apply it to every label on the page. | **Major** |
| „## Bildschirmkonfiguration Windows" | Preposition-less headline noun stack (*Display configuration Windows*). German body headings take „unter". | „## Bildschirmkonfiguration unter Windows" (likewise „…unter macOS") | **Major** |
| „Öffne die Systemeinstellungen. / Gehe zu Displays. / Klicke auf Anordnen." | The macOS block drops the quotation marks the Windows block applies to every UI label on the same page. | „Öffne die **Systemeinstellungen**. / Gehe zu „Displays". / Klicke auf „Anordnen"." | Minor |
| Frontmatter: „Anzeigeeinstellungen für Windows und macOS" (onecable, expand) vs. „Bildschirme unter Windows und macOS einrichten" (flip) | Byte-identical page, two different descriptions; the Expand/OneCable one also just echoes its own title. The Flip wording is the better German. | Use „Bildschirme unter Windows und macOS einrichten" on all three. | Minor |

*Out of scope, but worth a client query:* „**Brauchst du mehr Platz?** … stelle sie auf 150 % ein,
damit Text und Elemente größer dargestellt werden." Larger scaling yields *less* usable space. The
German is fine; the logic is self-contradictory and appears to originate in the source.

---

## de/manuals/onecable/installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Hebe den Ständer an und ziehe ihn mit der Taste aus oder schiebe ihn ein, um mehr Stabilität zu erhalten." | „ihn mit der Taste ausziehen" is not comprehensible German — a button does not *ausziehen*, and the trailing purpose clause attaches to both opposed actions. `expand/installation.mdx` step 4 describes the identical mechanism clearly. | „Hebe den Ständer an und ziehe ihn bei gedrückter Taste heraus. Zum Einschieben drückst du die Taste erneut." | **Major** |
| „Achte darauf, dass du zuerst beide Kabel an den Laptop anschließt, bevor du das andere Ende mit dem Screenmate verbindest." | Number mismatch: two cables, then singular „das andere Ende". The reader stops and re-reads. | „…bevor du die anderen Enden mit dem Screenmate verbindest." | **Major** |
| „1. Verbinde deinen Laptop über ein USB-C-Kabel mit dem Screenmate (mit vollem Funktionsumfang)" | Dangling parenthetical. As placed it modifies the connection, not the cable, and German offers no way to read it correctly — the reader cannot tell what needs full functionality. | „Verbinde deinen Laptop über ein USB-C-Kabel mit vollem Funktionsumfang mit dem Screenmate." | **Major** |
| „Hinweis: Verwende ein Netzteil mit mindestens 45 W. Kein USB-C-Ladegerät? Dann verwende ein passendes Netzteil." | Tautology: *Netzteil* and *Ladegerät* are the same object here, so the advice reads „no charger? then use a charger". `troubleshooting.mdx` phrases the same case correctly („Hat dein Laptop-Ladegerät keinen USB-C-Ausgang? Dann verwende ein PD-Ladegerät mit mindestens 45 W."). | Adopt the troubleshooting wording. | **Major** |
| „Dann schließe das andere USB-Kabel an eine Steckdose an." | A USB-A connector cannot go into a *Steckdose*; German expects „an ein Netzteil". | „Dann schließe das andere USB-Kabel an ein Netzteil an." | Minor |

---

## de/manuals/onecable/installation-mac.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| Step 4: „Gehe zu **„System Settings"** („Systemeinstellungen") > **„Privacy & Security"** („Datenschutz & Sicherheit") > **„Screen & System Audio Recording"** („Bildschirm- & Systemaudioaufnahme")." vs. lower on the same page: „1. Gehe zu **„Systemeinstellungen"** > **„Datenschutz & Sicherheit"** > **„Bildschirm- & Systemaudioaufnahme"**." | The identical macOS path appears twice on one page in two opposite conventions (English-first-with-gloss, then German-only). The alt texts follow the German-only convention, so the page contradicts itself three ways. | German first, English in parentheses on first mention only; German-only thereafter. | **Major** |
| „Gehe auf deinem **MacBook** so vor:" / „Starte … deinen **Mac** neu." / „Starte … deinen **Laptop** neu." / „Schließe den Screenmate an deinen **Laptop** an" | Three names for the customer's machine on one page, including inside two parallel step lists that otherwise mirror each other. | Use „Mac" throughout this page. | Minor |

---

## de/manuals/onecable/installation-windows.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…für Windows 10 oder 11 den Ordner **Win10&11** (die Ordner „mac OS" und „Win 7&8" sind ebenfalls vorhanden)." | Within one sentence, one folder name is bold-unquoted and the other two are quoted. | Treat all three identically: „…den Ordner **Win10&11** (die Ordner **mac OS** und **Win 7&8** sind ebenfalls vorhanden)." | Minor |

The manual-installation procedure (steps 1–5) is clean, idiomatic German — the strongest block in
the OneCable set. „Windows 10 oder höher" is a mild calque of *or higher* („oder neuer" / „ab
Windows 10" is more German) but is common enough in the wild to count as preference, not error.

---

## de/manuals/onecable/safety.mdx
*(body byte-identical in `lite/`, `lite-144hz/`, `flip/`, `expand/` — every finding publishes five times)*

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „5. Der Monitor arbeitet mit einem DC-Eingang zwischen 5 V und 20 V (mit einer Toleranz von ±2 V)." immediately followed by „6. Verwende das Gerät **ausschließlich** mit einer 5-V-Stromquelle über das passende Kabel." | **Direct contradiction between consecutive safety instructions.** Item 5 permits 5–20 V; item 6 forbids anything but 5 V. A German customer reading the two lines cannot determine which power supply is safe — and the same manual elsewhere instructs them to use a 45 W PD charger, i.e. not 5 V. The German is grammatical; the defect is that the two sentences cannot both be obeyed. Probably inherited from the source, but it is published on five product manuals and is safety copy, so it cannot be signed off as-is. | Confirm the electrical spec with the client, then e.g.: „5. Der Monitor arbeitet mit einer Eingangsspannung von 5 V bis 20 V DC (±2 V). 6. Verwende ausschließlich das mitgelieferte Kabel und ein Netzteil, das diesen Bereich einhält." | **Critical** |
| „12. Begrenze die Einwirkung von starken Magnetfeldern oder Sendeanlagen, um Störungen zu verhindern." | „Begrenze die Einwirkung von" is *limit exposure to* word-for-word, and „Sendeanlagen" (broadcast installations) is not something a consumer meets. German safety copy uses a *fernhalten* construction. | „12. Halte das Gerät von starken Magnetfeldern und Funksendern fern, um Störungen zu vermeiden." | **Major** |
| „…bevor du den **Monitor** verwendest" (intro) / „Reinige den **Bildschirm**…" (8) / „Berühre das **Gerät** nicht…" (9) / „Lass den **Monitor** nicht fallen und schütze den **Bildschirm**…" (10) / „Lebensdauer deines **Screenmate**" (intro) | Four words for the same object inside one 14-item list — twice within a single sentence (item 10). German readers treat a changed word as a changed referent, so in a safety list this is also a liability question: „schütze den Bildschirm vor Stößen" reads as covering the panel only. | Fix „der Monitor" for the device and reserve „der Bildschirm" for the panel surface (items 1, 8, 14). | **Major** |

Typography here is good: „−20 °C" uses a true minus sign, „±2 V" and SI spacing are correct, and
„keine Flüssigkeiten oder aggressiven Reinigungsmittel" is correctly declined.

---

## de/manuals/onecable/troubleshooting.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „ob das Treibersymbol oben rechts in der Menüleiste **deines Mac** zu sehen ist" and „Öffne das Launchpad **deines Mac**" | **Grammar error, twice.** *Mac* is a masculine loanword and takes the genitive -s (Duden: *der Mac, des Macs*). | „…in der Menüleiste deines Macs…" / „…das Launchpad deines Macs…" | **Major** |
| „Verwende das **doppelte** USB-A-auf-USB-C-Kabel:" | „das doppelte Kabel" is not a German thing, and it does not match the name used on the index page („2× USB-A-auf-USB-C-Kabel"). The reader cannot identify which accessory is meant — in a troubleshooting answer, where identification is the whole job. | „Verwende das USB-A-auf-USB-C-Kabel mit zwei USB-A-Steckern (schwarz und rot):" | **Major** |
| „Prüfe, ob die Kontrollleuchte der **Hauptplatine** leuchtet." | „Hauptplatine" (motherboard) is invisible to a customer, and a consumer monitor's indicator is a *Betriebs-LED*, not a mainboard light. As written, the very first troubleshooting step cannot be performed. | „Prüfe, ob die Betriebs-LED am Monitor leuchtet." | **Major** |
| „Schließe falls nötig eine externe Stromversorgung an" | Missing commas around the elliptical clause (Duden: *wenn/falls nötig* is set off). | „Schließe, falls nötig, eine externe Stromversorgung an" | Minor |
| „um Reverse Charging zu ermöglichen und die Bildschirmhelligkeit automatisch zu **verbessern**" | `installation.mdx` says „die Bildschirmhelligkeit wird automatisch **optimiert**" for the identical behaviour, and *optimieren* is the stronger collocation. | „…und die Bildschirmhelligkeit automatisch zu optimieren." | Minor |

„Das ist möglich, sofern die folgenden Voraussetzungen erfüllt sind:" followed by three run-on
prose statements instead of bullets is a formatting weakness rather than a language one — noted,
not counted.

---

## de/manuals/lite/index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…indem er deinem Laptop, Smartphone, Tablet oder deiner Spielkonsole einen zusätzlichen Bildschirm **hinzufügt**." | *adds a screen to your laptop* transferred literally. German does not *hinzufügen* a monitor to a device; it *erweitert* the device *um* a screen — exactly what `onecable/index.mdx` does two products earlier („erweitert … um zwei zusätzliche Bildschirme"). Unidiomatic *and* self-inconsistent. | „…indem er deinen Laptop, dein Smartphone, dein Tablet oder deine Spielkonsole um einen zusätzlichen Bildschirm erweitert." | **Major** |
| „ein leichter tragbarer 15,6"-Full-HD-Monitor" | Two coordinate adjectives with no comma, and an inch mark glued into a German compound with a hyphen. German product copy writes the size out. | „ein leichter, tragbarer 15,6-Zoll-Full-HD-Monitor" | Minor |

The „der darauf ausgelegt ist, deine Produktivität zu steigern," calque recurs here verbatim —
counted once, under `onecable/index.mdx`.

---

## de/manuals/lite/controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### Power- und Zurück-Taste" (and „Drücke die Power- und Zurück-Taste…" in `osd.mdx`) | The suspended hyphen makes this read as **two** buttons („die Power-Taste und die Zurück-Taste"), so „Drücke die Power- und Zurück-Taste" instructs the reader to press both. It is one button with two functions. | „### Power-/Zurück-Taste" — and „Drücke die Power-/Zurück-Taste…". | **Major** |
| „### Scrollrad — Kurz drücken: das Gerät einschalten / Lang drücken: das Gerät ausschalten" against „### Power- und Zurück-Taste — Drücken, um das Bildschirmmenü (OSD) zu öffnen" | As published, the *Scrollrad* powers the device on and off, and the control named *Power-Taste* does not. A German reader reads this as two swapped headings and will press the wrong control. Flagged as a content query — the labels may be faithful to the source, but the page cannot ship in German while a control's name contradicts the function printed beside it. | Verify against hardware/source; if the functions are correct, rename the button (e.g. „Menü-/Zurück-Taste") so its German name matches what it does. | **Major** |
| „**OSD-Modus**" (lite) vs. „**OSD-Menü-Modus**" (lite-144hz) | Identical page, two labels. | Standardise on „OSD-Modus". | Minor |

„3,5-mm-Klinkenanschluss" and „Mini-HDMI-auf-HDMI-Kabel" are correctly hyphenated — good.

---

## de/manuals/lite/installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Der Screenmate Lite unterstützt fünf **Anschlussszenarien**." (under the heading „**Anschlussmöglichkeiten**") — against „Der Screenmate Flip unterstützt zwei **Anschlussvarianten**." and „Der Screenmate Expand lässt sich auf drei **Arten** anschließen." | **Four German terms for one concept** across the set, the first two colliding within three lines of each other on this page. „Szenarien" is also the wrong register for a consumer manual, and „Anschlussszenarien" stacks three s's without the hyphen Duden recommends for legibility. | Heading „Anschlussmöglichkeiten" + lead sentence „Der Screenmate X lässt sich auf N Arten anschließen." everywhere. | **Major** |
| alt „HDMI-Verbindung mit einem PC, einer Konsole oder einer **Kamera**" | The body lists PC, Laptop, Xbox, PlayStation 4/5 and Nintendo Charging Dock — no camera appears anywhere in the German manual. | „HDMI-Verbindung mit einem PC, Laptop oder einer Spielkonsole" | Minor |

Also present but counted as preference: the over-stretched Satzklammer in „Schließe den Screenmate
über ein HDMI-Kabel für das Videosignal und zusätzlich über ein USB-C-auf-USB-A-Kabel für die
Stromversorgung **an**." (20 words before the prefix lands), the mid-paragraph rename
„USB-C-auf-USB-A-Kabel" → „USB-A-Kabel", the double „mit" in „mit einer Spielkonsole mit
USB-C-Anschluss", and „erscheint das Videosignal … auf dem Monitor" (a *Signal* does not
*erscheinen*; the *Bild* does).

---

## de/manuals/lite/osd.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „**Rot (0–100):** Passe die Helligkeit des roten RGB-Werts an." (likewise Grün, Blau) | A *Wert* has no *Helligkeit* — the sentence is not meaningful in German. `expand/osd.mdx` gets it right: „Passe den Rotkanal an (0–100)." | „**Rot (0–100):** Passe den Rotanteil an." | **Major** |
| „**Sprache:** Wähle aus 12 verfügbaren Sprachen für die Anzeige des OSD-Menüs." | English word order retained; „für die Anzeige des OSD-Menüs" dangles at the end with nothing to attach to. | „**Sprache:** Wähle die Sprache des OSD-Menüs aus 12 verfügbaren Sprachen." | **Major** |
| „**Farbtemperatur:** Wähle User, Warm oder Cool, um die gesamte Farbintensität anzupassen." | „die gesamte Farbintensität" is *the overall color intensity* transferred literally — and it is also the wrong concept under *Farbtemperatur*, which shifts the white point rather than intensity. | „**Farbtemperatur:** Wähle User, Warm oder Cool, um die Farbwiedergabe des Bildschirms anzupassen." | **Major** |
| Heading „### 1. Helligkeit" (Lite) vs. „## Hintergrundbeleuchtung" (Flip) vs. „### 1. Hintergrundbeleuchtung" (Expand) for the same OSD section | Cross-product inconsistency, and on this page the heading also collides with the „Helligkeit" setting inside it. | „### 1. Hintergrundbeleuchtung" | Minor |

Noted, not counted: „**Standard:** Standard-Bildmodus." (empty gloss), the stacked double
parentheses in „**DCR (Dynamic Contrast Ratio) (ON/OFF):**", and „Transparenz … für eine bessere
Sicht" (should be *Lesbarkeit*).

---

## de/manuals/lite-144hz/ (index, controls, installation, osd)

Content is otherwise identical to `lite/`, so all Lite findings apply again. Nothing additional
rises to Major. Worth noting for the fix pass: „Er ist **dafür gemacht**, Gamern und Power-Usern
einen **flüssigen** zweiten Bildschirm … zu bieten." — the parallel OneCable/Lite sentence uses the
formal „darauf ausgelegt", so the register drifts between sibling manuals; and a screen is not
*flüssig*, its *Darstellung* is („einen zweiten Bildschirm mit flüssiger Darstellung").
Frontmatter and the SI-spaced „144 Hz" are correct.

---

## de/manuals/flip/index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…ein faltbarer Multiscreen-Monitor, den du **um** deinen Laptop klemmst" | Wrong preposition — *um … klemmen* means clamping *around* something. `expand/index.mdx` has the right form: „den du **an** deinen Laptop klemmst". | „…den du an deinen Laptop klemmst" | **Major** |
| „Beide seitlichen Bildschirme **klappen** flach an das mittlere Gehäuse, sodass du…" | Intransitive *klappen* with a directional accusative reads as if the screens fold themselves. German needs the modal/reflexive form. | „Beide seitlichen Bildschirme **lassen sich** flach an das mittlere Gehäuse **klappen**, sodass du…" | **Major** |
| Tab „Flip 14"": „**Farbraum** \| 45 % NTSC" — Tab „Flip 15,6"": „**Farbgenauigkeit** \| 45 % NTSC" | **The same spec row carries two different German labels in two tabs of one table on one page.** Identical defect on `expand/index.mdx` („Farbraum" in the 14" tab, „Farbgenauigkeit" in the 15,6" tab). „Farbgenauigkeit" is additionally the wrong term for a gamut figure — it denotes colour *accuracy* (a ΔE quantity), not coverage; OneCable and Lite use it too („100 % sRGB", „99 % sRGB"). | „Farbraum" in every tab of every product. | **Major** |
| „0° – 245°" / „0° – 205°" (spaced en dash) vs. „(0–100)" and „(10–60 Sekunden)" (unspaced) elsewhere in the set | Inconsistent Bis-Strich typography across the German pages. | Standardise: „0°–245°", „0–100", „10–60 Sekunden". | Minor |

Noted, not counted: „der dir zwei zusätzliche Bildschirme … **gibt**" (German copy *bietet*); the
half-bolded label „- **Linker** Bildschirm:" where Expand bolds the whole label; and the
parenthetical „(lässt sich 180° nach oben und unten neigen)" sitting behind a stated 245° range,
which the German cannot reconcile.

---

## de/manuals/flip/controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „- **M** – OSD-Menütaste." (Flip controls) / „Drücke die Taste **M** (Menu)" (Flip osd) / „- **≡ Menütaste:** Öffnet das Bildschirmmenü (OSD)." (Expand controls) / „Drücke die Taste **M (Menu)**" (Expand osd) | **Inside the Expand manual the same button is „≡ Menütaste" on the controls page and „Taste M (Menu)" on the very next page** — the customer cannot map the instruction to the hardware. Flip additionally uses a third list format for identical content. | Name the button once per product (symbol + letter, e.g. „Menütaste **M** (≡)") and use that name on both pages. | **Major** |
| „- **USB-C-Anschluss:** Stromversorgung und Videoübertragung.<br>- **USB-C-Anschluss:** Stromversorgung und Videoübertragung." | Two byte-identical bullets. Reads as a copy-paste slip rather than "there are two of these ports". Same on `expand/controls.mdx`. | „- **2× USB-C-Anschluss:** Stromversorgung und Videoübertragung." (or number them 1 / 2) | Minor |

---

## de/manuals/flip/installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „2. Klappe den rechten Bildschirm **in die in Abbildung 2 gezeigte** Richtung auf.<br>3. Klappe den linken Bildschirm auf, **wie in Abbildung 3 gezeigt**." | The stacked „in die in …" participle is clumsy German — and the very next step renders the identical instruction the natural way. Two consecutive steps, two grammars. The same construction appears in „Den Screenmate verstauen" step 2 and on `expand/installation.mdx` step 2. | „2. Klappe den rechten Bildschirm auf, wie in Abbildung 2 gezeigt." | **Major** |
| „Um herauszufinden, welche Kabel du brauchst, **prüfe zuerst**, welche Anschlüsse infrage kommen." → „**Prüfe zuerst**, welche Anschlüsse der **Screenmate** hat." → „**Prüfe zuerst**, welche Anschlüsse dein **Laptop** hat." | Three „prüfe zuerst" in twelve lines, and the last two contradict each other about what to check first (device vs. laptop) with no stated reason. No German editor would leave this. | „Prüfe zuerst, welche Anschlüsse dein Laptop hat — die Symbole unten helfen dir dabei. Welche Anschlüsse der Screenmate selbst hat, siehst du hier:" | **Major** |

Noted, not counted: „&" used as a conjunction in German running text („1× USB-C & 1× USB-A & 1×
HDMI", also on Expand — „&" belongs in names and UI labels, not between cable counts); and the
section-name drift „## Installationsanleitung" (Flip, OneCable) vs. „## Installationsschritte"
(Expand).

---

## de/manuals/flip/osd.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Verfügbare Sprachen: Englisch, Französisch, Deutsch, **Vereinfachtes Chinesisch**, Italienisch, …" | **Orthography error**: the adjective must be lower-case („vereinfachtes Chinesisch"); the capital is English title-case bleeding through. `expand/osd.mdx` has both the correct case and the better German form, „Chinesisch (vereinfacht)". | „…, Chinesisch (vereinfacht), …" | **Major** |
| „das **OSD-Menü** zu öffnen" (step 1) / „nach der sich das **Einstellungsmenü** automatisch schließt" / „Transparenz des **Einstellungsmenüs**" / frontmatter „**Bildschirmmenü** (OSD)" | Three German names for the same menu on one page — four across the set (Bildschirmmenü / OSD-Menü / OSD / Einstellungsmenü). On a page whose entire purpose is explaining that menu, this is the most visible consistency defect in the German copy. | Introduce „das Bildschirmmenü (OSD)" once, then use „OSD-Menü" throughout; drop „Einstellungsmenü". | **Major** |

Noted, not counted: three formats for the same OSD row across three manuals („Einstellbar von 0 bis
100" / „Passe die Helligkeit des Bildschirms an (0–100)" / „**Helligkeit (0–100):** Passe die
Helligkeit des Bildschirms an."); „falls das Gerät kompatibel ist" where Expand says the clearer
„wenn dein Gerät es unterstützt"; and „Wähle aus **zwei** Signalquellen: Type-C1 / Type-C2 und
HDMI" listing three tokens.

---

## de/manuals/expand/index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „ist ein tragbarer Monitor **mit drei Bildschirmen**, den du an deinen Laptop klemmst und **zu zwei Full-HD-Bildschirmen** aufklappst – einer auf jeder Seite." | Three then two in the same sentence; the reader must reach the *next* sentence to resolve it. „zu zwei Bildschirmen aufklappen" is also not a German collocation, and the loose apposition „– einer auf jeder Seite" needs „je". | „Der Screenmate Expand ist eine tragbare Bildschirmerweiterung, die du an deinen Laptop klemmst und aufklappst: Du bekommst zwei Full-HD-Bildschirme, je einen auf jeder Seite. So wird aus deinem Laptop ein Arbeitsplatz mit drei Bildschirmen." | **Major** |
| „- **6× Schutzclips**" | Multiplier plus plural. German pairs „×" with the singular („6× Schutzclip") or drops it („6 Schutzclips"); every other item in the same list follows the singular pattern („2× USB-C-auf-USB-C-Kabel"). | „- **6× Schutzclip**" | Minor |

The „Farbgenauigkeit" (15,6") vs. „Farbraum" (14") split in this page's spec tabs is the same Major
logged under `flip/index.mdx`.

---

## de/manuals/expand/controls.mdx

The „≡ Menütaste" vs. „Taste M (Menu)" collision with `expand/osd.mdx` is logged as a Major under
`flip/controls.mdx`. Otherwise clean. Minor, not counted: „- **− Helligkeit verringern:**
Verringert die Helligkeit des Bildschirms." repeats its own label verbatim, twice in a row, and
says „des Bildschirms" (singular) on a three-screen product.

---

## de/manuals/expand/installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „## **Schutzkappe** — Wenn dein Laptopbildschirm dünner als 6 mm ist, verwende die Schutzkappe…" against `expand/index.mdx` Lieferumfang „- **6× Schutzclips**" | The part shipped as „Schutzclips" is called „Schutzkappe" — different word, different number — on the page that tells you to use it. The customer cannot find the part in the box. | One name on both pages, with agreeing count: „Setze einen der sechs **Schutzclips** auf…" | **Major** |

„2. Klappe die beiden Bildschirme in die in Abbildung 2 gezeigte Richtung auf." is the same Major
logged under `flip/installation.mdx`. Noted, not counted: „damit dein Bildschirm sicher
eingeklemmt ist" (alarming — the intent is that the *Screenmate* sits firmly); „Stecke den
HDMI-Hub … **in** deinen Laptop" (German connects peripherals *an*); alt „Installationsschritte 1
bis **6**" for a five-step procedure; and „die **richtigen** Kabel" / „die **passenden** Kabel" /
„die **benötigten** Kabel" across the three manuals.

---

## de/manuals/expand/osd.mdx

The best-written page in the reviewed set. „Passe den Rotkanal an (0–100)", „Chinesisch
(vereinfacht)", „wenn dein Gerät es unterstützt" and „Lege fest, wie lange das Einstellungsmenü
sichtbar bleibt, bevor es sich automatisch schließt" are all the forms the other manuals should
adopt. No findings of its own; „## Das OSD verwenden" vs. Flip's „## Das OSD-Menü verwenden" is
part of the menu-naming Major above.

---

## Frontmatter-only checks (bodies skipped as byte-identical)

| File(s) | title / description | Verdict |
|---|---|---|
| `lite`, `lite-144hz`, `flip`, `expand` `/safety.mdx` | „Sicherheitshinweise" / „Wichtige Sicherheitshinweise und Warnungen" | Idiomatic and identical across all five products. No findings. |
| `flip/display-settings.mdx` | „Anzeigeeinstellungen" / „Bildschirme unter Windows und macOS einrichten" | Good German — but differs from the byte-identical OneCable/Expand pages. Minor, logged above. |
| `expand/display-settings.mdx` | „Anzeigeeinstellungen" / „Anzeigeeinstellungen für Windows und macOS" | Description echoes its own title; Flip's wording is better. Same Minor. |

---

## Totals

| Severity | Count |
|---|---|
| **Critical** | **1** |
| **Major** | **34** |
| **Minor** | **20** (capped per brief; further polish items are named inline as "noted, not counted") |

Majors by file — manuals-index 1 · onecable/index 1 · onecable/controls 3 ·
onecable/display-settings 2 *(×3 pages)* · onecable/installation 4 · onecable/installation-mac 1 ·
onecable/safety 2 *(×5 pages)* · onecable/troubleshooting 3 · lite/index 1 · lite/controls 2 ·
lite/installation 1 · lite/osd 3 · flip/index 3 · flip/controls 1 · flip/installation 2 ·
flip/osd 2 · expand/index 1 · expand/installation 1.
Shared defects are counted once, at the file where they are clearest.

**Zero findings** in these categories, which is worth stating explicitly:

- No *Sie* leakage and no du/Sie mixing anywhere in `de/` (grep-verified).
- No case, gender or agreement errors — with exactly one exception, „deines Mac" → „deines Macs".
- Compound hyphenation around the retained English terms is correct throughout:
  „USB-C-auf-USB-A-Kabel", „3,5-mm-Klinkenanschluss", „Mini-HDMI-auf-HDMI-Kabel",
  „Real-Time-Strategy-Spiele", „Reverse-Charging-Modus", „Screenmate-Produkthandbücher". This is
  the single most common failure mode in German technical translation and it has been avoided
  completely.
- German quotation marks („…") wherever quotes appear; en dashes for parentheticals; true minus in
  „−20 °C" and „±2 V"; SI spacing („45 W", „100 %", „144 Hz", „5 V/2 A"); decimal commas („15,6"",
  „34,5 × 22 × 2,5 cm"); „ß" and capitalisation correct throughout.
- No untranslated Dutch or English source fragments in body copy (grep-verified).

---

## Verdict

**Would a German customer notice this is a translation?**

Not on a first pass. On a careful read of any single manual — yes, in three or four specific places.

**Readability grade: near-native**, with the OneCable pages trailing at the edge of *noticeably
translated* and the Expand pages reading essentially native.

**Reasoning.**

What is genuinely native here is the *surface*. Orthography, declension, compound hyphenation,
punctuation, unit typography and the du-voice are handled at the level of a competent German
editor, and handled consistently. A customer scanning for the cable diagram will find nothing to
trip over. That is the hard part, and it is done.

What gives the copy away is the *sentence architecture* in a recurring minority of sentences —
always the same tell, always English shape carried into German words: „der darauf ausgelegt ist, …
zu steigern, indem er …", „Das ist der Hauptanschluss, um … anzuschließen", „wird verwendet für:",
„Wähle aus 12 verfügbaren Sprachen für die Anzeige des OSD-Menüs", „Begrenze die Einwirkung von
starken Magnetfeldern", „Alle Screenmate-Produkte durchsuchen", „Passe die Helligkeit des roten
RGB-Werts an". Each is individually survivable; together they form a fingerprint. A German
technical writer starting from a blank page would produce none of them, and a reader who slows down
feels the English underneath — most strongly on the OneCable pages, least on Expand.

The second and more consequential tell is **terminology drift**, which is a German-internal defect
and cannot be attributed to the source. One menu carries four names (Bildschirmmenü / OSD-Menü /
OSD / Einstellungsmenü). One port carries four (Power-Anschluss / Power-USB-C-Anschluss /
USB-C-Anschluss (nur Strom) / Hauptanschluss). One spec row carries two labels *inside a single
table*, on both Flip and Expand (Farbraum vs. Farbgenauigkeit). One button is „≡ Menütaste" on one
page of the Expand manual and „Taste M (Menu)" on the next. The device is Monitor / Bildschirm /
Gerät / Screenmate within a single safety list. German readers are unusually intolerant of this —
in German technical prose, a changed word is read as a changed referent — so this, rather than any
one awkward sentence, is what a native would notice first.

Two items must be resolved before sign-off irrespective of language quality: the **5 V vs. 5–20 V
contradiction in the shared safety page** (Critical, published across five products), and the
**Scrollrad / „Power- und Zurück-Taste" function mismatch** on the Lite pages, where a control's
German name contradicts the function documented beside it.

Clearing the 34 Majors would move the whole set to native. Most are single-sentence rewrites, and
roughly a third are simply "use the wording Expand already uses" — the good German version of
nearly every defective sentence already exists somewhere in this corpus. It just has not been
propagated across the five manuals.
