# Suggested structure for a scientific poster project

Based on academic-templates/tex-poster-template. Use the same layout for LaTeX or for an HTML/CSS poster project.

```
your-poster/
├── main.tex          # or index.html / poster.html (single entry)
├── fonts/            # optional: custom fonts
├── imgs/              # figures, logos, QR code
│   ├── logo.png
│   └── qr-code.png
├── parts/             # optional: bibliography, data
│   └── bibliography.bib
├── styles/            # layout and theme (don’t edit unless customising)
│   └── poster.sty     # or poster.css
└── README.md          # “Parts to adapt: main.tex, parts/, imgs/”
```

## Build

- **LaTeX:** `latexmk -pdf -xelatex -use-make main.tex` → `main.pdf`
- **HTML:** Open `main.html` or run `node export-node.js` with path to `main.html` → PNG/PDF

## Parts you should adapt

1. **main.tex** (or main HTML): title, authors, sections, figure paths.
2. **parts/bibliography.bib**: references, if any.
3. **imgs/**: add your figures and replace paths in main file.
