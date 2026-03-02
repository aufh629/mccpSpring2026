# Quick Start Guide

## Process a YouTube Video in 3 Steps

### Step 1: Install Dependencies (One-time setup)

```bash
# Install ffmpeg
brew install ffmpeg

# Install Python packages
pip3 install --user playwright yt-dlp openai-whisper

# Install browser for Playwright
python3 -m playwright install chromium
```

### Step 2: Edit the Video URL

Open `scripts/youtube_capture.py` and change line 185:

```python
video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE"
```

### Step 3: Run the Script

```bash
cd scripts
python3 youtube_capture.py
```

## What You'll Get

After 3-5 minutes, check `output/youtube_output/` for:
- ✅ Video file (`.mp4`)
- ✅ Audio file (`.mp3`)
- ✅ Transcript (`.txt`)
- ✅ Detailed transcript with timestamps (`.detailed.json`)
- ✅ Metadata (`.json`)
- ✅ Screenshot (`.png`)

## Common Issues

| Problem | Solution |
|---------|----------|
| "ffmpeg not found" | `brew install ffmpeg` |
| "403 Forbidden" | Update yt-dlp: `pip3 install --upgrade yt-dlp` |
| Slow transcription | Use smaller model: change `"base"` to `"tiny"` on line 166 |

## Next Steps

Read the full [README.md](README.md) for:
- Customization options
- Batch processing
- Troubleshooting guide
- Advanced features
