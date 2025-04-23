# web_scraper.py
   
import asyncio
from playwright.async_api import async_playwright

class WebScraper:
    def __init__(self, headless: bool = True):
        self.headless = headless

    async def scrape_course_data(self, url: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page()
            await page.goto(url)

            # Attendre que le bloc apparaisse
            await page.wait_for_selector('[data-testid="courseNumberCard"]')

            # Récupère tous les divs contenant l'attribut
            parents = await page.query_selector_all('[data-testid="courseNumberCard"]')
            for parent in parents:
                # Récupère les deux premiers enfants <div>
                first_div = await parent.query_selector('div:nth-child(1)')
                second_div = await parent.query_selector('div:nth-child(2)')

                # Extrait le texte
                first_text = await first_div.inner_text() if first_div else "N/A"
                second_text = await second_div.inner_text() if second_div else "N/A"

                print('Premier div :', first_text)
                print('Deuxième div :', second_text)

                # Récupère le prochain div frère (sibling) après courseCard
                hour_div_handle = await page.evaluate_handle(
                    "(node) => node.nextElementSibling", parent
                )

                # Récupère le contenu texte du div contenant l'heure
                hour_text = await hour_div_handle.evaluate(
                    "(node) => node.querySelector('div div:nth-child(2)').textContent"
                ) if hour_div_handle else "N/A"

                print('🕒 Heure de la course :', hour_text)

            await browser.close()

    def get_course_data(self, url: str):
        asyncio.run(self.scrape_course_data(url))
