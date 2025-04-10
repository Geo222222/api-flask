from flask import Blueprint, jsonify
from services.crypto_service import fetch_crypto_ticker
from services.quote_service import fetch_inspirational_quote

utility_bp = Blueprint('utility', __name__)

@utility_bp.route("/crypto-ticker")
def crypto_ticker():
    try:
        return jsonify(fetch_crypto_ticker())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@utility_bp.route("/inspiration")
def get_inspiration():
    try:
        return jsonify(fetch_inspirational_quote())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
