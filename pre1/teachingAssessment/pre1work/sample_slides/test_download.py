#!/usr/bin/env python3
"""
Simple test to download YouTube video with pytube
"""

from pytube import YouTube
import sys

url = "https://www.youtube.com/watch?v=yY4A6ta9adQ"

try:
    print(f"Attempting to download: {url}")
    yt = YouTube(url)
    
    print(f"\nVideo Info:")
    print(f"  Title: {yt.title}")
    print(f"  Duration: {yt.length} seconds")
    print(f"  Views: {yt.views}")
    print(f"  Author: {yt.author}")
    
    print(f"\nAvailable streams:")
    for stream in yt.streams.filter(progressive=True):
        print(f"  - {stream.resolution} {stream.mime_type} ({stream.filesize / 1024 / 1024:.1f} MB)")
    
    # Download
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(f"\nDownloading: {stream.resolution}")
    output_file = stream.download(output_path="frames", filename="video.mp4")
    print(f"✓ Downloaded to: {output_file}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
