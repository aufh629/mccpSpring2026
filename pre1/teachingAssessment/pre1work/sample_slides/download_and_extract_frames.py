#!/usr/bin/env python3
"""
Download YouTube video and extract frames for slide analysis
Using pytube for download and opencv for frame extraction
"""

import os
import sys
from pathlib import Path
import cv2
from pytube import YouTube

def download_video(url, output_path="frames"):
    """Download YouTube video using pytube"""
    try:
        print(f"Downloading video from: {url}")
        yt = YouTube(url)
        
        # Get video info
        print(f"Title: {yt.title}")
        print(f"Duration: {yt.length} seconds")
        print(f"Views: {yt.views}")
        
        # Get the highest resolution progressive stream (video+audio)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        if not stream:
            print("No suitable stream found. Trying adaptive stream...")
            stream = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        print(f"Downloading: {stream.resolution} - {stream.mime_type}")
        
        # Download the video
        output_file = stream.download(output_path=output_path, filename="video.mp4")
        print(f"✓ Downloaded to: {output_file}")
        
        return output_file, yt.title, yt.length
        
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None, None, None

def extract_frames(video_path, output_dir="frames", interval_seconds=5, max_frames=50):
    """Extract frames from video at specified intervals"""
    try:
        print(f"\nExtracting frames from: {video_path}")
        
        # Create output directory
        Path(output_dir).mkdir(exist_ok=True)
        
        # Open video
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print("Error: Could not open video file")
            return []
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps
        
        print(f"Video properties:")
        print(f"  - FPS: {fps:.2f}")
        print(f"  - Total frames: {total_frames}")
        print(f"  - Duration: {duration:.2f} seconds")
        
        # Calculate frame interval
        frame_interval = int(fps * interval_seconds)
        
        print(f"\nExtracting frames every {interval_seconds} seconds (every {frame_interval} frames)...")
        
        extracted_frames = []
        frame_count = 0
        saved_count = 0
        
        while cap.isOpened() and saved_count < max_frames:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            # Save frame at intervals
            if frame_count % frame_interval == 0:
                timestamp = frame_count / fps
                output_file = os.path.join(output_dir, f"frame_{saved_count:03d}_t{int(timestamp)}s.jpg")
                cv2.imwrite(output_file, frame)
                extracted_frames.append(output_file)
                saved_count += 1
                print(f"  ✓ Saved frame {saved_count}: {output_file} (at {timestamp:.1f}s)")
            
            frame_count += 1
        
        cap.release()
        print(f"\n✓ Extracted {saved_count} frames to {output_dir}/")
        
        return extracted_frames
        
    except Exception as e:
        print(f"Error extracting frames: {e}")
        return []

def create_analysis_file(frames, video_title, output_file="frame_analysis.md"):
    """Create a markdown file for analyzing the extracted frames"""
    content = f"""# Slide Design Analysis - {video_title}

## Video Information
- **Title**: {video_title}
- **Total Frames Extracted**: {len(frames)}

## Frame Analysis

"""
    
    for i, frame_path in enumerate(frames, 1):
        frame_name = os.path.basename(frame_path)
        # Extract timestamp from filename
        timestamp = frame_name.split('_t')[1].replace('s.jpg', '') if '_t' in frame_name else 'unknown'
        
        content += f"""### Frame {i} - {frame_name}
![{frame_name}]({frame_name})

**Timestamp**: {timestamp} seconds

**Design Elements**:
- Layout: 
- Color Scheme: 
- Typography: 
- Visual Hierarchy: 
- Key Message: 

**Design Principles Observed**:
- [ ] Simplicity
- [ ] Contrast
- [ ] Alignment
- [ ] Repetition/Consistency
- [ ] White Space
- [ ] Visual Hierarchy

**Notes**: 


---

"""
    
    content += """## Summary

### Common Design Patterns Observed:
-

### Color Palette Used:
-

### Typography Choices:
-

### Key Takeaways for My Own Slides:
1. 
2. 
3. 
4. 
5. 

### Techniques to Implement:
-

"""
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"\n✓ Created analysis template: {output_file}")

def main():
    # Configuration
    youtube_url = "https://www.youtube.com/watch?v=yY4A6ta9adQ"
    output_dir = "frames"
    interval_seconds = 5  # Extract one frame every 5 seconds
    max_frames = 50  # Maximum number of frames to extract
    
    print("=" * 70)
    print("YouTube Video Frame Extractor for Slide Design Analysis")
    print("=" * 70)
    
    # Step 1: Download video
    video_path, video_title, duration = download_video(youtube_url, output_dir)
    
    if not video_path:
        print("\n✗ Failed to download video. Exiting.")
        return
    
    # Step 2: Extract frames
    frames = extract_frames(video_path, output_dir, interval_seconds, max_frames)
    
    if not frames:
        print("\n✗ Failed to extract frames. Exiting.")
        return
    
    # Step 3: Create analysis template
    analysis_file = os.path.join(output_dir, "frame_analysis.md")
    create_analysis_file(frames, video_title or "YouTube Video", analysis_file)
    
    print("\n" + "=" * 70)
    print("SUCCESS! Next steps:")
    print("=" * 70)
    print(f"1. Review the {len(frames)} extracted frames in the '{output_dir}/' folder")
    print(f"2. Open '{analysis_file}' to analyze each frame")
    print(f"3. Document design principles you observe")
    print(f"4. Update 'lessons4slides.md' with specific examples from this video")
    print("=" * 70)

if __name__ == "__main__":
    main()
