#!/usr/bin/env python3
"""
Find sentences in html_collection papers that serve critical functions
(inadequacies of previous studies; paucity/lack of previous research).
Uses templates from findCriticalSentences.md. Outputs report .md and .html.
"""
from __future__ import annotations

import html
import json
import os
import re
from datetime import datetime
from pathlib import Path

# Reuse extraction and LLM from map_sentences
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from map_sentences import (
    extract_sentences_from_html,
    _read_poe_key,
    _log,
    HTML_COLLECTION,
    MAX_SENTENCES_PER_REQUEST,
)
from map_sentences import OpenAI, HAS_OPENAI

BASE = Path(__file__).resolve().parent
CRITICAL_MD = BASE / "findCriticalSentences.md"
OUT_MD = BASE / "report_criticalSentences.md"
OUT_HTML = BASE / "report_criticalSentences.html"
POE_KEY_FILE = BASE.parent.parent.parent / "LLM" / "poe.md"
LOG_PATH = BASE / "process_critical.log"

# Template category labels for output
CATEGORY_1 = "Explaining the inadequacies of previous studies"
CATEGORY_2 = "Identifying the paucity or lack of previous research"


def parse_critical_md(md_path: Path) -> dict:
    """Parse findCriticalSentences.md into sections and items."""
    content = md_path.read_text(encoding="utf-8")
    sections = []
    current_section = None
    current_items = []

    for line in content.splitlines():
        line_stripped = line.strip()
        if line.startswith("## "):
            if current_section is not None:
                sections.append({"name": current_section, "items": current_items})
            current_section = line.lstrip("## ").strip()
            current_items = []
        elif line_stripped.startswith("Identifying the paucity or lack of previous research"):
            if current_section is not None:
                sections.append({"name": current_section, "items": current_items})
            # First part is section name; rest can be first item
            rest = line_stripped.replace("Identifying the paucity or lack of previous research", "").strip()
            current_section = CATEGORY_2
            current_items = [rest] if rest else []
        elif line_stripped.startswith("- ") and current_section is not None:
            current_items.append(line_stripped[2:].strip())
        elif line_stripped and not line_stripped.startswith("consider ") and not line_stripped.startswith("go through ") and not line_stripped.startswith("identify ") and not line_stripped.startswith("generate ") and current_section is not None:
            # Standalone line under section (e.g. "Previous studies of X have not dealt with …")
            if not line_stripped.startswith("http") and len(line_stripped) > 10:
                current_items.append(line_stripped)
    if current_section is not None:
        sections.append({"name": current_section, "items": current_items})

    return {"title": "Critical sentences (inadequacies; paucity/lack of research)", "sections": sections, "source": ""}


def all_template_phrases(data: dict) -> list[str]:
    phrases = []
    for sec in data["sections"]:
        phrases.extend(sec["items"])
    return phrases


def build_llm_prompt(paper_sentences: list[str], template_data: dict, paper_id: str) -> str:
    """Build prompt for matching sentences to critical template categories."""
    sentences_block = "\n".join(f"{i+1}. {s}" for i, s in enumerate(paper_sentences))
    templates_block = []
    for sec in template_data["sections"]:
        templates_block.append(f"**{sec['name']}**")
        for t in sec["items"][:25]:
            templates_block.append(f"  - {t}")
        if len(sec["items"]) > 25:
            templates_block.append(f"  - ... and {len(sec['items'])-25} more")
    templates_text = "\n".join(templates_block)

    return f"""You are an expert in academic writing and the Manchester Academic Phrasebank.

**Task:** From an academic paper we have extracted a list of sentences (below). We have two phrasebank-style "critical" functions with example templates:

1) **{CATEGORY_1}** — e.g. previous studies have not dealt with X, research has tended to focus on X rather than Y, existing accounts fail to address, limitations of prior work.
2) **{CATEGORY_2}** — e.g. little published data on X, few studies have investigated, no previous study has, paucity of evidence, understudied, scant attention.

Your job is to:
1. Identify which paper sentences serve a similar rhetorical function to **either** of these two categories.
2. For each matched sentence, indicate which category (1 or 2) and optionally suggest a short "extracted template" (generalized phrase with placeholders X, Y, …).

**Templates:**
{templates_text}

**Sentences from the paper (numbered):**
{sentences_block}

**Instructions:** Reply with a single JSON object only, no markdown or extra text:
{{
  "matches": [
    {{ "sentence": "exact sentence from the list", "category": 1, "extracted_template": "template with X/Y placeholders" }},
    ...
  ]
}}

- "sentence" must be an exact copy from the list above.
- "category" must be 1 (inadequacies of previous studies) or 2 (paucity/lack of previous research).
- If no sentence matches, use "matches": [].
"""


