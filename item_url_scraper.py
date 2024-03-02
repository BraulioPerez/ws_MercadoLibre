import requests
from bs4 import BeautifulSoup
import re

class ItemUrlScraper:
    def __init__(self, item):
        self.item = item
        self.request = None
        self.html = None
        self.urls = []
        
    def create_search_link(self):
        print("creando links de búsqueda")
        item = self.item.replace(" ", "-")
        return f"https://listado.mercadolibre.com.mx/{item}_Desde_01_NoIndex_True"
    
    def get_item_urls(self, url:str):
        self.request = requests.get(url)
        print(self.request.status_code)
        if self.request.status_code == 200:
            self.html = BeautifulSoup(self.request.content, "html.parser", from_encoding="utf-8")
        else:
            print(f"Error: Request failed with status code {self.request.status_code}")
            self.html = None
        # Input html
        # Process html
        # return list of urls
        
        if self.html is not None:  # Check if HTML was successfully parsed
            hrefs = self.html.select("div.ui-search-layout div.ui-search-item__group a")
            for item in hrefs:
                self.urls.append(item.get("href"))
            print(self.urls)
            return self.urls
        else:
            print("Error: Failed to parse HTML content")
    
if __name__ == "__main__":
    
    obj = ItemUrlScraper("laptop")

    url1 = obj.create_search_link()
    list = obj.get_item_urls(url1)

    print(url1)
    print(list)
    

    
    
        

    
    