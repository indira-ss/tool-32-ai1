from flask import Blueprint, request, jsonify
from services.groq_client import call_groq

describe_bp = Blueprint("describe", __name__)


@describe_bp.route("/describe", methods=["POST"])
def describe():

    data = request.get_json()

    text = data.get("text")

    result = call_groq(text)

    return jsonify({
        "result": result
    })