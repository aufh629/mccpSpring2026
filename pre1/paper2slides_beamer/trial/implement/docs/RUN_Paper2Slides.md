# Run Paper2Slides (Setup Complete)

**Status**: Repo cloned, conda env `paper2slides` created, dependencies installed. **API key is never stored in repo** — configure locally (see below).

---

## Configure API key locally (no key in repo)

**You do not need an OpenAI key.** Use **OpenRouter** or **Poe** (OpenAI-compatible). Keys live only in gitignored files; never commit them. **Poe does not support embeddings** — use `--fast` so only chat completions are used (no RAG indexing).

1. Copy your key from **one** of (all gitignored): `openRouterKey.md`, `poeAPIkey.md`, or `HKBUkey.md` (in `trial/implement/`).
2. Edit `Paper2Slides/paper2slides/.env` and set:
   - `RAG_LLM_API_KEY="<paste-key>"`
   - `RAG_LLM_BASE_URL`:
     - **OpenRouter**: `https://openrouter.ai/api/v1`
     - **Poe**: `https://api.poe.com/v1` (use `--fast` only; Poe has no embeddings)
     - **Azure OpenAI**: `https://<resource-name>.openai.azure.com/openai/deployments/<deployment-name>` (e.g. from HKBUkey; set this manually)
   - `IMAGE_GEN_API_KEY="<paste-key>"` (same key if using one provider for both)
3. Save. Do not commit `.env` or any `*Key*.md` / `poeAPIkey.md` / `openRouterKey.md`; they are in `.gitignore`.

The entire `Paper2Slides/` clone is also gitignored so it is never pushed to GitHub.

---

## Quick run (preview)

From the **Paper2Slides** repo directory:

```bash
conda activate paper2slides
cd "/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026/pre1/paper2slides_beamer/trial/implement/Paper2Slides"

# Fast preview (short, no RAG indexing)
# Input must be PDF (Paper2Slides does not support .tex). Add aaai25.pdf to trial/paper/ first.
python -m paper2slides \
  --input "../../paper/aaai25.pdf" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

Output will be under: `Paper2Slides/outputs/...` (see terminal for exact path). Look for `slides.pdf` in the output folder.

---

## Full run (medium length, with RAG)

```bash
conda activate paper2slides
cd ".../trial/implement/Paper2Slides"

python -m paper2slides \
  --input "../../paper/aaai25.pdf" \
  --output slides \
  --content paper \
  --style academic \
  --length medium \
  --parallel 2
```

---

## Paths

- **Repo**: `trial/implement/Paper2Slides/`
- **Paper**: `trial/paper/aaai25.tex`
- **.env**: `Paper2Slides/paper2slides/.env` (set key locally; file and clone are gitignored)
