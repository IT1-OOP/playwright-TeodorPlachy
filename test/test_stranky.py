from playwright.sync_api import sync_playwright, expect

def test_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("C:/Users/Teodor/Desktop/PlayWright/playwright-TeodorPlachy/index.html")  # Načte lokální HTML soubor
        nadpis_1 = page.locator('h1').first
        nadpis_2 = page.locator('h2').first
        nadpis_3 = page.locator('h3').first
        nadpis_text = page.locator('text="Nadpis 1"')
        div_1 = page.locator('.container')
        odkaz = page.locator('a')
        
        expect(nadpis_3).to_be_visible()
        expect(nadpis_2).to_be_visible()
        expect(odkaz).to_be_visible()
        expect(nadpis_1).to_be_visible()
        expect(nadpis_text).to_be_visible()
        expect(div_1).to_be_visible()
        expect(nadpis_text).to_have_count(1)
        odkaz.click()

        browser.close()

