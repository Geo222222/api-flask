from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables requests from localhost:5173

NEWS_API_KEY = "YOUR_NEWSAPI_KEY"  # Replace with your NewsAPI key

@app.route("/api/tech-news")
def get_tech_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": "technology",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])[:5]
        return jsonify([
            {"title": a["title"], "url": a["url"]}
            for a in articles
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
