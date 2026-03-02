# Ready to Turn Paper into Slides?

**Short answer:** Almost. You need the paper as a **PDF** for Paper2Slides to run successfully.

---

## What’s in place

- **Paper2Slides** cloned and set up under `trial/implement/Paper2Slides/`
- **Conda env** `paper2slides` with dependencies installed (`python -m pip install -r requirements.txt`)
- **OpenRouter** configured in `Paper2Slides/paper2slides/.env` (same key for RAG and image gen)
- **Paper sources** in `trial/paper/`: `aaai25.tex`, `aaai25.bbl`, `aaai25.sty`, `aaai25.md`, and figure PDFs

---

## What Paper2Slides accepts

- **Supported:** PDF, .docx, .pptx, .xlsx, images, .txt, .md  
- **Not supported:** `.tex` (LaTeX source)  
- **In practice:** Using `aaai25.md` failed during the tool’s internal text→PDF step (parse error). So for this project, **PDF is the reliable input**.

---

## What you need to do

**Provide a single PDF of the full paper** (e.g. `aaai25.pdf`) in `trial/paper/`.

### Option A: Compile locally (if you have LaTeX)

```bash
cd trial/paper
pdflatex aaai25.tex
bibtex aaai25
pdflatex aaai25.tex
pdflatex aaai25.tex
```

Then run Paper2Slides on `../../paper/aaai25.pdf`.

### Option B: Compile elsewhere

- Use **Overleaf** (upload `aaai25.tex` + `aaai25.bbl` + `aaai25.sty`, compile, download PDF), or  
- Any other LaTeX setup that produces `aaai25.pdf`.

Put the downloaded `aaai25.pdf` in `trial/paper/`.

### Option C: You already have the PDF

If you have the camera-ready or preprint PDF of the COLDQ paper, copy it to:

`trial/paper/aaai25.pdf`

---

## Run Paper2Slides (after PDF is in place)

From the Paper2Slides repo directory:

```bash
conda activate paper2slides
cd ".../trial/implement/Paper2Slides"

# Fast preview (short slides)
python -m paper2slides \
  --input "../../paper/aaai25.pdf" \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast

# Or full run (medium length, with RAG)
python -m paper2slides \
  --input "../../paper/aaai25.pdf" \
  --output slides \
  --content paper \
  --style academic \
  --length medium \
  --parallel 2
```

Output will be under `Paper2Slides/outputs/aaai25/paper/.../output/` (including `slides.pdf`).

---

## Summary

| Item              | Status |
|-------------------|--------|
| Paper2Slides set up | Yes   |
| Conda env & deps  | Yes   |
| OpenRouter key    | Yes (in local .env) |
| Paper as PDF      | **No – add `aaai25.pdf` to `trial/paper/`** |

Once `trial/paper/aaai25.pdf` exists, you’re ready to turn the paper into slides with the commands above.
