# FR — One 4K OLED: EN↔NL discrepancies

Task 7-fr / slug `one-4k-oled`. Pages: index, installation, controls, osd
(`safety.mdx` owned by Task 6). Format:
`- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 4. **Blocked: 0** — every entry is resolved by a binding glossary ruling or a
coordinator ruling. Phrasing-only differences are listed separately at the bottom.

## EN ↔ NL divergences

- [fr/manuals/one-4k-oled/installation.mdx, first `##`] EN says `## Getting Started` /
  NL says `## Aansluiten` (= *Connecting*) — proceeded-with `## Pour commencer`.
  Glossary §9.3 locks `Getting Started` → `Pour commencer`. EN is the structural template and
  the section body is a generic seven-bullet orientation list, not connection steps, so the EN
  label is the accurate one; the NL page renamed the section after its content. Only `one-4k` and
  `one-4k-oled` carry this heading, so the two slugs must agree — **verified byte-identical against
  the shipped `fr/manuals/one-4k/installation.mdx` (commit `de7b74a`)**. Client may wish to
  normalise the NL heading.

- [fr/manuals/one-4k-oled/installation.mdx, §1 callout] EN says `**Important:**` /
  NL says `**Let op:**` (= *Note:*) — proceeded-with `**Important&nbsp;:**`.
  Glossary §6 and §10.1.I keep `Important:` → `Important&nbsp;:` distinct from
  `Note:` → `Remarque&nbsp;:`. NL collapses the two lead-ins; French keeps them apart. Same call
  as the shipped `lite` and `one-4k` slugs.

- [fr/manuals/one-4k-oled/controls.mdx §Port USB-A; fr/manuals/one-4k-oled/osd.mdx after
  §Raccourcis] EN says `{/* TODO: confirm with Louie — … */}` in English / NL says the same two
  comments with their bodies translated into Dutch (`gebruik van USB-A-poort …`,
  `volledige OSD-menustructuur …`) — proceeded-with the **EN comment verbatim** in both files.
  Per the coordinator brief for this task, and consistent with glossary §10.1.H, which rules the
  analogous `{/* … */}` scaffold in `manuals-index.mdx` "not user-visible — leave in English".
  These are internal questions addressed to the client, not user copy; translating them into three
  new languages would make the open items harder to reconcile. Both comments are byte-identical to
  the EN source (verified programmatically). **Note the content is itself an open client question:**
  the USB-A port's function and the full OSD menu tree are still unconfirmed, so — exactly as on the
  EN and NL pages — `### Port USB-A` ships with no body copy.

- [fr/manuals/one-4k-oled/controls.mdx §Bouton Menu] EN says `### Menu Button (Power / OSD)` /
  NL says `### Menu-knop (Power / OSD)`, retaining the English word `Power` inside the
  parenthetical — proceeded-with `### Bouton Menu (alimentation / OSD)`.
  Glossary §9.4 locks this exact heading. `Power` is not an OSD caps label and is not in
  `translations/dnt.json`, so it is not DNT; §5.1 gives `power button` → `bouton d'alimentation`.
  `OSD` stays verbatim as a DNT token. **Cross-language note for the reviewer:** this is a
  deliberate three-way split — DE kept `Power` (treating it as an on-device literal), IT translated
  it (`accensione`), FR follows its own glossary and translates it. Worth a client eyeball if the
  physical unit is silk-screened "Power"; if so, all three glossaries should change together.

## Locked figures verified on this slug

- **Contrast ratio `100 000:1`** — glossary §4.1 / gate ruling R5, French space-separated
  thousands with a **plain** space between digit groups and the colon left tight (§3.4).
  Applied in **both** required places: the `## Qu'est-ce que le Screenmate One 4K OLED&nbsp;?`
  prose sentence and the `**Taux de contraste**` spec row. EN writes `100,000:1`, NL writes
  `100.000:1`; they agree in value. Verified `grep -nE '100[,.]000'` returns zero hits and
  `100 000:1` occurs exactly twice.
