#!/usr/bin/env python3
"""
Download HTML version of paper from arXiv.
For COCO paper: arXiv 2310.18955v3 (NeurIPS 2024).
"""

import requests
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

# COCO paper (matches COCO_2310.18955v3.pdf in this folder)
ARXIV_ID = "2310.18955v3"
OUTPUT_HTML = OUTPUT_DIR / "COCO_2310.18955v3_from_arxiv.html"


def download_arxiv_html(arxiv_id: str, output_path: Path) -> bool:
    url = f"https://arxiv.org/html/{arxiv_id}"
    print(f"  Fetching: {url}")
    try:
        response = requests.get(
            url,
            timeout=90,
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"},
        )
        response.raise_for_status()
        if "text/html" not in response.headers.get("Content-Type", "").lower():
            print(f"  ⚠ Content-Type: {response.headers.get('Content-Type')}")
        text = response.text
        output_path.write_text(text, encoding="utf-8")
        print(f"  ✓ Saved: {output_path.name} ({len(text):,} bytes)")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    print("Downloading HTML from arXiv\n")
    success = download_arxiv_html(ARXIV_ID, OUTPUT_HTML)
    print("\nDone." if success else "\nDownload failed.")


if __name__ == "__main__":
    main()
