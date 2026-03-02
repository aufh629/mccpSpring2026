# Install LaTeX and use it in Cursor

## 1. Install LaTeX (run in your Terminal)

Open **Terminal** (outside Cursor) and run:

```bash
brew install --cask mactex-no-gui
```

- This downloads and installs MacTeX (no GUI apps). It can take **5–15 minutes** depending on your connection.
- When it finishes, you may see a note about restarting the terminal or running a path helper.

## 2. Make `pdflatex` available

After the install, either:

- **Restart Terminal**, or  
- Run once:  
  ```bash
  eval "$(/usr/libexec/path_helper)"
  ```

Then check:

```bash
pdflatex -version
```

You should see version info. LaTeX tools are installed under `/Library/TeX/texbin/`.

## 3. Use LaTeX in Cursor

1. **Restart Cursor** (so it picks up the new PATH with `pdflatex`).
2. Open your project and open **`aaai25_3slides.tex`**.
3. **Build PDF:**  
   `Cmd+Shift+P` → type **“LaTeX Workshop: Build LaTeX project”** → Enter.
4. **View PDF:**  
   `Cmd+Shift+P` → **“LaTeX Workshop: View LaTeX PDF”** (or use the TeX icon in the left sidebar).

The PDF will be created in the same folder as the .tex file (`aaai25_3slides.pdf`).

## If you prefer not to use Homebrew

- Download **MacTeX** from: https://tug.org/mactex/mactex-download.html  
- Run the installer. Then restart Terminal and Cursor, and use steps 2–3 above.
