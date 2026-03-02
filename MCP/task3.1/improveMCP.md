# MCP Server Improvements Documentation

## Issues Identified from Generated HTML Files

After reviewing the generated HTML files from test runs, the following issues were identified:

### 1. **LaTeX Command Parsing Issues**

**Problem:**
- Title showed raw LaTeX: `Title\tnoteref{label1` instead of clean title
- Author showed raw LaTeX: `Name\corref{cor1` instead of clean author name
- Text excerpts contained raw LaTeX commands like `\cite{caponnetto2007optimal}`, `$...$` math notation

**Root Cause:**
- Regex pattern `r'\\title\{([^}]+)\}'` only captures until first `}`, doesn't handle nested braces
- No LaTeX command cleaning for text excerpts
- No HTML escaping for special characters

### 2. **Empty Connections in Network Visualization**

**Problem:**
- Interconnected visualization showed empty connections array
- Network diagram had no links between nodes

**Root Cause:**
- Connection analysis was too simplistic
- Only found connections based on limited keyword matching
- Didn't generate enough semantic connections

### 3. **Text Excerpt Quality**

**Problem:**
- Text excerpts contained LaTeX commands, comments, and special characters
- Hard to read in HTML output

**Root Cause:**
- Text extraction didn't skip LaTeX commands
- No cleaning of LaTeX syntax for HTML display

## Improvements Implemented

### 1. Enhanced LaTeX Parsing

#### 1.1 Balanced Brace Extraction

**Added Function:** `extract_balanced_braces()`
- Properly handles nested braces in LaTeX
- Extracts complete content from `{...}` even with nested structures
- Used for title and author extraction

**Before:**
```python
title_match = re.search(r'\\title\{([^}]+)\}', content)
title = title_match.group(1)  # Stops at first }
```

**After:**
```python
def extract_balanced_braces(text: str, start_pos: int) -> Optional[str]:
    """Extract content from balanced braces starting at start_pos"""
    # Handles nested braces correctly
```

#### 1.2 LaTeX Text Cleaning

**Added Function:** `clean_latex_text()`
- Removes LaTeX comments (`%...`) while preserving line content
- Converts citations: `\cite{ref}`, `\citep{ref}`, `\citet{ref}` → `[citation: ref]`
- Converts references: `\ref{label}`, `\eqref{label}` → `[ref: label]` or `[eq: label]`
- Removes label commands (not needed for display)
- Converts math mode: 
  - Inline: `$...$` → `[...]`
  - Display: `\[...\]`, `\(...\)`, `$$...$$` → `[...]`
- Preserves content from formatting commands:
  - `\textbf{text}` → `text`
  - `\textit{text}` → `text`
  - `\emph{text}` → `text`
- Removes footnote references (`\tnoteref`, `\corref`, `\fnref`)
- Converts footnotes: `\footnote{content}` → `(note: content)`
- Normalizes whitespace
- Escapes HTML special characters (final step)

**Features:**
- Preserves readable content from LaTeX commands
- Handles multiple citation/reference formats
- Converts math notation to readable format
- HTML-safe output

#### 1.3 Improved Title/Author Extraction

**New Functions:**
- `extract_latex_title()` - Handles nested braces and cleans LaTeX commands
- `extract_latex_author()` - Handles nested braces and cleans LaTeX commands

**Before:**
```python
title = "Title\tnoteref{label1"  # Incomplete, contains LaTeX
```

**After:**
```python
title = "Adaptive Parameter Selection for Kernel Ridge Regression"  # Clean
```

### 2. Enhanced Text Excerpt Extraction

#### 2.1 Smart Text Extraction

**Improvements:**
- Skips LaTeX commands when extracting text
- Skips LaTeX comments
- Extracts actual readable text content
- Cleans extracted text using `clean_latex_text()`

**Before:**
```python
text_excerpt = content[excerpt_start:excerpt_end]  # Contains \cite{}, $math$, etc.
```

**After:**
```python
# Smart extraction that skips LaTeX commands
# Then cleans with clean_latex_text()
text_excerpt = "Due to perfect theoretical behaviors in theory [citation: caponnetto2007optimal]..."
```

#### 2.2 HTML Escaping

**Added:**
- All text content is properly HTML-escaped
- Prevents XSS issues
- Ensures proper display in HTML

### 3. Improved Connection Analysis

#### 3.1 Enhanced Connection Detection

**Added Connection Types:**
1. **Sequential** - Each section connects to the next (strong)
2. **Hierarchical** - Sections to subsections, subsections to subsubsections (strong)
3. **Semantic** - Based on section names and content (medium/weak)
   - Introduction → Methods/Approach
   - Methods → Results/Experiments
   - Results → Discussion/Conclusion
   - Related Work → Introduction/Methods

