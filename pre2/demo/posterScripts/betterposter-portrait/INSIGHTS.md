# Insights: [LanaSina/better_poster_latex](https://github.com/LanaSina/better_poster_latex)

**~110 stars** · LaTeX · CC0-1.0 · Portrait-only Better Poster · [Overleaf](https://www.overleaf.com/latex/templates/better-poster-for-scientific-presentation/xpcssnwsgwqp)

## What It Is

Another LaTeX implementation of Mike Morrison's Better Poster, with **portrait** layout and a simpler command set: `\makefinding`, `\makemain`, `\makeextracolumn`, `\makefooter`.

## Actionable Takeaways

| Idea | How to use |
|------|------------|
| **Portrait option** | When space is vertical (e.g. narrow boards), use portrait; our HTML template can switch via CSS or a single class. |
| **Poster type** | `exp` (experimental), `methods`, `theory` — maps to colour themes. We can add a `data-theme` or class in HTML. |
| **Two-column main** | `\begin{multicols}{2}` inside `\makemain` for intro/methods/results. Replicate with CSS grid or columns. |
| **Compact lists** | `\begin{compactitem}` keeps bullets tight. Use a `.compact-list` CSS class with reduced spacing. |
| **Footer** | Logo + QR in footer (`\makefooter{logo}{qr}` or `\makealtfooter` for QR on right). Standardise in all our templates. |

## Code to Borrow

- **Skeleton:** `\postersize{a0paper}`, `\title{}`, `\author{}`, `\newcommand\postertype{exp}`.
- **Finding:** `\makefinding{ \textbf{Main finding} here. }`.
- **Main body:** `\makemain{ \raggedcolumns \begin{multicols}{2} ... \end{multicols} }`.
- **Extra column:** `\makeextracolumn{ supplementary content }`.
- **Footer:** `\makefooter{images/uni_logo.png}{images/qr-code.png}`.

## References

- Same design rationale as rafaelbailo; portrait variant.
- Original PowerPoint: [osf.io/vxqr6](https://osf.io/vxqr6/).
