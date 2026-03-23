import requests


def extract_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Data extracted successfully!")
        return data
    else:
        print("Error fetching data")
        return None
