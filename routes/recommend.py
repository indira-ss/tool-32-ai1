from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.validator import validate_text
import json
from services.logger import logger
recommend_bp = Blueprint("recommend", __name__)


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "text field is required"
        }), 400

    # Validate input
    is_valid, result = validate_text(data.get("text"))

    if not is_valid:
        return jsonify({
            "error": result
        }), 400

    user_input = result
    logger.info(f"/recommend called with input: {user_input}")
    # Load prompt
    with open("prompts/recommend_prompt.txt", "r") as file:
        template = file.read()

    final_prompt = template.replace("{user_input}", user_input)

    # Call AI
    ai_result = call_groq(final_prompt)

    try:
        parsed_result = json.loads(ai_result)
        return jsonify(parsed_result)

    except Exception:
        logger.error("Invalid AI response in /recommend")
        return jsonify({
            "error": "Invalid AI response",
            "raw_response": ai_result,

        }), 500