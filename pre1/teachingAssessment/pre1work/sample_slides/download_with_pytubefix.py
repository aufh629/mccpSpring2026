#!/usr/bin/env python3
"""
Download YouTube video using pytubefix and extract frames with ffmpeg
"""

from pytubefix import YouTube
import subprocess
import os
from pathlib import Path

url = "https://www.youtube.com/watch?v=yY4A6ta9adQ"
output_dir = "frames"

try:
    print(f"=" * 70)
    print("YouTube Video Downloader using pytubefix")
    print("=" * 70)
    print(f"\nAttempting to download: {url}")
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Download video
    yt = YouTube(url)
    
    print(f"\nVideo Info:")
    print(f"  Title: {yt.title}")
    print(f"  Duration: {yt.length} seconds ({yt.length // 60}:{yt.length % 60:02d})")
    print(f"  Views: {yt.views:,}")
    print(f"  Author: {yt.author}")
    
    print(f"\nAvailable streams:")
    for stream in yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()[:5]:
        print(f"  - {stream.resolution} {stream.mime_type} ({stream.filesize / 1024 / 1024:.1f} MB)")
    
    # Download highest resolution progressive stream
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(f"\nDownloading: {stream.resolution}")
    output_file = stream.download(output_path=output_dir, filename="video.mp4")
    print(f"✓ Downloaded to: {output_file}")
    
    # Extract frames using ffmpeg
    print(f"\nExtracting frames using ffmpeg...")
    frame_pattern = os.path.join(output_dir, "frame_%03d.jpg")
    
    # Extract 1 frame every 5 seconds
    cmd = [
        "ffmpeg",
        "-i", output_file,
        "-vf", "fps=1/5",  # 1 frame every 5 seconds
        "-q:v", "2",  # High quality
        frame_pattern
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Count extracted frames
        frames = sorted([f for f in os.listdir(output_dir) if f.startswith("frame_") and f.endswith(".jpg")])
        print(f"✓ Extracted {len(frames)} frames")
        
        print(f"\n" + "=" * 70)
        print("SUCCESS!")
        print("=" * 70)
        print(f"Video: {output_file}")
        print(f"Frames: {len(frames)} images in {output_dir}/")
        print(f"\nNext: Analyze the frames to learn slide design principles!")
        
    else:
        print(f"FFmpeg error: {result.stderr}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
