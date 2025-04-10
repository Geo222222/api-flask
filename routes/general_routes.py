from flask import Blueprint, jsonify, request
import requests

general_bp = Blueprint('general', __name__)

@general_bp.route("/")
def index():
    return jsonify({"message": "Welcome to the Tech News API by DJ Martin."})

@general_bp.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text or len(text.strip()) < 20:
            return jsonify({"error": "Input text is too short."}), 400

        api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {}
        payload = {"inputs": text[:1024]}
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        summary = response.json()[0]["summary_text"]
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@general_bp.route("/blog-feed")
def blog_feed():
    try:
        username = "madsstoumann"
        url = f"https://dev.to/api/articles?username={username}&per_page=6"
        response = requests.get(url)
        response.raise_for_status()

        articles = response.json()
        result = [
            {
                "title": a["title"],
                "url": a["url"],
                "description": a["description"][:150],
                "published": a["published_at"][:10]
            }
            for a in articles
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
