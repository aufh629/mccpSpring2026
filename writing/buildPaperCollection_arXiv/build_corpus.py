#!/usr/bin/env python3
"""
Build a corpus of papers from arXiv, starting from a seed paper.
Expands by following citations; for venue papers (ACM, IEEE, etc.) searches arXiv by title.
Stops at N papers. Logs process in real time to process.log.
Saves HTML to html_collection/, bibliographic info to papers.csv.
"""
from __future__ import annotations

import csv
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parent
HTML_DIR = BASE / "html_collection"
LOG_FILE = BASE / "process.log"
RATE_LIMIT = 3  # seconds between requests (arXiv guideline)
MAX_PAPERS = 100
ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}

# Venue patterns: papers from mainstream journals/conferences (search arXiv by title)
VENUE_PATTERNS = re.compile(
    r"\.\s+(?:In\s+|Proceedings\s+of|ACM\s|IEEE\s|Conference\s+on|Transactions\s+on|"
    r"Advances\s+in|Journal\s+of|Nature\s|WWW\s|SIGIR|KDD|NeurIPS|ICML|ACL|EMNLP|NAACL|"
    r"RecSys|CIKM|WSDM|ICDE|CVPR|ICCV|ECCV)",
    re.I
)


def log(msg: str) -> None:
    """Append to process log in real time (flush for immediate visibility)."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
    print(msg, flush=True)


def _base_id(aid: str) -> str:
    """Strip version suffix (v1, v2) - arXiv HTML URL uses base ID only."""
    return re.sub(r"v\d+$", "", aid)

def fetch_html(arxiv_id: str) -> str | None:
    """Fetch paper HTML from arXiv. Returns HTML string or None."""
    base = _base_id(arxiv_id)
    url = f"https://arxiv.org/html/{base}"
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"  [ERROR] fetch {arxiv_id}: {e}")
        return None


def fetch_metadata(arxiv_id: str) -> dict | None:
    """Fetch paper metadata from arXiv API."""
    base = _base_id(arxiv_id)
    url = f"http://export.arxiv.org/api/query?id_list={base}"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        root = ET.fromstring(r.content)
        entry = root.find("atom:entry", ARXIV_NS)
        if entry is None:
            return None
        title = _get_text(entry, "atom:title")
        summary = _get_text(entry, "atom:summary")
        authors = [
            a.text.strip()
            for a in entry.findall("atom:author", ARXIV_NS)
            if a.find("atom:name", ARXIV_NS) is not None
        ]
        published = _get_text(entry, "atom:published", default="")[:4]
        return {
            "arxiv_id": base,
            "title": (title or "").replace("\n", " ").strip(),
            "authors": "; ".join(authors) if authors else "",
            "year": published,
            "abstract": (summary or "").replace("\n", " ").strip(),
            "url": f"https://arxiv.org/abs/{base}",
        }
    except Exception as e:
        print(f"  [ERROR] metadata {arxiv_id}: {e}")
        return None


def _get_text(elem, tag: str, default: str = "") -> str:
    if elem is None:
        return default
    e = elem.find(tag, ARXIV_NS)
    return (e.text or "") + "".join((t.tail or "") for t in e.iter()) if e is not None else default


def search_arxiv_by_title(title: str, max_results: int = 3) -> list[str]:
    """Search arXiv by title, return list of arxiv_ids."""
    if not title or len(title) < 10:
        return []
    # Use first 80 chars, escape for query
    query = title[:80].replace('"', "").strip()
    url = f"http://export.arxiv.org/api/query?search_query=ti:{quote_plus(query)}&start=0&max_results={max_results}"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        root = ET.fromstring(r.content)
        ids = []
        for entry in root.findall("atom:entry", ARXIV_NS):
            id_elem = entry.find("atom:id", ARXIV_NS)
            if id_elem is not None and id_elem.text:
                aid = id_elem.text.strip().split("/abs/")[-1]
                ids.append(_base_id(aid))
        return ids
    except Exception as e:
        print(f"  [WARN] search '{title[:40]}...': {e}")
        return []


def extract_references(html: str) -> list[tuple[str, str | None]]:
    """
    Extract references from arXiv HTML. Returns [(title_or_id, arxiv_id or None), ...].
    - Refs with arXiv ID: (arxiv_id, arxiv_id)
    - Venue papers (ACM, IEEE, Proceedings, etc.): (title, None) for arXiv title search
    """
    refs = []
    seen_ids: set[str] = set()
    seen_titles: set[str] = set()

    # 1. Collect arXiv IDs (direct)
    for m in re.finditer(r"arXiv[:\s]*(?:preprint\s*)?(\d{4}\.\d{4,5})", html, re.I):
        aid = m.group(1)
        if aid not in seen_ids:
            seen_ids.add(aid)
            refs.append((aid, aid))

    # 2. Parse References section for venue papers (ACM, IEEE, Proceedings, etc.) -> search arXiv by title
    soup = BeautifulSoup(html, "html.parser")
    for bibitem in soup.find_all("li", class_=re.compile(r"ltx_bibitem|bibitem")):
        text = bibitem.get_text(separator=" ", strip=True)
        if "arXiv" in text or len(text) < 30:
            continue
        if not VENUE_PATTERNS.search(text):
            continue
        # Format: "Author (year). Names. year. TITLE. In Proceedings of ..."
        # Extract title: segment before ". In " (venue start)
        for pat in [
            r"\d{4}[a-z]?\.\s+(.+?)\.\s+In\s+",
            r"\)\s+[^.]+\.[^.]*\.\s+(.+?)\.\s+In\s+",
            r"\.\s+([^.]+(?:\?[^.]+)?)\.\s+In\s+(?:Proceedings|Proceedings of)",
        ]:
            m = re.search(pat, text, re.I | re.DOTALL)
            if m:
                title = m.group(1).strip()
                title = re.sub(r"\s+", " ", title)
                if len(title) > 15 and len(title) < 200:
                    norm = title.lower()[:80]
                    if norm not in seen_titles:
                        seen_titles.add(norm)
                        refs.append((title, None))
                break

    return refs


def _write_csv(corpus: list[dict], found_from: dict[str, str]) -> None:
    """Write corpus to papers.csv."""
    csv_path = BASE / "papers.csv"
    rows = [{**m, "found_from": found_from.get(m["arxiv_id"], "")} for m in corpus]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["arxiv_id", "title", "authors", "year", "abstract", "url", "found_from"],
        )
        w.writeheader()
        w.writerows(rows)


def main():
    HTML_DIR.mkdir(exist_ok=True)

    # Seed: 2402.15235 (from html_collection)
    seed_arxiv = "2402.15235"

    # Initialize process log (real-time updates)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"=== Paper corpus build started {datetime.now().isoformat()} ===\n")
        f.write(f"Max papers: {MAX_PAPERS}, seed: {seed_arxiv}\n")
        f.write("Format: [timestamp] message | found_from=source_arxiv_id\n")
        f.write("-" * 60 + "\n")

    seen: set[str] = set()
    queue: list[tuple[str, str]] = [(seed_arxiv, "SEED")]
    corpus: list[dict] = []
    found_from: dict[str, str] = {}

    log(f"Building corpus (max {MAX_PAPERS} papers), seed: {seed_arxiv}")
    log("=" * 50)

    while queue and len(corpus) < MAX_PAPERS:
        arxiv_id, source = queue.pop(0)
        if arxiv_id in seen:
            continue
        base_id = _base_id(arxiv_id)
        seen.add(base_id)
        found_from[base_id] = source

        log(f"[{len(corpus)+1}/{MAX_PAPERS}] Processing {arxiv_id} (found from: {source})")

        meta = fetch_metadata(base_id)
        time.sleep(RATE_LIMIT)
        if not meta:
            log(f"  SKIP {arxiv_id}: metadata fetch failed")
            continue

        html = fetch_html(base_id)
        time.sleep(RATE_LIMIT)
        if html:
            (HTML_DIR / f"{base_id.replace('/', '_')}.html").write_text(html, encoding="utf-8")
            log(f"  Saved HTML: {arxiv_id}.html")

        corpus.append(meta)
        log(f"  Added: {meta['title'][:70]}...")

        # Periodic CSV save (every 20 papers) to preserve progress
        if len(corpus) % 20 == 0:
            _write_csv(corpus, found_from)

        if len(corpus) >= MAX_PAPERS:
            break

        if html:
            refs = extract_references(html)
            queued_ids = {q[0] for q in queue}
            for title_or_id, rid in refs:
                if len(corpus) + len(queue) >= MAX_PAPERS:
                    break
                rid_base = _base_id(rid) if rid else None
                if rid and rid_base not in seen and rid_base not in queued_ids:
                    queue.append((rid_base, base_id))
                    queued_ids.add(rid_base)
                    log(f"  FOUND arXiv ref -> {rid} | cited_by={arxiv_id}")
                elif not rid and title_or_id:
                    found = search_arxiv_by_title(title_or_id)
                    time.sleep(RATE_LIMIT)
                    for fid in found:
                        fid_base = _base_id(fid)
                        if fid_base not in seen and fid_base not in queued_ids:
                            queue.append((fid_base, base_id))
                            queued_ids.add(fid_base)
                            log(f"  FOUND via title search '{title_or_id[:50]}...' -> {fid} | cited_by={arxiv_id}")
                            break

    if corpus:
        _write_csv(corpus, found_from)
        log(f"Wrote {len(corpus)} papers to {BASE / 'papers.csv'}")
    log(f"HTML files in {HTML_DIR}/")
    log(f"Process log: {LOG_FILE}")
    log("Done.")


if __name__ == "__main__":
    main()
