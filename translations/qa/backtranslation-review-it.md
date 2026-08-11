# Back-translation divergence review — Italian

Adjudication of the four blind Italian back-translations (`backtranslation-it-F1/F2/F3/F4.md`)
against the English originals (`en/manuals/**`, `en/manuals-index.mdx`), mapping `it/...` → `en/...`.

Scope: **semantic** divergence only — meaning changed, instruction inverted, quantity changed,
warning weakened or dropped, content dropped or added. Phrasing, register and style differences are
out of scope, as are artefacts of the back-translation itself.

Coverage: 62 EN files ↔ 62 IT files (all present, no orphans).

## Method and mechanical checks

Beyond the section-by-section read, two mechanical sweeps were run over all 62 file pairs:

- **Numeric sweep** — every numeric token extracted from both sides (Italian decimal commas
  normalised to points) and diffed. **Result: zero divergences.** Every voltage, amperage, wattage,
  angle, dimension, weight, timing, range and count in the Italian matches the English exactly. The
  only diffs reported were the `nl_link` frontmatter lines present in EN and absent in IT (which
  contain the digits `144` and `4` in their paths) — see the structural note at the end.
- **Structural sweep** — heading count, list-item count, callout count (`Note`/`Warning`/`Info`/
  `Tip`), `<img>` count and `<video>` count compared per pair. **Result: full parity on all 62
  pairs.** No section, list item, callout, image or video was dropped or added.

This means the two highest-risk categories — quantity drift and dropped warnings — are clean, and
the residual findings below are all wording-level.

---

## 1. Divergence table

| # | File | EN passage | Back-translated IT passage | Severity | Verdict |
|---|------|-----------|---------------------------|----------|---------|
| 1 | `it/manuals/infinity-lite/display-settings.mdx` (video tab) | "Select the relevant screen, go to 'Display orientation' and choose **'Mirrored'** to correct this." (section above the tabs says **'Flipped'**) | "…vai su 'Orientamento dello schermo' e scegli **'Duplicato'**…" (section above says **'Capovolto'**) | moderate | **EN-source quirk** — see adjudication A |
| 2 | 6 × `display-settings.mdx` (onecable, flip, dual-flip, expand, infinity-lite ×2) | "**Need more overview?** Click 'Scale' and set it to 150%…" | "**Vuoi più spazio a schermo?** ('Do you want more space on screen?') Fai clic su 'Ridimensionamento' e impostalo su 150%…" | cosmetic | **it-side drift** (benign harmonisation) — see adjudication C |
| 3 | `it/manuals/onecable/installation-mac.mdx` steps 4 / 1 | "Go to **'System Settings'** > **'Privacy & Security'** > **'Screen & System Audio Recording'**." (no gloss) | Same, plus added Italian glosses: "('Impostazioni di Sistema') … ('Privacy e sicurezza') … ('Registrazione schermo e audio di sistema')"; likewise "('Applicazioni')", "('Apri')" | cosmetic | **it-side addition** (beneficial; content added, meaning unchanged) |
| 4 | `it/manuals-index.mdx` (commented-out template block) | `href="/en/manuals/[product-slug]/index"` inside a JSX comment | Identical, still `/en/…` | cosmetic | **it-side drift** (copied verbatim; not reader-visible, maintenance nit only) |
| 5 | `it/manuals/expand/*` heading levels (F4 flag) | `## Ports and Buttons` → `### Buttons` / `### Ports` | Source checked: `## Porte e pulsanti` → `### Pulsanti` / `### Porte` — identical to EN | — | **loop artifact** (F4 rendered H2 as `###` throughout its own output) |
| 6 | `it/manuals/flip/display-settings.mdx`, `dual-flip` (F3 flag: "UI labels in English with Italian gloss") | EN keeps the English label + a **Dutch** gloss: `**Display settings** ('Beeldscherminstellingen')` | IT keeps the English label + an **Italian** gloss: `'Display orientation' ('Orientamento dello schermo')` — correct localisation of the gloss | — | **loop artifact** (F3 translated the Italian gloss into English, making it look duplicated) |
| 7 | `it/manuals/panorama/osd.mdx` (F2 flag: "Ridimensionamento is not the standard Windows Italian label") | "Click **Scale**…" | "Fai clic su **Ridimensionamento**…" | — | **loop artifact** — `Ridimensionamento` *is* the correct Italian Windows label (Impostazioni → Schermo → *Ridimensionamento e layout* → *Ridimensionamento*). No divergence. |
| 8 | `it/manuals/lite/index.mdx` etc. (F2 flag: decimal commas) | `15.6"`, `35.4 × 22.1 × 1.1 cm` | `15,6"`, `35,4 × 22,1 × 1,1 cm` | — | **loop artifact** — correct Italian decimal convention; values identical (confirmed by numeric sweep) |
| 9 | `it/manuals/panorama/installation.mdx` (F2 flag: "blocco anteriore" ambiguous) | "…until the legs sit in the **front lock**." | "…finché i piedini non entrano nel **blocco anteriore**." | — | **loop artifact** — faithful rendering of an ambiguity already present in EN ("front lock") |
| 10 | `it/manuals/flip/safety.mdx` vs `dual-flip/safety.mdx` (F3 flag: numbered vs bulleted) | EN Flip = numbered 1–14; EN Dual Flip = bulleted | IT Flip = numbered 1–14; IT Dual Flip = bulleted | — | **loop artifact** — exact mirror of the EN pair |
| 11 | `it/manuals/dual-flip/installation.mdx` (F3 flag: image after steps, unlike Flip) | EN Dual Flip places the image after the steps; EN Flip places it before | Identical placement in IT | — | **loop artifact** — exact mirror |
| 12 | `it/manuals/dual-flip/osd.mdx` (F3 flags: `COLOR TEMP` vs `COLOR TEMP.`, `HDR` vs `HDR MODE`, bare vs glossed tokens) | EN Dual Flip uses bare ALL-CAPS tokens, `COLOR TEMP`, `HDR`; EN Flip uses glossed names, `COLOR TEMP.`, `HDR MODE` | Identical split in IT | — | **loop artifact** — exact mirror of an EN sibling inconsistency |

