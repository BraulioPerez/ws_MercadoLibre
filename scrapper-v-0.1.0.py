import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
import time
import os
import pandas as pd


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


def get_item_product_links(url: str, item: str):
    all_ml_items = []

    try: 
        with requests.Session() as session:
            page = session.get(url)
            soup = BeautifulSoup(page.text, "html.parser")# Extract the total number of pages from the pagination information
            iterator = re.findall(r'\d+', soup.find("li", class_="andes-pagination__page-count").text)
            total_pages = int(iterator[0]) if iterator else 1
            for _ in range(total_pages):
                soup = BeautifulSoup(page.text, "html.parser")
                items = soup.find_all("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")
                all_ml_items.extend(items)
                print(len(all_ml_items))
                url = increase_page_num(url)
    except Exception as e:
        print(f"Error: {e}")
    return {f"{item}":all_ml_items}

x = get_item_product_links("https://autos.mercadolibre.com.mx/audi/a1/audi-a1_Desde_01_NoIndex_True", "audi-tt")


def extract_data_from_links(item_info: dict):
    for item in item_info.values():   
        print(item)
        print("\n")

extract_data_from_links(x)