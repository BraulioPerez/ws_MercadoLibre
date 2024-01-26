# Importamos las bibliotecas necesarias
import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp
from concurrent.futures import ProcessPoolExecutor
import os
import pandas as pd

# Esta función genera la URL de búsqueda para un artículo en MercadoLibre
def get_search_url(item: str):
    item = item.replace(" ", "-")
    base_url = 'https://listado.mercadolibre.com.mx/'
    return f"{base_url}{item}_Desde_01_NoIndex_True"

# Esta función extrae el atributo href de un elemento BeautifulSoup
def get_attribute(element):
    return element.get("href")

# Esta función asíncrona obtiene todos los enlaces de los productos para un artículo
async def get_item_product_links(session, url: str):
    all_ml_items = []
    while url:
        async with session.get(url) as page:
            soup = BeautifulSoup(await page.text(), "html.parser")
            items = soup.find_all("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")
            items = map(get_attribute, items)
            all_ml_items.extend(items)
            next_page_link = soup.find('a', {'title': 'Siguiente'})
            url = next_page_link['href'] if next_page_link else None
    print("links obtenidos")
    return all_ml_items

# Esta función asíncrona extrae el título de un producto a partir de su enlace
async def extract_data_from_links(session, url: str):
    for _ in range(3):
        try:
            async with session.get(url) as page:
                soup = BeautifulSoup(await page.text(), "html.parser")
                title = soup.find("h1", class_="ui-pdp-title")
                if title:
                    title = title.text
                return title
        except aiohttp.client_exceptions.ServerDisconnectedError:
            continue
    return None

# Esta es la función principal que coordina todo el proceso
async def main():
    items = ['cama', 'colchon', 'sofa', 'mesa', 'sillas', 'armarios', 'comodas', 'mesanoche', 'escritorio']
    all_titles = []
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for item in items:
            search_url = get_search_url(item)
            links = await get_item_product_links(session, search_url)
            titles = await asyncio.gather(*(extract_data_from_links(session, link) for link in links))
            all_titles.extend(titles)
    df = pd.DataFrame(all_titles, columns=['Title'])
    df.to_csv("testeo.csv")
    print(df)

# Este es el punto de entrada del programa
if __name__ == "__main__":
    asyncio.run(main())
