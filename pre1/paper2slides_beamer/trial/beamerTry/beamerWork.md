# Beamer work log: 3-slide trial

## Scope

- **Source:** Small part of `trial/paper/aaai25.tex` — title, abstract, and opening of Introduction (motivation + key question).
- **Output:** Exactly 3 slides: (1) Title, (2) Abstract, (3) Introduction teaser.

---

## Steps

1. **Revised plan** — Updated `plan.md` with a "Trial scope" section: 3 slides only; file names `aaai25_3slides.tex` / `aaai25_3slides.pdf`.
2. **Created Beamer file** — `aaai25_3slides.tex` in `trial/beamerTry/`:
   - `\documentclass{beamer}`, theme Madrid, packages `amsmath`, `amssymb` only (no `aaai25.sty`, no `.bib`).
   - **Slide 1:** `\titlepage` with paper title, authors (Juncheng Wang, Bingjie Yan, Yituo Liu), affiliation (HKBU CS).
   - **Slide 2:** Frame "Abstract" with bullet summary of problem (time-varying constrained OCO, hard violation), algorithm (COLDQ, doubly-bounded queue), main bounds ($\mathcal{O}(T^{(1+V_x)/2})$ regret, $\mathcal{O}(T^{V_g})$ violation), strongly convex and expert-tracking, experiments.
   - **Slide 3:** Frame "Introduction (teaser)" with motivation (gap between fixed vs time-varying bounds), key question (smooth approach to $\mathcal{O}(T^{1/2})$ and $\mathcal{O}(1)$?), and "Our answer: Yes — COLDQ."
3. **Build** — Ran `pdflatex aaai25_3slides.tex` in `beamerTry/`. **Result:** `pdflatex` not found in environment (LaTeX not installed or not in PATH). The `.tex` is ready; user can compile locally with:
   ```bash
   cd trial/beamerTry && pdflatex aaai25_3slides.tex
   ```

---

## Decisions

- **Theme:** Madrid (readable, common for talks).
- **No citations:** Omitted `\cite{}` and `.bib` for this trial to avoid dependency on paper’s bibliography.
- **Abstract:** Condensed into 5 bullets instead of one long paragraph.
- **Intro:** Only motivation + key question + one-line answer; no related work or contributions list.

---

## Issues

- **LaTeX not in PATH:** Build was not run in this environment. User needs TeX (e.g. MacTeX) installed and `pdflatex` on PATH to generate `aaai25_3slides.pdf`.

---

## Human input used

- None for this trial (scope and 3-slide choice were given in the task).
