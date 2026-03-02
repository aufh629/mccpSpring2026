# Inspiration from [palxiao/poster-design](https://github.com/palxiao/poster-design)

This document summarizes what we can learn from the **迅排设计 (Poster Design)** repo for our own poster-design work in MCCP pre2.

---

## 1. What the Repo Is

- **Online creative image / poster editor** (similar to 稿定设计).
- Use cases: posters, e-commerce share images, long-form article images, video/WeChat cover images.
- **Tech stack:** Vue 3, Vite 5, Pinia, Element Plus (frontend); Express (backend). Image output: **Puppeteer** (server) and **html2canvas** (client).

---

## 2. Architecture & Design Lessons

| Lesson | Detail |
|--------|--------|
| **DOM-based canvas** | The editor uses **native DOM** as the canvas (not Canvas/SVG only). Elements are HTML; this keeps styling with CSS, supports HTML5 features, and makes it easier to reuse existing UI components and export via html2canvas. |
| **Hybrid export** | **Frontend:** html2canvas for quick preview/cover thumbnails (lower scale, JPEG). **Backend:** Puppeteer for high-quality, pixel-accurate export. We can adopt the same split: fast client preview + server-side final image. |
| **Monorepo / packages** | Reusable parts live in `packages/` (e.g. `image-extraction` for matting, `color-picker`). Our poster scripts can be organized as small, focused modules (export, layout, assets). |
| **State & history** | Pinia stores for design state; history for undo/redo. For a simpler poster tool, we can still use a single store + a small history stack. |

---

## 3. Feature Ideas We Can Reuse

- **Element types:** Text, Image, SVG, QR code, Group. We can support at least text + image + group in a minimal version.
- **Export pipeline:** Clone the design DOM node → optional font loading (e.g. FontFaceObserver) → html2canvas with `useCORS: true` and scale from zoom → `canvas.toBlob()` for PNG/JPEG. Same pattern as in `CreateCover.vue`.
- **Backend export:** Service in `/service` uses Puppeteer for screenshots. We can run a small Node server that accepts HTML/URL and returns PNG for high-quality posters.
- **Libraries:** [moveable](https://github.com/daybrush/moveable) for drag/resize, [html2canvas](https://github.com/niklasvh/html2canvas) for client export, [qr-code-styling](https://qr-code-styling.com/) for QR codes. We can use the same stack in our scripts.

---

## 4. Technical Takeaways

1. **html2canvas options that matter:** `useCORS: true` for cross-origin images; `scale` to match zoom/DPI; `onclone` to copy fonts into the cloned document; `backgroundColor: null` for transparent PNG.
2. **Fonts:** Wait for fonts (e.g. FontFaceObserver) before calling html2canvas so text renders correctly in the exported image.
3. **Export flow:** Deselect widgets → set zoom (e.g. 100%) → clone design node → append to body → html2canvas → toBlob → cleanup. We can implement the same flow in our `posterScripts`.
4. **Docker:** They provide Docker Compose for frontend + API; we can add a similar setup later if we add a Puppeteer service.

---

## 5. What to Build in Our Demo

- **posterScripts:** Small scripts and templates that:
  - Generate or lay out a simple poster (HTML/CSS).
  - Export it with html2canvas (browser) or a minimal Puppeteer script (Node).
  - Optionally add QR code or basic text/image placeholders.
- **posterInspire.md:** This file — summary of what we learned and how we apply it.

---

## 6. Five more high-star academic poster repos

See **posterScripts/** subfolders for actionable insights and borrowed code from:

| Repo | Stars | Subfolder |
|------|-------|-----------|
| [rafaelbailo/betterposter-latex-template](https://github.com/rafaelbailo/betterposter-latex-template) | ~318 | `posterScripts/betterposter-latex/` |
| [LanaSina/better_poster_latex](https://github.com/LanaSina/better_poster_latex) | ~110 | `posterScripts/betterposter-portrait/` |
| [cpitclaudel/academic-poster-template](https://github.com/cpitclaudel/academic-poster-template) | ~92 | `posterScripts/html-poster/` |
| [overbool/poster](https://github.com/overbool/poster) | ~45 | `posterScripts/canvas-poster/` |
| [academic-templates/tex-poster-template](https://github.com/academic-templates/tex-poster-template) | ~7 | `posterScripts/tex-scientific/` |

Each subfolder has an **INSIGHTS.md** and templates/snippets you can use directly.

## 7. References (palxiao/poster-design)

- Repo: [github.com/palxiao/poster-design](https://github.com/palxiao/poster-design)
- Docs: [xp.palxp.cn](https://xp.palxp.cn/)
- Key files in repo: `README.md`, `src/components/business/save-download/CreateCover.vue`, `service/` (Puppeteer), `packages/image-extraction`, `packages/color-picker`
