#!/usr/bin/env python3
"""
Exploration script to inspect the video player structure on wemooc.sflep.com
This script will help us understand how to automate video capture.
"""
import asyncio
from playwright.async_api import async_playwright
from pathlib import Path
import json

# Configuration
COURSE_URL = "https://wemooc.sflep.com/course/courseSection?crid=261"
OUTPUT_DIR = Path(__file__).parent / "exploration_output"
SESSION_FILE = OUTPUT_DIR / "session.json"

async def explore_page():
    """Explore the course page structure"""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    async with async_playwright() as p:
        # Launch browser with visible UI for manual login
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        print(f"Navigating to: {COURSE_URL}")
        await page.goto(COURSE_URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)  # Wait 3 seconds for page to settle
        
        # Take initial screenshot (viewport only to avoid timeout)
        try:
            await page.screenshot(path=OUTPUT_DIR / "01_initial_page.png", timeout=10000)
            print("✓ Captured initial page screenshot")
        except Exception as e:
            print(f"⚠ Screenshot failed: {e}")
        
        # Wait for manual login
        print("\n" + "="*80)
        print("MANUAL LOGIN REQUIRED")
        print("="*80)
        print("Please complete WeChat login in the browser window.")
        print("After logging in and reaching the course page, press Enter here...")
        input()
        
        # Capture post-login state
        try:
            await page.screenshot(path=OUTPUT_DIR / "02_after_login.png", timeout=10000)
            print("✓ Captured post-login screenshot")
        except Exception as e:
            print(f"⚠ Screenshot failed: {e}")
        
        # Save session/cookies for future use
        cookies = await context.cookies()
        storage_state = await context.storage_state()
        with open(SESSION_FILE, 'w') as f:
            json.dump(storage_state, f, indent=2)
        print(f"✓ Saved session to {SESSION_FILE}")
        
        # Analyze page structure
        print("\n" + "="*80)
        print("ANALYZING PAGE STRUCTURE")
        print("="*80)
        
        # Check for video elements
        video_elements = await page.query_selector_all('video')
        print(f"Found {len(video_elements)} <video> elements")
        
        # Check for iframes
        iframe_elements = await page.query_selector_all('iframe')
        print(f"Found {len(iframe_elements)} <iframe> elements")
        
        # Check for common video player classes
        player_selectors = [
            '.video-player', '.player', '.video-container',
            '[class*="video"]', '[class*="player"]',
            '[id*="video"]', '[id*="player"]'
        ]
        
        for selector in player_selectors:
            elements = await page.query_selector_all(selector)
            if elements:
                print(f"Found {len(elements)} elements matching: {selector}")
        
        # Get page HTML structure
        html_content = await page.content()
        with open(OUTPUT_DIR / "page_structure.html", 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ Saved HTML structure to page_structure.html")
        
        # Check for video links in the page
        links = await page.query_selector_all('a')
        video_links = []
        for link in links:
            href = await link.get_attribute('href')
            text = await link.text_content()
            if href and ('video' in href.lower() or 'lesson' in text.lower() or '课' in text):
                video_links.append({'text': text, 'href': href})
        
        print(f"\nFound {len(video_links)} potential video/lesson links:")
        for i, link in enumerate(video_links[:10], 1):  # Show first 10
            print(f"  {i}. {link['text'][:50]} -> {link['href'][:80]}")
        
        # Save all links
        with open(OUTPUT_DIR / "video_links.json", 'w', encoding='utf-8') as f:
            json.dump(video_links, f, indent=2, ensure_ascii=False)
        
        # Listen for network requests to find video sources
        print("\n" + "="*80)
        print("NETWORK MONITORING")
        print("="*80)
        print("Please click on a video to play it, then press Enter...")
        
        video_requests = []
        
        def handle_request(request):
            url = request.url
            resource_type = request.resource_type
            # Look for video/audio resources
            if resource_type in ['media', 'xhr', 'fetch']:
                if any(ext in url.lower() for ext in ['.mp4', '.m3u8', '.ts', '.flv', 'video', 'stream']):
                    video_requests.append({
                        'url': url,
                        'type': resource_type,
                        'method': request.method
                    })
                    print(f"  📹 Detected: {url[:100]}")
        
        page.on('request', handle_request)
        
        input()
        
        # Save network data
        with open(OUTPUT_DIR / "network_requests.json", 'w', encoding='utf-8') as f:
            json.dump(video_requests, f, indent=2)
        print(f"✓ Saved {len(video_requests)} video-related network requests")
        
        # Final screenshot
        try:
            await page.screenshot(path=OUTPUT_DIR / "03_video_playing.png", timeout=10000)
            print("✓ Captured video playing screenshot")
        except Exception as e:
            print(f"⚠ Screenshot failed: {e}")
        
        print("\n" + "="*80)
        print("EXPLORATION COMPLETE")
        print("="*80)
        print(f"All output saved to: {OUTPUT_DIR}")
        print("\nNext steps:")
        print("1. Review the screenshots and HTML structure")
        print("2. Check network_requests.json for video URLs")
        print("3. Use session.json for authenticated requests")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(explore_page())
