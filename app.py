from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Tech News API by DJ Martin."})

@app.route("/api/tech-news")
def get_tech_news():
    if not NEWS_API_KEY:
        return jsonify({"error": "API key is not set."}), 500

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": "technology",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return jsonify([
            {
                "title": article.get("title", "No Title"),
                "url": article.get("url", "#")
            }
            for article in articles
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/crypto-ticker")
def crypto_ticker():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,ethereum,solana,cardano,dogecoin",
            "vs_currencies": "usd"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        prices = response.json()

        return jsonify([
            {"symbol": "BTC", "price": prices["bitcoin"]["usd"]},
            {"symbol": "ETH", "price": prices["ethereum"]["usd"]},
            {"symbol": "SOL", "price": prices["solana"]["usd"]},
            {"symbol": "ADA", "price": prices["cardano"]["usd"]},
            {"symbol": "DOGE", "price": prices["dogecoin"]["usd"]}
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/inspiration')
def get_inspiration():
    # Example: Get an inspirational quote
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    return jsonify({"quote": quote, "author": author})
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
