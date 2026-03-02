# Paper2Slides Setup – Do We Need to Clone?

**Short answer: Yes.** Paper2Slides is **not** on PyPI. You must clone the repo and run it from there.

**Security:** API keys are never stored in this repo or synced to GitHub. The key lives only in `openRouterKey.md` (gitignored) and in your local `Paper2Slides/paper2slides/.env`. The entire `Paper2Slides/` clone is gitignored so it is never pushed.

---

## Why clone?

- Paper2Slides is only distributed via GitHub (https://github.com/HKUDS/Paper2Slides).
- There is no `pip install paper2slides` package.
- You run it as `python -m paper2slides` **from inside the cloned repo** (or with `PYTHONPATH` set to the repo).

---

## Minimal setup (clone + env + API)

### 1. Clone the repo

Pick one location; then use that path in the commands below.

**Option A – Clone inside `implement/` (recommended)**

```bash
cd "/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026/pre1/paper2slides_beamer/trial/implement"

git clone https://github.com/HKUDS/Paper2Slides.git
cd Paper2Slides
```

**Option B – Clone elsewhere (e.g. home or projects)**

```bash
cd ~  # or any folder you prefer
git clone https://github.com/HKUDS/Paper2Slides.git
cd Paper2Slides
```

### 2. Create conda env and install

```bash
conda create -n paper2slides python=3.12 -y
conda activate paper2slides
pip install -r requirements.txt
```

### 3. Configure API key

- Copy: `paper2slides/.env.example` → `paper2slides/.env`
- Edit `paper2slides/.env` and add your keys (e.g. OpenRouter key from `../openRouterKey.md` in the paper2slides_beamer folder).

### 4. Run from the **Paper2Slides** repo directory

You must be in the cloned repo (or have it on `PYTHONPATH`) so that `python -m paper2slides` works. Example for **Option A** (repo inside `implement/`):

```bash
# You are in: .../trial/implement/Paper2Slides
conda activate paper2slides

# Input: paper in trial/paper/
# Use absolute path or path relative to current dir
python -m paper2slides \
  --input "../paper/aaai25.tex" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

If you cloned elsewhere (Option B), use the full path to the paper:

```bash
python -m paper2slides \
  --input "/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026/pre1/paper2slides_beamer/trial/paper/aaai25.tex" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

Output will appear under the Paper2Slides repo (e.g. `outputs/...`). You can copy the generated PDF/slides into `implement/` if you want them next to your trial files.

---

## Summary

| Question | Answer |
|----------|--------|
| Do we need to clone the repo? | **Yes** |
| Can we pip install it? | **No** |
| Where do we run the command? | From the **cloned repo** directory (or with repo on PYTHONPATH) |
| Where to put the clone? | Anywhere; cloning inside `trial/implement/` keeps everything together. |

After cloning once, you only need to `conda activate paper2slides` and run the `python -m paper2slides` command from the repo directory to generate slides.
