# Changelog - MCP Server Updates

## Latest Updates (2026-01-26)

### ✅ Added arXiv Link Support

- **New Tool**: `fetch_arxiv_paper`
  - Accepts arXiv URLs (e.g., `https://arxiv.org/abs/1234.5678`)
  - Automatically downloads LaTeX source (preferred) or HTML version
  - Returns local file path for processing

### ✅ Added HTML File Support

- **HTML Parsing**: Added `parse_html_structure()` function
  - Parses HTML headings (`<h1>` through `<h6>`)
  - Extracts structure and text excerpts
  - Supports both `.html` and `.htm` files

### ❌ Removed PDF Support

- **PDF files are NO LONGER supported**
- Updated all tool descriptions to clarify:
  - ✅ Supported: LaTeX (.tex), HTML (.html), Markdown (.md), arXiv links
  - ❌ NOT supported: PDF (.pdf)

### 📚 Added Comprehensive IDE Setup Guide

- **New File**: `IDE_SETUP.md`
  - Detailed instructions for Cursor IDE (built-in MCP support)
  - Instructions for VS Code (may require extension)
  - Instructions for JetBrains IDEs
  - Troubleshooting guide
  - Verification checklist

### 📝 Updated Documentation

- **README.md**: 
  - Added "Supported File Formats" section
  - Updated examples to show arXiv links
  - Added reference to IDE_SETUP.md
  - Clarified MCP installation requirements

- **QUICKSTART.md**:
  - Added note about supported formats
  - Added reference to IDE_SETUP.md
  - Updated examples

## Supported Input Formats

### ✅ Supported

1. **LaTeX files** (`.tex`)
   - Preferred format
   - Full structure parsing
   - Section/subsection extraction

2. **HTML files** (`.html`, `.htm`)
   - Parses HTML headings
   - Extracts structure from `<h1>` through `<h6>`
   - Text excerpt extraction

3. **Markdown files** (`.md`)
   - Parses Markdown headings
   - Structure extraction

4. **arXiv links**
   - Format: `https://arxiv.org/abs/1234.5678`
   - Format: `https://arxiv.org/pdf/1234.5678.pdf`
   - Automatically fetches LaTeX source (preferred) or HTML

### ❌ NOT Supported

- **PDF files** (`.pdf`)
  - Please use LaTeX source or HTML version instead
  - Convert PDF to HTML if needed, or use arXiv source

## IDE Support Status

| IDE | MCP Support | Installation Required |
|-----|-------------|---------------------|
| **Cursor** | ✅ Built-in | No - Ready to use |
| **VS Code** | ⚠️ Extension | Yes - May need MCP extension |
| **JetBrains** | ⚠️ Limited | Yes - Check for plugins |
| **Others** | ❌ May not support | Varies |

**See IDE_SETUP.md for detailed instructions for each IDE.**

## Usage Examples

### Example 1: arXiv Link (Recommended)
```
Extract and visualize:
https://arxiv.org/abs/2312.05885
```

### Example 2: Local LaTeX File
```
Extract and visualize:
/path/to/paper.tex
```

### Example 3: Local HTML File
```
Parse and visualize:
/path/to/paper.html
```

### Example 4: Archive with LaTeX
```
Extract and visualize:
/path/to/paper.tar.gz
```

## Breaking Changes

- **PDF files no longer supported** - Update any workflows using PDF files
- **Tool descriptions updated** - All tools now clearly state supported formats

## Migration Guide

If you were using PDF files:

1. **Use arXiv source instead:**
   - Change: `paper.pdf`
   - To: `https://arxiv.org/abs/1234.5678`

2. **Or convert PDF to HTML:**
   - Use online tools or `pdftohtml` command
   - Then use the HTML file

3. **Or extract LaTeX from archive:**
   - Many papers provide LaTeX source in archives
   - Extract and use the `.tex` file

---

**Last Updated**: 2026-01-26
