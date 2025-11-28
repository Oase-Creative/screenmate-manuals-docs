# Mintlify Syntax & Troubleshooting Guide

This guide helps you avoid common syntax errors and troubleshoot build failures in your Mintlify documentation.

## 🔍 Quick Validation Commands

Before pushing changes, run these commands to catch issues early:

```bash
# Install/update Mintlify CLI
npm i -g mint

# Check for broken internal links
mint broken-links

# Preview locally to catch errors before deployment
mint dev

# Check accessibility issues
mint a11y
```

**Note:** The `mint broken-links` command may show false positives for multi-language setups. The command checks file paths but may not correctly handle language routing. If:
- Files exist at the paths specified
- Paths match what's in `docs.json`
- Links work in `mint dev` preview

Then the links should work correctly in production, even if `mint broken-links` reports them as broken.

## ✅ Common Syntax Issues & Fixes

### 1. **MDX Frontmatter Issues**

#### ❌ **Problem: Missing or malformed frontmatter**
```mdx
title: "My Page"
description: "Page description"
---
```
**Fix:** Frontmatter must be wrapped in `---` on both sides:
```mdx
---
title: "My Page"
description: "Page description"
---
```

#### ❌ **Problem: Horizontal rules (`---`) in content**
Using `---` in your content can confuse the parser if it's too close to frontmatter or in certain positions.

**Fix:** Use HTML horizontal rule instead:
```mdx
<hr />
```

Or use markdown alternative:
```mdx
***
```

**Example from your codebase:**
In `playbooks/nl/handleidingen.mdx`, you have multiple `---` in the content (lines 14, 42, 58, 68, 75, 85, 99, 110, 123, 137, 158, 167, 185, 194, 203). These should be replaced with `***` or `<hr />`.

### 2. **Navigation Configuration Issues**

#### ❌ **Problem: Page paths don't match file structure**
```json
{
  "navigation": {
    "pages": [
      "playbooks/nl/product-listing"  // Missing .mdx extension
    ]
  }
}
```

**Fix:** Paths should match file paths WITHOUT the `.mdx` extension:
```json
{
  "navigation": {
    "pages": [
      "playbooks/nl/product-listing-design-guidelines"  // ✅ Correct
    ]
  }
}
```

#### ❌ **Problem: Pages not showing up**
Common causes:
1. **File path mismatch:** The path in `docs.json` doesn't match the actual file location
2. **Missing frontmatter:** File exists but has no frontmatter
3. **Invalid frontmatter:** Syntax error in frontmatter (missing quotes, trailing commas, etc.)
4. **File not in correct location:** File is outside the docs directory structure

**Fix checklist:**
- ✅ Verify file path in `docs.json` matches actual file location (case-sensitive!)
- ✅ Ensure file has valid frontmatter with `title` field
- ✅ Check file extension is `.mdx` (not `.md`)
- ✅ Run `mint broken-links` to find broken references

### 3. **Component Syntax Issues**

#### ❌ **Problem: Unclosed components**
```mdx
<Card title="My Card">
  Content here
// Missing closing tag
```

**Fix:** Always close components:
```mdx
<Card title="My Card">
  Content here
</Card>
```

#### ❌ **Problem: Invalid component props**
```mdx
<Card title="My Card" cols={2}>  // ❌ Card doesn't have cols prop
```

**Fix:** Use correct component structure:
```mdx
<CardGroup cols={2}>
  <Card title="My Card">
    Content
  </Card>
</CardGroup>
```

### 4. **JSON Configuration Issues**

#### ❌ **Problem: Trailing commas in docs.json**
```json
{
  "navigation": {
    "pages": [
      "page1",
      "page2",  // ❌ Trailing comma
    ]
  }
}
```

**Fix:** Remove trailing commas (or ensure your JSON parser supports them):
```json
{
  "navigation": {
    "pages": [
      "page1",
      "page2"  // ✅ No trailing comma
    ]
  }
}
```

#### ❌ **Problem: Invalid language configuration**
```json
{
  "navigation": {
    "languages": [
      {
        "language": "nl",
        "tabs": [...]  // ✅ Your structure is correct
      }
    ]
  }
}
```

**Your current structure is correct!** Just ensure:
- Language codes match file paths (`nl/` folder → `"language": "nl"`)
- All page paths include the language prefix when using languages

### 5. **Link Issues**

#### ❌ **Problem: Broken internal links**
```mdx
[Link Text](/playbooks/nl/product-listing)  // File doesn't exist
```

**Fix:** Use `mint broken-links` to find all broken links:
```bash
mint broken-links
```

