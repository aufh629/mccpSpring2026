# Insights: [cpitclaudel/academic-poster-template](https://github.com/cpitclaudel/academic-poster-template)

**~92 stars** · HTML + CSS (LESS) + Jinja2 · Accessible, responsive

## What It Is

An **HTML+CSS** academic poster template. No LaTeX or PowerPoint: semantic HTML, responsive layout, and reader-adjustable font size. Renders to PDF via print or headless browser. [Live example](https://cpitclaudel.github.io/academic-poster-template/koika/poster.html) · [Tutorial](https://cpitclaudel.github.io/academic-poster-template/tutorial/poster.html).

## Actionable Takeaways

| Idea | How to use |
|------|------------|
| **HTML-first** | Use semantic tags: `<header>`, `<main>`, `<article>`, `<figure>`, `<footer>`. Better for accessibility and our html2canvas/Puppeteer pipeline. |
| **CSS variables** | LESS vars for colours (Tango palette), column count, min/max width, spacing. We can use CSS custom properties in our templates. |
| **Responsive grid** | `display: grid` / `flex` with `@media` for wide vs narrow. Poster works on screen and print; we can add a “poster” media query for fixed dimensions. |
| **Accessibility** | Font-size adjustment, contrast, structure. Keep this in mind for any web poster we generate. |
| **Jinja2** | Template has `poster.jinja2` and `render.py` for variable injection. We can use the same pattern (e.g. Node/JS template) for title, authors, blocks. |

## Code to Borrow

- **Layout:** `main` as flex/grid with `flex-wrap`; items have `min-width` / `max-width` for column control.
- **Article blocks:** Each section as `<article>` with `<header>` (section title) and content; accent colour for headers.
- **Spacing:** `@thin-space`, `@mid-space`, `@thick-space` (e.g. 0.25rem, 0.5rem, 0.75rem).
- **Lists:** Custom list style with `::before` for bullets (e.g. coloured circle); optional `.inline` for horizontal lists.

## References

- Repo: `poster.less`, `poster.jinja2`, `render.py`, `Makefile`.
- Use our `export-poster.html` or Puppeteer to export this HTML to PNG/PDF.
