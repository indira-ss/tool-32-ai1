from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os
import logging

# Load env
load_dotenv()

# Flask app
app = Flask(__name__)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Root endpoint
@app.route("/")
def home():
    return jsonify({
        "message": "API working on Render"
    })

# Health endpoint
@app.route("/health")
def health():
    logger.info("Health endpoint accessed")

    return jsonify({
        "status": "healthy"
    })

# Generate report endpoint
@app.route("/generate-report", methods=["POST"])
def generate_report_api():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({
                "error": "Text field required"
            }), 400

        user_text = data["text"]

        logger.info(f"Generating report for: {user_text}")

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a structured AI report for: {user_text}"
                }
            ]
        )

        return jsonify({
            "status": "success",
            "input": user_text,
            "result": response.choices[0].message.content
        })

    except Exception as e:
        logger.error(str(e))

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)