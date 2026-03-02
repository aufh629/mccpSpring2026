# HTML → Slides (COCO paper)

**Input**: `COCO_2310.18955v3_from_arxiv.html`  
**Output**: `slidesHTML.html` (reveal.js presentation)

## How to generate

From this folder (`trial/implement`):

```bash
python3 html2slides.py
```

Requires: `beautifulsoup4` (`pip install beautifulsoup4`).

## Output

- **File**: `slidesHTML.html`
- **Format**: Single HTML file using [reveal.js](https://revealjs.com/) from CDN (no local assets).
- **Slides**: Title, Abstract, then one slide per main section (1–6: Introduction, COCO Problem, OCS, Experiments, Conclusion, Acknowledgement).

## Viewing

Open `slidesHTML.html` in a browser. Use arrow keys or click to navigate. To export to PDF: use the browser’s Print → Save as PDF while viewing the slides.

## Optional: .ppt

To get a PowerPoint file, open `slidesHTML.html` in the browser, then use “Print” → “Save as PDF”, and open the PDF in PowerPoint (or use an HTML-to-PPT converter). The script does not produce `.ppt` directly.
