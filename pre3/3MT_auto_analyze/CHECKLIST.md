# 3MT workflow – sub-tasks and checklist

Based on [idea.md](idea.md). Tick items as you complete them.

---

## Phase 1: Discover 3MT videos and build the list

- [x] **1.1** Decide how to find 3MT videos (e.g. YouTube search "3 minute thesis", or a known playlist/channel).
- [x] **1.2** Fetch/copy a set of 3MT video URLs (manual list or script using yt-dlp/API/search).
- [x] **1.3** For each video, get **title** and **speaker** (from title, description, or channel).
- [x] **1.4** Create **3MTlist.csv** with columns: `title`, `speaker`, `url` (and optional: `video_id`, `year`, `institution`).
- [x] **1.5** Save 3MTlist.csv in `ProcessYoutube/3MT/` (or a path you choose).

---

## Phase 2: Download one full example

- [x] **2.1** Pick one row from 3MTlist.csv as the "example" video (Emily Johnston 2014, video_id dh0pJdgY6Lc).
- [x] **2.2** Create a dedicated folder for that video (e.g. `3MT/output/<video_id>/` or `3MT/sample/<speaker_title>/`).
- [x] **2.3** Run the existing pipeline (e.g. set URL in `scripts/youtube_capture.py` and run it, or add a wrapper script that reads URL and writes to the chosen folder) so you get:
  - [x] Video (e.g. `.mp4`)
  - [x] Audio (e.g. `.mp3`)
  - [x] Script/transcript (e.g. `.txt` and/or `.detailed.json`)
  - [x] Images (e.g. thumbnail or screenshot `.png` from the current script).
- [x] **2.4** Confirm all assets are in the target folder and paths are documented (e.g. in process.log or a README in that folder).

---

## Phase 3: Analysis and logging

- [x] **3.1** Create **analysis.md** in `3MT/` to explore:
  - What multimodal elements you have (video, audio, text, images).
  - How you might analyze them (e.g. transcript themes, delivery, visuals) and what insights you want.
- [x] **3.2** process.log in `3MT/` created and updated in real time for each phase.

---

## Quick reference

| Deliverable    | Location / note                    |
|----------------|------------------------------------|
| 3MTlist.csv    | `3MT/3MTlist.csv`                  |
| One full sample| e.g. `3MT/output/<id>/` or `3MT/sample/<name>/` |
| analysis.md    | `3MT/analysis.md`                  |
| process.log    | `3MT/process.log` or `logs/process.log` |
| Download script| `ProcessYoutube/scripts/youtube_capture.py` (edit URL or add batch wrapper) |

---

*Update this checklist and process.log as you go; pause after each phase to review and adjust.*
