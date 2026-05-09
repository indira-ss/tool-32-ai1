from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.cache_service import (
    get_cached_response,
    set_cached_response
)
from datetime import datetime
import json

report_bp = Blueprint("report", __name__)


@report_bp.route("/generate-report", methods=["POST"])
def generate_report():

    data = request.get_json()

    text = data.get("text")

    cached_response = get_cached_response(text)

    if cached_response:

        return jsonify({
            "cached": True,
            "generated_at": datetime.now().isoformat(),
            "input": text,
            "result": cached_response
        })

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

        cleaned_result = result.replace("```json", "").replace("```", "").strip()

        parsed_result = json.loads(cleaned_result)

        set_cached_response(text, parsed_result)

        return jsonify({
            "cached": False,
            "generated_at": datetime.now().isoformat(),
            "input": text,
            "result": parsed_result
        })

    except Exception:

        return jsonify({
            "error": "Invalid AI response",
            "raw_response": result
        })