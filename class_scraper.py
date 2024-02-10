import requests
from bs4 import BeautifulSoup
import json
import os
import time
import re



class ScraperLibre:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.price_before = None
        self.price_now = None
        self.rating = None
        self.urls_img = None
        self.provider = None
        self.description = None
        

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


    def title_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer titulo de objeto
        # output = string del titulo
        print("Scraping title")

        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.select("div.ui-pdp-header__title-container h1")[0].text
        
        print(f"Title scraped: {title}")
        return title


    def price_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer precio de objeto
        # output = string del precio
        print("Scraping price")

        res = requests.get(url_objeto)
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
    

    def rating_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer rating de objeto
        # output = string del rating
        print("Scraping rating")

        res = requests.get(url_objeto)
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


    def images_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer url de imagenes de objeto
        # output = lista de urls
        print("Scraping images")

        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        images_list = soup.select("div.ui-pdp-gallery__column span.ui-pdp-gallery__wrapper label.ui-pdp-gallery__label div[role='presentation'] div.ui-pdp-thumbnail__picture img.ui-pdp-image")
        urls_img = []
        for img in images_list:
            url = img.get('data-src')
            urls_img.append(url)   
        
        print(f"Images scraped: {urls_img}")
        return urls_img
    
    
    def provider_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer titulo de proveedor del objeto
        # output = string del titulo del proveedor
        print("Scraping provider")

        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        provider_list = soup.select("div.ui-seller-info div.ui-pdp-seller__header__title")
        if len(provider_list) == 0:
            provider_unique = soup.select_one("div.ui-pdp-seller__header div.ui-pdp-seller__header__info-container div.ui-pdp-seller__header__info-container__title span[class*='ui-pdp-color--BLUE']")
            provider = provider_unique.text
        else:
            provider = provider_list[0].text 

        print(f"Provider scraped {provider}")
        return provider


    def description_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer Descripcion de objeto
        # output = string de la descripcion
        print("Scraping  Description")

        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")        
        description_list = soup.select("div[class*='ui-pdp-container__row'] div.ui-pdp-description p.ui-pdp-description__content")
        if len(description_list) == 0:
            description = None
        else:
            description = description_list[0].text

        print(f"Description scraped {description}")
        return description


    def data_scrap(self, url_objeto):
        result = {"title": self.title_scrap(url_objeto),
                    "prices" : self.price_scrap(url_objeto),
                    "images": self.images_scrap(url_objeto),
                    "rating": self.rating_scrap(url_objeto),
                    "provider": self.provider_scrap(url_objeto),
                    "description": self.description_scrap(url_objeto) 
                    }
        with open("result.json", "w") as outfile: 
            json.dump(result, outfile)
        return result


    def scrap_all(self):
        # La típica funcion de scrapear los links de busqueda del objeto
            # Aparte de sacar los links de búsqueda de cada objeto, debe entrar y scrapear los datos de cada objeto en forma de diccionarios
            # añade el diccionario a un json grande
            # se mueve a la siguiente página
                # El ciclo se rompe cuando ya no encuentra objetos que scrapear
        # return json con toda la info
        url_list = []
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "html.parser")
        selector = "a[class*=ui-search-item__group__element][class*=ui-search-link__title-card][class*=ui-search-link]"
        elements = soup.select(selector)

        all_data = {}
        for elm in elements:
            url = elm.get("href")
            print(url)
            all_data[url] = self.data_scrap(url)
            print(all_data[url])
        print(all_data)

        return all_data


    def debug_write_soup_to_file(self, url_objeto, file_name):
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")

        if not os.path.isfile(file_name):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(str(soup))
    

obj = ScraperLibre("url") #the class is planned to scrap multiple pages of a website so it is initialized with a string symbolizing a url
url = "https://articulo.mercadolibre.com.mx/MLM-1952179402-pc-gamer-ryzen-5600g-32gb-ram-1tb-ssd-graficos-radeon-7-wifi-_JM#position=2&search_layout=stack&type=item&tracking_id=a17e972d-e8fc-4a4c-924e-effb51bdbf30"

# Todays project due only asks to return the data from one item, so the method to use is data_scrap
print(obj.data_scrap(url))