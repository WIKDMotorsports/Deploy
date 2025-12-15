import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Mrs WIKD (Pink Theme)
        url = f"file://{os.getcwd()}/GallerSubPageMrsWIKD.html"
        page.goto(url)
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/GallerSubPageMrsWIKD_final.png", full_page=True)
        print("MrsWIKD Verified")

        # Verify F450 (No Dyno)
        url = f"file://{os.getcwd()}/GallerySubpageF450.html"
        page.goto(url)
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/GallerySubpageF450_final.png", full_page=True)
        print("F450 Verified")

        browser.close()

if __name__ == "__main__":
    verify()
