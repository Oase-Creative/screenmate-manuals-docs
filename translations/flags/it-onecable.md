# IT — onecable: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it (onecable: index, installation, installation-windows, installation-mac,
controls, troubleshooting). `safety.mdx` and `display-settings.mdx` belong to Task 6 — see
`it-shared.md`.

## Meaning discrepancies

**None.** Every one of the six pages was diffed passage-by-passage against its NL sibling; EN and
NL agree on meaning throughout. The differences that exist are phrasing, glossing or structure —
recorded below so the reviewer does not have to re-derive them.

## Translator decisions on EN-side anomalies (no EN↔NL conflict)

- [it/manuals/onecable/index.mdx, §Specifiche tecniche] EN writes the folded dimensions with a
  lowercase `x` (`39 x 24 x 2.5 cm`, `34.5 x 22 x 2.5 cm`); NL mirrors it (`39 x 24 x 2,5 cm`) —
  proceeded-with-`39 × 24 × 2,5 cm` / `34,5 × 22 × 2,5 cm` (multiplication sign).
  Glossary §4.1 locks Dimensions as "`×` with spaces, comma decimals". OneCable is the **only**
  one of the 12 EN index pages still on `x`; the other 11 already use `×`. EN-side typo —
  recommend the client normalise `en/manuals/onecable/index.mdx`.
- [it/manuals/onecable/index.mdx, §Informazioni importanti] EN writes the rotation ranges with a
  hyphen (`0° - 360°`); NL mirrors it — proceeded-with-`0° – 360°` / `0° – 330°` (en dash).
  Glossary §4.1 "Angle range: en-dash **with** spaces" and lists `0° – 360°` as its worked example.
  This line is the corpus's only angle range, so the gate ruled on exactly this string.
- [it/manuals/onecable/installation-mac.mdx, §Fasi di installazione + §Se il driver non funziona]
  EN gives the macOS menu path bare (`**'System Settings'** > **'Privacy & Security'** > …`) with
  no gloss; NL glosses each label in Dutch (`('Systeeminstellingen')` …) — proceeded-with-**the NL
  parenthetical pattern in Italian** (`**'System Settings'** ('Impostazioni di Sistema')` …).
  Rationale: glossary §8 locks `Privacy e sicurezza` and `Registrazione schermo e audio di sistema`,
  and this page is the **only** place in the whole EN corpus where those two labels occur — the
  glossary rows exist for this page or for nothing. The macOS screenshots here are English
  (`mac-english-*.png`), so the EN label must stay primary and the Italian rides in the
  parenthetical. Structural counts (headings, steps, components, `src`) are unaffected.
  Same treatment applied to the three `alt` strings on this page.
- [it/manuals/onecable/installation-windows.mdx, §Installazione manuale] EN carries a **Dutch**
  gloss inline (`**This PC** ('Deze pc')`) because the Windows screenshots for this product are
  Dutch-language (known client flag) — proceeded-with-`**This PC** ('Questo PC')` per glossary §8's
  "NL parenthetical pattern" note ("Never leave a Dutch string on an Italian page"). The Dutch
  screenshots themselves are untouched and remain a client item.

## Non-flags — checked and dismissed (recorded for the reviewer)

- `## Package Contents` (EN) vs `## Onderdelen overzicht` (NL, "components overview"); `Size` vs
  `Grootte`; `Color Accuracy` vs `Kleurechtheid` — spec-label phrasing, same referents. EN followed
  via glossary §9.3 / §5.4.
- [troubleshooting] EN `Connection method: Connect your laptop's…` is one paragraph; NL splits
  `Aansluitmethode:` onto its own line. Structure only — EN followed (paragraph counts match EN).
- [troubleshooting] EN `Go to your Mac's launchpad` vs NL `het opstartplatform van je Mac` — NL
  translates the product name; IT keeps `Launchpad` per glossary §8.
- [installation] EN `a power adapter of at least 45W` / `a suitable power adapter` vs NL's
  `netstroom-adapter` / `netstroom-oplader` (mains-specific) — NL is more specific, but not in
  conflict. EN followed: `un alimentatore da almeno 45 W` / `un alimentatore adatto` (§2.4).
- [installation] EN `to a power outlet` vs NL `op het netstroom` (the mains) — same instruction.
- [installation-windows] EN `it is recommended to restart your laptop` (impersonal) vs NL
  `wordt aangeraden` (impersonal) — rendered `ti consigliamo di riavviare il laptop`, because the
  Italian register rule (§1.1) bans the impersonal-infinitive instruction style.
- [installation] EN `as shown in Figure 2` vs NL `Afbeelding 2` — same referent; glossary §5.5
  locks `come mostrato nell'immagine 2`.
