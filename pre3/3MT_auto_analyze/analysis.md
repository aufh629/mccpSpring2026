# Analysing 3MT as multimodal texts

This note explores how to analyse the materials we have (video, audio, transcript, images) to gain insights from 3 Minute Thesis presentations.

---

## 1. Multimodal elements we have

For each 3MT we can store (e.g. in `3MT/output/<video_id>/`):

| Modality | File(s) | What it gives |
|----------|---------|----------------|
| **Video** | `*.mp4` | Full presentation: speaker, slides, gestures, timing. |
| **Audio** | `*.mp3` | Voice only: pace, tone, emphasis, pauses (for future prosody/sentiment). |
| **Text** | `*.txt` | Full transcript (one block); good for keyword/thematic search. |
| **Text (time-aligned)** | `*.detailed.json` | Whisper segments with `start`, `end`, `text`; links words to time. |
| **Image** | `video_page.png` | Single screenshot of the video page (thumbnail of the talk). |
| **Metadata** | `metadata.json` | `url`, `title`, `duration`; useful for filtering and labelling. |

From **3MTlist.csv** we also have **title**, **speaker**, **url** (and can add year, institution) for cross-video comparison.

---

## 2. How we might analyse them

### 2.1 Transcript-only (text)

- **Themes and keywords**: Count or extract terms (e.g. “research”, “question”, “method”, “impact”) across many 3MTs to see common themes.
- **Structure**: Map classic 3MT moves (hook → problem → method → results → impact) by segmenting the transcript (e.g. by time using `detailed.json`) and labelling segments.
- **Readability / accessibility**: Sentence length, vocabulary level, presence of jargon vs. plain language.
- **Comparison**: Compare vocabulary or themes by speaker, year, or institution (using metadata and 3MTlist).

### 2.2 Time-aligned text (detailed.json)

- **Pacing**: Use segment `start`/`end` to compute words per minute or time per “move” (e.g. how long on hook vs. method).
- **Scripted vs. spontaneous**: Segment length and repetition patterns; alignment with slide changes if we add frame/slide timestamps later.
- **Quotes and clips**: Pull exact phrases with timestamps for citation or montages.

### 2.3 Audio (future)

- **Prosody**: Pace, pitch, pauses (e.g. with librosa or parselmouth).
- **Sentiment / energy**: Simple audio features (loudness, spectral) as a proxy for delivery style.
- **Comparison**: “Calm” vs. “high-energy” presenters; correlation with discipline or year.

### 2.4 Visual (current: one screenshot)

- **Thumbnail**: Represents one moment; useful for quick recognition and UI.
- **Future**: Frame extraction (e.g. 1 fps) or slide-detection would allow: slide content (OCR), gesture phases, use of props, and alignment with transcript segments.

### 2.5 Combined (multimodal)

- **Text + time**: Describe structure (e.g. “minutes 0–0:30 = hook, 0:30–1:30 = problem”) and compare across talks.
- **Text + metadata**: “Do 3MTs from discipline X use more technical terms?” (if we add discipline to 3MTlist).
- **Audio + text**: “Where does the speaker slow down? What phrases get emphasis?” (once audio features are in place).

---

## 3. Insights we might want

- **Rhetorical patterns**: How often do 3MTs use a personal hook, a clear “my question is”, a “so what?” impact line?
- **Discipline / year**: Differences in vocabulary, structure, or length of sections (if we have more metadata).
- **Training**: “Good” vs. “weak” examples by structure and clarity (with human labels or rubrics).
- **Accessibility**: Which talks use less jargon and shorter sentences; useful for communication training.
- **Reuse**: Short, timestamped clips and quotes for teaching or promotion.

---

## 4. Next steps (optional)

- Add **video_id**, **year**, **institution** (or discipline) to 3MTlist.csv for richer comparison.
- Script: “Segment one 3MT transcript into moves” using heuristics or a small LLM prompt on `detailed.json` segments.
- Script: “Compare word counts / themes across all 3MTs in 3MTlist” using `.txt` and metadata.
- Later: frame extraction or slide detection; audio feature extraction (pace, energy).

---

*Sample used: Emily Johnston (2014), `3MT/output/dh0pJdgY6Lc/` — transcript and detailed.json available for testing the above.*
