# How This Tool Creates Value — First Principles

**Scope:** Paper2Slides-Beamer — turning a paper into presentation slides. Two paths: (1) **Paper2Slides** (AI pipeline), (2) **Beamer** (template + human content).

---

## 1. First principles

| Principle | Meaning |
|-----------|--------|
| **Problem** | Going from “I have a paper” to “I have slides” is slow: choose structure, condense, keep math correct, keep narrative faithful. |
| **Value** | Shorten that path and keep output tied to the paper — a usable first draft instead of a blank page. |
| **Mechanism** | Either **automate** structure and first-draft content (AI), or **constrain** the task with a fixed format and clear steps (Beamer + human). Both rely on **human judgment** for correctness, emphasis, and readiness. |

So: value = **reducing time and effort from paper to draft slides**, without replacing the human’s role for quality and narrative.

---

## 2. Two paths — AI vs no-AI

| Path | What it is | AI used? | Main human input |
|------|------------|----------|-------------------|
| **Paper2Slides** | Pipeline: paper (PDF/HTML) → RAG + LLM → slide plan (+ optional images) → HTML/outline. | **Yes.** LLM for summary and slide plan; optional image API. | Config (API, style, length), then **review and edit** output (fix content, math, flow). |
| **Beamer** | **Outline first**, then human (or AI-assisted) picks content from the paper and writes a Beamer `.tex`; compile to PDF. | **Optional.** The Beamer file itself is just LaTeX. Content can be written by human only, or drafted by AI and edited by human. | **Outline** (slide structure), **content choice** (what goes on each slide), **wording**, **math**, theme; **compile** (needs local LaTeX). |

**Summary:** Paper2Slides is an AI tool with a clear human-review step. Beamer is a format and workflow; AI is only involved if you use it to draft bullets or structure — the core value is “clear template + your content.”

---

## 3. Where value comes from (by path)

**Paper2Slides (AI path)**  
- **Efficiency:** First-draft structure and text in minutes.  
- **Consistency:** Plan and content come from the same source (the paper).  
- **Human input:** Set length/style, check facts and math, add emphasis and story. Value is **draft + human refinement**.

**Beamer (template path)**  
- **Control:** You choose every slide and phrase; no black box.  
- **Quality:** Math and layout are predictable (LaTeX/Beamer).  
- **Beautiful slides:** Themes, colorthemes, and font themes give a professional, consistent look; layout tips (one idea per slide, blocks, whitespace) keep slides readable.  
- **Human input:** Decide section→slide mapping (via an outline first), condense text, paste or type into `.tex`. Value is **your choices + a reliable, good-looking format**.

---

## 4. Human input — what must come from you

| Stage | Paper2Slides | Beamer |
|-------|--------------|--------|
| **Before** | Choose paper, style (academic/etc.), length; configure API if used. | Choose paper, scope (e.g. 3 slides vs full deck); **generate slide outline** (sections + slide-by-slide plan); choose theme and style for beautiful slides. |
| **During** | — (pipeline runs). | **Follow outline**; select and condense content; write or paste into `.tex` (or edit AI-drafted text). |
| **After** | Check correctness, fix chunking/math, add narrative, optionally export to Beamer/Reveal. | Compile (LaTeX), fix errors, tweak layout and wording. |

**Common to both:** The **final say** on correctness, emphasis, and “ready to present” is human. The tool gives a **starting point** or **structure**, not a finished talk.

---

## 5. One-sentence summary

- **Paper2Slides:** AI produces a first-draft slide plan (and optionally visuals); **human input** configures the run and then reviews/edits for accuracy and narrative.  
- **Beamer:** You **first generate a slide outline** (sections and slide-by-slide plan), then put paper content into a Beamer `.tex`; **human input** is outline design, content selection, wording, theme/beauty choices, and compilation.  

**First principle:** Value = **faster path from paper to draft slides** with **human in the loop** for quality; AI is optional in the Beamer path, central in the Paper2Slides path.
