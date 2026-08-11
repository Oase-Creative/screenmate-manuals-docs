# FR Panorama flags

Task 7-fr / slug `panorama`. Pages: index, installation, controls, osd
(`safety.mdx` belongs to Task 6; this product has no `display-settings.mdx`).

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 6. Blocked: 0.

## VERBATIM-SENSITIVE ZONE — client-dictated copy

- [installation.mdx] The `<Info>` block under `### Option 1 — USB-C (câble unique)` is
  **client-dictated copy**, authored in Dutch and mirrored into EN. EN says "Use the long
  white cable for power, and the short black cable to connect the Panorama to your
  laptop." / NL says "Gebruik de lange witte kabel voor stroom, en de korte zwarte kabel
  om de Panorama met je laptop te verbinden." — **EN and NL agree exactly**; no divergence
  to resolve. Translated with extra literalness, preserving all four load-bearing
  attributes and their pairings — `long + blanc → alimentation`, `court + noir →
  connexion à l'ordinateur portable` — and the source's comma before `et`:

  > `Utilisez le long câble blanc pour l'alimentation, et le court câble noir pour
  > connecter le Panorama à votre ordinateur portable.`

  **Do not paraphrase, reorder, or "improve" this sentence in any later pass.** The two
  cables are physically distinguishable only by length and colour, and Option 2 step 3
  ("le port HDMI situé à côté du câble d'alimentation blanc") depends on the white cable
  still being identified as the power cable here. Any client revision to the Dutch must be
  re-mirrored into FR verbatim rather than re-translated from EN.

## EN/NL divergences

