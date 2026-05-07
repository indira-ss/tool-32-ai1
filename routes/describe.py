from flask import Blueprint, request, jsonify
from services.groq_client import call_groq

describe_bp = Blueprint("describe", __name__)


@describe_bp.route("/describe", methods=["POST"])
def describe():

    data = request.get_json()

    user_input = data.get("text")

    with open("prompts/describe_prompt.txt", "r") as file:
        template = file.read()

    final_prompt = template.replace("{user_input}", user_input)

    result = call_groq(final_prompt)

    return jsonify({
        "input": user_input,
        "result": result
    })