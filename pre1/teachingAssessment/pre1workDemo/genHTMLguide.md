# Guide for Generating HTML Presentation Slides

This document captures the design principles and technical requirements for generating self-contained HTML presentation slides. These principles were refined through multiple iterations (V1→V3) and should be followed by any AI agent generating slides.

---

## 1. Layout & Spacing

### Side Margins
- Use **`padding: 5vh 10vw`** on each slide
- `10vw` side padding works well on 16:9 screens — wide enough to frame the content without wasting space
- **Do NOT** go below `8vw` (content stretches too wide) or above `12vw` (too much empty space on sides)

### Vertical Distribution
- Slides use `display: flex; flex-direction: column; justify-content: center` so content is vertically centered
- Content should **fill at least 70-80%** of the vertical space — avoid leaving large empty areas at the top or bottom
- If content is sparse, increase font sizes, spacing, or add more detail rather than leaving whitespace

### Slide Dimensions
- Each slide is `100vw × 100vh` (full viewport)
- Position slides with `position: absolute; top: 0; left: 0` and toggle visibility

---

## 2. Font Sizes — Must Be Presentation-Ready

This is the most common mistake. Fonts that look fine in a document are **too small for slides**. Use these minimums:

| Element | Recommended `clamp()` | Minimum |
|---|---|---|
| **Slide title** | `clamp(2.4rem, 4.2vw, 3.6rem)` | 2.2rem |
| **Body text / bullet items** | `clamp(1.25rem, 1.8vw, 1.55rem)` | 1.15rem |
| **Highlight / callout boxes** | `clamp(1.15rem, 1.6vw, 1.4rem)` | 1.05rem |
| **Transition cues** | `clamp(1.05rem, 1.4vw, 1.25rem)` | 0.95rem |
| **Captions / small text** | `clamp(1rem, 1.3vw, 1.15rem)` | 0.9rem |
| **Title slide heading** | `clamp(2.8rem, 5vw, 4rem)` | 2.5rem |
| **Subtitle** | `clamp(1.4rem, 2.2vw, 2rem)` | 1.3rem |
| **Big numbers (stats)** | `clamp(2.8rem, 5vw, 4.2rem)` | 2.5rem |
| **Diagram labels** | `clamp(0.8rem, 1.05vw, 1rem)` | 0.75rem |
| **Rubric tags** | `0.78rem` fixed | 0.7rem |

### Why `clamp()`?
- Format: `clamp(minimum, preferred, maximum)`
- The `vw`-based preferred value scales with screen width
- The min/max prevent text from being too small on narrow screens or too large on ultra-wide ones

---

## 3. Slide Numbers

- Every slide must display its number
- Place in the **bottom-right corner**: `position: absolute; bottom: 1.2rem; right: 2rem`
- Use a light color (`#ccc`) so it's visible but not distracting
- Top-right placement wastes vertical space in the content area

---

## 4. Assessment Rubric Labels

For academic presentations, add colored **rubric tags** that explicitly reference which assessment criterion each section addresses:

```html
<span class="rubric-tag content">CONTENT & STRUCTURE</span>
<span class="rubric-tag content">KEY FINDINGS</span>
<span class="rubric-tag content">SIGNIFICANCE</span>
<span class="rubric-tag content">WRITING SKILLS</span>
<span class="rubric-tag content">EVIDENCE</span>
<span class="rubric-tag content">NON-SPECIALIST</span>
<span class="rubric-tag delivery">DELIVERY</span>
```

- Tags should be small, inline, and color-coded by rubric category
- Place them at the **start** of the relevant section, before the body text
- They serve as visual cues that the presentation is aligned with assessment criteria

---

## 5. Transitional Cues

Each content slide (not the title or closing slide) should end with a **transition cue** — an italicized line that previews what comes next:

```html
<div class="transition-cue">Now let me explain how KVFlow solves this problem...</div>
```

- Style: italic, primary color, preceded by `→`
- Use `margin-top: auto` so it sits at the bottom of the slide
- Add a subtle `border-top` separator line above it
- These help the speaker maintain flow and signal structure to the audience

---

## 6. Content Volume for Timing

For an **8-minute presentation**:
- Plan **10-12 content slides** (excluding title and closing)
- That's roughly **40-50 seconds per slide**
- Each slide should have enough content to speak about for that duration:
  - A title + 1-2 paragraphs or 3-4 bullet points
  - A visual element (diagram, chart, callout box) where applicable
  - Slides with only a title and 2 short bullets are **too sparse**

