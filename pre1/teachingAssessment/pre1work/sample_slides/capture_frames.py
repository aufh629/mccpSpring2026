#!/usr/bin/env python3
"""
Script to help capture and analyze YouTube video frames for slide design analysis.
Since automated downloads are blocked, this provides a manual workflow.
"""

import os
from pathlib import Path

def create_frame_template():
    """Create a template for analyzing slide design from manual screenshots"""
    template = """
# Slide Design Analysis Template

## For each screenshot/frame captured:

### Frame [NUMBER]
- **Time**: [timestamp from video]
- **Slide Title/Topic**: 
- **Visual Elements**:
  - Layout structure: 
  - Color scheme: 
  - Typography: 
  - Images/Graphics: 
  - White space usage: 
- **Content Organization**:
  - Hierarchy: 
  - Key points: 
  - Supporting details: 
- **Design Principles Applied**:
  - [ ] Contrast
  - [ ] Alignment
  - [ ] Repetition
  - [ ] Proximity
  - [ ] Simplicity
- **Notes**: 

---
"""
    return template

def main():
    """Main function to set up the analysis workflow"""
    frames_dir = Path("frames")
    frames_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("YouTube Slide Design Analysis Workflow")
    print("=" * 60)
    print("\nSTEPS:")
    print("1. Open the YouTube video in your browser")
    print("2. Pause at interesting slide designs")
    print("3. Take screenshots (save to the 'frames' folder)")
    print("4. Use the template below to analyze each slide")
    print("\nScreenshot naming convention:")
    print("  - frame_001.png, frame_002.png, etc.")
    print("\n" + "=" * 60)
    
    # Create analysis template file
    template_file = frames_dir / "analysis_template.md"
    with open(template_file, 'w') as f:
        f.write(create_frame_template())
    
    print(f"\n✓ Created template: {template_file}")
    print(f"\n✓ Frames directory ready: {frames_dir}")
    print("\nNext: Watch the video and capture screenshots!")

if __name__ == "__main__":
    main()
