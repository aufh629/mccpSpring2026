#!/usr/bin/env python3
"""
Download PDFs from arXiv for papers in this folder.
Papers: arXiv 2310.18955v3 (COCO, NeurIPS 2024), 2412.10703v21 (AAAI 2025).
"""

import requests
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

# arXiv IDs already in this folder (from tarballs)
PAPERS = [
    {"arxiv_id": "2310.18955v3", "name": "COCO_NeurIPS24", "filename": "COCO_2310.18955v3.pdf"},
    {"arxiv_id": "2412.10703", "name": "AAAI25_COLDQ", "filename": "aaai25_2412.10703.pdf"},
]


def download_arxiv_pdf(arxiv_id: str, output_path: Path) -> bool:
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"  Downloading: {pdf_url}")
    try:
        response = requests.get(pdf_url, timeout=90, stream=True)
        response.raise_for_status()
        content = response.content
        if content[:4] != b"%PDF":
            print(f"  ✗ Not a PDF (got {content[:50]!r})")
            return False
        output_path.write_bytes(content)
        print(f"  ✓ Saved: {output_path.name} ({len(content):,} bytes)")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    print("WYQ* literature: downloading arXiv PDFs\n")
    for p in PAPERS:
        print(f"  [{p['name']}] arXiv {p['arxiv_id']}")
        out = OUTPUT_DIR / p["filename"]
        if out.exists():
            print(f"  (already exists: {out.name}, skipping)")
            continue
        download_arxiv_pdf(p["arxiv_id"], out)
    print("\nDone.")


if __name__ == "__main__":
    main()
