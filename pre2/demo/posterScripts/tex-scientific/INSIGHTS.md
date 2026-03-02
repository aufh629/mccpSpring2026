# Insights: [academic-templates/tex-poster-template](https://github.com/academic-templates/tex-poster-template)

**~7 stars** · LaTeX · CC-BY-4.0 · Classic scientific layout

## What It Is

A **traditional scientific poster** template in LaTeX: clear structure with `main.tex`, separate folders for **fonts**, **imgs**, **parts** (e.g. bibliography), and **styles**. Easy to configure and fill in; inspired by Jacobs University and ICTEAM poster templates.

## Actionable Takeaways

| Idea | How to use |
|------|------------|
| **Folder structure** | `doc/` or `src/`, `fonts/`, `imgs/`, `parts/`, `styles/`. We can mirror this in posterScripts: e.g. `assets/fonts`, `assets/imgs`, `styles/`. |
| **Single main file** | One `main.tex` that includes payload; minimal editing surface. Our HTML poster can be one `poster.html` that includes partials or CSS. |
| **Compilation** | `latexmk -pdf -xelatex -use-make %.tex` (e.g. in Texmaker). For our stack: one command to build (e.g. `npm run export`). |
| **Bibliography** | `parts/bibliography.bib` kept separate. For web posters, we can have a `references.json` or a small refs section in the template. |
| **Styles untouched** | Layout in `styles/`; user only edits main + content + images. Same idea: theme in one file, content in another. |

## Code to Borrow

- **Project layout:** Always separate: one entry file, assets, styles, optional data.
- **Documentation:** README with “Parts to adapt” (main.tex, bibliography, images). We list the same in each subfolder README.
- **Related templates:** Link to other academic-templates (book, slideshow, etc.) for consistency. We cross-link our posterScripts subfolders.

## References

- Repo: `main.tex`, `doc/`, `src/`, `fonts/`, `imgs/`, `parts/`, `styles/`.
- [Jacobs University template](https://teamwork.jacobs-university.de:8443/confluence/display/CoPandBiG/LaTeX+Poster); [Nathaniel Johnston](https://www.nathanieljohnston.com); [ICTEAM poster](https://github.com/UCL-INMA/ICTEAMposter).
