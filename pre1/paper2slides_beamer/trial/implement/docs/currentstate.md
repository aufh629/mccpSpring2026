# Current State of the Paper2Slides Implementation

**Last updated:** 2026-01-31  
**Folder:** `trial/implement/` (reorganized with subfolders)

---

## 1. Folder layout (after cleanup)

| Folder    | Purpose |
|-----------|--------|
| **implement/** (root) | Entry [README.md](README.md) and this layout. |
| **docs/** | All markdown: instructions, setup, API guides, assessments, [currentstate.md](currentstate.md), [howthistoolcreatevalue.md](howthistoolcreatevalue.md). |
| **scripts/** | Python: `download_html_from_arxiv.py`, `html2slides.py`, `plan2slides_text.py`. |
| **inputs/** | Input files for runs (e.g. `COCO_2310.18955v3_from_arxiv.html`). |
| **logs/** | Run logs (e.g. `COCO_paper2slides_run.log`). |
| **samples/** | Sample outputs (e.g. `slidesHTML.html`). |
| **Paper2Slides/** | Cloned repo (gitignored); run `python -m paper2slides` from here. |

---

## 2. What is in place

- **Paper2Slides** cloned under `implement/Paper2Slides/`; conda env `paper2slides` with dependencies installed.
- **API configuration:** Keys in gitignored files (e.g. `docs/bltkey.md`); copied into `Paper2Slides/paper2slides/.env`. See [INSTRUCTIONS.md](INSTRUCTIONS.md) and API-related docs in `docs/` (e.g. BLTKEY_API, HK_NON_OPENAI, OPENROUTER_401_FIX).
- **Inputs:** COCO paper as HTML in `inputs/COCO_2310.18955v3_from_arxiv.html`; can also use PDF (e.g. first 3 pages).
- **Runs:** Quick runs (first section only, or first 3 pages) and full-paper runs are documented in [INSTRUCTIONS.md](INSTRUCTIONS.md) and [RUN_Paper2Slides_COCO.md](RUN_Paper2Slides_COCO.md).
- **Text-only fallback:** When the image stage fails, `scripts/plan2slides_text.py` produces `slides_outline.md` and `slides_text.html` from the plan checkpoint and RAG markdown (output under the run’s config dir, e.g. `.../text_slides/`).
- **Assessment:** [assessSlides.md](assessSlides.md) evaluates the COCO text-only slides (content fidelity, structure, weaknesses, recommendations).

---

## 3. What works

- **RAG + summary + plan:** Paper2Slides runs with HTML or PDF input; RAG (or `--fast` without full RAG), summary, and plan stages complete when the LLM API is correctly configured.
- **Short runs:** `--max-sections 1` (first section) or `--max-pages 3` for quick previews.
- **Text-only output:** `plan2slides_text.py` reliably builds a minimal outline and HTML deck from the plan/RAG data when image generation is unavailable or fails.
- **Documentation:** Setup, run, API, and troubleshooting docs are in `docs/`.

---

## 4. What does not work (or is limited)

- **Image generation:** The **generate** stage (one image per slide → `slides.pdf`) fails in current setup:
  - **Poe:** 401 “No cookie auth credentials”; not suitable as image backend.
  - **GPT-Best (bltkey):** Server returns HTML (e.g. Apifox page) instead of JSON; client expects `response.choices` → stage fails.
  See [whynotimage.md](whynotimage.md).
- **Text-only limitations:** Chunk boundaries can split sentences; no equation rendering (raw LaTeX/Unicode); only generic sections (e.g. “Title”, “Content”) when plan is minimal. See [assessSlides.md](assessSlides.md).
- **LaTeX source:** Paper2Slides does not accept `.tex` directly; use PDF or (for this trial) HTML from arXiv.

---

## 5. Outputs produced so far

- **Paper2Slides run output:** Under `Paper2Slides/outputs/COCO_2310.18955v3_from_arxiv/paper/fast/slides_academic_short_1sec/` (or similar): checkpoints, RAG/summary/plan data, and (when text fallback is run) `text_slides/slides_outline.md` and `slides_text.html`.
- **Logs:** `logs/COCO_paper2slides_run.log`.
- **Sample HTML:** `samples/slidesHTML.html` (from `html2slides.py`, separate from Paper2Slides).

---

## 6. Next steps (concise)

1. **Fix or replace image backend** so the generate stage returns valid API JSON (e.g. OpenRouter with an image-capable model, or correct GPT-Best image endpoint).
2. **Improve text fallback:** In `plan2slides_text.py`, split by sentences/paragraphs instead of fixed character count; optionally add MathJax/KaTeX for HTML.
3. **Stronger plan stage:** Use a working LLM so the plan has clear sections (e.g. Motivation, Method, Results) and feed that into the text-only path.
4. **Optional:** Beamer/Reveal.js export from the outline for presentation-ready slides with math support.

---

**Summary:** Implementation is organized; RAG/summary/plan and text-only fallback work. Image-based slides are blocked by API/backend issues; improving chunking, plan quality, and math rendering would make the text-only output more useful for actual talks.
