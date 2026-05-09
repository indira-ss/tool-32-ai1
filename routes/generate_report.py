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

    ai_response = call_groq(prompt)

    # FALLBACK RESPONSE
    if not ai_response["success"]:

        fallback_response = {
            "title": "Fallback AI Report",
            "summary": "AI service temporarily unavailable.",
            "overview": f"Fallback response generated for: {text}",
            "key_items": [
                "Fallback mode activated",
                "Groq service unavailable"
            ],
            "recommendations": [
                "Try again later",
                "Check Groq API status"
            ],
            "is_fallback": True
        }

        return jsonify({
            "cached": False,
            "generated_at": datetime.now().isoformat(),
            "input": text,
            "result": fallback_response
        })

    try:

        result = ai_response["data"]

        cleaned_result = result.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

        parsed_result = json.loads(cleaned_result)

        parsed_result["is_fallback"] = False

        set_cached_response(text, parsed_result)

        return jsonify({
            "cached": False,
            "generated_at": datetime.now().isoformat(),
            "input": text,
            "result": parsed_result
        })

    except Exception:

        fallback_response = {
            "title": "Fallback AI Report",
            "summary": "Invalid AI response received.",
            "overview": f"Fallback response generated for: {text}",
            "key_items": [
                "Response parsing failed"
            ],
            "recommendations": [
                "Retry request"
            ],
            "is_fallback": True
        }

        return jsonify({
            "cached": False,
            "generated_at": datetime.now().isoformat(),
            "input": text,
            "result": fallback_response
        })