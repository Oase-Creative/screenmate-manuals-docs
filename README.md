# Screenmate Product Manuals Documentation

**QR Code-First Digital Manual System for Screenmate Hardware Products**

This documentation site serves digital manuals for Screenmate products, designed to be accessed via QR codes printed on product packaging. Users scan the QR code and land directly on their product's manual in their preferred language—no extra tabs, no distractions, just the manual they need.

---

## 🎯 Design Philosophy

### Core Principles
1. **QR Code-First**: Users scan a product QR code → land directly on the manual (language-specific)
2. **Zero Distraction**: No "Information" tabs, no unnecessary navigation—just the manual
3. **Multi-Product Scalability**: Easy to add new products as the company grows
4. **Intuitive for Hardware Users**: Simple sidebar navigation, clear sections
5. **Professional & Clean**: Impress clients with focused, well-organized documentation

### User Journey
```
Customer buys product → Scans QR code → Lands on manual (correct language) → Follows setup steps
```

---

## 📁 Project Structure

```
screenmate-manuals-docs/
├── docs.json                    # Main Mintlify configuration
├── images/                      # All images (logos, product photos, screenshots)
│   ├── screenmate-light-mode.png
│   ├── screenmate-dark-mode.png
│   ├── favicon.png
│   └── [Product] - [Manual Name] images/
├── style.css                    # Custom CSS (language-switcher flags)
├── en/
│   ├── manuals-index.mdx
│   └── manuals/
│       └── [product-name]/
│           ├── index.mdx        # Always: intro, render, in-the-box, specs
│           ├── installation.mdx # Always: setup, drivers, connections
│           ├── controls.mdx     # Always
│           ├── safety.mdx       # Always
│           ├── display-settings.mdx  # Conditional
│           ├── osd.mdx               # Conditional
│           └── troubleshooting.mdx   # Conditional
├── nl/
│   ├── manuals-index.mdx
│   └── manuals/
│       └── [product-name]/
│           ├── index.mdx        # Dutch version
│           ├── installation.mdx
│           └── ...
└── README.md
```

> **Note:** Paths are **language-first** (`en/manuals/...`, `nl/manuals/...`). This is required for
> Mintlify's language switcher to preserve the current page when toggling EN ↔ NL. Legacy
> `/manuals/en/...` URLs (printed on QR codes) are permanently redirected in `docs.json`.

---

## 🚀 Adding a New Product Manual

> **The authoritative procedure is the `screenmate-manual` skill**, which generates both
> languages from the product's v2 Dutch booklet PDF in `sources/`; follow it with
> `screenmate-dutch-fidelity` for the NL pass. What follows is a summary so this README
> doesn't contradict the skill — not a second procedure to run by hand.

### 1. Folders

Paths are **language-first**:

```bash
mkdir -p en/manuals/[product-slug] nl/manuals/[product-slug]
mkdir -p "images/Screenmate - [Product] - Handleiding images"
```

### 2. Pages — a conditional set, not a fixed eight

Always present:

| Page | Contents |
| :--- | :--- |
| `index.mdx` | Intro, overview render, in-the-box, specifications |
| `installation.mdx` | Physical setup, **driver installation**, connection options |
| `controls.mdx` | Physical buttons and indicators |
| `safety.mdx` | Safety warnings and care |

Add only what the product actually has:

| Page | Add when |
| :--- | :--- |
| `display-settings.mdx` | The product needs OS-level setup (screen arrangement, scaling, sound) |
| `osd.mdx` | The product has an on-screen display menu |
| `troubleshooting.mdx` | There is product-specific troubleshooting (currently OneCable only) |

There is **no `drivers.mdx` and no `downloads.mdx`.** Driver steps live inside
`installation.mdx` — see `en/manuals/panorama/installation.mdx` for the pattern. Where a
driver walkthrough is long enough to need its own pages, split it into
`installation-windows.mdx` / `installation-mac.mdx` and nest them in a group under
`installation` (see OneCable) rather than inventing a new page name.

EN and NL must stay in **exact structural parity**: same file set, same order, both languages.

### 3. Register in `docs.json`

Navigation is **tab-based — one tab per product, always `hidden: true`**. Hidden keeps the
product tab bar out of the UI, so a scanned QR code drops the customer straight into their
manual with nothing else competing for attention. Add the same block to **both** the `nl`
and the `en` language entry:

```json
{
  "tab": "Panorama",
  "hidden": true,
  "pages": [
    "nl/manuals/panorama/index",
    "nl/manuals/panorama/installation",
    "nl/manuals/panorama/controls",
    "nl/manuals/panorama/osd",
    "nl/manuals/panorama/safety"
  ]
}
```

Then add a **text-only card** — `title` and `href`, nothing else — to both
`en/manuals-index.mdx` and `nl/manuals-index.mdx`:

```mdx
<Card
  title="Panorama Manual"
  href="/en/manuals/panorama/index"
/>
```

Product renders belong on the product's own `index.mdx`, not on the listing cards.

**Do not touch the `redirects` array** — those entries back QR codes already printed and in
customers' hands. **Do not touch `style.css`** — it exists only to restore the
language-switcher flags and is keyed to Mintlify's own DOM hooks.

### 4. Generate the cross-language links

```bash
python scripts/generate_language_links.py
```