---

## 7. Visual Elements — CSS-Only Diagrams

All diagrams should be built with pure HTML/CSS (no images, no external libraries):

- **Agent/node diagrams**: Flexbox rows of colored circles with labels
- **Timeline/Gantt charts**: Flexbox rows with proportional `flex` values
- **Bar charts**: Flex containers with `align-items: flex-end`
- **Bridge diagrams**: Three boxes connected by arrow characters
- **Lesson/card grids**: CSS Grid with 2 columns

### Sizing for diagrams
- Agent nodes: `clamp(85px, 9vw, 115px)` width/height
- Timeline bars: `42px` height
- Bar chart container: `180px` height
- These are larger than typical web UI elements — remember, this is a slide deck

---

## 8. Color System

Use CSS custom properties for consistency:

```css
:root {
  --color-primary: #1B4942;       /* Dark teal — headings, accents */
  --color-text: #1a1a2e;          /* Body text */
  --color-bg: #FFFFFF;            /* Slide background */
  --color-bg-alt: #F8FAF4;        /* Alternate/card background */
  --color-accent-light: #E8F0ED;  /* Highlight box background */
}
```

- Use `--color-primary` for titles, borders, active states
- Keep backgrounds white or very light — dark backgrounds make text hard to read
- Use distinct colors for different diagram elements (agents, chart bars, etc.)

---

## 9. Self-Contained HTML

The generated file must be **a single `.html` file** with:
- All CSS in a `<style>` block in `<head>`
- All JavaScript in a `<script>` block before `</body>`
- **No external CSS/JS frameworks** (no Bootstrap, no Reveal.js)
- Google Fonts loaded via `@import url(...)` in the CSS (the only external dependency)
- No images — use CSS shapes, Unicode symbols, and emoji instead

---

## 10. Navigation (JavaScript)

Implement keyboard and mouse navigation:

| Input | Action |
|---|---|
| `→` or `Space` | Next slide |
| `←` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| Click right 60% | Next slide |
| Click left 40% | Previous slide |

Add a **progress bar** at the bottom: `position: fixed; bottom: 0; height: 4px; background: primary color`.

---

## 11. Editable Mode

Make all text content editable in the browser so users can customize the slides:

### Implementation
- Add `contenteditable="false"` to all text elements by default
- Toggle with JavaScript: pressing `E` switches all `contenteditable` attributes to `"true"`
- Provide a toolbar (hidden by default, toggled with `T`) with buttons for:
  - **Save to Cache** — `localStorage.setItem()` with the full `document.documentElement.outerHTML`
  - **Load from Cache** — `document.open(); document.write(saved); document.close()`
  - **Download HTML** — create a `Blob`, generate an object URL, trigger download
  - **Clear Cache** — remove localStorage entries

### Navigation in edit mode
- When edit mode is active, disable keyboard navigation (except `Escape` to exit edit mode)
- Disable click-to-navigate so users can click to position their cursor in text

---

## 12. Checklist Before Delivery

Before finalizing the HTML file, verify:

- [ ] All text is readable at **arm's length** on a laptop screen
- [ ] No slide has more than 50% empty space
- [ ] Every slide has a slide number
- [ ] Content slides have transition cues
- [ ] Rubric tags are present on relevant sections
- [ ] Navigation works (arrows, click, Home/End)
- [ ] Edit mode works (E to toggle, save/load/download)
- [ ] The file is self-contained (opens correctly when double-clicked)
- [ ] Total slide count supports the target presentation duration

---

## Example: Recommended Slide Structure

```
Slide 1:  Title + paper reference
Slide 2:  Roadmap / overview of presentation structure
Slide 3:  Hook / accessible entry point (analogy)
Slide 4:  Problem context and research gap
Slide 5:  Solution part 1 (main contribution)
Slide 6:  Solution part 2 (secondary contribution)
Slide 7:  Results / evidence
Slide 8:  Broader significance
Slide 9:  Impact on own research
Slide 10: Writing lessons (detailed analysis)
Slide 11: More writing lessons (additional evidence)
Slide 12: Thank you + key takeaway + Q&A
```

This gives ~40-50 seconds per content slide for an 8-minute presentation.
