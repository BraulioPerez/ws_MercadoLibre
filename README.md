# ws_MercadoLibre
This file describes the functions/methods used in the python script for a Web Scraper.

 - __init__():
 - - This is the special method which gets called when an object of a class is instantiated. This method is used to initialize the attributes of an object.

 - increase_page(search_url):
 - - This method increases the value in the base url by 50. Takes in URL and returns the modified URL.

 - title_scrap(url_objeto):
 - - Scrapes the title of the product page. Takes in URL and returns the title as a string.

 - price_scrap(url_objeto):
 - - Scrapes the price of the product page. Takes in URL and returns a list of string(s) representing the price.
 - - In the scraped webpage, if there are two prices present it returns both; if there is only one price it returns that one; if there are no prices it returns None.

 - rating_scrap(url_objeto):
 - - Scrapes the average rating of the product. Takes in URL and returns the average rating as a string. 
 - - If there are no ratings, it returns None.

 - images_scrap(url_objeto):
 - - Scrapes Links to the product images. Takes in URL and returns a list with links to the product images.

 - provider_scrap(url_objeto):
 - - Scrapes provider's name. Takes in URL and returns the name of the provider as a string.

 - description_scrap(url_objeto):
 - - Scrapes the product description. Takes in URL and returns the text of the description as a string. 
 - - If there are no descriptions, it returns None.

 - data_scrap(url_objeto):
 - - This function collects the scraped data of title, prices, images, rating, provider, and description from the other methods and returns this data as a dictionary.

 - scrap_all():
 - - This function collects all the data of each product item on the page and stores it in JSON format. 
 - - It collects the URLs of each item, scrapes the data for each link, and stores this in a single dictionary.

 - write_soup_to_file(url_objeto, file_name):
 - - his function writes the data from soup (BeautifulSoup object) into a file. It takes in URL and a filename, and  writes the complete HTML text of the webpage into a file.
 - - If the file already exists, it does not overwrite the file.