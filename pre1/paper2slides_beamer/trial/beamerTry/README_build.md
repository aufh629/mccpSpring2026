# How to read the .tex and generate PDF

## If extensions still don’t build or show PDF

**Likely cause:** No LaTeX distribution is installed (e.g. `pdflatex` not found). Extensions need LaTeX to compile.

**Quick fix (no install):** Use [Overleaf](https://overleaf.com) → New Project → Blank Project → paste the contents of `aaai25_3slides.tex` → Recompile → download the PDF.

**To use extensions locally:** Install a LaTeX distribution (e.g. MacTeX or `brew install --cask mactex-no-gui` on macOS), then restart Cursor. After that, LaTeX Workshop / Previewer can build and view the PDF.

---

## Reading the .tex file

- **In an editor:** Open `aaai25_3slides.tex` in Cursor, VS Code, or any text editor. It’s plain text.
- **Structure:** Each slide is a `\begin{frame}...\end{frame}` block. Commands like `\title`, `\item`, `\textbf{}` define the content you see on the slide.

## Generating the PDF

You need a **LaTeX distribution** installed. Then compile the .tex file.

### Option A: Command line (macOS / Linux)

1. Install LaTeX (if not already):
   - **macOS:** [MacTeX](https://tug.org/mactex/) (large) or `brew install --cask mactex-no-gui` (smaller).
   - **Linux:** `sudo apt install texlive-latex-extra` (Ubuntu/Debian) or equivalent.

2. Open Terminal, go to this folder, and run:
   ```bash
   cd "/path/to/PhDagentSpring2026/pre1/paper2slides_beamer/trial/beamerTry"
   pdflatex aaai25_3slides.tex
   ```
   Replace `/path/to/` with your actual path (e.g. your OneDrive folder).

3. Output: `aaai25_3slides.pdf` will appear in the same folder. Open it with any PDF viewer.

### Option B: Overleaf (no local install)

1. Go to [overleaf.com](https://www.overleaf.com) and create a free account.
2. New Project → Blank Project (or Upload Project and zip this folder).
3. Copy-paste the contents of `aaai25_3slides.tex` into the main .tex file (or upload the file).
4. Click **Recompile**. Download the PDF from the preview panel.

### Option C: Cursor/VS Code — LaTeX Workshop + LaTeX Previewer

You have **LaTeX Workshop** (James-Yu) and **LaTeX Previewer** (mjpvs). Use them like this:

**Requirements:** A LaTeX distribution must be installed (e.g. MacTeX) so that `pdflatex` is on your PATH. Otherwise builds will fail.

---

#### LaTeX Workshop (James-Yu.latex-workshop)

- **Open the .tex file:** Open `aaai25_3slides.tex` in the editor.
- **Build PDF:**
  - **Command Palette:** `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) → type **“LaTeX Workshop: Build LaTeX project”** → Enter.  
  - Or use the **TeX** icon in the left sidebar → **Build LaTeX project**.
- **View PDF:**
  - After a successful build, the PDF often opens in a tab (internal viewer).  
  - Or: Command Palette → **“LaTeX Workshop: View LaTeX PDF”** (or “View in web browser” / “View in external viewer”).
- **Recipe:** By default it uses the first “recipe” (often `pdflatex`). For this Beamer file that’s correct; no change needed.
- **Auto-build:** LaTeX Workshop can build on save; check **Settings → LaTeX Workshop → Auto Build** if you want that.

---

#### LaTeX Previewer (mjpvs.latex-previewer)

- **Purpose:** Inline or panel preview of the compiled PDF (or a selected fragment).
- **How to use:**
  - **Command Palette** → type **“LaTeX Previewer”** and pick the command (e.g. **“LaTeX Previewer: Show Preview”** or **“Preview in current editor”**).  
  - Or right‑click in the .tex file and look for a **“Preview”** or **“LaTeX Preview”** option.
- **Note:** Preview usually runs a build first. If `pdflatex` is not installed or not on PATH, the preview will fail; install LaTeX (see Option A above) then try again.

---

#### Quick workflow (both extensions)

1. Open `aaai25_3slides.tex`.
2. **Build:** `Cmd+Shift+P` → “LaTeX Workshop: Build LaTeX project”.
3. **View:** Use “View LaTeX PDF” from LaTeX Workshop, or “LaTeX Previewer: Show Preview” for the previewer.
4. Edit the .tex and rebuild to refresh the PDF.

---

## Troubleshooting: LaTeX Workshop build fails

If the **LaTeX Workshop** output shows:

| Log message | Meaning | Fix |
|-------------|---------|-----|
| `spawn latexmk ENOENT` | `latexmk` is not installed or not in PATH. | Install a LaTeX distribution (see Option A above). On macOS: `brew install --cask mactex-no-gui` or install [MacTeX](https://tug.org/mactex/). Then **restart Cursor** so it picks up the new PATH. |
| `kpsewhich returned with non-zero code null` | TeX tools (e.g. `kpsewhich`) not found or TeX not installed. | Same: install MacTeX/TeX Live and restart Cursor. |
| `TypeError: Cannot read properties of undefined (reading 'toString')` | Extension tried to detect `pdflatex` and got no executable. | Same: ensure `pdflatex` and `latexmk` are on your PATH (install TeX, restart Cursor). |

**Check from a terminal:** Run `which latexmk` and `which pdflatex`. If both report “not found”, install a LaTeX distribution. After install, Cursor may need a full restart (quit and reopen) so the extension sees the updated PATH.
