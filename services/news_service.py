import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print("DEBUG >>> Loaded NEWS_API_KEY:", NEWS_API_KEY)  # Add this line

def fetch_tech_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": "fintech",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])
    return [
        {"title": article.get("title", "No Title"), "url": article.get("url", "#")}
        for article in articles
    ]

def fetch_women_empowerment_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "women empowerment OR women leadership OR mentoring young women",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])
    return [
        {"title": article.get("title", "No Title"), "url": article.get("url", "#")}
        for article in articles
    ]
