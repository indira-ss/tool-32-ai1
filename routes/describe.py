from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime

describe_bp = Blueprint("describe", __name__)


@describe_bp.route("/describe", methods=["POST"])
def describe():

    data = request.get_json()

    # Validate input
    if not data or "text" not in data:
        return jsonify({
            "error": "text field is required"
        }), 400

    user_input = data.get("text").strip()

    if user_input == "":
        return jsonify({
            "error": "input cannot be empty"
        }), 400

    # Load prompt template
    with open("prompts/describe_prompt.txt", "r") as file:
        template = file.read()

    final_prompt = template.replace("{user_input}", user_input)

    # Call Groq
    result = call_groq(final_prompt)

    # Return structured JSON
    return jsonify({
        "input": user_input,
        "result": result,
        "generated_at": datetime.now().isoformat()
    })