def get_llm_matches_critical(
    paper_sentences: list[str],
    template_data: dict,
    paper_id: str,
    client: "OpenAI",
    model: str = "gpt-4o-mini",
) -> list[dict]:
    """Return list of {sentence, category, extracted_template} for this paper."""
    if not paper_sentences:
        return []
    all_matches = []
    for start in range(0, len(paper_sentences), MAX_SENTENCES_PER_REQUEST):
        chunk = paper_sentences[start : start + MAX_SENTENCES_PER_REQUEST]
        user_content = build_llm_prompt(chunk, template_data, paper_id)
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You respond only with a single valid JSON object. No explanation or markdown."},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.2,
            )
            text = resp.choices[0].message.content.strip()
            if text.startswith("```"):
                text = re.sub(r"^```(?:json)?\s*", "", text)
                text = re.sub(r"\s*```\s*$", "", text)
            data = json.loads(text)
            for m in data.get("matches") or []:
                m["paper_id"] = paper_id
                all_matches.append(m)
        except (json.JSONDecodeError, KeyError) as e:
            print(f"    [LLM parse error for {paper_id}]: {e}")
    return all_matches


def run_all_papers(use_llm: bool = True) -> list[dict]:
    """Process all HTML files in html_collection; return list of match dicts."""
    template_data = parse_critical_md(CRITICAL_MD)
    _log(f"Parsed {len(template_data['sections'])} sections, {len(all_template_phrases(template_data))} template items", LOG_PATH)

    html_files = sorted(HTML_COLLECTION.glob("*.html"))
    _log(f"Found {len(html_files)} HTML files in {HTML_COLLECTION}", LOG_PATH)

    client = None
    model = "gpt-4o-mini"
    if use_llm and HAS_OPENAI:
        api_key = os.environ.get("OPENAI_API_KEY")
        base_url = os.environ.get("OPENAI_BASE_URL")
        if not api_key:
            api_key = _read_poe_key()
            if api_key:
                base_url = "https://api.poe.com/v1"
        if api_key:
            client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)
            model = os.environ.get("MAP_SENTENCES_MODEL", "gpt-4o-mini")
            _log(f"Using LLM (model={model})", LOG_PATH)
        else:
            use_llm = False
            _log("No API key; skipping LLM matching", LOG_PATH)

    all_matches = []
    for i, html_path in enumerate(html_files, 1):
        paper_id = html_path.stem
        _log(f"Paper {i}/{len(html_files)}: {paper_id}", LOG_PATH)
        sentences = extract_sentences_from_html(html_path)
        sentences = [s for s in sentences if len(s.strip()) >= 15]
        if use_llm and client:
            matches = get_llm_matches_critical(sentences, template_data, paper_id, client, model)
            all_matches.extend(matches)
            _log(f"  matches: {len(matches)}", LOG_PATH)
        else:
            # Simple keyword-based fallback: any sentence containing critical phrases
            for s in sentences:
                low = s.lower()
                if any(x in low for x in ("previous stud", "prior work", "little attention", "few studies", "no previous", "paucity", "understudied", "scant attention", "have not dealt", "failed to address", "limited to", "no single study", "no research has been")):
                    all_matches.append({"paper_id": paper_id, "sentence": s, "category": 1, "extracted_template": ""})

    return all_matches


