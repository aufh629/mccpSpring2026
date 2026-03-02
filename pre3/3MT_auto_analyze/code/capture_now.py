#!/usr/bin/env python3
"""
Simple script to capture the current browser state
Run this while you have the page open in your regular browser
"""
import asyncio
from playwright.async_api import async_playwright
from pathlib import Path
import json

OUTPUT_DIR = Path(__file__).parent / "exploration_output"
SESSION_FILE = OUTPUT_DIR / "session.json"

async def capture_state():
    """Connect to existing browser and capture state"""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    async with async_playwright() as p:
        print("Launching browser in 5 seconds...")
        print("Please have the course page ready in the browser that will open...")
        await asyncio.sleep(5)
        
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Go to the URL
        print("Loading page...")
        try:
            await page.goto("https://wemooc.sflep.com/course/courseSection?crid=261", timeout=90000)
        except Exception as e:
            print(f"Navigation timeout/error (this is OK if you can see the page): {e}")
        
        # Wait a bit for any dynamic content
        await asyncio.sleep(5)
        
        print("\nAnalyzing page...")
        
        # Get page info
        current_url = page.url
        print(f"Current URL: {current_url}")
        
        # Check for video elements
        video_elements = await page.query_selector_all('video')
        print(f"Found {len(video_elements)} <video> elements")
        
        if video_elements:
            for i, video in enumerate(video_elements):
                src = await video.get_attribute('src')
                print(f"  Video {i+1} src: {src}")
        
        # Check for iframes
        iframe_elements = await page.query_selector_all('iframe')
        print(f"Found {len(iframe_elements)} <iframe> elements")
        
        if iframe_elements:
            for i, iframe in enumerate(iframe_elements):
                src = await iframe.get_attribute('src')
                print(f"  Iframe {i+1} src: {src}")
        
        # Get all links with "lesson" or Chinese characters
        links = await page.query_selector_all('a')
        lesson_links = []
        for link in links:
            try:
                href = await link.get_attribute('href')
                text = (await link.text_content() or "").strip()
                if text and href and (
                    'lesson' in text.lower() or 
                    'video' in text.lower() or 
                    '课' in text or 
                    '视频' in text or
                    len(text) < 50
                ):
                    lesson_links.append({'text': text, 'href': href})
            except:
                pass
        
        print(f"\nFound {len(lesson_links)} potential lesson links")
        for i, link in enumerate(lesson_links[:15], 1):
            print(f"  {i}. {link['text'][:60]}")
        
        # Save data
        with open(OUTPUT_DIR / "lesson_links.json", 'w', encoding='utf-8') as f:
            json.dump(lesson_links, f, indent=2, ensure_ascii=False)
        
        # Save HTML
        html_content = await page.content()
        with open(OUTPUT_DIR / "page_source.html", 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Save session
        storage_state = await context.storage_state()
        with open(SESSION_FILE, 'w') as f:
            json.dump(storage_state, f, indent=2)
        
        # Screenshot
        try:
            await page.screenshot(path=OUTPUT_DIR / "page_capture.png")
            print("\n✓ Screenshot saved")
        except Exception as e:
            print(f"⚠ Screenshot error: {e}")
        
        print("\n" + "="*80)
        print("CAPTURE COMPLETE")
        print("="*80)
        print(f"Output saved to: {OUTPUT_DIR}")
        print("\nBrowser will stay open for 30 seconds for you to explore...")
        print("You can manually check the page structure.")
        
        await asyncio.sleep(30)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_state())