- [installation.mdx] EN says the laptop USB-C port "does not supply enough power on its
  own to run the Panorama **at full brightness**" and closes "Always connect the 65 W
  adapter for stable operation." / NL distributes it differently: "levert niet genoeg
  stroom om de Screenmate Panorama **optimaal te laten functioneren**", with the
  brightness claim moved to the second sentence ("voor een stabiele werking **en maximale
  helderheid**"); NL also adds "meegeleverde" (= supplied) — proceeded-with the EN
  distribution (`… à sa luminosité maximale. Branchez toujours l'adaptateur 65 W pour un
  fonctionnement stable.`). Same total claim; EN is the structural template.

- [installation.mdx] EN says "Connecting a separate charger to your laptop **while the
  Panorama is also providing power** may cause interference." / NL drops the concessive
  clause: "Als je daarnaast nog een extra oplader aansluit, kan dit storingen
  veroorzaken." — proceeded-with the fuller EN version (`… alors que le Panorama
  l'alimente également …`). The clause names the actual failure condition, so dropping it
  loses information.

- [installation.mdx] EN says "your laptop" throughout the connection steps (Option 1
  step 2; Option 2 steps 2 and 3) / NL says "je pc of laptop" (PC *or* laptop) —
  proceeded-with EN (`votre ordinateur portable`). The driver section above already says
  "PC ou … ordinateur portable" in both trees, so the narrower wording in the steps is
  EN's deliberate scope, not an omission.

- [controls.mdx] EN says "Connect the supplied 65 W power adapter here using the USB-C to
  USB-C cable" (the adapter is the object) / NL inverts it: "Sluit hier de USB-C-kabel aan
  op de meegeleverde 65 W-voedingsadapter" (the cable is the object) — proceeded-with the
  EN direction (`Branchez ici l'adaptateur secteur 65 W fourni à l'aide du câble USB-C
  vers USB-C.`). Identical physical action; EN's phrasing keeps the section heading
  (`Port de charge USB-C`) as the thing being described.

- [osd.mdx] EN says "Follow the steps below to **configure each display**." / NL says
  "Volg de stappen hieronder om **alles eenvoudig** in te stellen" (= to set *everything*
  up easily — drops "each display", adds "easily") — proceeded-with EN (`Suivez les étapes
  ci-dessous pour configurer chacun d'eux.`). Per-screen configuration is the point of the
  whole chapter, so EN carries the meaning.

- [osd.mdx] EN says the Windows display-orientation option is `**"Flipped"**` / NL says
  `**"Gespiegeld"**` (= *Mirrored*) — two different Windows options, not two phrasings —
  proceeded-with `**«&nbsp;Paysage (inversé)&nbsp;»**` per glossary §8, which maps **both**
  `Flipped` and `Mirrored` to `Paysage (inversé)` and marks `Mirrored` as "superseded on EN
  pages by Flipped". Same ruling `fr-shared.md` already recorded for the display-settings
  chapter.

## Non-flag decisions worth recording

- **EN's mixed bullet voice in `controls.mdx` is normalised to the infinitive — French
  grammar forces this.** Under `### Bouton Bas (−)` / `### Bouton Haut (+)`, EN and NL both
  shift from infinitive/telegraphic ("Navigate within the menu." / "Navigeren in het menu.")
  to a subjectless finite verb on the third bullet ("Opens the brightness shortcut menu." /
  "Activeert het helderheidsmenu."). English, Dutch and German tolerate a subjectless finite
  verb in this register; **French does not** — a subjectless finite verb in French *is* the
  imperative, so `Ouvre le menu …` reads as tutoiement and trips the glossary §1 register
  grep as a genuine defect, not a false positive. Rendered as `Ouvrir le menu de raccourci
  de la luminosité.` / `… du volume.`, parallel to the two bullets above it. **This is a
  deliberate FR-only divergence from `de-panorama.md`, which mirrors the EN voice shift.**
- **R9 OSD alt shape `Menu OSD {Section}` does not apply to this slug.** `panorama/osd.mdx`
  ships no OSD-screenshot images — its three images are Windows/macOS OS screenshots. Alts
  translated fully as ordinary descriptive prose per R9 (`Paramètres d'affichage
  Windows&nbsp;: organiser les écrans et régler l'échelle`, `Image 1&nbsp;: réglages
  Moniteurs de macOS avec le bouton Disposition`, …).
- **R8 descriptive control names translated naturally**: `Down Button (−)` →
  `Bouton Bas (−)`, `Up Button (+)` → `Bouton Haut (+)`, `Confirm / Exit Button` →
  `Bouton Confirmer / Quitter`, `Power Button` → `Bouton d'alimentation` (all locked in
  glossary §9.4). NL's `Power-knop` / `Exit-knop` keep-EN pattern is **not** carried into
  French.
- **Windows/macOS UI labels are French-only in `osd.mdx`, no English parenthetical.** The
  glossary §8 first-mention gloss instruction is scoped to the display-settings chapter
  (Task 6); NL ships Dutch-only labels here (`Beeldscherminstellingen`, `Identificeren`,
  `Beeldschermstand`, `Schaal`), so FR ships French-only (`Paramètres d'affichage`,
  `Identifier`, `Orientation de l'affichage`, `Échelle`). **Same asset caveat as
  `fr-shared.md`:** the referenced screenshots are not French, so the labels will not match
  the images. Asset decision, not a translation change.
- **`reverse charging` glossed once on first use** per glossary §5.2 —
  `grâce à la charge inversée (reverse charging)` in `installation.mdx`. EN attaches the
  term as a bare parenthetical to "over USB-C"; French needs the term in the prose for the
  gloss to attach to, so `grâce à` was added. It appears exactly once in this slug, so
  there is no second occurrence to strip the gloss from.
- **French unit spacing** applied per glossary §4: `300&nbsp;cd/m²`, `10&nbsp;ms`,
  `60&nbsp;Hz`, `65&nbsp;W`, `100&nbsp;%&nbsp;sRGB`, `150&nbsp;%`, `42 × 36 × 2,8&nbsp;cm`.
  Deliberately unlike EN (`300 cd/m²`, `100% sRGB`, `150%`) and unlike the NL lock — **not**
  an en↔fr or nl↔fr parity defect.
- **`1920×1080` normalised to `1920 × 1080`** (glossary §4, resolutions take a spaced `×`);
  EN and NL both ship it unspaced in this file. Same precedent as `fr-expand.md`. The
  `(×3)` multiplier in the `Taille` row keeps EN's tight form — it is a count, not a
  resolution.
- **Frontmatter and body inch mark: `15,6`** with a comma in all three contexts
  (`description: "… Panorama 15,6\""`, the `<Note>` welcome line, the prose in
  `## Qu'est-ce que le Screenmate Panorama&nbsp;?`). NL leaves its frontmatter at `15.6\"`;
  FR applies §4 consistently. No `&quot;` context exists in this slug (no `<Tab>` elements).
- **Cable lengths abbreviated, not spelled out.** EN `(1.2 m)` / NL `(1,2 meter)` — FR keeps
  EN's abbreviation with a French decimal comma: `(1,2 m)`, `(0,5 m)`. Formatting only.
- **`65 Watt USB-C power adapter` → `Adaptateur secteur USB-C 65&nbsp;W`** per glossary §5.7,
  which collapses EN's spelled-out "Watt" (index.mdx) and its `65 W` symbol form (elsewhere
  in the slug) onto the single symbol form. EN's internal inconsistency is deliberately not
  preserved here because §5.7 locks the package-contents line verbatim.
- **`DP monitor` → `moniteur DP`** (`osd.mdx`, "Volume control is only available on the left
  screen"). `DP` is not in `dnt.json`; glossary §12 open item 1 records this as still open
  for the client. Rendered per §5.2.
- **`desktop layout` → `disposition du Bureau`** with capital `B` per glossary §5.3, even
  though the sentence covers both Windows and macOS. Matches the FR corpus house style
  established in `fr/manuals/*/display-settings.mdx`.
- **`**Extend your workspace:**` → `**Étendre votre espace de travail&nbsp;:**`** per
  glossary §10.2, which names `panorama/osd` as its single occurrence. Not to be confused
  with the display-settings chapter's question form
  (`**Vous souhaitez étendre votre espace de travail&nbsp;?**`).
- **Em dashes kept as `—` (U+2014)** with a plain space each side in
  `### Option 1 — USB-C (câble unique)` / `### Option 2 — USB-A + HDMI`, per glossary §3.5
  and matching the EN source. FR does **not** follow the DE en-dash conversion.
- **`icon` and `src` byte-identical to EN** on all four pages (verified by diff); no
  `nl_link` / `en_link` keys written.
