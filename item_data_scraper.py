import requests
from bs4 import BeautifulSoup
import json
import os
import time
import re



class ItemDataScraper:
    def __init__(self, url):
        self.url = url
        self.title = None


    def title_scrap(self, res):
        # input = url_objeto
        # funcion = extraer titulo de objeto
        # output = string del titulo
        print("Scraping title")

        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.select("div.ui-pdp-header__title-container h1")[0].text
        
        print(f"Title scraped: {title}")
        return title


    def price_scrap(self, res):
        # input = url_objeto
        # funcion = extraer precio de objeto
        # output = string del precio
        print("Scraping price")

        soup = BeautifulSoup(res.text, "html.parser")
        prices = soup.select("div.ui-pdp-price__main-container span.andes-money-amount__fraction")
        if len(prices) >= 2:
            price_before = prices[0].text
            price_current = prices[1].text
            price_credit = soup.select_one("div.ui-pdp-price__main-container div.ui-pdp-price__subtitles span.andes-money-amount__fraction")
            if prices[1] == price_credit:
                price_current = price_before
                price_before = None
            prices_list = [price_before, price_current]
            print(f"Prices scraped {prices_list}")
        elif len(prices) ==0:
            prices_list = None
            print(f"Prices scraped {prices_list}")            
        else:
            price_current = prices[0].text
            price_before = None
            prices_list = [price_before, price_current]
            print(f"Prices scraped {prices_list}")
            
        return prices_list
    

    def rating_scrap(self, res):
        # input = url_objeto
        # funcion = extraer rating de objeto
        # output = string del rating
        print("Scraping rating")

        soup = BeautifulSoup(res.text, "html.parser")
        review_div = soup.select("div[class*='ui-review-capability__rating'] p")
        if len(review_div) != 0:
            rate = review_div[0].text
        elif len(review_div) == 0:
            rate = soup.select_one("div.ui-pdp-header div[class*='ui-pdp-header__info'] a[class*='ui-pdp-review__label'] span.ui-pdp-review__rating")
        else:
            rate = None

        print(f"Rating scraped {rate}")
        return rate


    def images_scrap(self, res):
        # input = url_objeto
        # funcion = extraer url de imagenes de objeto
        # output = lista de urls
        print("Scraping images")

        soup = BeautifulSoup(res.text, "html.parser")
        images_list = soup.select("div.ui-pdp-gallery__column span.ui-pdp-gallery__wrapper label.ui-pdp-gallery__label div[role='presentation'] div.ui-pdp-thumbnail__picture img.ui-pdp-image")
        urls_img = []
        for img in images_list:
            url = img.get('data-src')
            urls_img.append(url)   
        
        print(f"Images scraped: {urls_img}")
        return urls_img
    
    
    def provider_scrap(self, res):
        # input = url_objeto
        # funcion = extraer titulo de proveedor del objeto
        # output = string del titulo del proveedor
        print("Scraping provider")

        soup = BeautifulSoup(res.text, "html.parser")
        provider_list = soup.select("div.ui-seller-info div.ui-pdp-seller__header__title")
        if len(provider_list) == 0:
            provider_unique = soup.select_one("div.ui-pdp-seller__header div.ui-pdp-seller__header__info-container div.ui-pdp-seller__header__info-container__title span[class*='ui-pdp-color--BLUE']")
            provider = provider_unique.text
        else:
            provider = provider_list[0].text 

        print(f"Provider scraped {provider}")
        return provider


    def description_scrap(self, res):
        # input = url_objeto
        # funcion = extraer Descripcion de objeto
        # output = string de la descripcion
        print("Scraping  Description")

        soup = BeautifulSoup(res.text, "html.parser")        
        description_list = soup.select("div[class*='ui-pdp-container__row'] div.ui-pdp-description p.ui-pdp-description__content")
        if len(description_list) == 0:
            description = None
        else:
            description = description_list[0].text

        print(f"Description scraped {description}")
        return description


    def data_scrap(self, url_objeto):
        
        with requests.Session() as session:
            ses = session.get(url_objeto)
            title = self.title_scrap(ses)

            result = {"title": title,
                        "prices" : self.price_scrap(ses),
                        "images": self.images_scrap(ses),
                        "rating": self.rating_scrap(ses),
                        "provider": self.provider_scrap(ses),
                        "description": self.description_scrap(ses) 
                        }
            with open(f"{title}.json", "w") as outfile: 
                json.dump(result, outfile)
        
        return result


    def debug_write_soup_to_file(self, url_objeto, file_name):
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")

        if not os.path.isfile(file_name):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(str(soup))
    
#the class is planned to scrap multiple pages of a website so it is initialized with a string symbolizing a url
obj = ScraperLibre("https://listado.mercadolibre.com.mx/pc-gamer#D[A:pc%20gamer]")

# Todays project due only asks to return the data from one item, so the method to use is data_scrap
obj.data_scrap("https://articulo.mercadolibre.com.mx/MLM-1328094335-pc-gamer-arcoteck-ryzen-5-5600g-16gb-ssd-480gb-gabinete-rgb-_JM#position=55&search_layout=stack&type=item&tracking_id=c09b0ff0-2931-4c70-85f2-86b3369f719b")
