import os 

import requests 
from dotenv import load_dotenv


def shorten_link(token_bitly, user_url):
    headers = {
        "Authorization": token_bitly  
    }
    params = {
        "long_url": user_url
    }
    url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()["link"]

    
if __name__ == "__main__":
    load_dotenv()
    user_url = input() 
    token_bitly = os.getenv("API_BITLINK_TOKEN")
    try:          
        bitlink = shorten_link(token_bitly, user_url)
        print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print("У вас ошибка в адресе")
