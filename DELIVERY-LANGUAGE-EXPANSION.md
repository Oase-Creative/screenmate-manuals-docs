# Delivery Report — German, French & Italian Manuals

**Date:** 2026-08-11 · **Branch:** `lang-expansion-de-fr-it` · **Scope:** full expansion of the Screenmate manuals site from 2 languages (NL, EN) to 5 (NL, EN, DE, FR, IT)

> **Round 4 addendum — 12 August 2026.** After the original delivery we ran one further review round: six independent native-reader fluency reviews and three line-by-line safety alignment audits, followed by three review-gated fix waves. Sections **3**, **4**, **7** and **8** below have been extended to reflect it. Nothing shipped in §1 has changed, the register decisions in §2 are unchanged, and the recommendation in §5 stands exactly as written.

---

## 1. What shipped

- **186 new pages** — the complete manual set (11 products + site index, 62 pages) in German, French and Italian, at `/de/…`, `/fr/…`, `/it/…` mirroring the existing URL scheme.
- **Language switcher** now offers all 5 languages, each with its country flag, and **preserves the current page** when switching (e.g. the Italian Flip OSD page switches directly to the German Flip OSD page). 1,116 cross-language links generated and machine-verified.
- **Locked terminology glossaries** per language (`translations/glossary-de.md`, `-fr.md`, `-it.md`) — the same role the Dutch glossary plays today: registers, technical terms, device labels, number formats, section names. All future copy in these languages should be written against them.
- The QR-code redirects and all existing NL/EN content are untouched (one whitespace-only fix aside).

## 2. Language register choices (need your sign-off)

| Language | Register | Rationale |
|---|---|---|
| German | informal **du** | Mirrors the Dutch "je" brand voice; common for consumer-tech brands in DACH. |
| French | formal **vous** | Deliberate exception: French consumer manuals overwhelmingly use vous even for casual brands; tu would read as an error, not warmth. |
| Italian | informal **tu** | Mirrors the Dutch voice; standard for consumer tech in Italy. |

Related conventions applied deliberately (details in the glossaries): SI unit spacing in all three languages (`45 W`, `100 %`) where NL/EN close them up; German title style `Screenmate OneCable – Handbuch`; `reverse charging` stays English in German, is translated with a first-use English gloss in French (`charge inversée`) and Italian (`ricarica inversa`).

## 3. Verification performed

