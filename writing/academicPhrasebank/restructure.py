#!/usr/bin/env python3
"""
Restructure academic phrasebank: organize into folders, deduplicate, clean format.
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent

PAPER_SECTIONS = [
    "introducing-work",
    "referring-to-sources",
    "describing-methods",
    "reporting-results",
    "discussing-findings",
    "writing-conclusions",
]

GENERAL_FUNCTIONS = [
    "using-cautious-language",
    "being-critical",
    "classifying-and-listing",
    "compare-and-contrast",
    "writing-definitions",
    "describing-trends",
    "describing-quantities",
    "explaining-cause-and-effect",
    "giving-examples",
    "signalling-transition",
    "writing-about-the-past",
]

# Noise patterns to remove
NOISE = [
    "GENERAL LANGUAGE FUNCTIONS",
    "Being cautious",
    "Being critical",
    "Classifying and listing",
    "Compare and contrast",
    "Defining terms",
    "Describing trends",
    "Describing quantities",
    "Explaining causality",
    "Giving examples",
    "Signalling transition",
    "Writing about the past",
    "An enhanced and expanded version",
    "ABOUT PHRASEBANK",
    "Contact Us",
    "Find Us",
    "Connect With Us",
    "The University of Manchester",
    "Oxford Rd",
    "Manchester",
    "M13 9PL",
    "UK",
    "+44 (0) 161 306 6000",
]


def is_noise(line: str) -> bool:
    line = line.strip()
    if len(line) < 5:
        return True
    for n in NOISE:
        if n in line or line.startswith("Academic Phrasebank /"):
            return True
    return False


def extract_sections(content: str) -> list[tuple[str, list[str]]]:
    """Split content by ####/##### headings. Return [(heading, [phrases]), ...]."""
    sections = []
    # Split by ##### or #### headings
    blocks = re.split(r"\n(#{4,6})\s+", content)
    seen_headings = set()

    i = 1
    while i < len(blocks):
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
        i += 2
        if not body.strip():
            continue

        lines = body.split("\n")
        heading = lines[0].strip()
        rest = "\n".join(lines[1:])

        if not heading or heading in seen_headings or len(heading) > 120:
            continue
        if is_noise(heading) or "Contact" in heading or "Find Us" in heading:
            continue
        seen_headings.add(heading)

        phrases = split_phrases_block(rest)
        if phrases:
            sections.append((heading, phrases))

    # Fallback: find ##### in content and extract
    if not sections:
        for m in re.finditer(r"#####\s+(.+?)\n(.*?)(?=#####|\Z)", content, re.DOTALL):
            heading, body = m.group(1).strip(), m.group(2)
            if is_noise(heading):
                continue
            phrases = split_phrases_block(body)
            if phrases:
                sections.append((heading, phrases))

    return sections


def split_phrases_block(text: str) -> list[str]:
    """Split run-on phrase block into individual phrases."""
    # Phrases often end with … or . or are separated by " X " patterns
    phrases = []
    # Split on sentence boundaries: … . | (for template alternation)
    parts = re.split(r"\s+…\s+|\s+\.{3}\s+", text)
    for p in parts:
        p = p.strip()
        if p and len(p) > 10 and not is_noise(p):
            if not p.endswith("…") and not p.endswith("."):
                p = p + " …"
            phrases.append(p)
    if not phrases:
        for s in re.split(r"\.\s+(?=[A-Z])", text):
            s = s.strip()
            if s and len(s) > 20:
                phrases.append(s + ("." if not s.endswith(".") else ""))
    # Deduplicate preserving order
    seen = set()
    out = []
    for p in phrases:
        norm = re.sub(r"\s+", " ", p).strip()
        if norm not in seen and len(norm) > 12:
            seen.add(norm)
            out.append(p)
    return out[:100]


