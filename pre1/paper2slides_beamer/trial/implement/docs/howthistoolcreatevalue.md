# How This Tool Creates Value

**Context:** Paper2Slides implementation in `trial/implement/` — turning papers (PDF/HTML) into presentation slides with AI.

---

## 1. Value proposition

- **Time saving:** Reduces the step from “I have a paper” to “I have a first-draft slide deck.” The tool does RAG over the paper, summarization, and slide planning (and optionally image generation) so the human can edit and refine instead of starting from scratch.
- **Consistency:** Slide structure and content are derived from the same source (the paper), which helps keep the narrative aligned with the written contribution.
- **Iteration:** Supports quick previews (e.g. first section or first 3 pages) and checkpoint/resume, so users can try different styles or lengths without redoing everything.
- **Fallback:** When the image API is unavailable or fails, the text-only path (`plan2slides_text.py`) still delivers an outline and a minimal HTML deck, so the pipeline yields *something usable* rather than nothing.

---

## 2. Who benefits

- **Presenters:** Need to turn a paper into a talk (conference, seminar, defense). The tool produces a draft structure and content; the human adds emphasis, storytelling, and polish.
- **Instructors:** Want to build slides from a paper (e.g. for a reading group or course). Fast/short runs give a starting point for teaching-oriented slides.
- **Authors:** Want to see how their paper “translates” into bullets and sections before writing slides by hand or in Beamer/Reveal.

---

## 3. How value is created (pipeline)

1. **Input:** Paper as PDF or HTML (e.g. from arXiv). Optional limits: first section or first N pages for quick trials.
2. **RAG (or --fast):** Tool ingests and indexes the paper so later stages can retrieve relevant chunks. In `--fast` mode this is skipped for speed (e.g. for Poe without embeddings).
3. **Summary + plan:** An LLM summarizes the paper and produces a slide plan (sections, titles, bullet-level content). This is where most of the “understanding” and structure come from.
4. **Generate (when available):** An image-generation API produces one image per slide and assembles `slides.pdf`. **Currently failing** in this setup (see [whynotimage.md](whynotimage.md)); value today is mainly from the plan and text fallback.
5. **Text-only fallback:** If generate fails, `plan2slides_text.py` builds `slides_outline.md` and `slides_text.html` from the plan and RAG markdown — still a usable draft outline.

So value is created by **automating structure and first-draft content** from the paper, and by **degrading gracefully** to text-only when the image path is unavailable.

---

## 4. Where human input matters

- **API and environment:** Choosing provider, keys, base URL; resolving 401/HTML-response issues for image generation.
- **Decisions before running:** Length (short/medium/long), style (academic/doraemon/custom), content emphasis — see [seekHumanInput.md](seekHumanInput.md).
- **After generation:** Reviewing content accuracy, fixing chunk boundaries, adding math rendering (e.g. MathJax/KaTeX), converting to Beamer/Reveal, and adding speaker notes or narrative flow.
- **Quality bar:** The tool is a starting point; human judgment is required for correctness, emphasis, and presentation readiness (see [assessSlides.md](assessSlides.md)).

---

## 5. Limitations (and why they matter for value)

- **Image stage broken in this setup:** Until the image API returns valid JSON, the main deliverable is the plan + text-only slides, not a full visual deck. Value is “draft outline and content,” not “ready-to-present PDF.”
- **Shallow plan when LLM is limited:** If the plan stage uses a constrained or failing backend, sections stay generic (e.g. “Title”, “Content”); value is lower than with a rich, sectioned plan.
- **No equation rendering in text HTML:** Math appears as raw LaTeX/Unicode; value for math-heavy talks is limited until we add MathJax/KaTeX or export to Beamer/Reveal.
- **Chunk boundaries:** Splitting by character count can cut sentences; fixing this in `plan2slides_text.py` would improve readability and perceived quality.

---

## 6. Summary

| Dimension | How value is created |
|-----------|------------------------|
| **Efficiency** | First-draft slides from paper in minutes; quick previews with `--max-sections` / `--max-pages`. |
| **Consistency** | Content and structure tied to the same source (paper). |
| **Resilience** | Text-only fallback ensures a usable outline even when image generation fails. |
| **Iteration** | Checkpoints and different styles/lengths support experimentation. |
| **Human role** | Configuration, quality review, math/formatting, and narrative polish remain essential. |

The tool creates value by **reducing the distance from paper to draft slides** and by **failing gracefully** to a text outline when the full image pipeline is unavailable.
