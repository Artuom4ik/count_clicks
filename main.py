import os 

import requests 
from dotenv import load_dotenv


load_dotenv()
url = "https://api-ssl.bitly.com/v4/shorten"
token_bitly = os.getenv("API_BITLINK_TOKEN")
headers = {
     "Authorization": token_bitly  
}
params = {
    "long_url": "https://python-scripts.com/json"
}

response = requests.post(url, headers=headers, json=params)

print(response.json())