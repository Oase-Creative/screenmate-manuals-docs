# Design: Italian, German, French Language Expansion

**Date:** 2026-08-11
**Status:** Approved pending user review
**Scope:** Add `it/`, `de/`, `fr/` as full languages to the Screenmate manuals Mintlify site, currently `en/` + `nl/`.

## 1. Context

- 62 MDX pages per language (`manuals-index` + 11 product manuals), ~20,000 words per language.
- 11 product slugs: `onecable, lite, lite-144hz, dual-flip, flip, expand, infinity, infinity-lite, one-4k, one-4k-oled, panorama`. OneCable has 8 pages; others 5–6.
- `scripts/generate_language_links.py` already generalizes to N languages (auto-discovers lang dirs, writes `<lang>_link` frontmatter keys). No changes needed — just run it after files exist.
- Site deploys from `main` on push → **all work happens on a feature branch; merge only after full verification passes.**

## 2. Decisions (locked)

| Decision | Value |
|---|---|
| Registers | DE informal **du** · FR formal **vous** · IT informal **tu** |
| Copy production | Claude drafts; self-verification suite; delivery doc hands the residual (native idiomaticity + regulatory fit) to the client's review partner |
| Source strategy | **Dual-source** (see §3) |
| Language order in switcher | nl, en, de, fr, it |
| OS screenshots | Reused as-is (English UI) on all language pages — established client decision (`c9e6d1f`) |
| OSD caps labels | `LANGUAGE`, `OSD TIMER`, `TRANSPARENCY`, etc. are printed on the physical device in English → **never translated**; surrounding prose is |

## 3. Dual-source translation

Relay-translation risk: DE/FR/IT from EN alone compounds drift, because EN was itself derived from the Dutch booklets. NL alone is wrong too — EN has absorbed client feedback rounds and was sometimes the corrected side.

Every translator agent receives **both** the EN and NL file for its page:

