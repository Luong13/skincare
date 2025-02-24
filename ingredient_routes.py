
from flask import Blueprint, request, jsonify
from services.ingredient_service import search_ingredients

# Create Blueprint for ingredient routes
ingredient_bp = Blueprint('ingredients', __name__)

@ingredient_bp.route('/search', methods=['POST'])
def search():
    data = request.json
    ingredients = data.get('ingredients', [])

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    results = search_ingredients(ingredients)
    return jsonify(results)
