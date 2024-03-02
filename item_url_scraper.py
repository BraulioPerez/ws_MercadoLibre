import requests
from bs4 import BeautifulSoup
import re

class ItemUrlScraper:
    def __init__(self, item):
        self.item = item.replace(" ","-")
        self.url = f"https://listado.mercadolibre.com.mx/{self.item}_Desde_01_NoIndex_True"
        self.urls = []
        self.request = None
        self.html = None
    
    def get_item_urls(self):
        self.request = requests.get(self.url)
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
            
            hrefs = self.html.select("div.ui-search-main ol.ui-search-layout li div.ui-search-item__group a[class*='ui-search-item__group__element ui-search-link__title-card ui-search-link']")
            if len(hrefs) == 0:
                hrefs = self.html.select("div.ui-search-layout div.ui-search-item__group a")
            
            for item in hrefs:
                self.urls.append(item.get("href"))
            return self.urls
        else:
            print("Error: Failed to parse HTML content")
    
if __name__ == "__main__":
    
    obj = ItemUrlScraper("control remoto")

    list = obj.get_item_urls()

    print(len(list))
    print(list)
    

    
    
        

    
    