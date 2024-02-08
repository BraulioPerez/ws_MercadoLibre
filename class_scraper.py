import requests
from bs4 import BeautifulSoup
import json

class ScraperLibre():
    def __init__(self, url):
        self.url = url

    def modify_url(self):
        # input = base url
        # function: hacer que el url sea modificable con el codigo
        # output = url modificado en forma de str
        None

    def increase_page(self):
        # input = link de búsqueda
        # funcion: aumenta en 50 el valor de la busqueda
        # output = link de busqueda modificado
        None

    def title_scrap(self, url_objeto):
        return("scrapeando titulo")
        # input = url_objeto
        # funcion = extraer titulo de objeto
        # output = string del titulo


    def price_scrap(self, url_objeto):
        return("scrapeando precio")
        # input = url_objeto
        # funcion = extraer precio de objeto
        # output = string del precio

    
    def rating_scrap(self, url_objeto):
        return ("scrapeando rating")
        # input = url_objeto
        # funcion = extraer rating de objeto
        # output = string del rating

    
    def images_scrap(self, url_objeto):
        return ("scrapeando imagenes")
        # input = url_objeto
        # funcion = extraer url de imagenes de objeto
        # output = lista de urls

    
    def provider_scrap(self, url_objeto):
        return ("scrapeando proveedor")
        # input = url_objeto
        # funcion = extraer titulo de proveedor del objeto
        # output = string del titulo del proveedor
    
    def description_scrap(self, url_objeto):
        return ("scrapeando descripcion")
        # input = url_objeto
        # funcion = extraer Descripcion de objeto
        # output = string de la descripcion


    def data_scrap(self, url_objeto):
        return {"title": self.title_scrap(url_objeto), "price": self.price_scrap(url_objeto), "rating": self.rating_scrap(url_objeto), "images": self.images_scrap(url_objeto), "provider": self.provider_scrap(url_objeto)}


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
            all_data[url] = self.data_scrap(url)
            print(all_data[url])
        print(all_data)

        return all_data

    


MercadoLibre = ScraperLibre("https://listado.mercadolibre.com.mx/television-60-pulgadas#D[A:television%2060%20pulgadas]")

json_res = MercadoLibre.scrap_all()

with open("sample.json", "w") as outfile: 
    json.dump(json_res, outfile)
