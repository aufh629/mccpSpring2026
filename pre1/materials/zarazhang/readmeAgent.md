# Frontend Slides - AI Agent Documentation

## Overview

This folder contains materials from [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides), a framework for creating stunning, animation-rich HTML presentations using AI assistants like GitHub Copilot, Cursor, or Claude.

## Purpose

The contents have been adapted from Claude-specific instructions into **generic AI coding assistant skills** that work with:
- **GitHub Copilot** (VS Code)
- **Cursor AI**
- **Claude** or other AI coding assistants

## Files in This Folder

### 📘 SKILL.md
**Core skill file** for AI assistants to create HTML presentations.

**Key Features:**
- Zero-dependency single HTML files (no npm, no build tools)
- Animation-rich presentations with smooth transitions
- "Show, don't tell" design philosophy - generate visual previews
- Viewport fitting requirements (no scrolling within slides)
- Responsive design that works on all screen sizes

**Use this when:** You want to create a presentation from scratch or convert PowerPoint to interactive HTML.

### 🎨 STYLE_PRESETS.md
**Visual design presets** for different presentation styles.

Contains 12+ ready-to-use design systems:
- Modern Minimal (clean, professional)
- Brutalist (bold, high-contrast)
- Glassmorphic (frosted glass effects)
- Neon Cyberpunk (vibrant, futuristic)
- Academic (scholarly, traditional)
- And more...

**Use this when:** You need a specific aesthetic but aren't sure how to describe it.

### 📋 PRESENTATION_GUIDE.md
**Comprehensive guide** for creating presentations with AI.

Covers:
- How to structure presentation requests for AI
- Content density guidelines (how much per slide)
- Animation and transition best practices
- Conversion from PowerPoint
- Troubleshooting common issues

**Use this when:** You're new to AI-assisted presentation creation or need a reference.

### 📖 README.md
Original project README with examples and philosophy.

## How to Use These Materials

### For Presentation Creation

1. **Choose your approach:**
   - **From scratch:** Describe your topic and desired style
   - **From PowerPoint:** Provide a .pptx file to convert

2. **Provide context to your AI assistant:**
   ```
   I want to create a presentation about [TOPIC].
   Please follow the guidelines in SKILL.md and use the [STYLE NAME] preset from STYLE_PRESETS.md.
   ```

3. **Iterate visually:**
   - AI generates preview
   - You provide feedback on what works/doesn't
   - AI refines based on your preferences

### Example Prompts

**Create from scratch:**
```
Create a 10-slide presentation about machine learning basics.
Use the "Modern Minimal" style from STYLE_PRESETS.md.
Target audience: Business executives with no technical background.
Follow all viewport fitting requirements from SKILL.md.
```

**Convert PowerPoint:**
```
Convert this PowerPoint file to an interactive HTML presentation.
Extract all text, images, and structure.
Apply the "Academic" style preset.
Add smooth slide transitions and subtle animations.
```

**Iterate on design:**
```
The current design feels too corporate. Can you try the "Neon Cyberpunk" 
preset instead? Keep the content but update the visual style.
```

## Key Principles

### 1. Viewport Fitting (Non-negotiable)
Every slide must fit completely in the viewport - no scrolling within slides. If content is too long, split into multiple slides or reduce text.

### 2. Single File Output
The AI should generate **one HTML file** with:
- All CSS inline in `<style>` tags
- All JavaScript inline in `<script>` tags
- No external dependencies

### 3. Show, Don't Tell
Don't ask the user to choose between abstract options like "Modern vs. Classic". Instead, generate visual previews and let them react to what they see.

### 4. Production Quality
The generated code should be:
- Well-commented
- Accessible (ARIA labels, keyboard navigation)
- Performant (60fps animations)
- Cross-browser compatible

## Adapting for Different AI Assistants

### GitHub Copilot (VS Code)
Open SKILL.md in VS Code and reference it in your prompt:
```
@workspace /file:SKILL.md Create a presentation about [TOPIC]
```

### Cursor AI
Use the "Add to Chat" feature to include SKILL.md and STYLE_PRESETS.md, then describe your presentation needs.

### Claude or ChatGPT
Copy the relevant sections from SKILL.md into your conversation, then request the presentation.

## Technical Requirements

The generated presentations require only:
- A modern web browser (Chrome, Firefox, Safari, Edge)
- No server (files open locally)
- No internet connection (for viewing)

Optional for PowerPoint conversion:
- Python 3.8+ with `python-pptx` library

## Examples

See the original repository for live examples:
https://github.com/zarazhangrui/frontend-slides

## Troubleshooting

**Slides are scrolling:**
- Reduce content per slide
- Use `clamp()` for responsive font sizing
- Check that `overflow: hidden` is applied to `.slide`

**Animations are choppy:**
- Use CSS transforms instead of position changes
- Limit simultaneous animations to 3-4 elements
- Test on target devices

**Text is too small/large:**
- Verify `clamp()` values in CSS variables
- Adjust the middle value (viewport-based sizing)

## License

MIT License (see LICENSE file)

## Credits

Original framework by Zara Zhang Rui
Adapted for generic AI coding assistants

---

**Last Updated:** February 23, 2026
