from playwright.sync_api import sync_playwright, expect

def test_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("C:/Users/Teodor/Desktop/PlayWright/playwright-TeodorPlachy/index.html")  # Načte lokální HTML soubor
        nadpis_1 = page.locator('h1').first
        expect(nadpis_1).to_be_visible()
        browser.close()