- **`### 3.5mm Headphone Jack`** (EN's unspaced variant) → `### Prise casque 3,5&nbsp;mm`
  per §9.4 — comma decimal, `&nbsp;` between number and unit symbol.
- **Four-digit figures keep no separator:** `3840 × 2160`. The contrast figure is the only one
  in this slug that crosses four digits.
- **French unit spacing applied against EN/NL closed forms:** `400&nbsp;cd/m²`, `1&nbsp;ms`,
  `60&nbsp;Hz`, `100&nbsp;%&nbsp;sRGB` (EN/NL `100% sRGB`). Angle `178°` keeps no space (§4).

## Coordinator ruling R9 — alt text (applied)

`alt` translates **fully** into French. All **7** alts on this slug (1 index, 5 installation,
1 controls) are fully French; `osd.mdx` has no images, so the FR OSD alt shape
`Menu OSD {Section}` had no site to apply on this slug. Remaining non-French tokens in alts are
DNT only: `Screenmate`, `One 4K OLED`, `USB-C`, `USB-A`, `HDMI`. Every `src` is byte-identical to
EN (verified programmatically), including the Dutch-derived `…%20Handleiding%20images/…` paths.

## Coordinator ruling R8 — descriptive names (applied)

- `### Indicator Light` → `### Voyant lumineux` (§9.4), body `Voyant d'état …` (§5.1
  `status LED` → `voyant d'état`) — not a calque of NL `Indicatielampje`.
- `### + and − Buttons` → `### Boutons + et −`; run-ins `**Bouton +&nbsp;:**` / `**Bouton −&nbsp;:**`
  (§10.2). The `−` is U+2212 throughout, copied from the EN source (§7 physical engravings),
  never a hyphen.
- `### OSD Lock` → `### Verrouillage de l'OSD` (§9.4). NL's `OSD vergrendeld` is stative
  ("OSD locked"); the FR form follows the EN nominal heading.

## Not flagged — checked and dismissed (recorded so a later pass does not re-open them)

- `index.mdx`: EN `| **Screen Size** | 15.6" |` / NL `| **Schermgrootte** | 15,6 inch |`
  (unit spelled out) — number-format only; FR uses the prime form `15,6"` per §3.5, matching the
  shipped `one-4k` page.
- `index.mdx`: EN `Special Features | Built-in stand` / NL `Met ingebouwde standaard`
  (= *With a built-in stand*) — phrasing only → `Caractéristiques particulières | Support intégré`
  (§5.6 + §5.1), byte-identical to the shipped `fr/manuals/one-4k/index.mdx` row.
- `controls.mdx`: EN link text `[On-Screen Menu]` / NL `[Beeldscherminstellingen (OSD)]`
  (NL substituted the target page's own frontmatter title) — phrasing only; EN template followed →
  `[Menu à l'écran]`, `href` retargeted to `/fr/manuals/one-4k-oled/osd`.
- `installation.mdx §5`: EN "To connect **the Screenmate** to an HDMI device …" /
  NL "Om **de draagbare monitor** aan te sluiten …" (= *the portable monitor*) — coreferential,
  phrasing only. Identical to the already-dismissed `lite` and `one-4k` cases.
- `installation.mdx`: NL converts several EN declaratives into rhetorical questions
  (`Werkt het niet direct?`, `Ondersteunt je apparaat opladen via USB-C?`) — a Dutch register
  device, no meaning change. FR follows the EN declarative form, matching the approved
  `fr/manuals/lite/installation.mdx` and `fr/manuals/one-4k/installation.mdx`.
- `osd.mdx`: NL renders "power button" as `aan/uit-knop` — same referent as EN `power button`;
  FR uses the §5.1 lock `bouton d'alimentation`.

## Corpus-consistency notes for the orchestrator (not EN↔NL flags)

1. **Cross-slug parity with `one-4k` enforced.** EN `one-4k` and `one-4k-oled` share large
   stretches of byte-identical prose. After the shipped `fr/manuals/one-4k` landed
   (commit `de7b74a`), this page was diffed against it line by line and **every** FR line whose EN
   counterpart is identical between the two slugs was aligned to the shipped wording
   (`passe automatiquement`, `associé au câble HDMI pour transporter le signal vidéo`,
   `prenant en charge le DisplayPort Alt Mode`, `Voyant d'état indiquant l'alimentation et l'état
   du signal.`, `dans l'OSD`, `de la luminosité` / `du volume`, `lorsque l'alimentation est
   raccordée`, `valider un réglage`, `pour l'enregistrer`, and the OSD-lock sentence, plus the
   index closing sentence). Verified: every remaining difference between the two FR pages
   corresponds to a real EN difference. **If either slug is re-edited, change both.**

2. **`cm` spacing is inconsistent across the shipped FR corpus.** `expand/index.mdx` writes
   `2,5&nbsp;cm` while `dual-flip`, `flip`, `lite`, `lite-144hz`, `onecable` and `one-4k` all write
   a plain space (`3,5 cm`). This page follows the majority form and its direct sibling `one-4k`
   (`34,8 × 22,4 × 1,3 cm`). The glossary is itself ambiguous here — §4's decimal-separator row
   shows `40,6 × 23,7 × 2,5 cm` with plain spaces, while §9.4 locks `3,5&nbsp;mm` for the
   standalone headphone-jack term (which this page applies). **Not a defect introduced here**, but
   a one-line glossary clarification would stop it recurring; the cheap fix is to normalise
   `expand` to the majority form.
