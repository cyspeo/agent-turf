from crewai import Crew, Agent, Task
from web_scraper import WebScraper
scraper = WebScraper()

def scraper_tool(url: str):
    return scraper.get_title(url)


# Agent qui scrape
scraper_agent = Agent(
    role="Scraper Web",
    goal="Extraire le titre d'une page web",
    backstory="Tu es un expert du scraping web avec Playwright.",
    allow_delegation=False,
    tools=[scraper_tool]
)

# Tâche de scraping
task = Task(
    description="Scrape le titre de la page https://example.com",
    expected_output="Le titre exact de la page web",
    agent=scraper_agent
)

# Crée la 'crew' (équipe)
crew = Crew(
    agents=[scraper_agent],
    tasks=[task],
    verbose=True
)

# Lance l’agent
result = crew.kickoff()
print("\nRésultat:", result)
