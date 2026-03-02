# Insights: [rafaelbailo/betterposter-latex-template](https://github.com/rafaelbailo/betterposter-latex-template)

**~318 stars** · LaTeX · GPL-3.0 · [Overleaf template](https://www.overleaf.com/latex/templates/better-poster-latex-template/gmkgjvxqbyyt)

## What It Is

LaTeX implementation of **Mike Morrison's #betterposter** layout: one big main column (main finding + QR) and two side columns (intro/methods/results; supplementary). Designed to improve knowledge transfer and make poster sessions more effective.

## Actionable Takeaways

| Idea | How to use |
|------|------------|
| **Three-zone layout** | Main finding in the centre; methods/details on left; extra/supplementary on right. Reuse this structure in HTML or any template. |
| **QR code for paper** | Always add a QR linking to full paper or supplementary. Use `\qrcode{path}{icon}{caption}` or a compact variant. |
| **Theme colours** | empirical, theory, methods, intervention (and imperialblue). Define similar semantic colours in CSS/design system. |
| **Paper sizes** | `a0paper`, `a1paper`, `a2paper` as class options. Our export scripts can target the same dimensions. |
| **Customisation** | Column widths, margins, font sizes, and colours are set via `\setlength` and `\renewcommand` before `\begin{document}`. |

## Code to Borrow

- **Structure:** `\betterposter{ main }{ left }{ right }` and `\maincolumn{ main content }{ QR block }`.
- **Font control:** `\renewcommand{\fontsizemain}{\fontsize{28}{35} \selectfont}` (size and baselineskip).
- **Class usage:** `\documentclass[a0paper,fleqn]{betterposter}`.

## References

- [Mike Morrison's video](https://www.youtube.com/watch?v=1RwJbhkCA58) on the design.
- [#betterposter on Twitter](https://twitter.com/hashtag/betterposter).
- Original PowerPoint: link in repo README.
