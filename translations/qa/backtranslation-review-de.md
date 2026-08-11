# Back-translation divergence review — German

Adjudication of the four blind German back-translations against the English originals.

| Batch | Scope | Files |
| :--- | :--- | ---: |
| `backtranslation-de-F1.md` | `onecable/` (8), `infinity/` (5), `infinity-lite/` (5) | 18 |
| `backtranslation-de-F2.md` | `lite/` (5), `lite-144hz/` (5), `panorama/` (5), `manuals-index` (1) | 16 |
| `backtranslation-de-F3.md` | `flip/` (6), `dual-flip/` (6) | 12 |
| `backtranslation-de-F4.md` | `expand/` (6), `one-4k/` (5), `one-4k-oled/` (5) | 16 |
| **Total** | | **62** |

Coverage is complete: `en/` and `de/` both contain 62 `.mdx` files with exact 1:1 path parity — no file missing, no file added.

## Method

Each `## {file path}` section of the back-translations was read against its `en/` counterpart (`de/...` → `en/...`) line by line. Phrasing, register, synonym choice and back-translation looseness were disregarded; only differences in the **meaning a German reader receives** were recorded.

Three mechanical parity sweeps backed up the manual read across all 62 file pairs:

| Sweep | Result |
| :--- | :--- |
| Numeric tokens in body prose (specs, voltages, angles, wattages, ranges, step numbers) | **0 mismatches** |
| Callout components (`Note` / `Warning` / `Info` / `Tip`) by type and count | **0 mismatches** |
| Structure (headings, bullet lists, ordered lists, table rows) | **0 mismatches** |

No quantity or specification value drifted in any file, no warning was downgraded, dropped or added, and no section was dropped or invented.

## 1. Divergence table

| File | EN passage | Back-translated passage | Severity | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| `infinity-lite/display-settings.mdx` (video tab, Windows) | "go to 'Display orientation' and choose **'Mirrored'** to correct this" | "go to 'Display orientation' and choose **'Landscape (flipped)'** to correct this" (DE: „Querformat (gedreht)“) | moderate | **EN-source quirk** — DE silently normalised. EN is the defect: this is the only `'Mirrored'` among 7 display-orientation instructions in `en/`, the other 6 say `'Flipped'`, and Mirrored is a different Windows feature that would not fix an upside-down screen. German is correct and internally consistent. Fix belongs in EN. |
| 6 × `display-settings` / `osd` pages (`onecable`, `flip`, `dual-flip`, `expand`, `infinity`, `panorama`) | "choose **'Flipped'**" | "choose **'Landscape (flipped)'**" (DE: „Querformat (gedreht)“) | cosmetic | **loop artifact / correct localisation** — DE expands EN's shorthand to the full Windows German label. More precise, not a meaning change. No action. |
| `flip/index.mdx` | "a foldable multi-screen monitor that **clips around** your laptop" | "a foldable multiscreen monitor that **folds around** your laptop" (DE: „um deinen Laptop herum geklappt wird“) | cosmetic | **de-side drift** — attachment verb generalised from clipping to folding. The following sentence about the side screens folding flat preserves the practical sense. Optional polish. |
| `infinity/index.mdx` | "that **clips behind** your laptop" | "**You attach it** behind your laptop" (DE: „Du befestigst ihn“) | cosmetic | **de-side drift** — same generalisation of the attachment verb. Optional polish. |
| `flip/index.mdx`, `expand/index.mdx` (package contents) | "Protective **Sleeve**" / "Cable **organizer**" | "Protective **case**" / "Cable **holder**" (DE: „Schutzhülle“ / „Kabelhalter“) | cosmetic | **de-side drift** — accessory nouns rendered one notch more generic. Note `dual-flip` and `onecable` EN say "Protective case", so German is at least self-consistent across the range. Glossary candidate. |
| `infinity-lite/installation.mdx` step 4 | "**Click open** the frame to extend it." | "**Fold the frame open until it clicks into place**, in order to extend it." | cosmetic | **de-side drift** — DE disambiguates an ambiguous EN phrase. The German is clearer; EN "Click open" is the weaker text. No action. |

**No critical divergence was found.** No instruction is inverted, no safety warning is weakened or missing, no specification value differs, and no content is dropped or added on the German side.