### Adjudication A — `Duplicato` vs `Capovolto` (F1's flag)

**Ruling: EN-source quirk faithfully mirrored. Not Italian-side drift.**

`en/manuals/infinity-lite/display-settings.mdx` gives two different fixes for the same problem on the
same page:

- line 18 (prose section): "…go to **Display orientation** and choose **Flipped** to correct it."
- line 54 (video tab): "…go to 'Display orientation' and choose **'Mirrored'** to correct this."

The Italian reproduces the pair one-for-one: `it/…/display-settings.mdx` line 17 → **`Capovolto`**,
line 53 → **`Duplicato`**.

- `Flipped` → `Capovolto` is exact: *Capovolto* is the Italian Windows orientation value
  (*Orizzontale (capovolto)* / *Verticale (capovolto)*). Italian uses `Capovolto` consistently in all
  8 other places across the corpus where EN says `Flipped` — verified by grep, no exceptions.
- `Mirrored` → `Duplicato` is a defensible rendering of the *concept*: Windows Italian names the
  mirroring mode *Duplica questi schermi* (EN "Duplicate these displays"), so mirroring ↔ duplicating
  are the same thing in Italian Windows vocabulary.

Both readers land in the same place: neither `Mirrored` nor `Duplicato` exists as a value in the
*Display orientation* / *Orientamento dello schermo* dropdown, and following either would not fix an
upside-down screen. The defect is identical in both languages and originates in EN. It belongs in the
EN fix list (item 1 below) and the Italian must be corrected in lockstep — but the Italian rendering
pair is a faithful mirror, not an Italian-side inconsistency.

### Adjudication B — Panorama box contents vs Option 2 (F2's flag)

