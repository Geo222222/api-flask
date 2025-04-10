from flask import Blueprint, jsonify
from services.news_service import fetch_tech_news, fetch_women_empowerment_news

news_bp = Blueprint('news', __name__)

@news_bp.route("/tech-news")
def get_tech_news():
    try:
        return jsonify(fetch_tech_news())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@news_bp.route("/womens-empowerment")
def womens_empowerment_news():
    try:
        return jsonify(fetch_women_empowerment_news())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