- **EN** = structural template: headings, components, step counts; also the diff anchor for back-translation.
- **NL** = semantic tiebreaker, register model (`je` → *du*/*tu*), number-format model (comma decimals, no thousands separator: `1820 gram`, `15,6"`).
- **Disagreement rule:** if EN and NL differ in *meaning* (not phrasing), the agent must **stop and flag**, never silently pick one. Flags are collected and reviewed; this doubles as a free QA sweep of the existing corpus.

## 4. Dedupe rules (translate once, propagate byte-identically)

Verified by body checksum (frontmatter stripped), 2026-08-11:

- **safety.mdx** — 5 distinct bodies, not 11:
  - Group A (227 w): onecable, lite, lite-144hz, flip, expand, one-4k, one-4k-oled
  - dual-flip · infinity (162 w) · infinity-lite · panorama
- **display-settings.mdx** — 3 distinct bodies across 6 products:
  - Shared body: onecable, dual-flip, flip, expand (the frozen shared chapter, `893478a`)
  - infinity · infinity-lite
- Each distinct body is translated **once** per language and propagated byte-identically, so the checksum-identical invariant holds in the new languages from day one.
- Pre-existing anomaly found during design: `nl/manuals/onecable/display-settings.mdx` has one trailing blank line vs. the other three NL copies — whitespace only, semantically identical. Normalize as a trivial cleanup commit.

## 5. Do-not-translate invariants

1. Product names (`Screenmate OneCable`, `One 4K OLED`, …) and model numbers.
2. OSD menu caps labels (physical device strings).
3. Retained-English glossary terms: `Drivers`, `Power Delivery`, `Backlight`, `FAQ`, etc. — each language glossary carries a keep-EN column mirroring the NL glossary's.
4. Image/video `src` paths — byte-identical across languages (alt text is translated).
5. Frontmatter `icon` values.

## 6. Verification model

### Mechanical (proofs) — `scripts/verify_translation.py`, exit 1 on failure

1. **Structural parity** vs. EN counterpart: heading count/level/order, numbered-step count, table row count, MDX component tag sequence (`<Note>`, `<Warning>`, `<Tabs>`…), `src` equality, `icon` equality.
2. **Numeric invariants:** all ~3,077 EN numeric tokens present in each target with locale transform applied (`15.6` → `15,6`); multiset comparison with a transform allow-list.
3. **Negation polarity** (safety files, 42 EN markers): count DE `nicht/kein/niemals`, FR `ne…pas/jamais/aucun`, IT `non/mai/nessun` against EN counts; mismatches become flags.
4. **Register check** (flag list, human-reviewed): DE no `Sie/Ihnen/Ihr` (case-sensitive; `Sie`-vs-`sie` ambiguity means this flags rather than hard-fails), FR no `\btu\b|\btoi\b|\bton\b`, IT no `\bLei\b|\bSuo\b`.
5. **DNT invariants** (§5) present verbatim.
6. **Mintlify build** passes; no broken links in any of the 5 languages.

### Semantic (evidence)

7. **Blind back-translation:** fresh Opus agents with *no* access to source EN translate each target page back to English; diff vs. source EN; divergences reviewed by orchestrator.
8. **Adversarial review:** separate Opus agents (not the translators), given EN + NL + target side by side, instructed to find errors, not confirm quality.

### Explicitly NOT proven (goes in the delivery doc)

- Native idiomaticity — that the copy reads naturally to a native speaker.
- Regulatory fit — EU GPSR (Reg. 2023/988, in force Dec 2024) requires safety information in the language of the member state of sale; client's compliance person must confirm the safety translations satisfy this. The bounded professional-review ask: **5 distinct safety bodies ≈ 1,000 words × 3 languages ≈ 3,000 words**, plus spec tables.

## 7. Pipeline & delegation

Fable (main session) orchestrates and QC-gates; Opus agents do translation/review work; Sonnet agents do mechanical work. No Fable subagents. All on branch `lang-expansion-de-fr-it`.

| Phase | Who | Work | Gate |
|---|---|---|---|
| 0. Plumbing | Sonnet | Scaffold `it/ de/ fr/` dirs; 3 `docs.json` language blocks (12 tabs each, products `hidden: true`; index tab labels *Handbücher / Manuels / Manuali*); 3 flags in `style.css` following its documented fail-safe pattern; no new redirects (no QR codes exist for new languages yet) | Orchestrator reviews diff; build still passes for nl/en |
| 1. Glossaries | Opus ×3 | Derive locked DE/FR/IT glossaries mirroring NL glossary structure (incl. keep-EN column, OSD labels, compound-hyphenation rules per language) | Orchestrator reviews each before any translation |
| 2. Translation | Opus, per product × language (33 tasks + 3 index pages, batched) | Dual-source, glossary-locked; dedupe rules §4 applied (distinct bodies translated once) | Disagreement flags collected & resolved |
| 3. Verification | Sonnet (script) + Opus (back-translation, adversarial) | Checks 1–8; fix loop until mechanical checks pass clean and semantic flags are dispositioned | Orchestrator reviews all outputs |
| 4. Delivery | Fable | `generate_language_links.py` run; delivery doc (§8); final QC; merge to `main` and push after user sign-off | User approves merge |

## 8. Delivery doc

`DELIVERY-LANGUAGE-EXPANSION.md` (repo root, English, client-facing). Contents:

1. What shipped: 186 new pages across 3 languages, URL scheme, switcher behavior.
2. Register choices per language and why (FR *vous* rationale explicit).
3. Verification performed: the 8 checks, with result counts.
4. What machine verification cannot prove, stated plainly.
5. The bounded review ask for their review partner: the 5 safety bodies + spec tables (~3,000 words), with file paths.
6. GPSR note for their compliance check — flagged as our reading, to be confirmed by them, not legal advice.

## 9. Out of scope

- New QR codes / redirects for the new languages (client-driven, later).
- Translating `sources/` PDFs or producing print booklets.
- Any change to existing EN/NL copy beyond the whitespace fix (§4) and whatever the disagreement-flag review explicitly approves.
