from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.validator import validate_text
from datetime import datetime
from services.logger import logger
describe_bp = Blueprint("describe", __name__)


@describe_bp.route("/describe", methods=["POST"])
def describe():

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
    logger.info(f"/describe called with input: {user_input}")
    # Load prompt template
    with open("prompts/describe_prompt.txt", "r") as file:
        template = file.read()

    final_prompt = template.replace("{user_input}", user_input)

    # Call AI
    ai_result = call_groq(final_prompt)

    return jsonify({
        "input": user_input,
        "result": ai_result,
        "generated_at": datetime.now().isoformat()
    })