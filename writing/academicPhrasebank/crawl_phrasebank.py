#!/usr/bin/env python3
"""Crawl Manchester Academic Phrasebank and save all content as markdown."""
import re
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.phrasebank.manchester.ac.uk"
OUT_DIR = Path(__file__).resolve().parent

# All known page URLs from site structure
PAGES = [
    ("index", f"{BASE_URL}/"),
    ("introducing-work", f"{BASE_URL}/introducing-work/"),
    ("referring-to-sources", f"{BASE_URL}/referring-to-sources/"),
    ("describing-methods", f"{BASE_URL}/describing-methods/"),
    ("reporting-results", f"{BASE_URL}/reporting-results/"),
    ("discussing-findings", f"{BASE_URL}/discussing-findings/"),
    ("writing-conclusions", f"{BASE_URL}/writing-conclusions/"),
    ("using-cautious-language", f"{BASE_URL}/using-cautious-language/"),
    ("being-critical", f"{BASE_URL}/being-critical/"),
    ("classifying-and-listing", f"{BASE_URL}/classifying-and-listing/"),
    ("compare-and-contrast", f"{BASE_URL}/compare-and-contrast/"),
    ("writing-definitions", f"{BASE_URL}/writing-definitions/"),
    ("describing-trends", f"{BASE_URL}/describing-trends/"),
    ("describing-quantities", f"{BASE_URL}/describing-quantities/"),
    ("explaining-cause-and-effect", f"{BASE_URL}/explaining-cause-and-effect/"),
    ("giving-examples", f"{BASE_URL}/giving-examples/"),
    ("signalling-transition", f"{BASE_URL}/signalling-transition/"),
    ("writing-about-the-past", f"{BASE_URL}/writing-about-the-past-2/"),
    ("about-academic-phrasebank", f"{BASE_URL}/about-academic-phrasebank/"),
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def slugify(s: str) -> str:
    return re.sub(r"[^\w\-]", "_", s.lower()).strip("_")[:80]


def html_to_md(soup: BeautifulSoup) -> str:
    """Extract main content as markdown-friendly text."""
    # Phrasebank uses .et_pb_post_content or main article area
    main = (
        soup.find("main")
        or soup.find("article")
        or soup.find("div", class_=re.compile(r"et_pb_post_content|content|entry|post"))
    )
    if not main:
        main = soup.find("div", class_="entry-content") or soup.body
    if not main:
        return soup.get_text(separator="\n", strip=True)

    # Remove nav, footer, scripts, sidebar
    for tag in main.find_all(["nav", "footer", "script", "style", "aside", "header"]):
        tag.decompose()

    def get_text(el):
        return el.get_text(separator=" ", strip=True)

    lines = []
    for el in main.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "ul", "ol", "table", "div"]):
        if el.name.startswith("h"):
            level = int(el.name[1])
            t = get_text(el)
            if t:
                lines.append(f"\n{'#' * level} {t}\n")
        elif el.name == "p":
            t = get_text(el)
            if t and len(t) > 10:
                lines.append(t + "\n")
        elif el.name == "li":
            t = get_text(el)
            if t:
                lines.append(f"- {t}\n")
        elif el.name in ("ul", "ol"):
            pass
        elif el.name == "table":
            for row in el.find_all("tr"):
                cells = [get_text(c) for c in row.find_all(["th", "td"])]
                if cells:
                    lines.append(" | ".join(cells) + "\n")
        elif el.name == "div" and "et_pb_" in str(el.get("class", [])):
            # Divi builder blocks - get direct text
            t = get_text(el)
            if t and len(t) > 30 and t not in [l.strip() for l in lines if l.strip()]:
                lines.append(t + "\n")

    text = "\n".join(lines)
    text = text.replace("&#8230;", "...").replace("&#039;", "'").replace("&amp;", "&").replace("&nbsp;", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_page(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.text


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update(HEADERS)

    fetched = []
    for slug, url in PAGES:
        try:
            print(f"Fetching {slug}...")
            html = session.get(url, timeout=30).text
            soup = BeautifulSoup(html, "html.parser")
            md = html_to_md(soup)
            title = soup.title.string if soup.title else slug
            content = f"# {title}\n\nSource: {url}\n\n{md}"
            path = OUT_DIR / f"{slug}.md"
            path.write_text(content, encoding="utf-8")
            fetched.append((slug, url, path))
            time.sleep(0.8)
        except Exception as e:
            print(f"  ERROR {slug}: {e}")

    # Index file
    index_lines = ["# Academic Phrasebank (Crawled)\n", f"Source: {BASE_URL}\n"]
    for slug, url, _ in fetched:
        index_lines.append(f"- [{slug}]({slug}.md) - {url}\n")
    (OUT_DIR / "INDEX.md").write_text("".join(index_lines), encoding="utf-8")
    print(f"\nDone. Saved {len(fetched)} pages to {OUT_DIR}")


if __name__ == "__main__":
    main()