def write_report_md(template_data: dict, matches: list[dict], out_path: Path, log_path: Path | None = None) -> None:
    """Write report_criticalSentences.md."""
    _log(f"Writing {out_path.name}", log_path or LOG_PATH)
    lines = [
        "# Report: Critical sentences (inadequacies; paucity/lack of research)",
        "",
        "**Template source:** `findCriticalSentences.md`",
        "**Paper collection:** `buildPaperCollection_arXiv/html_collection`",
        f"**Papers scanned:** all `.html` files",
        f"**Sentences found:** {len(matches)}",
        "",
        "---",
        "",
        "## 1. Original templates (phrasebank)",
        "",
    ]
    for sec in template_data["sections"]:
        lines.append(f"### {sec['name']}")
        lines.append("")
        for item in sec["items"][:35]:
            lines.append(f"- {item}")
        if len(sec["items"]) > 35:
            lines.append(f"- ... and {len(sec['items'])-35} more items")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Sentences found (by category)")
    lines.append("")

    for cat_num, cat_name in [(1, CATEGORY_1), (2, CATEGORY_2)]:
        cat_matches = [m for m in matches if m.get("category") == cat_num]
        lines.append(f"### {cat_name}")
        lines.append("")
        if not cat_matches:
            lines.append("*No sentence in the collection matched this category.*")
            lines.append("")
            continue
        for m in cat_matches:
            lines.append(f"- **[{m['paper_id']}]** {m['sentence']}")
            if m.get("extracted_template"):
                lines.append(f"  - *Template:* {m['extracted_template']}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 3. New or modified templates (extracted)")
    lines.append("")
    templates_seen = set()
    for m in matches:
        t = (m.get("extracted_template") or "").strip()
        if t and t not in templates_seen:
            templates_seen.add(t)
            lines.append(f"- {t}")
    if not templates_seen:
        lines.append("*None extracted (use phrasebank templates above).*")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    _log(f"Wrote {out_path}", log_path or LOG_PATH)


def write_report_html(template_data: dict, matches: list[dict], out_path: Path, log_path: Path | None = None) -> None:
    """Write report_criticalSentences.html."""
    _log(f"Writing {out_path.name}", log_path or LOG_PATH)
    by_cat = {1: [], 2: []}
    for m in matches:
        c = m.get("category", 1)
        if c in by_cat:
            by_cat[c].append(m)

    def esc(s):
        return html.escape(str(s))
    def row(m):
        return f"<tr><td>{esc(m['paper_id'])}</td><td>{esc(m['sentence'])}</td><td class='template'>{esc(m.get('extracted_template') or '—')}</td></tr>"
    rows_1 = "".join(row(m) for m in by_cat[1])
    rows_2 = "".join(row(m) for m in by_cat[2])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Critical sentences report</title>