**Mechanical (machine-checked, all passing):**
1. Structural parity vs. English on every page: headings, steps, tables, components, images — 0 failures.
2. Numeric fidelity: every number in the English corpus verified present with correct locale formatting — 0 failures.
3. Safety-negation counts, register scans (no Sie/tu/Lei leakage), do-not-translate term survival (42 locked terms) — clean.
4. Shared-chapter byte-identity: safety and display-settings chapters are literally identical across the products that share them, per language — enforced by checksum.
5. Build check and link check pass at the pre-existing baseline (the checker's known false positives on URL-encoded image paths; all images verified rendering in the browser).
6. An automated checker (`scripts/verify_translation.py`) with a 20-test suite (`tests/test_verify_translation.py`) now guards all of the above for future edits.

**Semantic (independent AI review):**
7. **Blind back-translation:** 12 independent agents translated every one of the 186 pages back to English *without access to the originals*; 3 comparers then diffed against the source. Result: **zero critical and zero moderate meaning drift in all three languages** (12 cosmetic notes, fixed or logged).
8. **Adversarial review:** 12 further agents read English + Dutch + target side by side with instructions to find errors. ~130 findings were raised; 102 accepted findings were fixed in three review-verified fix waves — including three safety-relevant catches (a French modifier that weakened the 5 V power restriction, a dropped "properly" in the Italian grounding clause, French partial-negation phrasing). **Zero critical findings survived.**

**Semantic — round 4 (added 12 August 2026):**

9. **Native-reader fluency review:** 6 further independent reviewers — 2 per language — read every page in their own language *as a customer would*, with **no access to the English or Dutch source**, so that anything reading as translation-ese had nowhere to hide. Every one of the six returned the same verdict: **near-native, with flawless mechanics** — spelling, agreement, punctuation, and number/unit formatting all clean.
10. **Line-by-line safety alignment audit:** 3 auditors re-verified every line of the **5 distinct safety texts plus the shared OS-settings chapter** against the English, sentence by sentence, including a regression check on every safety correction made in earlier rounds. Result: **0 critical findings**, every earlier safety fix confirmed still in place, and two passages where the audit judged the translation *less* ambiguous than its English original (the scope of the "only use…" restriction) and deliberately left it that way.
11. **Review-gated fix waves:** the findings were then worked in three waves, each reviewed and approved before the next began. **112 accepted improvements across 101 files** — idiom and rhythm, terminology consistency, and **2 corrected glossary strings whose previous targets inverted the meaning of the source**. Every fix was verified against both the English and the Dutch before it was applied. The safety bodies were not touched in these waves and were re-verified afterwards.
12. **Source-side findings were quarantined, not absorbed.** Roughly **122 of the round-4 findings turned out to be faithful renderings of a defective source** — the same wrong, vague or self-contradictory statement is present in the English (and often the Dutch). "Fixing" those in German, French or Italian would have made the translated page disagree with the English on a point of fact, so none of them were applied. They were routed to the flags report instead — see §7.

**Visual:** all three languages rendered and navigated in a live build; switcher, flags, page-preservation, and images verified by screenshot.

## 4. What machine verification cannot prove

Stated plainly: the checks above prove the translations are **structurally complete and semantically faithful**, and since round 4 they also carry six independent native-reader verdicts that the copy **reads naturally** in German, French and Italian. That materially reduces the readability risk we flagged at delivery — it is no longer the open question it was on 11 August.

What no amount of further machine or AI review can establish is whether the safety wording meets each market's **regulatory and in-house expectations**, and whether a reader in that market would sign off on the tone of the highest-stakes paragraphs. That residual risk is what §5 and §6 remain for, and our recommendation there is unchanged.

## 5. The bounded ask for your review partner

This remains our recommendation after round 4. A native-speaker review does not need to cover 60,000 words. Because the safety chapters are shared across products, the entire high-stakes surface is:

- **5 distinct safety texts ≈ 1,000 words per language ≈ 3,000 words total**, plus the spec tables.
- Canonical files (fixing the first file of a group fixes all its copies — they are byte-identical):
  - `de|fr|it/manuals/onecable/safety.mdx` (shared by 7 products)
  - `de|fr|it/manuals/dual-flip/safety.mdx`, `…/infinity/safety.mdx`, `…/infinity-lite/safety.mdx`, `…/panorama/safety.mdx`
- Optional second tier: the OS-settings chapter (`onecable/display-settings.mdx`, shared by 4 products) and the per-product spec tables.

## 6. Compliance note (please confirm with your advisor)

Our reading of **EU Regulation 2023/988 (GPSR, in force since December 2024)** is that safety information must be provided in the language of each member state where the product is sold. If that reading is correct, the safety translations above carry legal weight in Germany, France, Italy (and other markets where these languages apply). This is our reading, not legal advice — please confirm with your compliance contact.

## 7. Findings for you — `translations/flags-consolidated.md`

The review process also audited your existing content. Round 4 added roughly 122 further source-side findings; most corroborated entries that were already there, and those rows now carry the extra evidence rather than being duplicated. The report is marked **Version 2** and now contains:

- **65 English-source issues** — confirmed independently by multiple languages; we recommend an EN/NL cleanup pass.
  - **Top item, and the one we would act on first: the safety chapter contradicts itself on input voltage.** Item 5 of every numbered safety page states that the monitor operates on a DC input **between 5 V and 20 V**; item 6 then restricts the customer to a **5 V** power source only — while the same manuals elsewhere tell them to use a 45 W USB-C charger, which is not 5 V. It was re-raised independently by **all six** round-4 native readers and is the only finding any of them rated Critical. It is present on all 8 safety pages and now published in five languages, and it needs an **engineering ruling**, not an editorial one. One decision fixes all five languages in a single pass.
  - Longer-standing examples: the same spec value labelled "Color Gamut" on one tab and "Color Accuracy" on another; "two signal sources" followed by a list of three; a port-check instruction that differs between the 14″ and 15.6″ tabs.
  - **New in round 4** (24 further English-source items, tagged **[R4]** in the report; §2 and §3 gained 5 more between them). Three worth naming: (a) `en/manuals/infinity-lite/display-settings.mdx:57` still says `'Mirrored'` where the rest of the corpus says `Flipped` — **we have escalated this one**, because "Mirrored" is not a Windows label in English (the real one is "Landscape (flipped)"), while its literal Italian rendering *does* match a real Windows control, the multi-display mode *Duplica questi schermi*, so an Italian customer with an upside-down screen is sent to a setting that does the wrong thing; (b) two products with no battery are told "the screen automatically charges"; (c) the 150 % scaling prompt exists as **three** different English strings against **one** uniform Dutch string, and one of the three ("Want more on-screen space?") promises the opposite of what the instruction printed beneath it delivers.
- **22 Dutch-side observations** (e.g. `nl` says the Infinity layout is "identiek" where EN and all three new languages say mirrored) — NL was frozen during this project; your call.
- **15 product-fact questions** only you can answer (e.g. the Infinity vs Infinity Lite control-direction contradiction; whether the Lite's button is silk-screened in English; and, new in round 4, what power hardware actually ships in the Flip / Dual Flip / Expand / OneCable boxes, the Panorama's real viewing angle, and what failure mode the Panorama "interference" note is describing).
- 11 minor internal items we deferred deliberately.

## 8. Numbers

~124 commits · ~405 files changed · ~39,000 lines added · 3 locked glossaries · **48 QA artifacts** under `translations/qa/` — the original 30 (back-translations, adversarial reviews, fix logs) plus 18 added by round 4 under `translations/qa/round4/`: 6 native-reader fluency reviews, 3 safety alignment audits, 3 diff reviews, 3 fix logs and the 3 source-flag files feeding §7. Full audit trail, per language.
