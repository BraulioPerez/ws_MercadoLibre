import requests
from bs4 import BeautifulSoup
import json

class ScraperLibre:
    def __init__(self, url):
        self.url = url

    def increase_page(self):
        # Function to increase the value of the search by 50
        None

    def title_scrap(self, url_objeto):
        # Function to extract the title of the object
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        
        title = soup.select("div.ui-pdp-header__title-container h1")[0].text
        print(title)
        return title

    def price_scrap(self, url_objeto):
        # Function to extract the price of the object
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        
        prices = soup.select("div.ui-pdp-price__main-container span.andes-money-amount__fraction")
        print(len(prices))
        if len(prices) >= 2:
            price_before = prices[0].text
            price_current = prices[1].text
            prices_list = [price_before, price_current]            
        else:
            price_current = prices[0].text
            price_before = None
            prices_list = [price_before, price_current]
        
        print(price_before, price_current)
        return prices_list
    
    def rating_scrap(self, url_objeto):
        # Function to extract the rating of the object
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        
        review_div = soup.select("div[class*='ui-review-capability__rating'] p")
        if len(review_div) == 0:
            rate = None
        else:
            rate = review_div[0].text
            
        print(review_div)
        print(rate)
        return rate
    
    def images_scrap(self, url_objeto):
        # Function to extract the URLs of the images of the object
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        
        images_list = soup.select("div.ui-pdp-gallery__column span.ui-pdp-gallery__wrapper label.ui-pdp-gallery__label div[role='presentation'] div.ui-pdp-thumbnail__picture img.ui-pdp-image")
        urls_img = []
        for img in images_list:
            url = img.get('data-src')
            urls_img.append(url)   
            
        print(urls_img)
        return urls_img
    
    def provider_scarp(self, url_objeto):
        # Function to extract the title of the provider of the object
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        
        provider_list = soup.select("div.ui-seller-info div.ui-pdp-seller__header__title")
        provider = provider_list[0].text
        print(provider)
        return provider
    
    def description_scrap(self, url_objeto):
        # Function to extract the description of the object
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")        
        
        description_list = soup.select("div[class*='ui-pdp-container__row'] p.ui-pdp-description__content")
        description = description_list[0].text
        print(description)
        return description
    
    def data_scrap(self, url_objeto):
        # Use all the previous "xxxx_scrap" functions to extract the info of the product
        title = self.title_scrap(url_objeto)
        prices = self.price_scrap(url_objeto)
        rating = self.rating_scrap(url_objeto)
        images = self.images_scrap(url_objeto)
        provider = self.provider_scarp(url_objeto)
        description = self.description_scrap(url_objeto)

        # Construct dictionary with collected data
        data = {
            "title": title,
            "prices": prices,
            "rating": rating,
            "images": images,
            "provider": provider,
            "description": description
        }

        return data

    def scrap_all(self):
        # Typical function to scrape the search links of the object
        # Apart from fetching the search links of each object, it must enter and scrape the data of each object in the form of dictionaries
        # Add the dictionary to a big JSON
        # Move to the next page
        # The loop breaks when it no longer finds objects to scrape

        # For demonstration purposes, let's just return a single object's data in JSON format
        data = self.data_scrap(self.url)
        json_data = json.dumps(data, indent=4)  # Convert dictionary to JSON string with indentation
        return json_data
    

url = "https://www.mercadolibre.com.mx/lg-pantalla-uhd-tv-ai-thinq-60-4k-smart-tv-60uq8000psb/p/MLM20656479?pdp_filters=category:MLM1002#searchVariation=MLM20656479&position=1&search_layout=stack&type=product&tracking_id=206d5c4e-efeb-4809-b0d5-4cce35d3a100"
object = ScraperLibre(url)
json_data = object.scrap_all()
print(json_data)