## 2. EN-source issues

Defects and inconsistencies that originate in `en/` and were faithfully mirrored into `de/`. These are not translation defects — but because they are mirrored, they reach the German reader too, so they should be fixed in EN and re-propagated. The back-translators' embedded "notable" flags are adjudicated here.

### Safety and specification

1. **Safety items 5 and 6 contradict each other** — "The monitor operates on a DC input between 5V and 20V (±2V)" immediately followed by "Only use the device with a 5V power source via the appropriate cable." Present on all 8 numbered safety pages (`onecable`, `lite`, `lite-144hz`, `flip`, `dual-flip`, `expand`, `one-4k`, `one-4k-oled`) and mirrored verbatim. Flagged independently by F1 and F4. Highest-value EN fix in this list.
2. **"Recommended ambient temperature: between -20°C and 60°C"** — a -20 °C to 60 °C span is an operating/storage limit, not a *recommended* ambient. Present on every safety page.
3. **`flip/osd.mdx` and `expand/osd.mdx` SOURCE: "Choose between two signal sources: Type-C1 / Type-C2 and HDMI"** — says two, lists three. `dual-flip/osd.mdx` gets it right ("three signal sources: Type-C1, Type-C2, and HDMI"). Flagged by F4.
4. **`one-4k-oled/safety.mdx` carries no OLED-specific guidance** — no burn-in / static-image warning on an AM-OLED panel, despite being otherwise byte-identical to the LCD siblings' safety text. Flagged by F4.

### Contradictory or impossible instructions

5. **`infinity/controls.mdx` gesture pairing is incomplete** — "Press right ('Plus'): increase the backlight (brightness). Press left ('Min'): decrease the volume." Neither function gets both directions: brightness can be raised but never lowered, volume lowered but never raised. Flagged by F1; confirmed as EN-source, mirrored exactly.
6. **`infinity-lite/controls.mdx` inverts its sibling's mapping** — Infinity Lite assigns Left "Min" to brightness and Right "Plus" to volume; Infinity assigns right "Plus" to brightness and left "Min" to volume. The two sibling products contradict each other in EN.
7. **`infinity-lite/installation.mdx` references a "third" port** — the Warning says to connect the HDMI-to-USB-C cable to the **third** port, but `infinity-lite/controls.mdx` documents only two USB-C ports plus a 3.5 mm jack.
8. **`panorama/controls.mdx` Power Button documents only power-off** — "Long press (1 second): Switch the monitor off"; no power-on gesture is given anywhere on the page.
9. **`onecable/installation.mdx` charging note is circular** — "Use a power adapter of at least 45W. No USB-C charger? Use a suitable power adapter." Flagged by F1.

### Single-screen product carrying dual-screen text

10. **`infinity-lite/installation.mdx`: "safely deploy both extension screens"** — plural, on a one-screen product. Flagged by F1.
11. **`infinity-lite/display-settings.mdx` sound sections: "(the other screen appears as S6-R)" / "(the other screen appears as S6-L)"** — copied from the dual-screen Infinity page. Flagged by F1.

### Labelling and consistency

12. **`expand/index.mdx` colour-spec row labelled differently per tab** — 15.6" tab says "Color Accuracy 72% NTSC", 14" tab says "Color Gamut 45% NTSC" for the same row. Flagged by F4.
13. **`flip/index.mdx` has the same split** — 14" tab "Color Gamut", 15.6" tab "Color Accuracy", both 45% NTSC.
14. **`one-4k/index.mdx` "Dimensions" vs `one-4k-oled/index.mdx` "Dimensions (folded)"** — same 34.8 × 22.4 × 1.3 cm figure, and neither is a folding product. Flagged by F4.
15. **`expand/installation.mdx` step count vs image alt** — 5 numbered steps, alt text reads "Installation steps 1 through 6"; step 2 cites "image 2" though the page has no figure numbering. Flagged by F4.
16. **`expand/installation.mdx` "Protective Cap" (singular) vs `expand/index.mdx` "6x protective clips"** — same accessory, two names, two counts. Flagged by F4.
17. **`expand/controls.mdx` lists two byte-identical USB-C bullets** — "Power supply and video transfer" twice, with nothing distinguishing left/right or port 1/2. Flagged by F4.
18. **`expand/osd.mdx` files "HDR Mode" under the "Reset" section heading.** Flagged by F4.
19. **`flip/installation.mdx` heading asymmetry** — the Flip 14" section says "First check which ports **the Screenmate** has", the Flip 15.6" section says "First check which ports **your laptop** has".
20. **`infinity/installation.mdx` cable list reads "1× USB-C & 1× USB & 1× HDMI"** — "1× USB" is incomplete; the surrounding prose says USB-A.
21. **`infinity/installation.mdx` horizontal and vertical dual-screen setups have identical steps** — the two procedures differ only in the words "horizontal"/"vertical", so the instructions do not actually distinguish the layouts.
22. **`one-4k` and `one-4k-oled` installation §5 alt text mentions a "camera"** that appears nowhere in the body's device list (PC, laptop, Xbox, PlayStation 4/5, Nintendo Charging Dock). Flagged by F4.
23. **`one-4k-oled/installation.mdx` §3 omits the "not every USB-C port can output video" caveat** that `one-4k/installation.mdx` §3 carries. Flagged by F4.

