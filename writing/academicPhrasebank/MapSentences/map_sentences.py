#!/usr/bin/env python3
"""
Map sentences from papers to academic phrasebank templates/functions.
Uses an LLM to match paper sentences to phrasebank functions; generates one report
per function with: original templates, similar sentences, source paper, and
extracted/new template.
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser

# Optional: use pattern matching if no LLM available
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

BASE = Path(__file__).resolve().parent
PHRASEBANK = BASE.parent
GENERAL_FUNCTIONS = PHRASEBANK / "general-functions"
PAPER_SECTIONS = PHRASEBANK / "paper-sections"
HTML_COLLECTION = BASE.parent.parent / "buildPaperCollection_arXiv" / "html_collection"
# Poe API key file (relative to PhDagentSpring2026 folder)
POE_KEY_FILE = BASE.parent.parent.parent / "LLM" / "poe.md"
PROCESS_LOG = BASE / "process.log"
POE_BASE_URL = "https://api.poe.com/v1"

# Max sentences per LLM request to avoid context overflow
MAX_SENTENCES_PER_REQUEST = 120


def _read_poe_key(poe_key_file: Path | None = None) -> str | None:
    """Read Poe API key from poe.md: first line that looks like a key (alphanumeric + underscores)."""
    path = poe_key_file or POE_KEY_FILE
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("http") or len(line) < 20:
            continue
        if re.match(r"^[A-Za-z0-9_-]+$", line):
            return line
    return None


def _log(msg: str, log_path: Path | None = None) -> None:
    """Append a timestamped line to process.log and flush."""
    path = log_path or PROCESS_LOG
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}\n"
    with path.open("a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
    print(msg)


class TextExtractor(HTMLParser):
    """Extract text from HTML, skipping script/style."""
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.in_para = False

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == "p" and attrs_d.get("class") == "ltx_p":
            self.in_para = True

    def handle_endtag(self, tag):
        if tag == "p" and self.in_para:
            self.in_para = False
            self.text_parts.append("\n")

    def handle_data(self, data):
        if self.in_para:
            self.text_parts.append(data)

    def get_text(self):
        return "".join(self.text_parts)


def extract_sentences_from_html(html_path: Path) -> list[str]:
    """Extract paragraph text from LaTeXML HTML (ltx_p)."""
    text = html_path.read_text(encoding="utf-8", errors="replace")
    parser = TextExtractor()
    parser.feed(text)
    raw = parser.get_text()
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    return lines


def parse_template_md(md_path: Path) -> dict:
    """Parse a phrasebank .md: title, source, sections with bullet items."""
    content = md_path.read_text(encoding="utf-8")
    out = {"title": "", "source": "", "sections": []}
    current_section = None
    current_items = []

    for line in content.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            if current_section is not None:
                out["sections"].append({"name": current_section, "items": current_items})
            out["title"] = line.lstrip("# ")
            current_section = None
            current_items = []
        elif line.startswith("## "):
            if current_section is not None:
                out["sections"].append({"name": current_section, "items": current_items})
            current_section = line.lstrip("## ")
            current_items = []
        elif line.strip().startswith("- ") and current_section is not None:
            current_items.append(line.strip()[2:].strip())
        elif line.strip().startswith("*") and "Source:" in line:
            out["source"] = line.strip()
    if current_section is not None:
        out["sections"].append({"name": current_section, "items": current_items})
    return out


def all_template_phrases(data: dict) -> list[str]:
    phrases = []
    for sec in data["sections"]:
        phrases.extend(sec["items"])
    return phrases


def _build_llm_prompt(
    paper_sentences: list[str],
    func_name: str,
    template_data: dict,
    template_sample: list[str],
) -> str:
    """Build the user prompt for the LLM: sentences + function/templates."""
    sentences_block = "\n".join(f"{i+1}. {s}" for i, s in enumerate(paper_sentences))
    templates_block = "\n".join(f"- {t}" for t in template_sample)
    return f"""You are an expert in academic writing and the Manchester Academic Phrasebank.

**Task:** From an academic paper we have extracted a list of sentences (below). We also have a phrasebank "function" (rhetorical role) with example templates. Your job is to:
1. Identify which paper sentences serve a **similar rhetorical function** to the given templates (e.g. introducing work, being critical, describing methods, referring to sources). Match by function and style, not by literal wording.
2. For each matched sentence, optionally suggest a short "extracted template" (generalized phrase with placeholders like X, Y, …) that could be added to the phrasebank.

