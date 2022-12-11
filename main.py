from urllib.parse import urlparse
import os
import argparse

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
    return response.json()['link']


def count_clicks(token_bitly, bitlink):
    headers = {
        "Authorization": token_bitly
    }
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    count_clicks = requests.get(url, headers=headers)
    count_clicks.raise_for_status()
    return count_clicks.json()["total_clicks"]


def is_bitlink(token_bitly, prepared_url):
    headers = {
        "Authorization": token_bitly
    }
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{prepared_url}"
    response = requests.get(url, headers=headers)
    return response.ok


def get_user_url():
    parser = argparse.ArgumentParser(
        description=
        """Программа создает из вашей ссылки короткую\
        и считает количество переходов по ней."""
    )
    parser.add_argument("link", help="Ваша ссылка")
    args = parser.parse_args()
    return args.link


if __name__ == "__main__":
    load_dotenv()
    token_bitly = os.getenv("API_BITLINK_TOKEN")
    user_url = get_user_url()
    parsed_url = urlparse(user_url)
    prepared_url = f"{parsed_url.netloc}{parsed_url.path}"
    try:
        if is_bitlink(token_bitly, prepared_url):
            clicks_count = count_clicks(token_bitly, prepared_url)
            print("Сделано кликов", clicks_count)
            get_user_url()
        else:
            bitlink = shorten_link(token_bitly, user_url)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print("У вас ошибка в адресе")
