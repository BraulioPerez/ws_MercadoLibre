import requests
from bs4 import BeautifulSoup

"""
Author: Francisco Chan
Date: January 26, 2024
"""

# Modification History:
# - Version 0.1: Initial release (January 26, 2024)


def get_information(url:str):
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    #rate = soup.find("span", attrs={"aria-hidden":"true", "class":"ui-pdp-review__rating"})
    #amont_rates = soup.find("span", attrs={"aria-hidden":"true", "class":"ui-pdp-review__amount"})
    try:
        title = soup.find("h1", {"class": "ui-pdp-title"}).text
        prices = soup.find_all("span", {"class": "andes-money-amount__fraction"}, limit=2)


        desc = soup.find("p", {"class": "ui-pdp-description__content"}).text
        seller = soup.find("div", {"class":"ui-pdp-seller__header__title"})
        complete_sellername = seller.find_all("span")
        if len(complete_sellername) == 2:
            seller_name = complete_sellername[0].text + " " + complete_sellername[1].text
        else:
            seller_name = complete_sellername.text

        rate_div = soup.find("div", attrs={"class":"ui-review-capability__rating"})
        rate_p = rate_div.find_all("p")
        rate = rate_p[0].text
        amont_rates = rate_p[2].text
        
        store_url_div = soup.find("div", {"class":"ui-pdp-container__col col-2 mr-32"})
        store_url = store_url_div.find("a")['href']
        
        if len(prices) == 2:
            price_before = prices[0].text
            price_current = prices[1].text
            information_list = [title, seller_name, store_url, price_before, price_current, desc, rate, amont_rates]
        else:
            price_current = prices[0].text
            price_before = None
            information_list = [title, seller_name, store_url, price_before, price_current, desc, rate, amont_rates]
            
    except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e)

    return information_list
    
    
Mercado_url = "https://www.mercadolibre.com.mx/tableta-digitalizadora-wacom-intuos-s-ctl-4100wl-con-bluetooth-black/p/MLM15071474#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes-univb&reco_client=home_navigation-recommendations&reco_item_pos=1&reco_backend_type=function&reco_id=db5af8a2-11b0-4627-98a8-76e608a3844a&wid=MLM796398553&sid=recos&c_id=/home/navigation-recommendations/element&c_uid=7ee30c16-110a-41aa-ac9e-622452c137fa"

product1 = get_information(Mercado_url)

print(product1)
    