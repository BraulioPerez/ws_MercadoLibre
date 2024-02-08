import requests
from bs4 import BeautifulSoup



class ScraperLibre:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.prices_list = None
        self.rate = None
        self.urls_img = None
        self.provider = None
        self.description = None
        

    def increase_page(self):
        # input = link de búsqueda
        # funcion: aumenta en 50 el valor de la busqueda
        # output = link de busqueda modificado
        None

    def title_scrap(self, url_objeto):
        # input = url_objeto
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        
        title = soup.select("div.ui-pdp-header__title-container h1")[0].text
        print(title)
        # funcion = extraer titulo de objeto
        # output = string del titulo
        self.title = title

    def price_scrap(self, url_objeto):
        # input = url_objeto
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        # funcion = extraer precio de objeto
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
        
        print(prices_list)
        # output = string del precio
        self.prices_list = prices_list
    
    def rating_scrap(self, url_objeto):
        # input = url_objeto
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        # funcion = extraer rating de objeto
        review_div = soup.select("div[class*='ui-review-capability__rating'] p")
        if len(review_div) != 0:
            rate = review_div[0].text
        elif len(review_div) == 0:
            rate = soup.select_one("div.ui-pdp-header div[class*='ui-pdp-header__info'] a[class*='ui-pdp-review__label'] span.ui-pdp-review__rating")
            print(rate)
            
        print(review_div)
        print(rate)
        # output = string del rating
        self.rate = rate
    
    def images_scrap(self, url_objeto):
        # input = url_objeto
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        # funcion = extraer url de imagenes de objeto
        #images_list = soup.select("div.ui-pdp-gallery__column span figure.ui-pdp-gallery__figure img")
        images_list = soup.select("div.ui-pdp-gallery__column span.ui-pdp-gallery__wrapper label.ui-pdp-gallery__label div[role='presentation'] div.ui-pdp-thumbnail__picture img.ui-pdp-image")
        urls_img = []
        for img in images_list:
            url = img.get('srcset')
            urls_img.append(url)   
            
        print(urls_img)
        # output = lista de urls
        self.urls_img = urls_img
    
    
    def provider_scarp(self, url_objeto):
        # input = url_objeto
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")
        # funcion = extraer titulo de proveedor del objeto
        provider_list = soup.select("div.ui-seller-info div.ui-pdp-seller__header__title")
        print(provider_list)
        if len(provider_list) == 0:
            provider_unique = soup.select_one("div.ui-pdp-seller__header div.ui-pdp-seller__header__info-container div.ui-pdp-seller__header__info-container__title span[class*='ui-pdp-color--BLUE']")
            provider = provider_unique.text
        else:
            provider = provider_list[0].text
            
        
        
        print(provider)
        # output = string del titulo del proveedor
        self.provider = provider
    
    def description_scrap(self, url_objeto):
        # input = url_objeto
        res = requests.get(url_objeto)
        soup = BeautifulSoup(res.text, "html.parser")        
        # funcion = extraer Descripcion de objeto
        description_list = soup.select("div[class*='ui-pdp-container__row'] div.ui-pdp-description p.ui-pdp-description__content")
        if len(description_list) == 0:
            description = None
        else:
            description = description_list[0].text
        print(description)
        # output = string de la descripcion
        self.description = description
    
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
        None
    

url = "https://www.mercadolibre.com.mx/escurridor-alto-ajustable-doble-tarja-para-platos-moda-cm-color-negro/p/MLM22619015#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes-univb&reco_client=home_navigation-recommendations&reco_item_pos=4&reco_backend_type=function&reco_id=7a4ccfd2-bc47-4336-ab65-452b41bbeb27&wid=MLM2014535193&sid=recos&c_id=/home/navigation-recommendations/element&c_uid=860e4efd-4c3c-459a-99af-e98f3db8c91a"
object = ScraperLibre(url)
url2 = "https://articulo.mercadolibre.com.mx/MLM-1763817956-kit-mantenimiento-pc-aire-alcohol-pasta-termica-3g-_JM#polycard_client=recommendations_home_second-best-navigation-trend-recommendations&reco_backend=machinalis-homes-univb&reco_client=home_second-best-navigation-trend-recommendations&reco_item_pos=3&reco_backend_type=function&reco_id=fb570432-c61a-45d9-aa5e-3a14c9d58d30&c_id=/home/second-best-navigation-trend-recommendations/element&c_uid=2654a610-4c2f-4b18-864f-4e723dc901a6"
object.title_scrap(url2)
object.price_scrap(url2)
object.rating_scrap(url2)
object.images_scrap(url2)
object.provider_scarp(url2)
object.description_scrap(url2)

    