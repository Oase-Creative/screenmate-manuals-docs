# Back-translation divergence review — French

Adjudication of the four blind back-translations (`backtranslation-fr-F1.md` … `-F4.md`) against the **English originals** (`en/manuals/**`, `en/manuals-index.mdx`), mapping `fr/...` → `en/...` section by section.

Scope: **semantic** divergence only — meaning changed, instruction inverted, quantity changed, warning weakened or dropped, content dropped or added. Phrasing, register and back-translation-loop wording are ignored except where they were mistaken for drift and need adjudicating.

Coverage: all 61 FR pages vs their 61 EN counterparts (F1 = OneCable / Infinity / Infinity Lite; F2 = Lite / Lite 144 Hz / Panorama / manuals-index; F3 = Flip / Dual Flip; F4 = Expand / One 4K / One 4K OLED).

**Headline: no critical divergence, and no fr-side drift above cosmetic.** No instruction was inverted, no quantity was altered, no warning was dropped, no content block was added or removed.

---

## 1. Divergence table

| # | File | EN passage | Back-translated FR passage | Severity | Verdict |
|---|---|---|---|---|---|
| 1 | `onecable/installation.mdx` | "provided the laptop delivers an output power **of more than 10W**. Is the output power **lower than 10W**?" | "provided that the laptop delivers an output power **greater than 10 W**. Is the output power **lower than 10 W**?" | moderate | **EN-source quirk** — the gap at exactly 10 W is in the English original, character for character (« supérieure à 10 W » / « inférieure à 10 W »). FR mirrored it faithfully. **F1's flag resolved: not FR drift.** |
| 2 | 8 display-settings / OSD pages (onecable, infinity, infinity-lite ×2, panorama, flip, dual-flip, expand) | "Go to **Displays**." / "Click **Arrange**." | F1: "Go to **Monitors**." F2–F4: "Go to **Displays**." | cosmetic | **Loop artifact** — the FR source is « Moniteurs » in all 8 places and « Disposition » for Arrange. Those are the actual French macOS System Settings labels. FR is 100 % internally consistent; only the back-translators disagreed on how to render the same French word. **F1's flag resolved: not FR drift, and not an EN issue.** |
| 3 | 7 pages: `onecable`, `flip`, `dual-flip`, `expand`, `infinity`, `infinity-lite`, `panorama` display-settings/osd | "go to 'Display orientation' and choose **'Flipped'**" | "go to 'Display orientation' and choose **'Landscape (flipped)'**" (« Paysage (inversé) ») | cosmetic | **EN-source quirk** — "Flipped" is not a Windows option label; the real English label is "Landscape (flipped)". FR uses the correct French Windows label, consistently in all 7 places. Meaning delivered is the same fix; FR is the more actionable of the two. |
| 4 | `infinity-lite/display-settings.mdx` (Arrange Your Displays → Windows tab) | "go to 'Display orientation' and choose **'Mirrored'** to correct this." | "go to 'Display orientation' and choose **'Landscape (flipped)'** to correct this." | moderate | **EN-source quirk (FR silently corrected)** — this is the one place where the two readers receive materially different instructions. EN contradicts itself on the same page (line 18 says "Flipped", line 54 says "Mirrored"), and "Mirrored" is a different Windows feature that would not fix an upside-down screen. FR normalised both occurrences to « Paysage (inversé) ». Divergence is real; direction of harm is on the EN side. **Fix EN, not FR.** |
| 5 | `manuals-index.mdx` | Card title **"Shop Products"** | Card title **"View the products"** (« Voir les produits ») | cosmetic | **fr-side drift** — commercial CTA softened to a neutral browse label. Card body ("Browse all Screenmate products"), `href` and the `shopping-cart` icon are unchanged, so intent survives. |
| 6 | `panorama/installation.mdx` (Caution callout) | "Watch your fingers **when folding the screens** to avoid pinching." | "watch your fingers **when you fold the screens back**, in order to avoid pinching." | cosmetic | **fr-side drift** — pinch-hazard scope narrowed to the closing direction only (« lorsque vous repliez »). Mitigated: `panorama/safety.mdx` keeps both directions in FR (« repliez ou dépliez »), matching EN's "folding the screens in or out". EN's own installation wording is ambiguous. Warning is not weakened in force, only in scope. |
| 7 | `panorama/index.mdx` | "(or USB-A + HDMI **as a fallback**)" | "(or USB-A + HDMI **as an alternative**)" (« en alternative ») | cosmetic | **fr-side drift** — "fallback" (second-best, use only if USB-C won't do) flattened to "alternative" (co-equal option). Preference ordering is still recoverable from the Option 2 body, which states it is for laptops whose USB-C port does not support video output. |
| 8 | `infinity/index.mdx` (package contents) + `infinity/installation.mdx` (Tip) | "**8x stability rubbers**" / "Use the included **stability rubbers** if your monitor doesn't sit completely steady." | "**8 anti-slip pads**" / "use the supplied **anti-slip pads** if your monitor is not perfectly stable." | cosmetic | **fr-side drift** — the part is renamed by a different function (« patins antidérapants », anti-slip) than EN names (stability). Same component, same quantity (8), same use case preserved verbatim. |
| 9 | `onecable/installation.mdx` step 3 | "Place the **bracket** firmly on a flat surface." (steps 4–5 then refer to the "adjustable **stand**") | F1: "Place the **mounting stand** firmly on a flat surface." | cosmetic | **Loop artifact** — FR reads « support de fixation » (mounting bracket) in step 3 and « support réglable » (adjustable stand) in steps 4–5. The two parts are distinguished in FR, just by qualifier rather than by separate nouns. F1's "mounting stand" was a rendering choice, not the FR text. |
| 10 | `onecable`, `flip`, `dual-flip`, `expand` display-settings; `onecable/installation-windows.mdx` | English UI label + **Dutch gloss**: "Display settings ('Beeldscherminstellingen')", "This PC ('Deze pc')", "'Identify' ('Identificeren')" | French UI labels only: « Paramètres d'affichage », « Étendre le Bureau à cet écran », « Échelle », « Ce PC » | cosmetic | **fr-side drift (intentional localisation)** — the Dutch parentheticals are a residue of the Dutch source booklets and carry no meaning for a French reader. Dropping them and substituting real French Windows labels is correct localisation, applied consistently. |

### Structural verification (mechanical, all 61 file pairs)

Run to catch silent drops/additions the back-translations could have smoothed over. **All clean:**

- Heading counts (`^#{1,6}`) — identical EN↔FR in every file.
- List-item counts (ordered + unordered) — identical in every file.
- `<img>` counts — identical in every file.
- Callout-type sequences (`<Note>` / `<Warning>` / `<Tip>` / `<Info>`) — identical in every file; no warning downgraded to a note anywhere.
- Numeric sweep of every digit token — no quantity divergence. The only differences are the French thousands separator in `100 000:1` (One 4K OLED) and the `nl_link` frontmatter lines that FR pages do not carry.

---

## 2. EN-source issues

Faults that originate in the English originals. The FR pages mirror them faithfully (except #2, which FR silently corrected — see row 4). Fixing these means editing `en/**` first, then propagating.

**Correctness / user-facing**

1. `onecable/installation.mdx` — ">10 W" for single-cable operation vs "<10 W" for the extra-supply case leaves **exactly 10 W undefined**. Pick one boundary (e.g. "10 W or more" / "less than 10 W").
2. `infinity-lite/display-settings.mdx` — the **same page** gives two different fixes for an upside-down screen: "Flipped" (line 18) and **"Mirrored"** (line 54). "Mirrored" is a different Windows feature and would not correct the problem.
3. All display-settings pages — **"Flipped" is not a Windows option label**. The English UI string is "Landscape (flipped)".
4. Safety pages (all products) — item 5 ("DC input between 5 V and 20 V") and item 6 ("Only use the device with a 5 V power source") read as contradictory.
5. `infinity/controls.mdx` — the multifunction button is documented as "Press right = **increase** the backlight / Press left = **decrease** the volume". Asymmetric, and there is no documented way to decrease brightness or increase volume.
6. `infinity/controls.mdx` vs `infinity-lite/controls.mdx` — **opposite left/right mapping** for two sibling products (Infinity: right = brightness, left = volume; Infinity Lite: left = brightness, right = volume). At least one is likely wrong.
7. `flip/osd.mdx` and `expand/osd.mdx` — "Choose between **two** signal sources: Type-C1 / Type-C2 and HDMI" lists three. `dual-flip/osd.mdx` correctly says three.
8. `expand/installation.mdx` — **5** numbered steps, but the image alt reads "Installation steps 1 through **6**".
9. `expand/installation.mdx` vs `expand/index.mdx` — "Protective **Cap**" (singular) in installation vs "**6x** protective **clips**" in package contents.
10. `expand/controls.mdx` — the two USB-C port bullets are **worded identically**, though installation warns "make sure you use the correct USB-C port".
11. `one-4k-oled/controls.mdx` — the **"USB-A Port" heading has no body**, only a TODO MDX comment. Renders as an empty heading. (The One 4K equivalent is fully written.)
12. `flip/installation.mdx` — the 14" subsection says to check **the Screenmate's** ports; the 15.6" subsection says to check **your laptop's** ports.
13. `infinity/installation.mdx` — cable list reads "1× USB-C & 1× **USB** & 1× HDMI" (unqualified "USB"; means USB-A).

**Content gaps / open TODOs**

14. `one-4k/osd.mdx` and `one-4k-oled/osd.mdx` — the **OSD menu tree is undocumented** on both; each carries a TODO MDX comment, worded differently ("the client" vs "Louie").
15. `one-4k-oled/safety.mdx` — byte-identical to Expand and One 4K safety; **no OLED-specific guidance** (burn-in, static images).
16. `one-4k/index.mdx` — **no Package Contents section**, unlike every other index page.

**Consistency / cosmetic**

17. `flip/index.mdx` and `expand/index.mdx` — one size tab labels the NTSC row "Color **Gamut**", the other "Color **Accuracy**", for the same value.
18. `one-4k-oled/index.mdx` — "Dimensions **(folded)**" on a monitor that does not fold; no Product Name / Model Number rows (One 4K has both), identical measurements.
19. `one-4k/installation.mdx`, `lite`, `lite-144hz` — the final image alt mentions a **camera**, which appears nowhere in that section's body.
20. `flip/index.mdx` "Protective **Sleeve**" vs `dual-flip/index.mdx` "Protective **case**" for the same accessory class.
21. English pages still carry **Dutch UI glosses** ('Beeldscherminstellingen', 'Deze pc', 'Identificeren', 'Beeldschermstand', 'Schaal') — a residue of the Dutch source booklets that reads as noise to an English audience.
22. `dual-flip/safety.mdx` uses a bulleted list where every other product's safety page is numbered; `dual-flip/index.mdx` says "the maximum **angle**" (singular) where `flip/index.mdx` says "angles" and lists two.

---

## 3. Summary counts

**fr-side drift** (meaning a French reader receives that differs from the English reader, attributable to the FR translation):

| Severity | Count | Rows |
|---|---|---|
| critical | **0** | — |
| moderate | **0** | — |
| cosmetic | **5** | 5, 6, 7, 8, 10 |

**All divergences by verdict:**

| Verdict | Count | Rows |
|---|---|---|
| fr-side drift | 5 | 5, 6, 7, 8, 10 |
| EN-source quirk | 3 | 1, 3, 4 |
| loop artifact | 2 | 2, 9 |
| **Total table rows** | **10** | |

**EN-source issues:** **22** (13 correctness/user-facing, 3 content gaps, 6 consistency/cosmetic).

### Adjudication of the two named flags

- **F1's ">10 W vs <10 W" flag** → **EN-source quirk, mirrored.** The English original contains the identical boundary gap. No FR action; fix `en/manuals/onecable/installation.mdx` and propagate to all locales.
- **F1's macOS "Monitors" vs "Displays" flag** → **Loop artifact, no drift.** The FR source says « Moniteurs » in all 8 occurrences — the genuine French macOS System Settings pane name. F1 back-translated it literally; F2–F4 back-translated the same word semantically. FR is consistent and correct. No action.

### Verdict

The French translation is **semantically faithful**. Every meaning-bearing element — quantities, thresholds, port assignments, rotation limits, voltage/wattage figures, button gestures, warning severity, step ordering — matches the English. The five fr-side items are all cosmetic register/terminology choices, none of which would lead a French reader to a different action. The one place where the two audiences receive genuinely different instructions (row 4, "Mirrored") is an English defect that the French corrected.

**Recommended action: no French remediation required.** Work the EN-source list, then re-propagate.

---

### Non-semantic note (out of scope, flagged for follow-up)

None of the 61 FR pages carry cross-language link frontmatter (no `en_link` / `fr_link`), while every EN page carries `nl_link`. Per the language-switcher architecture these keys are load-bearing for preserving the current page across a language switch. Not a translation-fidelity issue, but it will need resolving before the FR locale ships.