**Before:**
```python
connections = []  # Often empty
```

**After:**
```python
# Generates multiple connection types:
# - Sequential connections (always)
# - Hierarchical connections (section structure)
# - Semantic connections (based on keywords)
```

#### 3.2 Duplicate Removal

**Added:**
- Removes duplicate connections
- Ensures unique connection set

### 4. Enhanced HTML Generation

#### 4.1 Proper HTML Escaping

**Updated:** `generate_hierarchical_content()` and `generate_interconnected_content()`
- All user content is HTML-escaped
- Prevents HTML injection
- Ensures proper rendering

#### 4.2 Subsubsection Support

**Added:**
- Support for subsubsections in hierarchical view
- Proper nesting and styling
- CSS classes for subsubsections

#### 4.3 Improved Network Visualization

**Enhanced:**
- Better handling of empty connections (arranges nodes in circle)
- Color-coded connection types
- Different stroke widths for different connection types
- Collision detection for better node spacing

### 5. Template Improvements

#### 5.1 Hierarchical Template

**Added:**
- CSS styling for subsubsections
- Better visual hierarchy
- Improved readability

#### 5.2 Interconnected Template

**Enhanced:**
- Better handling of empty connections
- Color-coded links (hierarchical=green, sequential=blue, semantic=orange)
- Improved node positioning
- Fallback layout when no connections

## Code Changes Summary

### Files Modified

1. **`tools/paper_tools.py`**
   - Added `extract_balanced_braces()` function
   - Added `clean_latex_text()` function
   - Added `extract_latex_title()` function
   - Added `extract_latex_author()` function
   - Updated `parse_latex_structure()` to use new extraction methods
   - Enhanced text excerpt extraction with LaTeX command skipping
   - Improved `analyze_section_interconnections()` with better connection detection

2. **`tools/visualization_tools.py`**
   - Updated `generate_hierarchical_content()` with HTML escaping
   - Added subsubsection support
   - Updated `generate_interconnected_content()` with proper JSON encoding

3. **`templates/hierarchical.html`**
   - Added CSS for subsubsections
   - Improved styling

4. **`templates/interconnected.html`**
   - Enhanced network visualization
   - Added color-coded connections
   - Improved empty connection handling

## Testing Recommendations

### Test Cases

1. **LaTeX with Nested Braces:**
   ```
   \title{Title\tnoteref{label1}}
   ```
   Should extract: "Title" (clean)

2. **LaTeX with Citations:**
   ```
   Text with \cite{ref1} and \cite{ref2}
   ```
   Should display: "Text with [citation: ref1] and [citation: ref2]"

3. **LaTeX with Math:**
   ```
   Formula: $x = y + z$
   ```
   Should display: "Formula: [x = y + z]"

4. **Connection Generation:**
   - Should always have sequential connections
   - Should have hierarchical connections if subsections exist
   - Should have semantic connections based on section names

## Expected Improvements

### Before vs After

| Aspect | Before | After |
|--------|--------|-------|
| **Title** | `Title\tnoteref{label1` | `Adaptive Parameter Selection for Kernel Ridge Regression` |
| **Author** | `Name\corref{cor1` | `Shao-Bo Lin` |
| **Text Excerpts** | Contains `\cite{}`, `$math$`, LaTeX commands | Clean, readable text with citations as `[citation: ...]` |
| **Connections** | Often empty | Multiple connection types (sequential, hierarchical, semantic) |
| **HTML Safety** | Raw LaTeX in HTML | Properly escaped HTML |
| **Subsubsections** | Not displayed | Properly nested and styled |

## Usage Notes

### For Users

The improved MCP server will now:
- ✅ Generate cleaner, more readable HTML visualizations
- ✅ Show proper connections in network diagrams
- ✅ Handle complex LaTeX documents with nested structures
- ✅ Display text excerpts without LaTeX commands
- ✅ Properly escape HTML for security

### For Developers

**Key Functions to Know:**
- `clean_latex_text()` - Use for any LaTeX text that needs HTML display
- `extract_balanced_braces()` - Use for extracting content from nested braces
- `analyze_section_interconnections()` - Generates multiple connection types

## Future Enhancements

Potential improvements for future versions:

1. **Math Rendering**: Use MathJax or KaTeX for proper math display
2. **Citation Links**: Make citations clickable
3. **Better Semantic Analysis**: Use NLP to detect more connection types
4. **Interactive Features**: Add search, filtering, and highlighting
5. **Export Options**: PDF export, JSON export of structure

---

**Last Updated**: 2026-01-26
**Version**: 2.0 (Improved)
