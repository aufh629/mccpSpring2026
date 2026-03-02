# Beamer trial: paper → slides

**Objective.** Use Beamer to turn (a small part of) the paper into slides and document the process.

**Deliverable.** Process notes in `beamerWork.md` (in this folder).

---

## Trial scope (current): 3 slides only

- **Source:** Small part of the paper = title + abstract + opening of Introduction (motivation and key question).
- **Slides:**
  1. **Title** — Paper title, authors, affiliation.
  2. **Abstract** — Condensed summary (bullets or short paragraph).
  3. **Introduction (teaser)** — Motivation + key question (“Can a constrained OCO algorithm …?”) and “Our answer is yes.”
- **Goal:** Validate Beamer workflow and compile without paper-specific packages (no `aaai25.sty`, no `.bib` for this trial).

---

## File locations

| Role | Path |
|------|------|
| **Input paper** | `trial/paper/aaai25.tex` (AAAI 2025 article, ~1033 lines) |
| **Output slides** | `trial/beamerTry/` (e.g. `aaai25_3slides.tex`, `aaai25_3slides.pdf`) |
| **Process doc** | `trial/beamerTry/beamerWork.md` |

Shared assets (if needed): `trial/paper/` for `.bib`, figures, and `aaai25.sty`; copy or use relative paths as appropriate.

---

## Sub-tasks (order)

**For 3-slide trial:**
1. **Setup** – Create Beamer `.tex` in `beamerTry/` with standard packages only; confirm `pdflatex` works.
2. **Content** – Add exactly 3 frames: (1) title + authors, (2) abstract (condensed), (3) intro motivation + key question.
3. **Build** – Compile to PDF in `beamerTry/`.
4. **Document** – Write `beamerWork.md` with steps, decisions, issues.

**Later (full deck):** Structure full section map, port remaining sections, add `.bib`/figures as needed.

---

## Constraints

- **Slide count (trial):** Exactly 3 slides. (Full deck later: ~15–25 main slides.)
- **Style:** One Beamer theme (e.g. default, Madrid, Berlin); consistent font/size; readable math.
- **Scope:** Main body only for primary deck; proofs and appendix as backup slides or omitted.
- **Compatibility:** Paper uses `aaai25` document class and custom packages; Beamer file should not depend on `aaai25.sty`; reuse only standard/Beamer packages plus needed math/citations.

---

## What to put in `beamerWork.md`

- **Steps:** What you did (e.g. create `aaai25_slides.tex`, add frames per section, copy `.bib`/figures).
- **Decisions:** Section ↔ slide mapping, theme, what was shortened or dropped (e.g. full proofs).
- **Issues:** Compilation errors, missing dependencies, layout problems and how they were fixed.
- **Human input used:** Any manual edits, theme choice, or content cuts you asked a human to confirm.

---

## Paper section map (reference)

- §1 Introduction  
- §2 Related Work (OCO fixed / time-varying)  
- §3 Constrained Online Convex Optimization (assumptions, metrics, variation)  
- §4 COLDQ (virtual queue, Lyapunov drift, algorithm)  
- §5 Performance Bounds (regret & violation)  
- §6 Experiments (time-varying, fixed, job scheduling)  
- §7 Conclusions  
- §Appendix: proofs, experiment details → backup or skip
