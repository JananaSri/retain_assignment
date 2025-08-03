from flask import Blueprint, request, jsonify, redirect
from app.services.shortener_service import shorten_url, get_original_url, get_stats

shortener_bp = Blueprint("shortener", __name__)

@shortener_bp.route("/api/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    url = data.get("url")
    result, error = shorten_url(url)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(result), 201

@shortener_bp.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    url = get_original_url(short_code)
    if not url:
        return jsonify({"error": "Short code not found"}), 404
    return redirect(url)

@shortener_bp.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    result = get_stats(short_code)
    if not result:
        return jsonify({"error": "Short code not found"}), 404
    return jsonify(result), 200
