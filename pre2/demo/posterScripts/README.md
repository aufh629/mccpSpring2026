# posterScripts

Scripts and files for designing and exporting posters, inspired by [palxiao/poster-design](https://github.com/palxiao/poster-design) and **5 additional high-star academic poster repos** (see subfolders below).

## Root-level files

| File / folder | Purpose |
|---------------|--------|
| `export-poster.html` | Single-file demo: simple poster layout + **html2canvas** export in the browser. Open in a browser, edit content if needed, click "Export PNG" to download. |
| `poster-template.html` | Minimal HTML/CSS poster template (title, subtitle, optional image/QR placeholder). Use as starting point for your design. |
| `export-node.js` | Node script using **Puppeteer** to render an HTML file and save a PNG (high-quality export). Run with Node after `npm install puppeteer`. |

## Subfolders: 5 repos → actionable insights

Each subfolder contains an **INSIGHTS.md** (lessons + code to borrow) and **actionable files** (templates, snippets, or config).

| Subfolder | Repo | Stars | What you get |
|-----------|------|-------|--------------|
| **betterposter-latex** | [rafaelbailo/betterposter-latex-template](https://github.com/rafaelbailo/betterposter-latex-template) | ~318 | Better Poster LaTeX layout; `example-minimal.tex` skeleton. |
| **betterposter-portrait** | [LanaSina/better_poster_latex](https://github.com/LanaSina/better_poster_latex) | ~110 | Portrait Better Poster; `skeleton.tex` with `\makefinding`, `\makemain`, `\makefooter`. |
| **html-poster** | [cpitclaudel/academic-poster-template](https://github.com/cpitclaudel/academic-poster-template) | ~92 | HTML+CSS accessible poster; `poster-basic.html` with grid layout and CSS variables. |
| **canvas-poster** | [overbool/poster](https://github.com/overbool/poster) | ~45 | Config-driven JS poster; `INSIGHTS.md` + `config-example.js` for title/content/style + export callback. |
| **tex-scientific** | [academic-templates/tex-poster-template](https://github.com/academic-templates/tex-poster-template) | ~7 | Classic scientific poster structure; `INSIGHTS.md` + `STRUCTURE.md` for folders and build. |

## Quick start (browser export)

1. Open `export-poster.html` in a browser (or serve via a local server if you hit CORS).
2. Click **Export PNG** to download the poster as an image.

## Quick start (Node export)

```bash
cd posterScripts
npm install puppeteer
node export-node.js
```

This will generate `output-poster.png` from the built-in HTML template.

## Customization

- Edit the HTML inside `export-poster.html` or the template in `export-node.js` to change layout, text, and styles.
- For html2canvas: options (scale, useCORS, backgroundColor) are set in the script; see `../posterInspire.md` for details.
