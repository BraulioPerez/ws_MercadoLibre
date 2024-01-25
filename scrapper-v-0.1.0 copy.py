import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
import time
import os


def get_search_url(item: str):
    # Replace spaces with hyphens and construct the search URL
    item = item.replace(" ", "-")
    base_url = 'https://listado.mercadolibre.com.mx/'
    return f"{base_url}{item}_Desde_01_NoIndex_True"


def increase_page_num(url: str):
    # Increment the page number in the URL by 50
    beginning, ending = url.split("_", 1)
    pattern = r'\d+'
    modified_ending = re.sub(pattern, lambda match: str(int(match.group()) + 50), ending)
    return beginning + "_" + modified_ending


def get_attribute(element):
    return element.get("href")


def get_item_product_links(url: str, item: str):
    all_ml_items = []

    try: 
        with requests.Session() as session:
            while url:  # Mientras haya una URL para procesar
                page = session.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                items = soup.find_all("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")
                items = map(get_attribute, items)
                all_ml_items.extend(items)
                print(len(all_ml_items))
                # Busca el enlace a la siguiente página en lugar de calcularlo
                next_page_link = soup.find('a', {'title': 'Siguiente'})
                url = next_page_link['href'] if next_page_link else None
    except Exception as e:
        print(f"Error: {e}")
    return {f"{item}":all_ml_items}

x = get_item_product_links("https://autos.mercadolibre.com.mx/audi/a1/audi-a1_Desde_01_NoIndex_True", "audi-tt")

def extract_data_from_links(url: str):
    try:
        with requests.Session() as session:
            page = session.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            title = soup.find("h1", class_="ui-pdp-title")
            print(title)
    except Exception as e:
        print(f"Error: {e}")

map(extract_data_from_links, x)