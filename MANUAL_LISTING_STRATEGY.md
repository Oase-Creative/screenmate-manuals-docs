# Manual Listing Page Strategy

**When to add a "List All Manuals" page vs. keeping direct QR code links**

---

## Current Setup (1 Product)

✅ **Keep as-is**: QR codes land directly on the OneCable manual
- No listing page needed
- Zero friction for users
- Clean, focused experience

---

## Future Strategy by Product Count

### 2-3 Products
**Status**: Still use direct QR links

**Action**: 
- QR codes still bypass listing page → go direct to product manuals
- Add listing page to main Screenmate.com website as: `Support > Manuals`
- Users can find it if they need a different product manual
- But QR codes remain the primary entry point

### 5+ Products
**Status**: Consider adding listing page to docs.json

**Action**:
- Add `en/manuals-index.mdx` and `nl/manuals-index.mdx` to `docs.json` navigation
- Make it the root/landing page for the docs site
- **BUT**: QR codes still bypass it and go direct to product manuals
- Listing page serves as:
  - Fallback if QR code doesn't work
  - Discovery page for users who need a different manual
  - Link from main website support section

---

## Key Principle

**QR codes ALWAYS go direct to the product manual** - never to a listing page.

The listing page is only for:
- Users who manually navigate to the docs site
- Users who need a different product manual
- Discovery/search purposes
- Website navigation

---

## Implementation Notes

### Files Created
- `en/manuals-index.mdx` - English listing page (ready to use)
- `nl/manuals-index.mdx` - Dutch listing page (ready to use)

### To Activate Listing Page

When ready, add to `docs.json`:

```json
{
  "navigation": {
    "languages": [
      {
        "language": "en",
        "pages": [
          "en/manuals-index",  // Add this as first page
          "manuals/en/onecable/index",
          // ... rest of pages
        ]
      }
    ]
  }
}
```

---

## Decision Tree

```
Do we have 1 product?
  → No listing page needed

Do we have 2-3 products?
  → Keep direct QR links
  → Add listing page to main website only

Do we have 5+ products?
  → Keep direct QR links
  → Add listing page to docs.json navigation
  → QR codes still bypass listing page
```

---

**Remember**: The listing page is a **nice-to-have** for discovery, but QR codes should **always** take users directly to their product manual. This maintains the zero-friction experience that makes this system so effective.

