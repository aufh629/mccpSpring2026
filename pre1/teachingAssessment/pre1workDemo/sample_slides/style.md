# Style Guide — Sample Presentation Slides

This document describes the visual styles and formats of the two sample presentation decks, providing specifications that can be recreated in HTML/CSS.

---

## Sample 1: Presentation 1 (Infographic Style)

**Source:** `Presentation 1.pptx`

### Dimensions & Layout
- **Aspect ratio:** Portrait (13.3" × 17.8") — unusual poster/infographic format
- **Slides:** 1 (single-page infographic)
- **Layout type:** "Title and Content" — dense information layout

### Design Characteristics
- **Style:** Data-driven infographic with statistics prominently displayed
- **Structure:** Grid-based layout with multiple data cards
- **Images:** 8 embedded images (icons, charts, photos)
- **Typography:** Theme-inherited fonts (no explicit font overrides)
- **Content pattern:** Large statistics (44%, 35%, 66%, 63%, 20%) paired with short descriptive text

### Key Visual Elements
- Large percentage numbers as focal points
- Small chart visualizations embedded alongside statistics
- Photo placeholders for visual interest
- Footer with contact information and disclaimer
- Color-coded sections for different data categories

### HTML/CSS Recreation Notes
```css
/* Infographic grid layout */
.infographic-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    padding: 2rem;
}

/* Large statistic cards */
.stat-card {
    text-align: center;
    padding: 1.5rem;
}

.stat-number {
    font-size: 4rem;
    font-weight: 800;
    color: #1a5276;  /* deep blue for emphasis */
}

.stat-description {
    font-size: 1rem;
    color: #555;
    margin-top: 0.5rem;
}
```

---

## Sample 2: Monsha AI for Teachers (Widescreen Presentation)

**Source:** `Monsha Ultimate PD Deck - AI for Teachers.pptx`

### Dimensions & Layout
- **Aspect ratio:** Widescreen (20.0" × 11.2") — approximately 16:9
- **Slides:** 38
- **Layout type:** All "BLANK" layouts (fully custom positioning)

### Typography
| Element | Font | Size Range | Weight |
|---|---|---|---|
| Main titles | Poppins | 60–80pt | Bold |
| Section headings | Poppins / Open Sans | 35–40pt | Bold |
| Subheadings | Open Sans | 23–30pt | Bold |
| Body text | Open Sans | 16–18pt | Regular |
| Bullet points | Open Sans | 16–18pt | Regular |

### Color Palette
| Color | Hex | Usage |
|---|---|---|
| Dark teal/green | `#1B4942` | Primary accent, headings |
| Near black | `#000000` | Body text |
| Light cream/sage | `#F8FAF4` | Background, light elements |

### Design Characteristics
- **Style:** Clean, modern, professional — corporate/educational feel
- **Background:** Light/white with occasional teal accent sections
- **Text density:** Low — typically 3-5 bullet points max per slide
- **Visual hierarchy:** Strong — large titles, medium subtitles, smaller body
- **Images:** 12 embedded (mostly icons and screenshots)
- **Bold usage:** Frequent (101 of 230 text runs) — used for emphasis and titles
- **Slide patterns:**
  - Title slides: Large text, centered
  - Content slides: Title + 3-5 bullet points
  - Feature slides: Title + description + screenshot/icon
  - Pro tip slides: Highlighted box with tip icon

### Content Organization
- Opening (context/hook): Slides 1-4
- Feature overview: Slides 5-8
- Detailed walkthroughs: Slides 9-31
- Pro tips: Slides 32-37
- Closing/CTA: Slide 38

### HTML/CSS Recreation Notes
```css
/* Base presentation styles inspired by Monsha deck */

@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Poppins:wght@600;700;800&display=swap');

:root {
    --color-primary: #1B4942;       /* Dark teal */
    --color-text: #000000;          /* Body text */
    --color-bg: #F8FAF4;            /* Light sage background */
    --color-white: #FFFFFF;
    --color-accent-light: #E8F0ED;  /* Lighter teal for cards */
    --font-heading: 'Poppins', sans-serif;
    --font-body: 'Open Sans', sans-serif;
}

/* Slide container */
.slide {
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 5% 8%;
    background-color: var(--color-white);
    font-family: var(--font-body);
    color: var(--color-text);
}

/* Title */
.slide-title {
    font-family: var(--font-heading);
    font-size: 3rem;
    font-weight: 700;
    color: var(--color-primary);
    margin-bottom: 1.5rem;
}

/* Subtitle */
.slide-subtitle {
    font-family: var(--font-heading);
    font-size: 1.8rem;
    font-weight: 600;
    color: var(--color-primary);
    margin-bottom: 1rem;
}

/* Body text */
.slide-body {
    font-size: 1.3rem;
    line-height: 1.8;
    max-width: 80%;
}

/* Bullet list */
.slide-bullets {
    list-style: none;
    padding: 0;
}

.slide-bullets li {
    font-size: 1.3rem;
    line-height: 1.8;
    padding-left: 1.5rem;
    position: relative;
    margin-bottom: 0.8rem;
}

.slide-bullets li::before {
    content: '•';
    color: var(--color-primary);
    font-weight: bold;
    position: absolute;
    left: 0;
}

/* Highlight box (for key stats or tips) */
.highlight-box {
    background-color: var(--color-accent-light);
    border-left: 4px solid var(--color-primary);
    padding: 1.5rem 2rem;
    border-radius: 0 8px 8px 0;
    margin: 1rem 0;
}

/* Large number emphasis */
.big-number {
    font-family: var(--font-heading);
    font-size: 4rem;
    font-weight: 800;
    color: var(--color-primary);
}
```

---

## Combined Style Recommendations for HTML Slides

Based on both sample presentations, the recommended style for the demo HTML slides should:

1. **Use widescreen 16:9 aspect ratio** (following Monsha's modern approach)
2. **Typography hierarchy:** Poppins for headings, Open Sans for body — both Google Fonts
3. **Color scheme:** Dark teal `#1B4942` as primary accent on white/light backgrounds
4. **Minimal text per slide:** Maximum 3-5 bullet points; let visuals carry the message
5. **Strong visual hierarchy:** Large titles (3rem+), medium body (1.3rem), clear spacing
6. **Use highlight boxes** for key statistics and quotes
7. **Data visualization:** Use CSS-based charts/diagrams rather than images where possible
8. **Bold for emphasis** — use generously for key terms and statistics
9. **Clean, generous whitespace** — padding of 5-8% around content
10. **Subtle transitions** — fade between slides, no distracting animations
