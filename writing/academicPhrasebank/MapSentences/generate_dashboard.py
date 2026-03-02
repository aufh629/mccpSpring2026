#!/usr/bin/env python3
"""
Parse MapSentences trial reports and process.log, then generate an HTML dashboard
with quantitative stats: sentences processed, similar sentences found, new templates identified.
"""
from __future__ import annotations

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
TRIAL_DIR = BASE / "trial"
PROCESS_LOG = BASE / "process.log"


def parse_process_log(log_path: Path) -> dict[str, int]:
    """Extract latest 'Paper: X, sentences: N' from process.log. Returns {paper_id: sentence_count}."""
    out = {}
    if not log_path.exists():
        return out
    for line in log_path.read_text(encoding="utf-8").splitlines():
        m = re.search(r"Paper: (\S+), sentences: (\d+)", line)
        if m:
            out[m.group(1)] = int(m.group(2))
    return out


def parse_report(md_path: Path) -> dict:
    """Parse one report_*.md: paper_id, function_name, title, similar_count, new_templates_count."""
    text = md_path.read_text(encoding="utf-8")
    name = md_path.stem.replace("report_", "")
    data = {
        "function": name,
        "paper_id": "",
        "title": "",
        "similar_count": 0,
        "new_templates_count": 0,
    }
    # Source paper
    m = re.search(r"\*\*Source paper:\*\* `(\S+)`", text)
    if m:
        data["paper_id"] = m.group(1)
    # Title from # Report: Title
    m = re.search(r"# Report: (.+)", text)
    if m:
        data["title"] = m.group(1).strip()
    # Section 2: Similar sentences (list items only; exclude placeholder)
    sec2 = re.search(r"## 2\. Similar sentences found in the paper\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if sec2:
        block = sec2.group(1)
        for line in block.splitlines():
            line = line.strip()
            if line.startswith("- ") and "*Sentence not found*" not in line:
                data["similar_count"] += 1
    # Section 4: New template (list items only; exclude placeholder lines)
    sec4 = re.search(r"## 4\. New template extracted from the paper\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if sec4:
        block = sec4.group(1)
        for line in block.splitlines():
            line = line.strip()
            if line.startswith("- ") and "*Not applicable" not in line and "Candidate phrases" not in line:
                data["new_templates_count"] += 1
    return data


def collect_trial_data(trial_dir: Path, process_log: Path) -> tuple[list[dict], int, str]:
    """Parse all report_*.md and process.log. Returns (per_function_rows, sentences_processed, paper_id)."""
    reports = sorted(trial_dir.glob("report_*.md"))
    rows = []
    paper_id = ""
    for p in reports:
        row = parse_report(p)
        rows.append(row)
        if row["paper_id"]:
            paper_id = row["paper_id"]
    paper_sentences = 0
    log_data = parse_process_log(process_log)
    if paper_id and paper_id in log_data:
        paper_sentences = log_data[paper_id]
    # If multiple papers in log, use the one that matches reports
    if not paper_sentences and log_data:
        paper_sentences = list(log_data.values())[-1]
        paper_id = list(log_data.keys())[-1]
    return rows, paper_sentences, paper_id


def generate_html(rows: list[dict], sentences_processed: int, paper_id: str, out_path: Path) -> None:
    """Write dashboard HTML with summary stats and per-function table."""
    total_similar = sum(r["similar_count"] for r in rows)
    total_templates = sum(r["new_templates_count"] for r in rows)
    num_functions = len(rows)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MapSentences Dashboard — {paper_id}</title>
<style>
:root {{ --bg: #0f1419; --card: #1a2332; --accent: #3b82f6; --muted: #8b98a5; --text: #e7e9ea; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 1.5rem; line-height: 1.5; }}
h1 {{ font-size: 1.5rem; margin: 0 0 1rem; color: var(--text); }}
h2 {{ font-size: 1.1rem; margin: 1.5rem 0 0.5rem; color: var(--muted); }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }}
.stat {{ background: var(--card); border-radius: 8px; padding: 1rem; border: 1px solid #2f3640; }}
.stat-num {{ font-size: 1.75rem; font-weight: 700; color: var(--accent); }}
.stat-label {{ font-size: 0.85rem; color: var(--muted); margin-top: 0.25rem; }}
table {{ width: 100%; border-collapse: collapse; background: var(--card); border-radius: 8px; overflow: hidden; border: 1px solid #2f3640; }}
th, td {{ padding: 0.6rem 0.75rem; text-align: left; }}
th {{ background: #252d38; color: var(--muted); font-size: 0.8rem; font-weight: 600; }}
tr:nth-child(even) {{ background: rgba(255,255,255,0.02); }}
td {{ font-size: 0.9rem; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.fn {{ font-weight: 500; }}
.none {{ color: var(--muted); }}
</style>
</head>
<body>
<h1>MapSentences dashboard</h1>
<p style="color: var(--muted); margin: 0;">Paper: <strong>{paper_id}</strong></p>

<div class="stats">
  <div class="stat">
    <div class="stat-num">{sentences_processed}</div>
    <div class="stat-label">Sentences processed</div>
  </div>
  <div class="stat">
    <div class="stat-num">{total_similar}</div>
    <div class="stat-label">Similar sentences found</div>
  </div>
  <div class="stat">
    <div class="stat-num">{total_templates}</div>
    <div class="stat-label">New templates identified</div>
  </div>
  <div class="stat">
    <div class="stat-num">{num_functions}</div>
    <div class="stat-label">Functions covered</div>
  </div>
</div>

<h2>Per function</h2>
<table>
<thead><tr><th>Function</th><th>Similar sentences</th><th>New templates</th><th>Report</th></tr></thead>
<tbody>
"""
    for r in rows:
        sim = r["similar_count"]
        tmpl = r["new_templates_count"]
        sim_c = str(sim) if sim else '<span class="none">0</span>'
        tmpl_c = str(tmpl) if tmpl else '<span class="none">0</span>'
        report_file = f"report_{r['function']}.md"
        html += f"<tr><td class=\"fn\">{r['title'] or r['function']}</td><td>{sim_c}</td><td>{tmpl_c}</td><td><a href=\"{report_file}\">{report_file}</a></td></tr>\n"
    html += """</tbody>
</table>
</body>
</html>
"""
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path}")


def main() -> None:
    rows, sentences_processed, paper_id = collect_trial_data(TRIAL_DIR, PROCESS_LOG)
    if not rows:
        print("No report_*.md found in trial/")
        return
    out_path = TRIAL_DIR / "dashboard.html"
    generate_html(rows, sentences_processed, paper_id or "unknown", out_path)


if __name__ == "__main__":
    main()
