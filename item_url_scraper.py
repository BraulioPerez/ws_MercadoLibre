import requests
from bs4 import BeautifulSoup
import re

class ItemUrlScraper:
    def __init__(self, search_url):
        self.search_url = search_url
        self.request = requests.get(self.search_url)
        if self.request.status_code == 200:
            self.html = BeautifulSoup(self.request.content, "html.parser", from_encoding="utf-8")
        else:
            print(f"Error: Request failed with status code {self.request.status_code}")
            self.html = None
        self.urls = []

    def increase_page(self, search_url):
        # input = link de búsqueda
        # funcion: aumenta en 50 el valor de la busqueda
        # output = link de busqueda modificado
        print("Increasing page")

        beginning, ending = search_url.split("_", 1)
        pattern = r'\d+'
        modified_ending = re.sub(pattern, lambda match: str(int(match.group()) + 50), ending)

        print("Page increased")
        return beginning + "_" + modified_ending

    def get_item_urls(self):
        # Input html
        # Process html
        # return list of urls
        if self.html is not None:  # Check if HTML was successfully parsed
            hrefs = self.html.select("div.ui-search-layout div.ui-search-item__group a")
            for item in hrefs:
                self.urls.append(item.get("href"))
            print(self.urls)
        else:
            print("Error: Failed to parse HTML content")


    def extract_all(self):
        None


if __name__ == "__main__":
    url = "https://listado.mercadolibre.com.mx/control-remoto#D[A:control%20remoto]"
    scraper = ItemUrlScraper(url)
    scraper.get_item_urls()