from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import os
import time

def create_search_link(item:str):
    print("creando links de búsqueda")
    item = item.replace(" ", "-")
    return f"https://listado.mercadolibre.com.mx/{item}_Desde_01_NoIndex_True"

def extract_href(url:str):
    with requests.Session() as session:
        page = session.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        return [link.get("href") for link in soup.find_all('a')]

def extract_item_urls(search_url:str):
    print("extrayendo urls de items")
    href_values = []
    try:
        with requests.Session() as session:
            page = session.get(search_url)
            soup = BeautifulSoup(page.text, "html.parser")
            urls = [link.get("href") for link in soup.find_all("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")]
            for url in urls:
                href_values.append(extract_href(url))
    except Exception as e:
        print(f"Error {e}")
    return href_values




if __name__ == '__main__':
    start = time.time()
    items = [
        'cama king size', 'sofa', 'mesa', 'sillas', 'armarios', 'nevera', 'lavadora', 'television 60 pulgadas', 'cocina', 'seguridad'
    ]

    urls = list(map(create_search_link, items))
    all_urls = list(map(extract_item_urls, urls))
    end = time.time()
