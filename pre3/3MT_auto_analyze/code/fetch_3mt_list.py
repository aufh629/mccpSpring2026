#!/usr/bin/env python3
"""
Fetch 3 Minute Thesis videos from YouTube search and write 3MTlist.csv.
Uses yt-dlp for search (no API key). Speaker is parsed from title when possible.
"""
import subprocess
import json
import csv
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CSV_PATH = SCRIPT_DIR / "3MTlist.csv"
SEARCH_QUERY = "3 minute thesis"
MAX_RESULTS = 20  # increase for a longer list


def extract_speaker_from_title(title: str, channel: str) -> str:
    """Try to get speaker name from common 3MT title patterns."""
    if not title:
        return channel or ""
    # "by Emily Johnston" / "by X"
    m = re.search(r"\bby\s+([^|–\-]+?)(?:\s*[|–\-]|$)", title, re.I)
    if m and "thesis" not in m.group(1).lower():
        return m.group(1).strip()
    # "Favour Nerrise, 1st Place" / "Name, 1st Place" (name before comma, not "3 Minute Thesis")
    m = re.search(r"[|]\s*([^|,]+?),?\s*(?:1st|2nd|3rd|\d+(?:st|nd|rd|th))\s+Place", title, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"(?:3MT|3 Minute Thesis)[^|]*[|]\s*([^|,]+?),?\s*(?:1st|2nd|3rd)", title, re.I)
    if m:
        return m.group(1).strip()
    # "Winner Esther Li" / "Winner X"
    m = re.search(r"Winner\s+([A-Za-z][A-Za-z\s]{1,40}?)(?:\s*[|–\-]|$)", title, re.I)
    if m and "thesis" not in m.group(1).lower():
        return m.group(1).strip()
    # "Winner - Matthew Thompson" / "Winner - Name"
    m = re.search(r"Winner\s*[–\-]\s*([A-Za-z][A-Za-z\s]+?)(?:\s*[|–\-]|$)", title, re.I)
    if m:
        return m.group(1).strip()
    # "Imogen Swift: 'Topic'" / "Name: 'Topic'"
    m = re.search(r"–\s*([A-Za-z][A-Za-z\s]+?):\s*['\"]", title)
    if m:
        return m.group(1).strip()
    # "Maria Caluianu - 2022 UCL" / "Name - Year Institution"
    m = re.search(r"([A-Za-z][A-Za-z\s]{2,35}?)\s*[–\-]\s*\d{4}\s+", title)
    if m and "thesis" not in m.group(1).lower() and "minute" not in m.group(1).lower():
        return m.group(1).strip()
    # "Siti Aimi Sarah Zainal Abidin (UPM)" / "Name (Institution)"
    m = re.search(r"([A-Za-z][A-Za-z\s]{2,50}?)\s*\([A-Za-z0-9]+\)", title)
    if m and "thesis" not in m.group(1).lower():
        return m.group(1).strip()
    # "Willemijn Doedens" after "Winner - "
    m = re.search(r"Winner\s*[–\-]\s*([A-Za-z][A-Za-z\s]+?)(?:\s*$|\s*[|])", title, re.I)
    if m:
        return m.group(1).strip()
    # "Niamh MacSweeney" in "Topic | 3MT | Niamh MacSweeney"
    m = re.search(r"[|]\s*([A-Za-z][A-Za-z\s]{2,40}?)\s*$", title)
    if m and "thesis" not in m.group(1).lower():
        return m.group(1).strip()
    # "PENG Yingying" in "2nd Runner-up | PENG Yingying"
    m = re.search(r"(?:Runner-up|Place)\s*[|]\s*([A-Za-z\s]+?)\s*$", title)
    if m:
        return m.group(1).strip()
    # "2013 Three Minute Thesis Winner - Sharon Savage" -> Sharon Savage
    m = re.search(r"Winner\s*[–\-]\s*([A-Za-z][A-Za-z\s]+?)\s*$", title, re.I)
    if m:
        return m.group(1).strip()
    # "Deepanjali Mishra - 2025" style
    m = re.search(r"([A-Za-z][A-Za-z\s]{2,40}?)\s*[–\-]\s*\d{4}\s+Three", title, re.I)
    if m:
        return m.group(1).strip()
    # Fallback: last segment after " - " if it looks like a name (no digits/year)
    if " - " in title:
        part = title.split(" - ")[-1].strip()
        if 3 <= len(part) <= 45 and re.match(r"^[A-Za-z][A-Za-z\s]+$", part) and "thesis" not in part.lower():
            return part
    return ""  # leave blank; user can fill


def main():
    print(f"Searching YouTube for: {SEARCH_QUERY} (max {MAX_RESULTS} results)")
    cmd = [
        "python3", "-m", "yt_dlp",
        f"ytsearch{MAX_RESULTS}:{SEARCH_QUERY}",
        "--flat-playlist", "-j", "--no-warnings"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=SCRIPT_DIR)
    if result.returncode != 0:
        print("yt-dlp error:", result.stderr or result.stdout)
        return 1

    lines = [l.strip() for l in result.stdout.strip().split("\n") if l.strip()]
    rows = []
    for line in lines:
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if data.get("_type") != "url":
            continue
        title = data.get("title") or ""
        url = data.get("url") or data.get("webpage_url") or ""
        channel = data.get("channel") or data.get("uploader") or ""
        speaker = extract_speaker_from_title(title, channel)
        if not speaker:
            speaker = channel  # fallback to channel as institution/speaker
        rows.append({"title": title, "speaker": speaker, "url": url})

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["title", "speaker", "url"])
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {CSV_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