**Function name:** {func_name}
**Function title:** {template_data['title']}

**Sample phrasebank templates for this function (the full list has more):**
{templates_block}

**Sentences from the paper (numbered):**
{sentences_block}

**Instructions:** Reply with a single JSON object only, no markdown or extra text:
{{
  "matched_sentences": [ "exact sentence 1 from the list", "exact sentence 2", ... ],
  "extracted_templates": [ "template form 1 with X/Y placeholders", "template form 2", ... ]
}}

- "matched_sentences" must be exact copies of sentences from the list above that match this function.
- "extracted_templates" should be one per matched sentence (or fewer if redundant), in generalized form (use X, Y, … for slot fillers).
- If no sentence matches this function, use empty arrays: "matched_sentences": [], "extracted_templates": [].
"""


def get_llm_matches(
    paper_sentences: list[str],
    func_name: str,
    template_data: dict,
    client: "OpenAI",
    model: str = "gpt-4o-mini",
) -> tuple[list[str], list[str]]:
    """
    Ask the LLM which paper sentences match the given function and get extracted templates.
    Returns (matched_sentences, extracted_templates).
    """
    phrases = all_template_phrases(template_data)
    template_sample = phrases[:40]  # keep prompt smaller
    if not paper_sentences:
        return [], []

    all_matched = []
    all_templates = []
    for start in range(0, len(paper_sentences), MAX_SENTENCES_PER_REQUEST):
        chunk = paper_sentences[start : start + MAX_SENTENCES_PER_REQUEST]
        user_content = _build_llm_prompt(chunk, func_name, template_data, template_sample)
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You respond only with a single valid JSON object. No explanation or markdown.",
                    },
                    {"role": "user", "content": user_content},
                ],
                temperature=0.2,
            )
            text = resp.choices[0].message.content.strip()
            # Strip markdown code block if present
            if text.startswith("```"):
                text = re.sub(r"^```(?:json)?\s*", "", text)
                text = re.sub(r"\s*```\s*$", "", text)
            data = json.loads(text)
            all_matched.extend(data.get("matched_sentences") or [])
            all_templates.extend(data.get("extracted_templates") or [])
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            print(f"    [LLM parse error for {func_name}]: {e}")
    return all_matched, all_templates


def generate_report(
    func_name: str,
    template_data: dict,
    paper_id: str,
    out_path: Path,
    similar_sentences: list[str] | None = None,
    extracted_templates: list[str] | None = None,
    process_log: Path | None = None,
) -> None:
    """Write one report .md per function. Uses similar_sentences/extracted_templates if provided."""
    similar = similar_sentences if similar_sentences is not None else []
    extracted = extracted_templates if extracted_templates is not None else []

    lines = [
        f"# Report: {template_data['title']}",
        "",
        f"**Function file:** `{func_name}`",
        f"**Source paper:** `{paper_id}`",
        "",
        "---",
        "",
        "## 1. Original templates (phrasebank)",
        "",
    ]
    if template_data.get("source"):
        lines.append(template_data["source"])
        lines.append("")
    for sec in template_data["sections"]:
        lines.append(f"### {sec['name']}")
        lines.append("")
        for item in sec["items"][:30]:
            lines.append(f"- {item}")
        if len(sec["items"]) > 30:
            lines.append(f"- ... and {len(sec['items']) - 30} more items")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Similar sentences found in the paper")
    lines.append("")
    if not similar:
        lines.append("*Sentence not found.* (No sentence in the paper matched this function's templates.)")
        lines.append("")
    else:
        for s in similar:
            lines.append(f"- {s}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Source of the paper")
    lines.append("")
    lines.append(f"- File: `{paper_id}.html`")
    lines.append(f"- Path: `{HTML_COLLECTION / (paper_id + '.html')}`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. New template extracted from the paper")
    lines.append("")
    if not similar:
        lines.append("*Not applicable — no matching sentence found. Use phrasebank templates above.*")
    elif extracted:
        for t in extracted:
            lines.append(f"- {t}")
    else:
        lines.append("Candidate phrases (from similar sentences above):")
        for s in similar:
            lines.append(f"- {s}")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    _log(f"  wrote {out_path.name}", process_log)


def run_trial(html_basename: str, out_dir: Path, use_llm: bool = True, process_log: Path | None = None) -> None:
    """Run mapping for one HTML file; output reports to out_dir. If use_llm=True, call LLM for matching. Writes to process.log in real time."""
    log_path = process_log or PROCESS_LOG
    _log(f"Starting map_sentences: paper={html_basename}, out_dir={out_dir}", log_path)

    html_path = HTML_COLLECTION / f"{html_basename}.html"
    if not html_path.exists():
        html_path = HTML_COLLECTION / html_basename
    if not html_path.exists():
        _log(f"ERROR: HTML file not found: {html_basename}", log_path)
        raise FileNotFoundError(html_path)
    paper_id = html_path.stem
    paper_sentences = extract_sentences_from_html(html_path)
    # Filter very short fragments
    paper_sentences = [s for s in paper_sentences if len(s.strip()) >= 15]
    _log(f"Paper: {paper_id}, sentences: {len(paper_sentences)}", log_path)
    if paper_sentences:
        _log(f"  sample: {paper_sentences[0][:80]}...", log_path)

    out_dir.mkdir(parents=True, exist_ok=True)
    all_md = list(GENERAL_FUNCTIONS.glob("*.md")) + list(PAPER_SECTIONS.glob("*.md"))

    if use_llm and HAS_OPENAI:
        api_key = os.environ.get("OPENAI_API_KEY")
        base_url = os.environ.get("OPENAI_BASE_URL")
        if not api_key:
            api_key = _read_poe_key()
            if api_key:
                base_url = POE_BASE_URL
                _log("Using Poe API (key from LLM/poe.md).", log_path)
        if not api_key:
            _log("OPENAI_API_KEY not set and no Poe key in LLM/poe.md; falling back to pattern matching (no LLM).", log_path)
            use_llm = False
        else:
            client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)
            model = os.environ.get("MAP_SENTENCES_MODEL", "gpt-4o-mini")
            _log(f"Using LLM for matching (model={model}).", log_path)
    elif use_llm and not HAS_OPENAI:
        _log("Install openai (pip install openai) for LLM matching; falling back to pattern matching.", log_path)
        use_llm = False

    for i, md_path in enumerate(sorted(all_md), 1):
        name = md_path.stem
        _log(f"Processing function {i}/{len(all_md)}: {name}", log_path)
        data = parse_template_md(md_path)
        report_path = out_dir / f"report_{name}.md"
        try:
            if use_llm:
                similar, extracted = get_llm_matches(paper_sentences, name, data, client, model)
                generate_report(name, data, paper_id, report_path, similar_sentences=similar, extracted_templates=extracted, process_log=log_path)
            else:
                phrases = all_template_phrases(data)
                similar = _find_similar_sentences_pattern(paper_sentences, phrases)
                generate_report(name, data, paper_id, report_path, similar_sentences=similar, extracted_templates=None, process_log=log_path)
        except Exception as e:
            _log(f"ERROR in {name}: {e}", log_path)
            raise
    _log(f"Done. Reports in {out_dir}", log_path)


def _find_similar_sentences_pattern(paper_sentences: list[str], template_items: list[str], min_shared: int = 2) -> list[str]:
    """Legacy pattern-based matching (used when LLM is not available)."""
    def normalize(s: str) -> set[str]:
        s = re.sub(r"[^\w\s]", " ", s.lower())
        return set(s.split()) - {"a", "an", "the", "of", "to", "in", "on", "and", "or", "is", "are", "for"}
    similar = []
    template_tokens = [normalize(t) for t in template_items]
    for sent in paper_sentences:
        if not sent or len(sent) < 10:
            continue
        tok = normalize(sent)
        for tt in template_tokens:
            if len(tok & tt) >= min_shared:
                similar.append(sent)
                break
    return similar


if __name__ == "__main__":
    import sys
    html_name = sys.argv[1] if len(sys.argv) > 1 else "2211.12588"
    out = sys.argv[2] if len(sys.argv) > 2 else str(BASE / "trial")
    use_llm = "--pattern" not in sys.argv
    run_trial(html_name, Path(out), use_llm=use_llm)
