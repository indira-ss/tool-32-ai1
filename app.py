import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# -------------------------
# HEALTH CHECK
# -------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "running",
        "service": "AI Service is live"
    })


# -------------------------
# AI REPORT GENERATION
# -------------------------
@app.route("/generate-report", methods=["POST"])
def generate_report():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({
                "error": "Missing 'text' field"
            }), 400

        user_input = data["text"]

        # Groq AI call
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a structured AI report on: {user_input}"
                }
            ]
        )

        ai_output = response.choices[0].message.content

        return jsonify({
            "input": user_input,
            "result": ai_output
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# -------------------------
# RUN SERVER (RENDER READY)
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)