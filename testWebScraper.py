# test_scraper.py
from WebScraper import WebScraper

scraper = WebScraper()
courses = scraper.get_course_data("https://www.pmu.fr/turf/")
print("Titre de la page :", courses)