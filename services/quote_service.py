import requests

def fetch_inspirational_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "quote": data[0]["q"],
        "author": data[0]["a"]
    }
