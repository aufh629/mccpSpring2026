# Run Paper2Slides on COCO paper (HTML input)

**Paper**: COCO 2310.18955 — "Optimal Algorithms for Online Convex Optimization with Adversarial Constraints"  
**Input**: `COCO_2310.18955v3_from_arxiv.html` (arxiv LaTeXML HTML)  
**Tool**: Paper2Slides in `Paper2Slides/`

Paper2Slides now accepts **HTML** input: the RAG stage converts the HTML to markdown and runs the same pipeline (RAG queries → summary → plan → generate slides).

---

## Prerequisites

1. **Conda env** (from `SETUP_Paper2Slides.md`):
   ```bash
   conda activate paper2slides
   ```

2. **API key** in `Paper2Slides/paper2slides/.env`:
   - `RAG_LLM_API_KEY` — copy from `poeAPIkey.md`, `openRouterKey.md`, or `HKBUkey.md` (Azure; all gitignored).
   - `RAG_LLM_BASE_URL` — Poe: `https://api.poe.com/v1`; OpenRouter: `https://openrouter.ai/api/v1`; **Azure**: put your endpoint in `HKBUbaseURL.md` (one line; gitignored) and run `python3 set_env_key_from_hkbu.py`, or set manually in `.env`. See `RUN_Paper2Slides.md`.
   - **Poe**: use `--fast` only (no embeddings). OpenRouter and Azure support both.

3. **Dependencies** (includes `beautifulsoup4` for HTML):
   ```bash
   cd Paper2Slides && pip install -r requirements.txt
   ```

---

## Quick run (HTML → slides)

From **this folder** (`trial/implement`):

```bash
conda activate paper2slides
cd Paper2Slides

# Input: HTML file (one level up)
python -m paper2slides \
  --input "../COCO_2310.18955v3_from_arxiv.html" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

## Quick try: first section only (HTML, faster)

Use only the first section (e.g. Introduction) for a quick run:

```bash
cd Paper2Slides
python -m paper2slides \
  --input "../COCO_2310.18955v3_from_arxiv.html" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast \
  --max-sections 1
```

Omit `--max-sections` for the full paper.

## Quick try: first 3 pages only (PDF, faster)

To avoid long runs, use **PDF** input and limit to the first 3 pages:

```bash
cd Paper2Slides
python -m paper2slides \
  --input "../COCO_2310.18955v3.pdf" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast \
  --max-pages 3
```

This parses only pages 1–3, so RAG and later stages are much faster. Omit `--max-pages` for the full PDF.

Or with **absolute path** to the HTML:

```bash
python -m paper2slides \
  --input "/path/to/trial/implement/COCO_2310.18955v3_from_arxiv.html" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

---

## Output

- **Base dir**: `Paper2Slides/outputs/COCO_2310.18955v3_from_arxiv/paper/`
- **Config dir**: `.../fast/slides_academic_short/` (or similar)
- **Slides**: `.../slides_academic_short/<timestamp>/` — look for generated slide files (e.g. Markdown or HTML/PDF depending on generator stage).

Use `--list` to list existing outputs:

```bash
cd Paper2Slides
python -m paper2slides --list
```

---

## Options

| Option       | Example   | Description                    |
|-------------|-----------|--------------------------------|
| `--input`   | `../COCO_2310.18955v3_from_arxiv.html` | HTML (or PDF) input |
| `--output`  | `slides`  | Output type: slides or poster  |
| `--content` | `paper`   | Content type                   |
| `--style`   | `academic`| academic / doraemon / custom   |
| `--length`  | `short`   | short / medium / long          |
| `--fast`    | (flag)   | Fast mode: no RAG indexing, direct LLM on markdown |

For HTML input, the pipeline converts the file to markdown first, then runs the same RAG (fast) and generate stages as for PDF.

**Note**: Later stages (summary, plan, generate) require the full Paper2Slides env (e.g. `lightrag`). Install all deps: `pip install -r requirements.txt` in the Paper2Slides repo.
