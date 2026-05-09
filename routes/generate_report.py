from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime
import json

report_bp = Blueprint("report", __name__)


@report_bp.route("/generate-report", methods=["POST"])
def generate_report():

    data = request.get_json()

    text = data.get("text")

    prompt = f"""
Generate a report for: {text}

Return ONLY valid JSON.

Required format:

{{
    "title": "",
    "summary": "",
    "overview": "",
    "key_items": [],
    "recommendations": []
}}
"""

    result = call_groq(prompt)

    try:
        # Remove markdown formatting
        cleaned_result = result.replace("```json", "").replace("```", "").strip()

        # Convert string response to JSON
        parsed_result = json.loads(cleaned_result)

        return jsonify({
            "generated_at": datetime.now().isoformat(),
            "input": text,
            "result": parsed_result
        })

    except Exception as e:
        return jsonify({
            "error": "Invalid AI response",
            "raw_response": result
        })