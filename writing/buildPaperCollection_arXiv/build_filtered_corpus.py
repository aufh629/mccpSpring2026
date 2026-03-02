#!/usr/bin/env python3
"""
Build a filtered corpus from papers.csv using filter criteria.
Applies filter based on title and abstract matching seed paper topics.
Creates filtered corpus in demo/filteredCorpus with process.log.
"""

import csv
import os
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
CSV_FILE = BASE / "papers.csv"
FILTER_FILE = BASE / "demo" / "filter.md"
FILTERED_CORPUS_DIR = BASE / "demo" / "filteredCorpus"
FILTERED_LOG = FILTERED_CORPUS_DIR / "process.log"
HTML_DIR = BASE / "html_collection"

# Filter keywords - topics related to multi-agent collaboration, LLM agents, recommendations
FILTER_KEYWORDS = {
    "agent": 5,
    "multi-agent": 8,
    "collaboration": 6,
    "cooperative": 5,
    "recommendation": 7,
    "recommender": 7,
    "llm": 5,
    "language model": 6,
    "autonomous": 4,
    "reasoning": 4,
    "task planning": 6,
    "decision-making": 5,
    "interactive": 4,
    "framework": 3,
    "system": 2,
}

def read_filter():
    """Read filter preferences from filter.md."""
    if FILTER_FILE.exists():
        return FILTER_FILE.read_text(encoding="utf-8")
    return ""

def score_paper(title, abstract):
    """Score paper based on keyword matching. Higher score = more relevant."""
    text = f"{title} {abstract}".lower()
    score = 0
    matched_keywords = []
    
    for keyword, weight in FILTER_KEYWORDS.items():
        if keyword in text:
            count = text.count(keyword)
            score += count * weight
            matched_keywords.append((keyword, count * weight))
    
    return score, matched_keywords

def log_message(msg):
    """Write to process.log with timestamp."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}\n"
    with open(FILTERED_LOG, "a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
    print(msg)

def main():
    # Create output directory
    FILTERED_CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Initialize log
    with open(FILTERED_LOG, "w", encoding="utf-8") as f:
        f.write(f"=== Filtered Paper Corpus Build started {datetime.now().isoformat()} ===\n")
        f.write("Filter: Multi-agent systems, LLM-based agents, recommendation systems\n")
        f.write("Criteria: Title and abstract keyword matching\n")
        f.write("-" * 70 + "\n")
    
    filter_desc = read_filter()
    log_message(f"Filter criteria: {filter_desc.strip()}")
    log_message("=" * 70)
    
    # Read all papers
    papers = []
    if not CSV_FILE.exists():
        log_message(f"ERROR: {CSV_FILE} not found!")
        return
    
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        papers = list(reader)
    
    log_message(f"Total papers in corpus: {len(papers)}")
    log_message("Scoring and filtering papers...")
    log_message("")
    
    # Score and filter papers
    scored_papers = []
    for i, paper in enumerate(papers, 1):
        arxiv_id = paper["arxiv_id"]
        title = paper["title"]
        abstract = paper["abstract"]
        
        score, keywords = score_paper(title, abstract)
        scored_papers.append({
            **paper,
            "filter_score": score,
            "matched_keywords": keywords
        })
        
        if score > 0:  # Include all papers with at least one match
            keyword_str = ", ".join([f"{kw}({cnt})" for kw, cnt in sorted(keywords, key=lambda x: x[1], reverse=True)[:5]])
            log_message(f"[{i}/100] {arxiv_id} | Score: {score:3d} | Keywords: {keyword_str}")
            log_message(f"        Title: {title[:70]}...")
    
    # Filter to papers with score > 0
    filtered = [p for p in scored_papers if p["filter_score"] > 0]
    filtered_sorted = sorted(filtered, key=lambda x: x["filter_score"], reverse=True)
    
    log_message("")
    log_message("=" * 70)
    log_message(f"Papers matching filter criteria: {len(filtered_sorted)}/{len(papers)}")
    log_message(f"Pass rate: {len(filtered_sorted)/len(papers)*100:.1f}%")
    log_message("")
    
    # Write filtered papers to CSV
    filtered_csv = FILTERED_CORPUS_DIR / "papers.csv"
    fieldnames = list(papers[0].keys()) + ["filter_score", "matched_keywords"]
    
    with open(filtered_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for paper in filtered_sorted:
            # Format matched_keywords for CSV
            keywords_str = ";".join([f"{kw}({cnt})" for kw, cnt in paper["matched_keywords"]])
            paper["matched_keywords"] = keywords_str
            writer.writerow(paper)
    
    log_message(f"Wrote filtered papers to: {filtered_csv}")
    
    # Copy HTML files for filtered papers
    html_copied = 0
    for paper in filtered_sorted:
        arxiv_id = paper["arxiv_id"]
        src_html = HTML_DIR / f"{arxiv_id}.html"
        if src_html.exists():
            dest_html = FILTERED_CORPUS_DIR / f"{arxiv_id}.html"
            dest_html.write_bytes(src_html.read_bytes())
            html_copied += 1
    
    log_message(f"Copied {html_copied} HTML files to: {FILTERED_CORPUS_DIR}/")
    
    # Summary statistics
    log_message("")
    log_message("=" * 70)
    log_message("TOP 10 PAPERS BY FILTER SCORE:")
    log_message("-" * 70)
    for i, paper in enumerate(filtered_sorted[:10], 1):
        matched = paper["matched_keywords"]
        if isinstance(matched, str):
            keywords_str = matched
        else:
            keywords_str = ";".join([f"{kw}({cnt})" for kw, cnt in matched[:3]])
        log_message(f"{i:2d}. [{paper['filter_score']:3d}] {paper['arxiv_id']} - {paper['title'][:60]}...")
        log_message(f"     Keywords: {keywords_str}")
    
    log_message("")
    log_message("=" * 70)
    log_message("EXCLUDED PAPERS (score = 0):")
    log_message("-" * 70)
    excluded = [p for p in scored_papers if p["filter_score"] == 0]
    for i, paper in enumerate(excluded[:10], 1):
        log_message(f"{i:2d}. {paper['arxiv_id']} - {paper['title'][:60]}...")
    
    if len(excluded) > 10:
        log_message(f"... and {len(excluded) - 10} more excluded papers")
    
    log_message("")
    log_message("=" * 70)
    log_message(f"FILTERING COMPLETE")
    log_message(f"Total papers: {len(papers)}")
    log_message(f"Included papers: {len(filtered_sorted)}")
    log_message(f"Excluded papers: {len(excluded)}")
    log_message(f"Process log: {FILTERED_LOG}")
    log_message(f"Filtered corpus: {FILTERED_CORPUS_DIR}/")
    log_message(f"Done.")

if __name__ == "__main__":
    main()