### Assets and authoring residue

24. **`expand`, `flip` and `dual-flip` `display-settings.mdx` all embed OneCable screenshots** — `Screenmate - OneCable - Handleiding images/...`, not the products' own assets. Flagged by F4.
25. **`one-4k-oled/controls.mdx` "USB-A Port" section is empty** — it contains only an unresolved `{/* TODO: confirm with Louie ... */}` comment, so the heading renders with no body while the non-OLED sibling has a full paragraph. Flagged by F4.
26. **Unresolved authoring TODOs still in source** — `one-4k/osd.mdx`, `one-4k-oled/osd.mdx` and `one-4k-oled/controls.mdx` carry MDX comments naming Louie / "the client". Not rendered, but they mark genuinely unconfirmed content (the per-section OSD menu tree). They are also the one place the two OSD pages diverge in wording, which is why F4 saw them as suspicious.

### Structural note (outside the semantic scope)

27. **No cross-language frontmatter on any German page** — 0 of 62 `de/` files carry `en_link` or `nl_link`, and 0 of 62 `en/` files carry `de_link`. Per the language-switcher architecture (language-first paths since `ab10152`), these keys are required on every page for the switcher to resolve. Expected work-in-progress on `lang-expansion-de-fr-it`, flagged here so it is not lost before merge.

## 3. Summary counts

### German-side divergences

| Severity | Count |
| :--- | ---: |
| Critical (wrong instruction / safety / spec) | **0** |
| Moderate (noticeable meaning shift) | **0** |
| Cosmetic | **4** |

The 4 cosmetic items are two attachment-verb generalisations (`flip/index`, `infinity/index`), one accessory-noun pair (`Schutzhülle` / `Kabelhalter`), and one clarifying elaboration (`infinity-lite/installation` step 4). None requires action; the accessory nouns are the only glossary candidates.

### Divergence table by verdict

| Verdict | Rows | Severity spread |
| :--- | ---: | :--- |
| de-side drift | 4 | 0 critical, 0 moderate, 4 cosmetic |
| EN-source quirk | 1 | 1 moderate |
| loop artifact | 1 | 1 cosmetic |
| **Total rows** | **6** | |

### EN-source issues

| Category | Count |
| :--- | ---: |
| Safety and specification | 4 |
| Contradictory or impossible instructions | 5 |
| Single-screen product carrying dual-screen text | 2 |
| Labelling and consistency | 12 |
| Assets and authoring residue | 3 |
| Structural (outside semantic scope) | 1 |
| **Total** | **27** |

## Verdict

The German translation is faithful. Across 62 file pairs, every specification value, voltage, angle, wattage, range and step number matches; every callout retains its original severity; every heading, list and table row is preserved. No instruction is inverted and no warning is weakened.

The single moderate divergence found (`infinity-lite/display-settings.mdx`, `'Mirrored'`) resolves in the German's favour — the translator normalised an English defect. The remaining German-side differences are four cosmetic word choices.

The substantive quality risk in this content set sits in the **English source**, not the German. Items 1, 5, 6, 7 and 8 above are the ones that mislead a reader in any language and should be resolved in `en/` and re-propagated to `de/`, `nl/`, `fr/` and `it/`.