def process_file(path: Path) -> str:
    """Read file, deduplicate, extract sections. Return clean markdown."""
    raw = path.read_text(encoding="utf-8")

    # Remove first header line and source URL
    lines = raw.split("\n")
    start = 0
    for i, ln in enumerate(lines):
        if "Source: http" in ln or ln.startswith("# Academic Phrasebank"):
            start = i + 1
            break

    content = "\n".join(lines[start:])

    # Extract main title from first # heading
    title_match = re.search(r"^#\s+(.+?)(?:\s*\||$)", content, re.M)
    title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()

    sections = extract_sections(content)

    # If extract_sections didn't find #### style, try splitting by " ##### " in raw
    if not sections:
        # Fallback: split by lines that look like section titles (Title Case long phrase)
        block = content
        for noise in NOISE:
            block = block.replace(noise, "")
        # Split on "Category name" followed by phrases
        parts = re.split(r"(?=[A-Z][a-z]+(?:\s+[a-z]+)*:)", block)
        for p in parts:
            p = p.strip()
            if len(p) > 50:
                first_line = p.split("\n")[0][:80]
                rest = "\n".join(p.split("\n")[1:])
                phrases = split_phrases_block(rest)
                if phrases:
                    sections.append((first_line, phrases))

    out = [f"# {title}", "", f"*Source: https://www.phrasebank.manchester.ac.uk/{path.stem}/*", ""]

    for heading, phrases in sections:
        if not heading or heading.startswith("Contact") or "Find Us" in heading:
            continue
        out.append(f"## {heading}")
        out.append("")
        # Deduplicate phrases
        seen_p = set()
        for p in phrases:
            norm = re.sub(r"\s+", " ", p).strip()
            if norm in seen_p:
                continue
            seen_p.add(norm)
            # Format as bullet; handle template alternations (X | Y | Z)
            if "|" in p and len(p) < 150:
                out.append(f"- {p}")
            else:
                out.append(f"- {p}")
        out.append("")

    return "\n".join(out).strip()


def slugify(s: str) -> str:
    return re.sub(r"[^\w\-]+", "-", s.lower()).strip("-")[:60]


def main():
    (BASE / "paper-sections").mkdir(exist_ok=True)
    (BASE / "general-functions").mkdir(exist_ok=True)

    paper_links = []
    general_links = []

    raw_dir = BASE / "raw"
    for slug in PAPER_SECTIONS:
        src = raw_dir / f"{slug}.md" if (raw_dir / f"{slug}.md").exists() else BASE / f"{slug}.md"
        if not src.exists():
            continue
        md = process_file(src)
        dst = BASE / "paper-sections" / f"{slug}.md"
        dst.write_text(md, encoding="utf-8")
        title = slug.replace("-", " ").title()
        paper_links.append(f"- [{title}](paper-sections/{slug}.md)")

    for slug in GENERAL_FUNCTIONS:
        src = raw_dir / f"{slug}.md" if raw_dir.exists() and (raw_dir / f"{slug}.md").exists() else BASE / f"{slug}.md"
        if not src.exists():
            continue
        md = process_file(src)
        dst = BASE / "general-functions" / f"{slug}.md"
        dst.write_text(md, encoding="utf-8")
        title = slug.replace("-", " ").title()
        general_links.append(f"- [{title}](general-functions/{slug}.md)")

    # About and index
    for slug in ["about-academic-phrasebank", "index"]:
        src = BASE / f"{slug}.md"
        if src.exists():
            md = process_file(src)
            (BASE / f"{slug}.md").write_text(md, encoding="utf-8")

    # README
    # Move original flat topic files to raw/ after processing (if still in root)
    (BASE / "raw").mkdir(exist_ok=True)
    for slug in PAPER_SECTIONS + GENERAL_FUNCTIONS:
        src = BASE / f"{slug}.md"
        if src.exists():
            src.rename(BASE / "raw" / f"{slug}.md")

    readme = f"""# Academic Phrasebank

Crawled and restructured from [The University of Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/).

## Structure

### Paper sections (research article structure)
{chr(10).join(paper_links)}

### General language functions
{chr(10).join(general_links)}

### Meta
- [About](about-academic-phrasebank.md)
- [Index / Home](index.md)

## Retrieval

Each file is organised by **section headings** (##) with **phrases as bullet points** (-). Use headings to navigate and grep for specific phrases.
"""
    (BASE / "README.md").write_text(readme, encoding="utf-8")

    print(f"Restructured: {len(paper_links)} paper sections, {len(general_links)} general functions")
    print("Output: paper-sections/, general-functions/, README.md")


if __name__ == "__main__":
    main()
