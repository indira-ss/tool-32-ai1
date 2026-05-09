import app

from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os


@app.route("/generate-report", methods=["POST"])
def generate_report():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({
                "status": "error",
                "message": "Missing 'text' field"
            }), 400

        user_input = data["text"]

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a structured AI report for: {user_input}"
                }
            ]
        )

        return jsonify({
            "status": "success",
            "input": user_input,
            "result": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500