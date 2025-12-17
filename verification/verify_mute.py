
from playwright.sync_api import sync_playwright

def verify_muted_attribute():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Create a mobile context
        context = browser.new_context(
            viewport={'width': 390, 'height': 844},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
        )
        page = context.new_page()

        # Load the file directly
        import os
        cwd = os.getcwd()
        filepath = f'file://{cwd}/720GallerySubpage.html'

        print(f'Navigating to {filepath}')
        page.goto(filepath)

        # Wait for JS to execute and create mobile view
        page.wait_for_timeout(2000)

        # Take a screenshot
        page.screenshot(path='verification/720GallerySubpage_mobile.png')

        # Verify video attributes
        videos = page.locator('#mobileTickerInner video')
        count = videos.count()
        print(f'Found {count} videos in mobile ticker')

        for i in range(count):
            video = videos.nth(i)
            muted_prop = video.evaluate('el => el.muted')
            muted_attr = video.evaluate('el => el.hasAttribute("muted")')
            print(f'Video {i}: Property .muted is {muted_prop}, Attribute [muted] is {muted_attr}')

            if not muted_prop or not muted_attr:
                print(f'Error: Video {i} is not fully muted!')
            else:
                print(f'Success: Video {i} is muted correctly.')

        browser.close()

if __name__ == '__main__':
    verify_muted_attribute()
