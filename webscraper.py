import requests
from bs4 import BeautifulSoup
import re


class WebScraper:
    def __init__(self, link, regular_expression):
        self.link = link
        self.regular_expression = regular_expression

    def scraper(self):
        req = requests.get(self.link)
        soup = BeautifulSoup(req.text, 'html.parser')
        regex = re.compile(self.regular_expression)
        results = soup.find_all('p', {'class': regex})
        scrapedData = [result.text for result in results]

        return scrapedData

