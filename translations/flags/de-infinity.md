# DE Infinity flags

Task 7-de / slug `infinity`. Pages: index, installation, controls
(safety.mdx and display-settings.mdx belong to Task 6).

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 2. Blocked: 0. Resolved by orchestrator ruling: 1 (R10).

- [controls.mdx] EN says `The layout is mirrored on both the left and right screen.` /
  NL says `De indeling is identiek op het linker- en rechterscherm.` (= *identical*) —
  **resolved by orchestrator ruling R10 in favour of EN** — proceeded-with
  `Die Anordnung ist auf dem linken und dem rechten Bildschirm spiegelbildlich.`
  R10 rationale: the adjacent `### Lautsprecher` section states each screen's speaker
  sits on its **outer** edge, which is a mirrored layout by definition, not an identical
  one; the IT agent resolved the same conflict the same way and its corroboration was
  decisive. NL `identiek` goes to the client as a probable **NL defect** — the Dutch line
  should become `gespiegeld` on a future NL pass.
  Word choice: `spiegelbildlich` (adjective, standard German technical usage for a
  mirror-image arrangement). Deliberately **not** `gespiegelt` — `Gespiegeld` is the
  Dutch rendering of the Windows *orientation* option, an unrelated string that glossary
  §9 already tells the German pass not to imitate, and reusing the participle here would
  invite exactly that confusion. Proposed glossary addition:
  `| mirrored (physical layout) | spiegelbildlich | Infinity controls; not the Windows orientation option (§9) | — |`

- [index.mdx] EN says `Each screen has built-in speakers` (plural) in `index.mdx` but
  `Each screen has a built-in speaker` (singular) in `controls.mdx`; NL mirrors the same
  split (`ingebouwde luidsprekers` / `een ingebouwde luidspreker`) — proceeded-with the
  per-file EN number: `integrierte Lautsprecher` in `index.mdx`,
  `einen integrierten Lautsprecher` in `controls.mdx`. EN and NL agree with each other in
  each file, so this is an EN-source inconsistency rather than an EN/NL disagreement; not
  normalised, per the dual-source rule. One screen almost certainly has one speaker —
  worth a client confirmation.

## Non-flag decisions worth recording

- **Multifunction-button directions mirrored verbatim.** `controls.mdx` states
  right = *increase brightness*, left = *decrease volume* — an asymmetric pairing that EN
  and NL state identically for this product. Translated faithfully as
  `**Nach rechts drücken („Plus“):** die Hintergrundbeleuchtung (Helligkeit) erhöhen.` /
  `**Nach links drücken („Min“):** die Lautstärke verringern.` The known upstream
  contradiction with `infinity-lite` (which assigns the two directions the other way
  round) is a **pending client question** and was deliberately **not** reconciled here.
  Both bold run-ins are the §10.5 locked forms, and `Hintergrundbeleuchtung` is the §6.1
  ruling for lowercase `backlight` in a button description.

- **Anchor link translated with its heading.** `controls.mdx` carries the only
  in-page anchor in the whole corpus. EN `[On-Screen Menu](#on-screen-menu-osd)` →
  DE `[Bildschirmmenü](#bildschirmmenü-osd)`, derived from the translated heading
  `## Bildschirmmenü (OSD)` (§7.3). NL sets the precedent by translating both the link
  text and the anchor (`[OSD-instellingen](#osd-instellingen)`). The slug keeps the
  umlaut because the site's slugger preserves Unicode letters; **verify this one anchor
  resolves on the first DE build** — it is the only place in the DE tree where a slug
  contains a non-ASCII character.

- **`sticker` → `Aufkleber`** (EN "blue sticker" / "red sticker", NL "sticker"). Not in
  the glossary. Proposed addition:
  `| sticker | Aufkleber | Infinity port marking, `blauer`/`roter Aufkleber` | — |`
  Reason: `infinity/installation.mdx` §"Anschlussmöglichkeiten" and
  `infinity/controls.mdx` §"USB-C"; `Aufkleber` is the standard German noun, and the
  loan `Sticker` reads as merchandise rather than a factory port marking.

- **`single screen stand` → `Ständer für einen Bildschirm`** (§1.1, which explicitly
  forbids building `Einzelbildschirmständer`). The §7.7 image caption
  `Den Bildschirm auf den Ständer setzen` deliberately drops the qualifier, as locked.

- **Resolution normalised to the spaced form.** EN writes `1920×1080` (unspaced) in
  `index.mdx`; DE ships `1920 × 1080` per glossary §4 and the §11 precedent for
  normalising EN-source typographic inconsistencies. Same call as `de-expand`.

- **DIN 5008 unit spacing** applied: `72 % NTSC` (EN `72% NTSC`). Per §4/§11 this
  deliberately differs from the NL lock (`72% NTSC`) and must **not** be reported as an
  nl↔de parity defect. Angles (`178°`, `235°`, `90°`, `360°`) keep no space, as in both
  source languages.

- **Em dashes → en dashes** (§3.6): the two `### Dual screen — …` headings become
  `### Zwei Bildschirme – vorne und hinten, horizontal|vertikal` (§7.4), and the
  `index.mdx` product description uses `–`.

- **German quotes** (§3.6) replace the EN straight quotes in the `**„L“** / **„R“**`
  step and in `**Nach rechts drücken („Plus“):**` / `**Nach links drücken („Min“):**`.
  `Left`/`Right` are rendered lowercase (`für **links**` / `für **rechts**`) because they
  are directions in German, not label nouns; the device labels themselves stay `L` / `R`.

- **`15,6"` kept as an inch mark**, never expanded to `Zoll` (§4), and compounded as
  `15,6"-Bildschirmen` — matching the committed `de/manuals/dual-flip/index.mdx`
  (`16"-Bildschirmen`). No `&quot;` or `\"` escape is needed anywhere on these three
  pages: the only inch marks sit in markdown prose and a markdown table cell (§4.1).

- **No `*_link` frontmatter keys** on any of the three pages, matching the rest of the
  committed DE tree.
