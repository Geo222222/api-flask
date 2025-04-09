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

@app.route("/api/womens-empowerment")
def womens_empowerment_news():
    if not NEWS_API_KEY:
        return jsonify({"error": "API key is not set."}), 500

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "women empowerment OR women leadership OR mentoring young women",
        "language": "en",
        "sortBy": "publishedAt",
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

        result = []
        for coin in coins:
            result.append({
                "symbol": coin["symbol"].upper(),
                "price": coin["current_price"],
                "change_1h": coin.get("price_change_percentage_1h_in_currency", 0.0"%")
            })

        return jsonify(result)

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
