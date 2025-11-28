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
├── manuals/
│   ├── en/
│   │   └── [product-name]/
│   │       ├── index.mdx        # Product intro, specs, what's in the box
│   │       ├── installation.mdx
│   │       ├── drivers.mdx
│   │       ├── display-settings.mdx
│   │       ├── controls.mdx
│   │       ├── troubleshooting.mdx
│   │       ├── safety.mdx
│   │       └── downloads.mdx
│   └── nl/
│       └── [product-name]/
│           ├── index.mdx        # Dutch version
│           ├── installation.mdx
│           └── ...
└── README.md
```

---

## 🚀 Adding a New Product Manual

### Step 1: Create the Manual Folders

```bash
# Create English manual folder
mkdir -p manuals/en/[product-name]

# Create Dutch manual folder
mkdir -p manuals/nl/[product-name]

# Create image folder for the product
mkdir -p "images/[Product Name] - [Manual Name] images"
```

### Step 2: Create Manual Pages

Use this standard structure for **every product**:

#### English Pages (`manuals/en/[product-name]/`)
1. **index.mdx** - Introduction, what's in the box, key features, specs
2. **installation.mdx** - Physical setup and connection instructions
3. **drivers.mdx** - Driver installation (if needed)
4. **display-settings.mdx** - OS-specific configuration (Windows, MacOS)
5. **controls.mdx** - Physical buttons and OSD menu
6. **troubleshooting.mdx** - Common issues and solutions
7. **safety.mdx** - Safety warnings and care instructions
8. **downloads.mdx** - PDF manual and driver links

#### Dutch Pages (`manuals/nl/[product-name]/`)
Create the same structure with Dutch translations.

### Step 3: Update `docs.json`

Add the new product to the `navigation.languages` array:

```json
{
  "navigation": {
    "languages": [
      {
        "language": "nl",
        "pages": [
          "manuals/nl/onecable/index",
          "manuals/nl/onecable/installation",
          "manuals/nl/onecable/drivers",
          "manuals/nl/onecable/display-settings",
          "manuals/nl/onecable/controls",
          "manuals/nl/onecable/troubleshooting",
          "manuals/nl/onecable/safety",
          "manuals/nl/onecable/downloads",
          
          // Add new product here
          "manuals/nl/[new-product]/index",
          "manuals/nl/[new-product]/installation",
          // ... etc
        ]
      },
      {
        "language": "en",
        "pages": [
          // Same structure for English
        ]
      }
    ]
  }
}
```

### Step 4: Page Template

Use this template for `index.mdx`:

```mdx
---
title: "[Product Name] Manual"
description: "Complete user guide for your [Product Name]"
icon: "book-open"
---

<Note>
**Welcome!** This is your complete digital manual for the [Product Name]. Use the navigation menu on the left to jump to any section.
</Note>

## What is [Product Name]?

[Brief product description - 2-3 sentences about what it does and who it's for]

### Key Features

- **Feature 1** - Description
- **Feature 2** - Description
- **Feature 3** - Description
- **Feature 4** - Description
- **Feature 5** - Description

## In the Box

Check if all the following items are present in the package.

<div className="grid grid-cols-2 gap-4">
  <div className="text-center">
    <img className="h-40 object-contain mx-auto" src="/images/[Product] - [Manual] images/item1.png" alt="Item 1" />
    <p className="font-semibold mt-2">Item Name</p>
  </div>
  <!-- Add more items -->
</div>

## Technical Specifications

| Feature | Specification |
| :--- | :--- |
| **Screen Size** | 15.6 inch |
| **Resolution** | 1920 x 1080 (Full HD) |
| **Panel Type** | IPS |
| **Weight** | ~800g |

<Note>Specifications are subject to change. Please refer to the official product page for the most up-to-date information.</Note>
```

---

## 🔗 QR Code Generation

### QR Code URL Format

Each product gets language-specific QR codes:

- **Dutch QR Code**: `https://docs.screenmate.com/nl/manuals/nl/[product-name]/index`
- **English QR Code**: `https://docs.screenmate.com/en/manuals/en/[product-name]/index`

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
- **Flat sidebar** (no tabs, no groups in current design)
- Pages listed in logical order:
  1. Introduction
  2. Installation
  3. Drivers
  4. Display Settings
  5. Controls
  6. Troubleshooting
  7. Safety
  8. Downloads

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

- [ ] Create manual folders: `manuals/en/[product]/` and `manuals/nl/[product]/`
- [ ] Create image folder: `images/[Product] - [Manual] images/`
- [ ] Create all 8 standard pages (index, installation, drivers, etc.)
- [ ] Add product to `docs.json` navigation for both languages
- [ ] Add product images to image folder
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

## 🎯 Future Enhancements

### When You Have Multiple Products

Consider adding a **landing page** that lists all available manuals:

```mdx
# Screenmate Product Manuals

<CardGroup cols={2}>
  <Card
    title="OneCable Manual"
    icon="monitor"
    href="/manuals/en/onecable/index"
  >
    Portable monitor with single-cable connectivity
  </Card>
  
  <Card
    title="[Product 2] Manual"
    icon="laptop"
    href="/manuals/en/[product-2]/index"
  >
    Description of product 2
  </Card>
</CardGroup>
```

This can serve as:
- A general support page on screenmate.com
- A fallback if users need to find a different product manual
- But **QR codes should still link directly to specific product manuals**

---

**Last Updated**: November 2025  
**Maintained By**: OASE Creative
