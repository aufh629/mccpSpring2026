#!/usr/bin/env python3
"""
YouTube video capture and transcription
Downloads video, extracts audio, and transcribes.

Usage:
  python3 youtube_capture.py                    # use default URL and output dir
  python3 youtube_capture.py <video_url>        # use default output dir
  python3 youtube_capture.py <video_url> <output_dir>  # custom output dir
"""
import asyncio
import sys
from playwright.async_api import async_playwright
from pathlib import Path
import json
import subprocess
import os

OUTPUT_DIR = Path(__file__).parent / "youtube_output"
OUTPUT_DIR.mkdir(exist_ok=True)

async def capture_youtube_video(video_url, output_dir=None):
    """Capture YouTube video metadata and download"""
    out = Path(output_dir) if output_dir else OUTPUT_DIR
    out.mkdir(parents=True, exist_ok=True)

    print(f"Processing: {video_url}")
    print("="*80)
    
    async with async_playwright() as p:
        print("\n1. Launching browser...")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        print("2. Loading YouTube video...")
        await page.goto(video_url, wait_until='domcontentloaded', timeout=60000)
        
        # Wait for video to load
        await asyncio.sleep(5)
        
        print("3. Extracting video metadata...")
        
        # Get video title
        try:
            title_element = await page.query_selector('h1.ytd-video-primary-info-renderer, h1 yt-formatted-string')
            title = await title_element.text_content() if title_element else "Unknown"
            title = title.strip()
        except:
            title = "Unknown"
        
        print(f"   Title: {title}")
        
        # Get video duration
        try:
            duration_element = await page.query_selector('.ytp-time-duration')
            duration = await duration_element.text_content() if duration_element else "Unknown"
        except:
            duration = "Unknown"
        
        print(f"   Duration: {duration}")
        
        # Get video element
        video_elements = await page.query_selector_all('video')
        print(f"   Found {len(video_elements)} video element(s)")
        
        if video_elements:
            video = video_elements[0]
            video_src = await video.get_attribute('src')
            print(f"   Video src: {video_src[:100] if video_src else 'None'}...")
        
        # Take screenshot
        screenshot_path = out / "video_page.png"
        await page.screenshot(path=screenshot_path)
        print(f"   ✓ Screenshot saved: {screenshot_path}")
        
        # Save metadata
        metadata = {
            'url': video_url,
            'title': title,
            'duration': duration,
            'timestamp': str(asyncio.get_event_loop().time())
        }
        
        metadata_path = out / "metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        print(f"   ✓ Metadata saved: {metadata_path}")
        
        print("\n4. Browser will stay open for 10 seconds...")
        await asyncio.sleep(10)
        
        await browser.close()
    
    return title

def download_youtube_video(video_url, output_path):
    """Download YouTube video using yt-dlp"""
    print("\n5. Downloading video with yt-dlp...")
    
    # Find yt-dlp path
    yt_dlp_path = 'yt-dlp'
    try:
        subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Try user installation path
        user_path = os.path.expanduser('~/Library/Python/3.9/bin/yt-dlp')
        if os.path.exists(user_path):
            yt_dlp_path = user_path
        else:
            print("   ⚠ yt-dlp not found. Installing...")
            subprocess.run(['pip3', 'install', '--user', 'yt-dlp'], check=True)
            yt_dlp_path = user_path
    
    # Download video with options to bypass restrictions
    cmd = [
        yt_dlp_path,
        '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '--merge-output-format', 'mp4',
        '--extractor-args', 'youtube:player_client=android',  # Use Android client to bypass restrictions
        '--user-agent', 'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36',
        '-o', str(output_path),
        video_url
    ]
    
    print(f"   Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"   ✓ Video downloaded: {output_path}")
        return True
    else:
        print(f"   ✗ Download failed: {result.stderr}")
        return False

def extract_audio(video_path, audio_path):
    """Extract audio from video using ffmpeg"""
    print("\n6. Extracting audio...")
    
    cmd = [
        'ffmpeg',
        '-i', str(video_path),
        '-vn',  # No video
        '-acodec', 'libmp3lame',  # MP3 codec
        '-ab', '192k',  # Bitrate
        '-ar', '44100',  # Sample rate
        '-y',  # Overwrite
        str(audio_path)
    ]
    
    print(f"   Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"   ✓ Audio extracted: {audio_path}")
        return True
    else:
        print(f"   ✗ Extraction failed: {result.stderr}")
        return False

def transcribe_audio(audio_path, transcript_path):
    """Transcribe audio using Whisper"""
    print("\n7. Transcribing audio with Whisper...")
    
    # Check if whisper is installed
    try:
        import whisper
    except ImportError:
        print("   ⚠ Whisper not found. Installing...")
        subprocess.run(['pip3', 'install', 'openai-whisper'], check=True)
        import whisper
    
    print("   Loading Whisper model (this may take a while on first run)...")
    model = whisper.load_model("base")  # Use 'small', 'medium', or 'large' for better accuracy
    
    print("   Transcribing...")
    result = model.transcribe(str(audio_path))
    
    # Save transcript
    with open(transcript_path, 'w', encoding='utf-8') as f:
        f.write(result['text'])
    
    print(f"   ✓ Transcript saved: {transcript_path}")
    print(f"\n   Preview:")
    print(f"   {result['text'][:300]}...")
    
    # Save detailed transcript with timestamps
    detailed_path = transcript_path.with_suffix('.detailed.json')
    with open(detailed_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"   ✓ Detailed transcript saved: {detailed_path}")
    
    return result['text']

async def main():
    video_url = "https://www.youtube.com/watch?v=B4jIyufgy-s"
    output_dir = OUTPUT_DIR
    if len(sys.argv) >= 2:
        video_url = sys.argv[1]
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2]).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

    print("YouTube Video Capture and Transcription")
    print("="*80)
    print(f"Output dir: {output_dir}")
    
    # Step 1-4: Capture metadata with Playwright
    title = await capture_youtube_video(video_url, output_dir)
    
    # Create safe filename
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title[:50]  # Limit length
    
    # Step 5: Download video
    video_path = output_dir / f"{safe_title}.mp4"
    if not download_youtube_video(video_url, video_path):
        print("\n✗ Failed to download video. Exiting.")
        return
    
    # Step 6: Extract audio
    audio_path = output_dir / f"{safe_title}.mp3"
    if not extract_audio(video_path, audio_path):
        print("\n✗ Failed to extract audio. Exiting.")
        return
    
    # Step 7: Transcribe
    transcript_path = output_dir / f"{safe_title}.txt"
    transcribe_audio(audio_path, transcript_path)
    
    print("\n" + "="*80)
    print("COMPLETE!")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print(f"  - Video: {video_path.name}")
    print(f"  - Audio: {audio_path.name}")
    print(f"  - Transcript: {transcript_path.name}")
    print(f"  - Metadata: metadata.json")

if __name__ == "__main__":
    asyncio.run(main())