**Ruling: EN-source quirk faithfully mirrored. Not Italian-side drift.**

`en/manuals/panorama/index.mdx` "Package Contents" lists: Screenmate Panorama; 1× USB-C to USB-C
(1.2 m); 1× USB-C to USB-C (0.5 m); 1× Mini-HDMI to HDMI; 65 W USB-C power adapter — **no USB-A to
USB-C cable**. `en/manuals/panorama/installation.mdx` Option 2 step 2 then instructs: "Connect the
monitor to a USB-A port on your laptop using **a USB-A to USB-C cable**."

`it/manuals/panorama/index.mdx` was read directly and is a line-for-line match of the EN list (same
five entries, same cables, same lengths, same wattage). The Italian neither dropped nor added
anything. The gap is entirely in the English source.

### Adjudication C — "more space on screen" harmonisation

EN uses three different headings for the identical "set Scale to 150%" instruction: **"Need more
overview?"** (×6), **"Want more on-screen space?"** (×1, Infinity), **"Need more room?"** (×1,
Panorama). Italian normalises all nine to **"Vuoi più spazio a schermo?"**.

The Italian therefore matches one EN variant exactly and is a near-synonym of a second ("more room" =
"più spazio"). Only against "Need more overview?" is there any shift, and it is slight. Logged as
cosmetic it-side drift because the wording change was made on the Italian side; the underlying
self-contradiction (150% scaling makes elements *larger*, i.e. fits *less* on screen) is an EN-source
defect and is listed separately below.

---

## 2. EN-source issues

Defects that originate in the English and are faithfully carried into the Italian. Fixing these means
editing EN **and** IT together. None of them is an Italian translation error.

**Contradictory or unfollowable instructions (fix first)**

1. **`Flipped` vs `Mirrored` on the same page** — `infinity-lite/display-settings.mdx` gives two
   different values for the same fix (line 18 vs line 54), and `Mirrored` is not an option in the
   Windows *Display orientation* dropdown at all. IT mirrors as `Capovolto` / `Duplicato`.
2. **Safety list items 5 and 6 contradict each other** — "The monitor operates on a DC input between
   5 V and 20 V" followed by "Only use the device with a 5 V power source". Present in 8 products:
   onecable, lite, lite-144hz, flip, dual-flip, expand, one-4k, one-4k-oled.
3. **Infinity multifunction button offers no way to lower brightness or raise volume** —
   `infinity/controls.mdx`: "Press right ('Plus'): increase the backlight (brightness). Press left
   ('Min'): decrease the volume." The two directions control two different parameters, each in one
   direction only.
4. **Infinity and Infinity Lite map the same buttons to opposite functions** — Infinity: right/Plus =
   brightness, left/Min = volume. Infinity Lite (`infinity-lite/controls.mdx`): left/Min =
   brightness, right/Plus = volume.
5. **Infinity Lite "third port" is undocumented** — `infinity-lite/installation.mdx` Warning:
   "Connect the HDMI to USB-C cable to the **third** port", but `infinity-lite/controls.mdx`
   documents only two USB-C ports plus a headphone jack.
6. **Panorama box contents omit the USB-A to USB-C cable Option 2 requires** — see adjudication B.
7. **Lite / Lite 144 Hz button naming is inverted** — the *scroll wheel* turns the device on and off,
   while the button named *"Power & Return"* opens the OSD and never touches power.
8. **Panorama Power button never documents switching on** — `panorama/controls.mdx` covers long-press
   = off and short-press = OSD only.
9. **One 4K OLED "USB-A Port" section is published empty** — `one-4k-oled/controls.mdx` has a heading
   with nothing under it but a `TODO: confirm with Louie` JSX comment.
10. **Infinity Lite screen count is inconsistent** — index says "one extra portable display";
    installation says "safely deploy **both** extension screens"; display-settings asks "Working with
    **three** screens?".

**Framing / wording defects**

