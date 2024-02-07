import requests
from bs4 import BeautifulSoup


class ScraperLibre():
    def __init__(self, url):
        self.url = url

    def increase_page(self):
        # input = link de búsqueda
        # funcion: aumenta en 50 el valor de la busqueda
        # output = link de busqueda modificado
        None

    def title_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer titulo de objeto
        # output = string del titulo
        None

    def price_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer precio de objeto
        # output = string del precio
        None
    
    def rating_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer rating de objeto
        # output = string del rating
        None
    
    def images_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer url de imagenes de objeto
        # output = lista de urls
        None
    
    def provider_scarp(self, url_objeto):
        # input = url_objeto
        # funcion = extraer titulo de proveedor del objeto
        # output = string del titulo del proveedor
        None
    
    def description_scrap(self, url_objeto):
        # input = url_objeto
        # funcion = extraer Descripcion de objeto
        # output = string de la descripcion
        None
    
    def data_scrap(self, url_objeto):
        # Usar todas las previas "xxxx_scrap" para extraer la info del producto
        None

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
            parsed_elements.append(elm.get("href"))
            url = elm.get("href")
            all_data[url] = self.data_scrap(url)
            

        return parsed_elements

    


MercadoLibre = ScraperLibre("https://listado.mercadolibre.com.mx/television-60-pulgadas#D[A:television%2060%20pulgadas]")

print(MercadoLibre.scrap_all())