<style>
:root {{ --bg: #0f1419; --card: #1a2332; --accent: #3b82f6; --muted: #8b98a5; --text: #e7e9ea; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 1.5rem; line-height: 1.5; }}
h1 {{ font-size: 1.5rem; margin: 0 0 0.5rem; }}
h2 {{ font-size: 1.15rem; margin: 1.5rem 0 0.5rem; color: var(--muted); }}
p {{ color: var(--muted); margin: 0 0 1rem; }}
table {{ width: 100%; border-collapse: collapse; background: var(--card); border-radius: 8px; overflow: hidden; border: 1px solid #2f3640; margin-bottom: 1rem; }}
th, td {{ padding: 0.6rem 0.75rem; text-align: left; vertical-align: top; }}
th {{ background: #252d38; color: var(--muted); font-size: 0.8rem; }}
td {{ font-size: 0.9rem; }}
tr:nth-child(even) {{ background: rgba(255,255,255,0.02); }}
td:nth-child(1) {{ white-space: nowrap; color: var(--accent); }}
.template {{ font-style: italic; color: var(--muted); }}
a {{ color: var(--accent); }}
</style>
</head>
<body>
<h1>Critical sentences report</h1>
<p>Template source: findCriticalSentences.md · Papers: html_collection · Total matches: {len(matches)}</p>

<h2>1. Explaining the inadequacies of previous studies ({len(by_cat[1])} sentences)</h2>
<table>
<thead><tr><th>Paper</th><th>Sentence</th><th>Extracted template</th></tr></thead>
<tbody>{rows_1 or "<tr><td colspan='3'>None</td></tr>"}</tbody>
</table>

<h2>2. Identifying the paucity or lack of previous research ({len(by_cat[2])} sentences)</h2>
<table>
<thead><tr><th>Paper</th><th>Sentence</th><th>Extracted template</th></tr></thead>
<tbody>{rows_2 or "<tr><td colspan='3'>None</td></tr>"}</tbody>
</table>

<p><a href="report_criticalSentences.md">report_criticalSentences.md</a></p>
</body>
</html>
"""
    out_path.write_text(html_content, encoding="utf-8")
    _log(f"Wrote {out_path}", log_path or LOG_PATH)


SENTENCES_JSON = BASE / "sentences_all.json"
MATCHES_JSON = BASE / "matches_from_ai.json"

# Keywords that suggest a sentence might be "critical" (inadequacies or paucity/lack)
CANDIDATE_KEYWORDS = (
    "previous stud", "prior work", "prior data", "prior research", "prior studies",
    "little attention", "few studies", "no previous", "paucity", "understudied",
    "scant attention", "have not dealt", "failed to address", "limited to",
    "no single study", "no research has been", "lack of", "still lacking",
    "not been", "have not been", "has not been", "does not take", "failed to",
    "only focused on", "only been", "rather than", "in contrast to",
    "contrasts with", "different from prior", "unlike previous", "most studies",
    "existing accounts", "such approaches", "research to date", "to date",
    "no studies have", "no controlled studies", "few empirical", "few writers",
    "far too little", "very little attention", "no attempt", "overlook",
    "restricted to", "limited comparisons", "systematic research",
    "systematic understanding", "literature revealed few", "understudied",
)


def run_extract_only() -> None:
    """Extract sentences from all HTMLs to sentences_all.json (no LLM, no report)."""
    html_files = sorted(HTML_COLLECTION.glob("*.html"))
    out = {}
    for i, html_path in enumerate(html_files, 1):
        paper_id = html_path.stem
        sentences = extract_sentences_from_html(html_path)
        sentences = [s for s in sentences if len(s.strip()) >= 15]
        out[paper_id] = sentences
        print(f"Paper {i}/{len(html_files)}: {paper_id} ({len(sentences)} sentences)")
    SENTENCES_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"Wrote {SENTENCES_JSON}")


def run_candidates_to_tsv() -> None:
    """Write candidate sentences (keyword-filtered) to candidates.tsv for AI review."""
    if not SENTENCES_JSON.exists():
        run_extract_only()
    data = json.loads(SENTENCES_JSON.read_text(encoding="utf-8"))
    tsv_path = BASE / "candidates.tsv"
    count = 0
    with tsv_path.open("w", encoding="utf-8") as f:
        for paper_id, sentences in data.items():
            for s in sentences:
                if len(s.strip()) < 20:
                    continue
                low = s.lower()
                if any(kw in low for kw in CANDIDATE_KEYWORDS):
                    f.write(paper_id + "\t" + s.replace("\n", " ").replace("\t", " ") + "\n")
                    count += 1
    print(f"Wrote {count} candidates to {tsv_path}")


def run_from_matches(matches_path: Path) -> None:
    """Generate report .md and .html from precomputed matches JSON (no LLM)."""
    matches = json.loads(matches_path.read_text(encoding="utf-8"))
    if isinstance(matches, list):
        pass
    else:
        matches = matches.get("matches", matches.get("results", []))
    template_data = parse_critical_md(CRITICAL_MD)
    write_report_md(template_data, matches, OUT_MD, LOG_PATH)
    write_report_html(template_data, matches, OUT_HTML, LOG_PATH)
    print(f"Done. {len(matches)} matches → {OUT_MD.name}, {OUT_HTML.name}")


if __name__ == "__main__":
    if "--extract-only" in sys.argv:
        run_extract_only()
        sys.exit(0)
    if "--candidates" in sys.argv:
        run_candidates_to_tsv()
        sys.exit(0)
    for i, arg in enumerate(sys.argv):
        if arg == "--from-matches" and i + 1 < len(sys.argv):
            run_from_matches(Path(sys.argv[i + 1]))
            sys.exit(0)
    use_llm = "--pattern" not in sys.argv
    _log("Starting find_critical_sentences", LOG_PATH)
    matches = run_all_papers(use_llm=use_llm)
    template_data = parse_critical_md(CRITICAL_MD)
    write_report_md(template_data, matches, OUT_MD, LOG_PATH)
    write_report_html(template_data, matches, OUT_HTML, LOG_PATH)
    _log(f"Done. {len(matches)} matches → {OUT_MD.name}, {OUT_HTML.name}", LOG_PATH)
