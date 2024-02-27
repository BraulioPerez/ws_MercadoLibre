import requests
from bs4 import BeautifulSoup
import os



class ItemDataScraper:
    def __init__(self, url):
        self.url = url
        self.title = None
        with requests.Session() as session:
            self.session = session.get(self.url)


    def title_scrap(self):
        # input = url_objeto
        # funcion = extraer titulo de objeto
        # output = string del titulo

        soup = BeautifulSoup(self.session.text, "html.parser")
        title = soup.select("div.ui-pdp-header__title-container h1")[0].text
        return title


    def price_scrap(self):
        # input = url_objeto
        # funcion = extraer precio de objeto
        # output = string del precio

        soup = BeautifulSoup(self.session.text, "html.parser")
        prices = soup.select("div.ui-pdp-price__main-container span.andes-money-amount__fraction")
        if len(prices) >= 2:
            price_before = prices[0].text
            price_current = prices[1].text
            price_credit = soup.select_one("div.ui-pdp-price__main-container div.ui-pdp-price__subtitles span.andes-money-amount__fraction")
            if prices[1] == price_credit:
                price_current = price_before
                price_before = None
            prices_list = [price_before, price_current]
        elif len(prices) ==0:
            prices_list = None          
        else:
            price_current = prices[0].text
            price_before = None
            prices_list = [price_before, price_current]
            
        return prices_list
    
    def rating_scrap(self):
        # input = url_objeto
        # funcion = extraer rating de objeto
        # output = string del rating

        soup = BeautifulSoup(self.session.text, "html.parser")
        review_div = soup.select("div[class*='ui-review-capability__rating'] p")
        if len(review_div) != 0:
            rate = review_div[0].text
        elif len(review_div) == 0:
            rate = soup.select_one("div.ui-pdp-header div[class*='ui-pdp-header__info'] a[class*='ui-pdp-review__label'] span.ui-pdp-review__rating")
        else:
            rate = None

        return rate


    def images_scrap(self):
        # input = url_objeto
        # funcion = extraer url de imagenes de objeto
        # output = lista de urls

        soup = BeautifulSoup(self.session.text, "html.parser")
        images_list = soup.select("div.ui-pdp-gallery__column span.ui-pdp-gallery__wrapper label.ui-pdp-gallery__label div[role='presentation'] div.ui-pdp-thumbnail__picture img.ui-pdp-image")
        urls_img = []
        for img in images_list:
            url = img.get('data-src')
            urls_img.append(url)   
        
        return urls_img
    
    
    def provider_scrap(self):
    # input = url_objeto
    # funcion = extraer titulo de proveedor del objeto
    # output = string del titulo del proveedor

        try:
            soup = BeautifulSoup(self.session.text, "html.parser")
            provider_list = soup.select("div.ui-seller-info div.ui-pdp-seller__header__title")
            if len(provider_list) == 0:
                provider_unique = soup.select_one("div.ui-pdp-seller__header div.ui-pdp-seller__header__info-container div.ui-pdp-seller__header__info-container__title span[class*='ui-pdp-color--BLUE']")
                provider = provider_unique.text if provider_unique else "No provider found"
            else:
                provider = provider_list[0].text 

            return provider
        except Exception as e:
            print(f"An error occurred: {e}")
            return None



    def description_scrap(self):
        # input = url_objeto
        # funcion = extraer Descripcion de objeto
        # output = string de la descripcion

        soup = BeautifulSoup(self.session.text, "html.parser")        
        description_list = soup.select("div[class*='ui-pdp-container__row'] div.ui-pdp-description p.ui-pdp-description__content")
        if len(description_list) == 0:
            description = None
        else:
            description = description_list[0].text

        return description


    def data_scrap(self):
        #No input
        # Returns information in json format
        title = self.title_scrap()
        result = {"title": title,
                    "prices" : self.price_scrap(),
                    "images": self.images_scrap(),
                    "rating": self.rating_scrap(),
                    "provider": self.provider_scrap(),
                    "description": self.description_scrap() 
                    }
        return result


    def debug_write_soup_to_file(self, url_objeto, file_name):
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")

        if not os.path.isfile(file_name):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(str(soup))