11. **150% scaling framed as gaining space** — "Need more overview?" / "Want more on-screen space?" /
    "Need more room?" all precede an instruction that makes elements larger, i.e. fits less on
    screen. Three different EN headings for one instruction (see adjudication C).
12. **Panorama Option 2 step 3 says "the HDMI port" (singular)** while `panorama/controls.mdx` lists
    **3 × Mini HDMI Ports** — the reader is not told which of the three.
13. **"1× USB-C & 1× USB & 1× HDMI"** in `infinity/installation.mdx` leaves "USB" unqualified where
    the icon row directly above specifies USB-A.
14. **One 4K OLED drops a caveat its sibling keeps** — `one-4k/installation.mdx` §3 warns "not every
    USB-C port can output video"; `one-4k-oled/installation.mdx` §3 omits it.

**Cosmetic EN inconsistencies**

15. **Flip spec tabs label the same value differently** — 14" tab = "Color Gamut" 45% NTSC; 15.6" tab
    = "Color Accuracy" 45% NTSC.
16. **Expand spec tabs likewise** — 15.6" = "Color Accuracy" 72% NTSC; 14" = "Color Gamut" 45% NTSC.
17. **"two signal sources" followed by three** — `flip/osd.mdx` and `expand/osd.mdx`: "Choose between
    two signal sources: Type-C1 / Type-C2 and HDMI". `dual-flip/osd.mdx` correctly says three.
18. **Flip installation image references skip** — 6 steps, references run image 2 → image 3 → image 6.
19. **Expand installation step/image mismatch** — 5 steps listed, image alt reads "Installation steps
    1 through 6".
20. **Dual Flip "the maximum angle" is singular** but two angles follow; Flip uses the plural.
21. **Dual Flip storage alt text says "Three-step"** while four steps are listed.
22. **Dual Flip installation step 4 says "in the direction shown"** with no direction given in the
    text and the diagram placed after the list.
23. **One 4K "Dimensions"** vs One 4K OLED **"Dimensions (folded)"** for the same 34.8 × 22.4 ×
    1.3 cm.

---

## 3. Summary counts

**Italian-side drift**

| Severity | Count | Items |
|---|---|---|
| critical | **0** | — |
| moderate | **0** | — |
| cosmetic | **3** | #2 scaling-heading harmonisation; #3 added Italian macOS glosses; #4 commented-out `/en/` template path |

**Other verdicts**

| Category | Count |
|---|---|
| EN-source quirks faithfully mirrored (table rows) | 1 (row #1 — the two adjudicated flags resolve to EN-source items 1 and 6) |
| Loop artifacts / non-divergences (table rows) | 8 (rows #5–#12) |
| **EN-source issues** (consolidated list) | **23** — 10 contradictory/unfollowable, 4 framing/wording, 9 cosmetic |

**Both back-translator flags run down as requested resolve to EN-source, not Italian drift:**

- F1's `Duplicato` vs `Capovolto` → **faithful mirror** of EN's own `Flipped` vs `Mirrored`
  inconsistency on the same page (adjudication A).
- F2's Panorama box-contents omission → **faithful mirror**; the EN box list omits the USB-A to USB-C
  cable too (adjudication B).

**Verdict:** the Italian translation is semantically sound. No meaning was changed, no instruction
inverted, no quantity altered, no warning weakened or dropped, and no content added or lost beyond
three benign cosmetic items. Every substantive problem surfaced by the back-translators traces to the
English source. Priority is to fix EN items 1–10 and propagate the corrections to IT (and to the
other locales, since the same defects will have been mirrored there).

---

## Structural note (outside semantic scope)

The `it/` pages carry **no cross-language frontmatter keys**. Every `en/` page has `nl_link:`; no
`it/` page has an `en_link:` or equivalent (grep across `it/`: 0 hits for `en_link`/`it_link`/
`nl_link`). Under the language-first path architecture the switcher depends on these keys, so they
will need adding to all 62 Italian pages before the locale ships. Flagged here because the numeric
sweep surfaced it; it is not a translation-fidelity finding.
