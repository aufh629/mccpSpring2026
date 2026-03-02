#!/usr/bin/env python3
"""
Convert COCO paper HTML (from arxiv LaTeXML) to an HTML slide deck.
Input: COCO_2310.18955v3_from_arxiv.html
Output: slidesHTML.html (reveal.js presentation)
"""
from pathlib import Path
import re
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Status: beautifulsoup4 required. Install: pip install beautifulsoup4", file=sys.stderr)
    sys.exit(1)

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_HTML = SCRIPT_DIR / "COCO_2310.18955v3_from_arxiv.html"
OUTPUT_HTML = SCRIPT_DIR / "slidesHTML.html"

# Main sections to include (S1..S6 = Introduction .. Acknowledgement)
SECTION_IDS = ["S1", "S2", "S3", "S4", "S5", "S6"]
MAX_PARAS_PER_SLIDE = 4
MAX_CHARS_PER_PARA = 420


def get_text_from_node(node):
    """Extract plain text; for math use a single representation (alttext or x-tex)."""
    if node is None:
        return ""
    text_parts = []
    for elem in node.descendants:
        if isinstance(elem, str):
            text_parts.append(elem.strip())
        elif elem.name == "math":
            alt = elem.get("alttext")
            if alt:
                text_parts.append(alt)
            else:
                ann = elem.find("annotation", encoding="application/x-tex")
                if ann and ann.string:
                    text_parts.append(ann.string.strip())
        elif elem.name in ("annotation", "annotation-xml", "semantics") and elem.find_parent("math"):
            continue  # avoid duplicating math from descendants
        elif elem.name in ("script", "style"):
            continue
    return " ".join(text_parts).replace("\n", " ").strip()


def shorten(s, max_len=MAX_CHARS_PER_PARA):
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 3].rsplit(" ", 1)[0] + "..."


def extract_slides(soup):
    """Extract title and one slide per main section from the paper HTML."""
    slides = []

    # Title slide
    title_el = soup.find("h1", class_=re.compile(r"ltx_title_document"))
    title = (title_el.get_text(strip=True) if title_el else "Optimal Algorithms for OCO with Adversarial Constraints")
    slides.append({"type": "title", "title": title, "body": []})

    # Abstract (optional one slide)
    abstract_el = soup.find("h6", class_=re.compile(r"ltx_title_abstract"))
    if abstract_el:
        abs_para = abstract_el.find_next("p", class_="ltx_p")
        if abs_para:
            abs_text = get_text_from_node(abs_para)
            slides.append({"type": "section", "title": "Abstract", "body": [shorten(abs_text, 500)]})

    # Main sections S1..S6
    for sid in SECTION_IDS:
        section = soup.find("section", class_="ltx_section", id=sid)
        if not section:
            continue
        # Section title (h2)
        h2 = section.find("h2", class_=re.compile(r"ltx_title_section"))
        sec_title = get_text_from_node(h2) if h2 else f"Section {sid}"
        # First few paragraphs (direct ltx_para under this section, not in subsection)
        body_items = []
        for para in section.find_all("div", class_="ltx_para", limit=20):
            # Skip if inside a subsection (we want only top-level paras for brevity)
            if para.find_parent("section", class_="ltx_subsection"):
                continue
            for p in para.find_all("p", class_="ltx_p"):
                t = get_text_from_node(p)
                if t and len(t) > 15:
                    body_items.append(shorten(t))
                    if len(body_items) >= MAX_PARAS_PER_SLIDE:
                        break
            if len(body_items) >= MAX_PARAS_PER_SLIDE:
                break
        # If no top-level paras, get first paragraph from section anywhere
        if not body_items:
            first_p = section.find("p", class_="ltx_p")
            if first_p:
                body_items.append(shorten(get_text_from_node(first_p)))
        slides.append({"type": "section", "title": sec_title, "body": body_items})

    return slides


def build_reveal_html(slides):
    """Build a single HTML file with reveal.js from CDN."""
    title = slides[0]["title"] if slides else "Slides"
    sections_html = []
    for s in slides:
        if s["type"] == "title":
            sections_html.append(
                f'        <section><h1>{s["title"]}</h1>'
                '<p style="margin-top:1em;font-size:0.6em;">From paper: COCO 2310.18955 (HTML → slides)</p></section>'
            )
        else:
            body = "".join(f"<li>{b}</li>" for b in s["body"]) if s["body"] else ""
            if body:
                body = f"<ul>{body}</ul>"
            sections_html.append(f'        <section><h2>{s["title"]}</h2>{body}</section>')

    sections_joined = "\n".join(sections_html)
    return (
        """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>"""
        + title
        + """</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.css"/>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/theme/white.css"/>
  <style>
    .reveal ul { font-size: 0.85em; margin-top: 0.5em; }
    .reveal h2 { font-size: 1.4em; }
  </style>
</head>
<body>
  <div class="reveal">
    <div class="slides">
"""
        + sections_joined
        + """
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/reveal.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/plugin/notes/notes.js"></script>
  <script>
    Reveal.initialize({ hash: true, plugins: [ RevealNotes ] });
  </script>
</body>
</html>
"""
    )


def main():
    print("Status: Reading", INPUT_HTML.name)
    html = INPUT_HTML.read_text(encoding="utf-8", errors="replace")
    print("Status: Parsing HTML")
    soup = BeautifulSoup(html, "html.parser")
    print("Status: Extracting slides")
    slides = extract_slides(soup)
    print("Status: Built", len(slides), "slides")
    out = build_reveal_html(slides)
    OUTPUT_HTML.write_text(out, encoding="utf-8")
    print("Status: Wrote", OUTPUT_HTML)
    return 0


if __name__ == "__main__":
    sys.exit(main())
