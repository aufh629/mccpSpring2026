#!/usr/bin/env python3
"""
Manual exploration script - keeps browser open for manual navigation
This version doesn't auto-navigate, allowing you to handle network issues manually
"""
import asyncio
from playwright.async_api import async_playwright
from pathlib import Path
import json

# Configuration
OUTPUT_DIR = Path(__file__).parent / "exploration_output"
SESSION_FILE = OUTPUT_DIR / "session.json"

async def explore_page():
    """Explore the course page structure with manual control"""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    async with async_playwright() as p:
        # Launch browser with visible UI
        print("Launching browser...")
        browser = await p.chromium.launch(
            headless=False,
            args=['--disable-blink-features=AutomationControlled']
        )
        
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        
        page = await context.new_page()
        
        print("\n" + "="*80)
        print("MANUAL NAVIGATION MODE")
        print("="*80)
        print("The browser is now open. Please:")
        print("1. Navigate to: https://wemooc.sflep.com/course/courseSection?crid=261")
        print("2. Complete WeChat login")
        print("3. Navigate to the course page with videos")
        print("\nPress Enter when you're on the course page with videos visible...")
        input()
        
        # Capture current state
        print("\nCapturing page state...")
        try:
            await page.screenshot(path=OUTPUT_DIR / "01_course_page.png")
            print("✓ Screenshot saved")
        except Exception as e:
            print(f"⚠ Screenshot error: {e}")
        
        # Save session
        storage_state = await context.storage_state()
        with open(SESSION_FILE, 'w') as f:
            json.dump(storage_state, f, indent=2)
        print(f"✓ Session saved to {SESSION_FILE}")
        
        # Get current URL
        current_url = page.url
        print(f"Current URL: {current_url}")
        
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
        
        # Get all links
        links = await page.query_selector_all('a')
        all_links = []
        for link in links:
            try:
                href = await link.get_attribute('href')
                text = (await link.text_content() or "").strip()
                if text and href:
                    all_links.append({'text': text, 'href': href})
            except:
                pass
        
        print(f"Found {len(all_links)} links on the page")
        
        # Save links
        with open(OUTPUT_DIR / "all_links.json", 'w', encoding='utf-8') as f:
            json.dump(all_links, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved links to all_links.json")
        
        # Get page HTML
        html_content = await page.content()
        with open(OUTPUT_DIR / "page_structure.html", 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ Saved HTML structure")
        
        # Network monitoring
        print("\n" + "="*80)
        print("NETWORK MONITORING")
        print("="*80)
        print("Now monitoring network requests...")
        print("Please click on a video lesson to play it.")
        print("Press Enter after the video starts playing...")
        
        video_requests = []
        
        def handle_request(request):
            url = request.url
            resource_type = request.resource_type
            if resource_type in ['media', 'xhr', 'fetch', 'other']:
                if any(ext in url.lower() for ext in ['.mp4', '.m3u8', '.ts', '.flv', 'video', 'stream', 'media']):
                    video_requests.append({
                        'url': url,
                        'type': resource_type,
                        'method': request.method
                    })
                    print(f"  📹 {url[:120]}")
        
        page.on('request', handle_request)
        
        input()
        
        # Save network data
        with open(OUTPUT_DIR / "network_requests.json", 'w', encoding='utf-8') as f:
            json.dump(video_requests, f, indent=2)
        print(f"\n✓ Saved {len(video_requests)} video-related requests")
        
        # Capture video playing
        try:
            await page.screenshot(path=OUTPUT_DIR / "02_video_playing.png")
            print("✓ Captured video playing screenshot")
        except Exception as e:
            print(f"⚠ Screenshot error: {e}")
        
        print("\n" + "="*80)
        print("EXPLORATION COMPLETE")
        print("="*80)
        print(f"All output saved to: {OUTPUT_DIR}")
        print("\nReview the following files:")
        print("  - session.json (for authenticated requests)")
        print("  - network_requests.json (video URLs)")
        print("  - all_links.json (lesson links)")
        print("  - page_structure.html (page HTML)")
        print("\nPress Enter to close the browser...")
        input()
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(explore_page())
