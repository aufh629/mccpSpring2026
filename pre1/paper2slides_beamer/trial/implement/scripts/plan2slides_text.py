#!/usr/bin/env python3
"""
Produce text-only slides from Paper2Slides checkpoints when image generation fails.
Reads checkpoint_plan.json and summary.md, writes slides_outline.md and slides_text.html.
Run from trial/implement/ with:
  python plan2slides_text.py [path_to_config_dir]
Default: Paper2Slides/outputs/COCO_2310.18955v3_from_arxiv/paper/fast/slides_academic_short_1sec
"""
import json
import re
from pathlib import Path


def main():
    import sys
    base = Path(__file__).resolve().parent
    config_dir = base / "Paper2Slides" / "outputs" / "COCO_2310.18955v3_from_arxiv" / "paper" / "fast" / "slides_academic_short_1sec"
    if len(sys.argv) > 1:
        config_dir = Path(sys.argv[1])

    plan_path = config_dir / "checkpoint_plan.json"
    fast_dir = config_dir.parent  # fast/
    summary_path = fast_dir / "summary.md"

    if not plan_path.exists():
        print("Not found:", plan_path)
        return 1
    with open(plan_path) as f:
        data = json.load(f)
    plan = data.get("plan", {})
    sections = plan.get("sections", [])

    summary_preview = ""
    rag_out = fast_dir.parent / "rag_output"
    rag_mds = list(rag_out.glob("*.md")) if rag_out.exists() else []
    if rag_mds:
        summary_preview = rag_mds[0].read_text(encoding="utf-8", errors="replace")[:4000].strip()
    if not summary_preview and summary_path.exists():
        summary_text = summary_path.read_text(encoding="utf-8", errors="replace")
        if "<!DOCTYPE" not in summary_text and "apifox" not in summary_text.lower():
            summary_preview = summary_text[:2000].strip()
        else:
            summary_preview = summary_text[:2000].strip()

    out_dir = config_dir / "text_slides"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Build markdown slides (--- separator for Reveal/Marp style)
    md_lines = []
    for i, sec in enumerate(sections):
        title = sec.get("title") or f"Slide {i+1}"
        content = (sec.get("content") or "").strip()
        if not content and summary_preview:
            # Use a chunk of summary for this slide
            chunk_size = max(400, len(summary_preview) // max(1, len(sections)))
            start = i * chunk_size
            content = summary_preview[start : start + chunk_size].strip()
            if not content:
                content = summary_preview[:500].strip()
        md_lines.append("---")
        md_lines.append("")
        md_lines.append(f"# {title}")
        md_lines.append("")
        if content:
            md_lines.append(content)
        else:
            md_lines.append("(Content from paper summary.)")
        md_lines.append("")

    if md_lines and md_lines[0] == "---":
        md_lines.pop(0)  # drop leading ---
    md_content = "\n".join(md_lines)

    md_path = out_dir / "slides_outline.md"
    md_path.write_text(md_content, encoding="utf-8")
    print("Wrote:", md_path)

    # Simple HTML (one slide per section, viewable in browser)
    html_slides = []
    for i, sec in enumerate(sections):
        title = sec.get("title") or f"Slide {i+1}"
        content = (sec.get("content") or "").strip()
        if not content and summary_preview:
            chunk_size = max(400, len(summary_preview) // max(1, len(sections)))
            start = i * chunk_size
            content = summary_preview[start : start + chunk_size].strip() or summary_preview[:500].strip()
        content = content.replace("<", "&lt;").replace(">", "&gt;")
        html_slides.append(f'    <section><h2>{title}</h2><div class="content"><pre>{content}</pre></div></section>')
    html_body = "\n".join(html_slides)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Slides (text only)</title>
  <style>
    section {{ padding: 2rem; min-height: 80vh; }}
    .content {{ white-space: pre-wrap; font-size: 1rem; }}
  </style>
</head>
<body>
{html_body}
</body>
</html>
"""
    html_path = out_dir / "slides_text.html"
    html_path.write_text(html, encoding="utf-8")
    print("Wrote:", html_path)
    print("Output dir:", out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
