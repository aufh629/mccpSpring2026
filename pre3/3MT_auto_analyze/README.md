# YouTube Video Processing Pipeline

Automated system for downloading YouTube videos, extracting audio, and generating transcripts using AI.

## Overview

This pipeline automates the complete workflow for processing YouTube videos:
1. **Download** video from YouTube
2. **Extract** audio track
3. **Transcribe** audio to text using OpenAI Whisper
4. **Generate** timestamped transcripts

## Quick Start

### Prerequisites

Ensure you have the following installed:

```bash
# Python 3.9 or higher
python3 --version

# Homebrew (macOS)
brew --version

# Install system dependencies
brew install ffmpeg

# Install Python packages
pip3 install --user playwright yt-dlp openai-whisper
python3 -m playwright install chromium
```

### Basic Usage

1. Navigate to the scripts directory:
```bash
cd "ProcessYoutube/scripts"
```

2. Run the main script:
```bash
python3 youtube_capture.py
```

3. By default, it processes the video URL hardcoded in the script. To process a different video, edit line 185 in `youtube_capture.py`:
```python
video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

4. Find your output in `ProcessYoutube/output/youtube_output/`

## Output Files

For each video processed, you'll get:

| File | Description |
|------|-------------|
| `[title].mp4` | Full video file |
| `[title].mp3` | Extracted audio (192kbps, 44.1kHz) |
| `[title].txt` | Plain text transcript |
| `[title].detailed.json` | Transcript with timestamps |
| `metadata.json` | Video metadata (title, duration, URL) |
| `video_page.png` | Screenshot of YouTube page |

## Processing Time

Approximate processing times (for a 30-minute video):

| Step | Duration |
|------|----------|
| Browser automation & metadata | 15 seconds |
| Video download | 20-60 seconds (network dependent) |
| Audio extraction | 5-10 seconds |
| Transcription (first run) | 15 seconds (model download) + 2-3 minutes |
| Transcription (subsequent) | 2-3 minutes |
| **Total** | **3-5 minutes** |

## Whisper Model Options

The script uses the `base` model by default. You can change this in `youtube_capture.py` line 166:

| Model | Size | Speed | Accuracy | Best For |
|-------|------|-------|----------|----------|
| `tiny` | 39 MB | Fastest | Lower | Quick drafts |
| `base` | 139 MB | Fast | Good | **Default - balanced** |
| `small` | 244 MB | Medium | Better | Higher accuracy needed |
| `medium` | 769 MB | Slow | High | Professional use |
| `large` | 1.5 GB | Slowest | Highest | Maximum accuracy |

To change the model, edit line 166:
```python
model = whisper.load_model("small")  # Change "base" to your preferred model
```

## Customization

### Change Output Directory

Edit line 10 in `youtube_capture.py`:
```python
OUTPUT_DIR = Path(__file__).parent / "custom_output_folder"
```

### Change Audio Quality

Edit lines 138-140 in `youtube_capture.py`:
```python
'-ab', '320k',  # Change from '192k' to '320k' for higher quality
```

### Change Video Quality

Edit line 116 in `youtube_capture.py`:
```python
'-f', 'bestvideo[height<=720]+bestaudio/best',  # Limit to 720p
```

## Troubleshooting

### Error: "HTTP Error 403: Forbidden"

**Cause**: YouTube blocking the download.

**Solution**: The script already includes Android client emulation. If this persists:
1. Update yt-dlp: `pip3 install --upgrade yt-dlp`
2. Check if the video is region-restricted or private

### Error: "FileNotFoundError: ffmpeg"

**Cause**: ffmpeg not installed or not in PATH.

**Solution**:
```bash
brew install ffmpeg
```

### Error: "yt-dlp not found"

**Cause**: yt-dlp installed but not in PATH.

**Solution**: The script automatically uses the full path `~/Library/Python/3.9/bin/yt-dlp`. If this doesn't work:
```bash
# Find yt-dlp location
find ~/Library/Python -name yt-dlp

# Update line 104 in youtube_capture.py with the correct path
```

### Slow Transcription

**Cause**: Using CPU instead of GPU, or large model.

**Solutions**:
1. Use a smaller model (`tiny` or `base`)
2. If you have an M1/M2 Mac, Whisper will automatically use the Neural Engine
3. For very long videos, consider splitting the audio first

### Chinese/Special Characters in Filename

**Status**: Works correctly on macOS.

If you encounter issues on other systems, the script automatically sanitizes filenames (line 193):
```python
safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
```

## Batch Processing

To process multiple videos, create a simple wrapper:

```python
import asyncio
from youtube_capture import main

videos = [
    "https://www.youtube.com/watch?v=VIDEO_ID_1",
    "https://www.youtube.com/watch?v=VIDEO_ID_2",
    "https://www.youtube.com/watch?v=VIDEO_ID_3",
]

for video_url in videos:
    # Edit the video_url in youtube_capture.py or pass it as parameter
    asyncio.run(main())
```

## Advanced: Custom Video Sites

For non-YouTube videos (e.g., course platforms), use the experimental scripts:

1. `explore_video_player_manual.py` - For sites requiring login
2. `explore_video_player_v2.py` - For automated exploration with manual checkpoints

These scripts help you:
- Inspect video player structure
- Capture network requests
- Extract video URLs
- Save authentication sessions

## Project Structure

```
ProcessYoutube/
├── README.md                 # This file
├── scripts/                  # All Python scripts
│   ├── youtube_capture.py    # Main production script ⭐
│   ├── explore_video_player.py
│   ├── explore_video_player_manual.py
│   ├── explore_video_player_v2.py
│   └── capture_now.py
├── output/                   # All generated files
│   ├── youtube_output/       # Video, audio, transcripts
│   └── exploration_output/   # Exploration artifacts
└── logs/                     # Process logs
    └── process.log           # Detailed development log
```

## Best Practices

1. **Test with short videos first** - Verify the pipeline works before processing long videos
2. **Check disk space** - Videos can be large (1GB+ for HD content)
3. **Use appropriate Whisper model** - Balance speed vs. accuracy based on your needs
4. **Keep yt-dlp updated** - YouTube frequently changes their API
5. **Save transcripts separately** - Consider backing up transcripts to cloud storage

## Performance Tips

1. **Audio-only download** (if you don't need video):
   ```python
   '-f', 'bestaudio[ext=m4a]',  # Line 116
   ```
   This is much faster and saves disk space.

2. **Skip video download** if you already have it:
   Comment out lines 194-197 in `youtube_capture.py`

3. **Parallel processing** for multiple videos:
   Use Python's `multiprocessing` or run multiple instances

## Legal & Ethical Considerations

- Respect copyright laws and YouTube's Terms of Service
- Only download videos you have permission to download
- Use transcripts for personal study and research
- Do not redistribute downloaded content without permission

## Support & Updates

For issues or questions:
1. Check `logs/process.log` for detailed development history
2. Review error messages in terminal output
3. Verify all dependencies are correctly installed
4. Update all packages to latest versions

## Version History

- **v1.0** (2026-02-04): Initial release
  - YouTube download with Android client emulation
  - Audio extraction with ffmpeg
  - Transcription with Whisper base model
  - Automated dependency installation
  - Chinese language support verified

## Future Enhancements

See `logs/process.log` section "FUTURE IMPROVEMENTS" for planned features:
- Batch processing
- Resume capability
- Quality selection
- Language detection
- Subtitle integration
- Progress indicators
- Multiple output formats

---

**Last Updated**: 2026-02-04  
**Status**: Production Ready ✅  
**Tested On**: macOS (Apple Silicon), Python 3.9