Then fix paths to match actual file locations:
```mdx
[Link Text](/playbooks/nl/product-listing-design-guidelines)  // ✅ Correct
```

#### ❌ **Problem: External links without protocol**
```mdx
[Link](www.example.com)  // ❌ Missing https://
```

**Fix:** Always include protocol:
```mdx
[Link](https://www.example.com)  // ✅ Correct
```

## 🚨 Build Failure Troubleshooting

### Issue: "Page not found" or 404 errors

**Checklist:**
1. ✅ File exists in the correct location
2. ✅ Path in `docs.json` matches file path (case-sensitive!)
3. ✅ File has valid frontmatter with `title`
4. ✅ File extension is `.mdx`
5. ✅ No syntax errors in frontmatter (check for unclosed quotes, etc.)

**Debug steps:**
```bash
# 1. Validate configuration
mint validate

# 2. Check for broken links
mint broken-links

# 3. Preview locally
mint dev
# Navigate to the page and check console for errors
```

### Issue: "Build failed" with syntax errors

**Common causes:**
1. **Invalid MDX syntax:** Unclosed tags, invalid components
2. **JSON syntax errors:** Check `docs.json` with a JSON validator
3. **Frontmatter errors:** Missing quotes, invalid YAML

**Debug steps:**
```bash
# 1. Validate JSON
# Use an online JSON validator or:
node -e "JSON.parse(require('fs').readFileSync('docs.json', 'utf8'))"

# 2. Check MDX files for syntax errors
# Look for:
# - Unclosed tags
# - Invalid component usage
# - Malformed frontmatter
```

### Issue: Page works locally but not in production

**Common causes:**
1. **Caching:** Mintlify may cache old versions
2. **Case sensitivity:** File paths are case-sensitive in production
3. **Deployment delay:** Changes may take a few minutes to deploy

**Debug steps:**
1. Wait 2-3 minutes after push
2. Check Mintlify dashboard for deployment status
3. Verify file paths are exactly correct (case-sensitive)
4. Clear browser cache or use incognito mode

## 📋 Pre-Deployment Checklist

Before pushing changes, verify:

- [ ] All MDX files have valid frontmatter with `title`
- [ ] All paths in `docs.json` match actual file locations
- [ ] No trailing commas in `docs.json` (unless your parser supports them)
- [ ] All internal links are valid (run `mint broken-links`)
- [ ] No horizontal rules (`---`) in content (use `***` or `<hr />` instead)
- [ ] All components are properly closed
- [ ] No syntax errors in MDX files
- [ ] Local preview works (`mint dev`)
- [ ] JSON is valid (use JSON validator)

## 🔧 Your Current Setup - Potential Issues

### ✅ **What's Correct:**
- Frontmatter structure is consistent
- Navigation structure with languages is properly configured
- Component usage (Card, CardGroup, Warning, Tip, Note) is correct
- File paths in `docs.json` match file structure

### ⚠️ **Potential Issues Found:**

1. **Horizontal rules in content:**
   - `playbooks/nl/handleidingen.mdx` has multiple `---` in content
   - These should be replaced with `***` or `<hr />` to avoid parser confusion

2. **File path verification:**
   - Ensure all paths in `docs.json` exactly match file locations
   - Case-sensitive: `playbooks/nl/Product-Listing` ≠ `playbooks/nl/product-listing`

## 🛠️ Recommended Workflow

1. **Before making changes:**
   ```bash
   mint dev  # Start local preview
   ```

2. **While editing:**
   - Keep `mint dev` running to see changes in real-time
   - Check browser console for errors

3. **Before committing:**
   ```bash
   mint validate        # Validate config
   mint broken-links    # Check links
   ```

4. **After pushing:**
   - Wait 2-3 minutes for deployment
   - Check Mintlify dashboard for build status
   - Verify pages load correctly

## 📚 Additional Resources

- [Mintlify Documentation](https://mintlify.com/docs)
- [MDX Documentation](https://mdxjs.com/)
- [Mintlify Components Reference](https://mintlify.com/docs/components)

## 🆘 Still Having Issues?

1. **Check Mintlify Dashboard:**
   - View build logs
   - Check deployment status
   - Review error messages

2. **Validate locally:**
   ```bash
   mint validate
   mint broken-links
   mint dev
   ```

3. **Common fixes:**
   - Clear browser cache
   - Wait for deployment (2-3 minutes)
   - Verify file paths are exact (case-sensitive)
   - Check for syntax errors in frontmatter

4. **Get help:**
   - [Mintlify Discord](https://mintlify.com/discord)
   - [Mintlify GitHub Discussions](https://github.com/mintlify/docs/discussions)

