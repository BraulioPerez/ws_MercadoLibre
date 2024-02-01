from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import os
import time
import re

def create_search_link(item:str):
    print("creando links de búsqueda")
    item = item.replace(" ", "-")
    return f"https://listado.mercadolibre.com.mx/{item}_Desde_01_NoIndex_True"


def extract_href(session, url):
    try:
        with session.get(url) as response:
            page = response.text
            soup = BeautifulSoup(page, "html.parser")
            return [link.get("href") for link in soup.find_all('a')]
    except Exception as e:
        print(f"Error accessing URL {url}: {e}")


def get_information(url:str):
    return None
    # try:
    #     #Generar soup
    #     res = requests.get(url)
    #     soup = BeautifulSoup(res.text, "html.parser")
        
    #     #Obtener titulo
    #     title = soup.find("h1", {"class": "ui-pdp-title"}).text
    #     prices = soup.find_all("span", {"class": "andes-money-amount__fraction"}, limit=2)

    #     #Obtener precios
    #     desc = soup.find("p", {"class": "ui-pdp-description__content"}).text
        
    #     #Obtener vendedor
    #     seller = soup.find("div", {"class":"ui-pdp-seller__header__title"})
    #     complete_sellername = seller.find_all("span")
        
    #     #Dividir entre nombre del vendedor y separar link
    #     if len(complete_sellername) == 2:
    #         seller_name = complete_sellername[0].text + " " + complete_sellername[1].text
    #     else:
    #         seller_name = complete_sellername.text

    #     rate_div = soup.find("div", attrs={"class":"ui-review-capability__rating"})
    #     rate_p = rate_div.find_all("p")
    #     rate = rate_p[0].text
    #     amont_rates = rate_p[2].text

    #     store_url_div = soup.find("div", {"class":"ui-pdp-container__col col-2 mr-32"})
    #     store_url = store_url_div.find("a")['href']
    
    #     if len(prices) == 2:
    #         price_before = prices[0].text
    #         price_current = prices[1].text
    #         information_list = [title, seller_name, store_url, price_before, price_current, desc, rate, amont_rates]            
    #     else:
    #         price_current = prices[0].text          
    #         price_before = None         
    #         information_list = [title, seller_name, store_url, price_before, price_current, desc, rate, amont_rates]            

    #     return information_list



    # except Exception as e:
    #    # By this way we can know about the type of error occurring
    #     print("The error is: ",e)
    #     return []


def extraer_elementos(url):
    # Realizar la solicitud HTTP a la url
    response = requests.get(url)
    
    # Crear una instancia de BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscar los elementos por clase y extraer el texto
    titulo = soup.find(class_='ui-pdp-title').get_text()
    fraccion = soup.find(class_='andes-money-amount__fraction').get_text()
    contenido = soup.find(class_='ui-pdp-description__content').get_text()
    vendedor = soup.find(class_='ui-pdp-seller__header__title').get_text()
    
    # Devolver los resultados en un diccionario
    resultados = [titulo, fraccion, contenido, vendedor]
    print(resultados)
    return resultados


def increase_page_num(url: str):
    # Increment the page number in the URL by 50
    beginning, ending = url.split("_", 1)
    pattern = r'\d+'
    modified_ending = re.sub(pattern, lambda match: str(int(match.group()) + 50), ending)
    return beginning + "_" + modified_ending


def extract_item_urls(search_url:str):
    href_values = []
    try:
        with requests.Session() as session:
            while True:
                page = session.get(search_url)
                print(search_url)
                soup = BeautifulSoup(page.text, "html.parser")
                urls = [link.get("href") for link in soup.find_all("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")]
                if not urls:
                    break
                for url in urls:
                    href_values.append(extract_href(session, url))
                search_url = increase_page_num(search_url)
    except Exception as e:
        print(f"Error {e}")
    print(len(href_values))
    return href_values


if __name__ == '__main__':
    start = time.time()
    # Test 
    # items = [
    #     'television 60 pulgadas', "control de xbox"
    # ]

    #lista de item con pocas pag para que funcione rápido
    items = ["television 60 pulgadas"]

    #se aplican las funciones con la funcion map para que sea más rápido y evitar loops sobre loops sobre loops
    urls = list(map(create_search_link, items))
    all_urls = list(map(extract_item_urls, urls))
    for url in all_urls:
        extraer_elementos(url)
    end = time.time()
    print(f"el programa tardó {(end-start)//60} minutos")
