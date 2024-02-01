from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import os
import time

def create_search_link(item:str):
    print("creando links de búsqueda")
    item = item.replace(" ", "-")
    return f"https://listado.mercadolibre.com.mx/{item}_Desde_01_NoIndex_True"
    # Increment the page number in the URL by 50
    beginning, ending = url.split("_", 1)
    pattern = r'\d+'
    modified_ending = re.sub(pattern, lambda match: str(int(match.group()) + 50), ending)
    return beginning + "_" + modified_ending


def extract_href(session, url):
    try:
        with session.get(url) as response:
            page = response.text
            soup = BeautifulSoup(page, "html.parser")
            return [link.get("href") for link in soup.find_all('a')]
    except Exception as e:
        print(f"Error accessing URL {url}: {e}")


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
            page = session.get(search_url)
            soup = BeautifulSoup(page.text, "html.parser")
            urls = [link.get("href") for link in soup.find_all("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")]
            for url in urls:
                print(url)
                href_values.append(extract_href(session, url))
    except Exception as e:
        print(f"Error {e}")
    print(len(href_values))
    return href_values


if __name__ == '__main__':
    start = time.time()
    items = [
        'television 60 pulgadas', "control de xbox"
    ]

    urls = list(map(create_search_link, items))
    all_urls = list(map(extract_item_urls, urls))
    end = time.time()
