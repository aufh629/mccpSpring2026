# Paper2Slides — Instructions Summary

**Folder**: `trial/implement/` (subfolders: `docs/`, `scripts/`, `inputs/`, `logs/`, `samples/`, `Paper2Slides/`)  
**Goal**: Turn the COCO paper (HTML or PDF) into slides using Paper2Slides in `Paper2Slides/`.

---

## 1. Prerequisites

- **Conda**: `conda activate paper2slides` (see [SETUP_Paper2Slides.md](SETUP_Paper2Slides.md)).
- **API key**: Set in `Paper2Slides/paper2slides/.env` — see [API_KEYS.md](API_KEYS.md).
- **Dependencies**: `cd Paper2Slides && pip install -r requirements.txt`

---

## 2. API keys and base URL

Keys live in **gitignored** files under `docs/` (e.g. `bltkey.md`); never commit them.

| Provider   | Key file         | Base URL / extra step |
|-----------|-------------------|-------------------------|
| **Poe**   | `poeAPIkey.md`    | `RAG_LLM_BASE_URL="https://api.poe.com/v1"` — use `--fast` only (no embeddings). |
| **OpenRouter** | `openRouterKey.md` | `RAG_LLM_BASE_URL="https://openrouter.ai/api/v1"` |
| **Azure (HKBU)** | `HKBUkey.md`   | Put endpoint in `HKBUbaseURL.md` (one line) or in `.env` as `RAG_LLM_BASE_URL`. Then run `cd Paper2Slides/paper2slides && python3 set_env_key_from_hkbu.py`. |
| **GPT-Best (Apifox)** | `bltkey.md` | Run `cd Paper2Slides/paper2slides && python3 set_env_key_from_blt.py` (sets key + base URL). |

Copy the key into `Paper2Slides/paper2slides/.env` as `RAG_LLM_API_KEY="..."` and set `RAG_LLM_BASE_URL` as above. Helpers: `set_env_key_from_poe.py`, `set_env_key_from_hkbu.py`, `set_env_key_from_blt.py` (in `Paper2Slides/paper2slides/`).

---

## 3. Quick runs (from `implement/`)

**First section only (HTML, fastest):**
```bash
conda activate paper2slides
cd Paper2Slides
python -m paper2slides --input "../inputs/COCO_2310.18955v3_from_arxiv.html" --output slides --content paper --style academic --length short --fast --max-sections 1
```

**First 3 pages only (PDF):**
```bash
cd Paper2Slides
python -m paper2slides --input "../inputs/COCO_2310.18955v3.pdf" --output slides --content paper --style academic --length short --fast --max-pages 3
```

**Full paper (HTML):**
```bash
cd Paper2Slides
python -m paper2slides --input "../inputs/COCO_2310.18955v3_from_arxiv.html" --output slides --content paper --style academic --length short --fast
```

Always use `--fast` with Poe (Poe has no embeddings). Omit `--max-sections` or `--max-pages` for the full document.

---

## 4. Output

- **Base**: `Paper2Slides/outputs/<project>/paper/`
- **Config dir**: e.g. `.../fast/slides_academic_short/` or `.../slides_academic_short_1sec/` (when using `--max-sections 1`).
- **Image slides**: Inside the config dir, in a timestamped subfolder (`slides.pdf` + per-section images). Requires a working **image-generation API** (e.g. OpenRouter with image model).
- **Text-only slides** (when image API fails or is unavailable): From `implement/` run  
  `python3 scripts/plan2slides_text.py [config_dir]`  
  (default config_dir = `Paper2Slides/outputs/COCO_2310.18955v3_from_arxiv/paper/fast/slides_academic_short_1sec`).  
  Output: `.../text_slides/slides_outline.md` and `slides_text.html`.

Use `cd Paper2Slides && python -m paper2slides --list` to list outputs.

---

## 5. Other docs

| File | Purpose |
|------|--------|
| [RUN_Paper2Slides.md](RUN_Paper2Slides.md) | Configure API key, quick/full run (generic). |
| [RUN_Paper2Slides_COCO.md](RUN_Paper2Slides_COCO.md) | COCO paper: HTML/PDF input, first section / first 3 pages. |
| [SETUP_Paper2Slides.md](SETUP_Paper2Slides.md) | Clone, conda env, dependencies. |
| [API_KEYS.md](API_KEYS.md) | Key files and .env reference (no secrets). |
| [SLIDES_HTML.md](SLIDES_HTML.md) | Simple HTML slides from `html2slides.py` (no Paper2Slides). |
