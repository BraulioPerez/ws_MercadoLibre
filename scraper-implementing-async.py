from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import aiohttp
import asyncio
import os
import time

def create_search_link(item:str):
    print("creando links de búsqueda")
    item = item.replace(" ", "-")
    return f"https://listado.mercadolibre.com.mx/{item}_Desde_01_NoIndex_True"

async def extract_href(session, url):
    try:
        async with session.get(url) as response:
            page = await response.text()
            soup = BeautifulSoup(page, "html.parser")
            return [link.get("href") for link in soup.find_all('a')]
    except Exception as e:
        print(f"Error accessing URL {url}: {e}")  # Print any exceptions that occur

async def extract_item_urls(search_url:str):
    print("extrayendo urls de items")
    href_values = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(search_url) as response:
                page = await response.text()
                soup = BeautifulSoup(page, "html.parser")
                urls = [link.get("href") for link in soup.find_all("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")]
                tasks = [extract_href(session, url) for url in urls]
                href_values = await asyncio.gather(*tasks)
                await asyncio.sleep(2)  # Add a delay of 1 second
    except Exception as e:
        print(f"Error {e}")
    return href_values

import concurrent.futures

def process_urls(urls):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    all_urls = loop.run_until_complete(asyncio.gather(*(extract_item_urls(url) for url in urls)))
    return all_urls

if __name__ == '__main__':
    start = time.time()
    items = [
        'cama king size', 'sofa', 'mesa', 'sillas', 'armarios', 'nevera', 'lavadora', 'television 60 pulgadas', 'cocina', 'seguridad'
    ]

    urls = list(map(create_search_link, items))
    print(urls)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(process_urls, urls)
        all_urls = future.result()

    print(all_urls)
    end = time.time()
    print(all_urls)
