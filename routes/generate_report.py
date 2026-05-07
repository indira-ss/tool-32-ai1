from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import json

report_bp = Blueprint("report", __name__)


@report_bp.route("/generate-report", methods=["POST"])
def generate_report():

    data = request.get_json()

    # Validation
    if not data or "text" not in data:
        return jsonify({
            "error": "text field is required"
        }), 400

    user_input = data.get("text").strip()

    if user_input == "":
        return jsonify({
            "error": "input cannot be empty"
        }), 400

    # Load prompt
    with open("prompts/report_prompt.txt", "r") as file:
        template = file.read()

    final_prompt = template.replace("{user_input}", user_input)

    # Call AI
    result = call_groq(final_prompt)

    try:
        parsed_result = json.loads(result)
        return jsonify(parsed_result)

    except Exception:
        return jsonify({
            "error": "Invalid AI response",
            "raw_response": result
        }), 500