Nothing links EN ↔ NL until this runs — see [Cross-Language Links](#-cross-language-links) below.

---

## 🌐 Cross-Language Links

Every product tab in `docs.json` is `hidden: true`. Hidden tabs give Mintlify's language
switcher nothing to match on, so it cannot work out which Dutch page corresponds to the
English one you're reading. Each page must therefore name its counterpart explicitly in
frontmatter — an EN page carries `nl_link`, an NL page carries `en_link`:

```mdx
---
title: "Display Settings"
nl_link: "/nl/manuals/onecable/display-settings"
---
```

With N languages that's N-1 keys on every page, which is why it's generated rather than
hand-maintained:

```bash
# after adding/renaming/removing any manual page, or adding a language
python scripts/generate_language_links.py

# validate only — exits 1 if anything is missing, wrong, or out of parity (CI / pre-commit)
python scripts/generate_language_links.py --check

python scripts/generate_language_links.py --verbose   # per-file detail
```

Run it from the repo root (it refuses to run anywhere else). Python 3, stdlib only.

What it does:

- **Discovers languages** from the tree — any top-level `en`/`nl`/`pt-BR`-style directory
  containing `manuals-index.mdx` or a `manuals/` folder. Adding a language folder is all
  it takes; there's no list to update.
- **Checks EN ↔ NL parity** and reports any page that exists in one language but not
  another. Links to a missing counterpart are never written.
- **Adds, corrects, and removes** `<lang>_link` keys, including stale ones pointing at a
  language or page that no longer exists.
- **Idempotent and non-destructive** — targeted line edits only, never a YAML
  parse-and-redump, so key order, formatting and each file's CRLF/LF style survive
  byte-for-byte. Nothing outside the language folders is touched.

---

## 🔗 QR Code Generation

### QR Code URL Format

Each product gets language-specific QR codes:

- **Dutch QR Code**: `https://manuals.screenmate.com/nl/manuals/[product-name]/index`
- **English QR Code**: `https://manuals.screenmate.com/en/manuals/[product-name]/index`

### Recommended QR Code Setup
- Generate QR codes using a service like [QR Code Generator](https://www.qr-code-generator.com/)
- Print QR codes on product packaging or include on a card in the box
- Test QR codes on multiple devices before printing

---

## 🎨 Design Guidelines

### Colors (Screenmate Brand)
- **Primary**: `#16A34A` (Green)
- **Light**: `#07C983`
- **Dark**: `#15803D`

### Navigation Structure
- **One `hidden: true` tab per product**, mirrored in both language blocks
- Pages in this order, skipping any the product doesn't have:
  1. Introduction (`index`)
  2. Installation (optionally grouping `installation-windows` / `installation-mac`)
  3. Display Settings *(conditional)*
  4. Controls
  5. OSD menu *(conditional)*
  6. Troubleshooting *(conditional)*
  7. Safety

### Writing Style
- **Clear & Concise**: Hardware users need quick answers
- **Step-by-Step**: Use numbered lists for procedures
- **Visual**: Include images/screenshots for every major step
- **Multilingual**: Keep English and Dutch in sync

### Image Guidelines
- Use PNG format for screenshots and product photos
- Keep filenames descriptive: `USB-C Port.png`, `Driver Installation Windows.png`
- Use URL-encoded paths in MDX: `%20` for spaces
- Store all images in `/images/[Product] - [Manual] images/`

---

## 🛠️ Development Workflow

### Local Development

1. **Install Mintlify CLI**:
   ```bash
   npm i -g mint
   ```

2. **Run Dev Server**:
   ```bash
   mint dev
   ```
   View at `http://localhost:3000`

3. **Test Language Switching**: Toggle between EN/NL to ensure both versions work

### Publishing Changes

Changes pushed to `main` branch are automatically deployed via the Mintlify GitHub app.

### Common Issues

| Issue | Solution |
|-------|----------|
| 404 on manual page | Ensure page is listed in `docs.json` navigation |
| Logo not showing | Use `/images/` prefix (leading slash) |
| Images not loading | Check for URL encoding of spaces (`%20`) |
| Language code error | Use `en` not `en-GB`, `nl` not `nl-NL` |

---

## 📋 Checklist for New Manuals

- [ ] Create manual folders: `en/manuals/[product]/` and `nl/manuals/[product]/`
- [ ] Create image folder: `images/[Product] - [Manual] images/`
- [ ] Create the 4 always-on pages (index, installation, controls, safety) + any conditional ones
- [ ] Add a `hidden: true` product tab to `docs.json` for **both** languages
- [ ] Add a text-only card to `en/manuals-index.mdx` and `nl/manuals-index.mdx`
- [ ] Add product images to image folder
- [ ] Run `python scripts/generate_language_links.py` (cross-language frontmatter links)
- [ ] Confirm `python scripts/generate_language_links.py --check` exits clean
- [ ] Test all pages locally with `mint dev`
- [ ] Generate QR codes for both languages
- [ ] Test QR codes on mobile devices
- [ ] Push to `main` branch to deploy

---

## 📚 Resources

- [Mintlify Documentation](https://mintlify.com/docs)
- [Mintlify Components](https://mintlify.com/docs/components)
- [Screenmate Website](https://screenmate.com)
- [Screenmate Blog](https://screenmate.com/blogs/blog)

---

## 🎯 The Manuals Index

`en/manuals-index.mdx` and `nl/manuals-index.mdx` are the only non-hidden pages in the site.
They list every product as a **text-only card** (`title` + `href`, no icon, no body copy) and serve as:

- A general support landing page to link from screenmate.com
- A fallback for customers who need a different product's manual
- **Not** the QR-code target — printed QR codes always point straight at a specific product manual

---

**Last Updated**: November 2025  
**Maintained By**: OASE Creative
