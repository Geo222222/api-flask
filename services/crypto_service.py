import requests

def fetch_crypto_ticker():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "price_change_percentage": "1h"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    coins = response.json()

    return [
        {
            "symbol": coin["symbol"].upper(),
            "price": coin["current_price"],
            "change_1h": coin.get("price_change_percentage_1h_in_currency", 0.0)
        }
        for coin in coins
    ]
