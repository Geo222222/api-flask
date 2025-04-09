from flask import Flask, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests from frontend (e.g., GitHub Pages)

# Get the News API key securely from environment variables
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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # 2 Options: Use PORT env var or default port 10000
    app.run(host="0.0.0.0", port=port)
