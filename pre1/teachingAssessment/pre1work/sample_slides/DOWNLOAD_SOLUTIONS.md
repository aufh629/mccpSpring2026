# Alternative Approaches to Analyze YouTube Slide Designs

## The Problem
YouTube has strong bot protection that blocks most automated download tools:
- yt-dlp: Blocked (requires cookies from browser)
- pytube: HTTP 400 Bad Request error
- pytubefix: Hanging/blocked

## ✅ **RECOMMENDED SOLUTIONS**

### Option 1: Browser Extension (Easiest & Most Reliable)
Use a browser extension to download the video directly:

1. **Install a YouTube downloader extension:**
   - Video DownloadHelper (Firefox/Chrome)
   - SaveFrom.net Helper
   - YouTube Video and Audio Downloader

2. **Download the video:**
   - Visit: https://www.youtube.com/watch?v=yY4A6ta9adQ
   - Click the extension icon
   - Download the video (MP4 format recommended)
   - Save to: `/workspaces/mccpSpring2026/pre1/teachingAssessment/pre1work/sample_slides/frames/`

3. **Extract frames using ffmpeg command:**
```bash
cd /workspaces/mccpSpring2026/pre1/teachingAssessment/pre1work/sample_slides
ffmpeg -i frames/video.mp4 -vf "fps=1/5" -q:v 2 frames/frame_%03d.jpg
```

### Option 2: Manual Screenshots (Fastest)
Since the goal is to analyze slide design, you don't need every frame:

1. **Open video in browser:** https://www.youtube.com/watch?v=yY4A6ta9adQ
2. **Pause at interesting slides**
3. **Take screenshots** (tool varies by OS):
   - **Linux**: `Shift + Print Screen` or `gnome-screenshot`
   - **Mac**: `Cmd + Shift + 4`
   - **Windows**: `Win + Shift + S`
4. **Save screenshots** to `frames/` folder
5. **Name them:** `slide_001.png`, `slide_002.png`, etc.

### Option 3: Online Download Services
Use a web-based YouTube downloader:

1. **Go to one of these sites:**
   - https://y2mate.com
   - https://savefrom.net
   - https://yt5s.com

2. **Paste the URL:** https://www.youtube.com/watch?v=yY4A6ta9adQ

3. **Download the MP4**

4. **Upload to workspace** and extract frames with ffmpeg

### Option 4: yt-dlp with Browser Cookies (Advanced but Most Reliable)
If you want automated downloading to work:

1. **Export cookies from your browser:**
   - Install "Get cookies.txt LOCALLY" extension
   - Visit YouTube while logged in
   - Export cookies to `youtube_cookies.txt`

2. **Use yt-dlp with cookies:**
```bash
/workspaces/mccpSpring2026/.venv/bin/yt-dlp \\
  --cookies youtube_cookies.txt \\
  -f "best[ext=mp4]" \\
  -o "frames/video.mp4" \\
  "https://www.youtube.com/watch?v=yY4A6ta9adQ"
```

3. **Extract frames:**
```bash
ffmpeg -i frames/video.mp4 -vf "fps=1/5" -q:v 2 frames/frame_%03d.jpg
```

## 📊 Frame Extraction Commands

Once you have the video downloaded, use one of these ffmpeg commands:

### Extract 1 frame every 5 seconds (recommended for slides):
```bash
ffmpeg -i video.mp4 -vf "fps=1/5" -q:v 2 frame_%03d.jpg
```

### Extract 1 frame every 10 seconds (for longer videos):
```bash
ffmpeg -i video.mp4 -vf "fps=1/10" -q:v 2 frame_%03d.jpg
```

### Extract specific timestamps:
```bash
ffmpeg -i video.mp4 -ss 00:01:30 -frames:v 1 frame_90s.jpg  # At 1:30
ffmpeg -i video.mp4 -ss 00:02:45 -frames:v 1 frame_165s.jpg  # At 2:45
```

### Extract frames at specific intervals with high quality:
```bash
ffmpeg -i video.mp4 -vf "select='not(mod(n,150))'" -vsync vfr -q:v 1 frame_%03d.jpg
```

## 🔧 Tools Created for Analysis

### 1. Python Script (once video is downloaded):
```bash
# If you get video file, run:
python analyze_slides.py frames/video.mp4
```

### 2. Manual Analysis Template:
```bash
# Open the analysis template:
cat frames/analysis_template.md
```

### 3. Comprehensive Guide:
```bash
# Read the slide design guide:
cat lessons4slides.md
```

## 📝 Next Steps (Pick One):

###  Quick Route (15 minutes):
1. Open video in browser
2. Take 10-15 screenshots of good slides
3. Save to `frames/` folder
4. Open `lessons4slides.md`
5. Compare screenshots to principles

### Medium Route (30 minutes):
1. Use online downloader to get MP4
2. Move MP4 to `frames/video.mp4`
3. Run: `ffmpeg -i frames/video.mp4 -vf "fps=1/5" -q:v 2 frames/frame_%03d.jpg`
4. Analyze extracted frames

### Complete Route (1 hour):
1. Export YouTube cookies from browser
2. Use yt-dlp with cookies to download
3. Extract frames with ffmpeg
4. Create detailed analysis using template
5. Update `lessons4slides.md` with specific examples

## 🎯 Recommendation

**For this specific task**, I recommend **Option 2 (Manual Screenshots)**:
- **Why**: You only need examples of good slide designs, not every frame
- **Time**: 10-15 minutes
- **Quality**: You choose the best examples
- **No technical issues**: Works 100% of the time

The goal is to **learn slide design principles**, not to create a complete video analysis. 10-15 well-chosen screenshots will teach you more than 100 automated frames.

## 📚 What You Already Have

I've created:
- ✅ **lessons4slides.md**: Comprehensive slide design guide (ready to use!)
- ✅ **README.md**: Project overview
- ✅ **capture_frames.py**: Helper script for workflow
- ✅ **frames/**: Directory ready for your screenshots

**You can start learning from `lessons4slides.md` right now**, then enhance it with specific examples from the video using any of the methods above!
