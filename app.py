from flask import Flask, request, jsonify
import logging
app = Flask(__name__)
import os
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
# 🔐 SECURITY HEADERS (ADD HERE)
@app.after_request
def add_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response


# ---------------- ROUTES START HERE ----------------

@app.route("/")
def home():
    return "AI Service Running"


@app.route("/health")
def health():
    return jsonify({"status": "running"})


@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()
    return jsonify({"result": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


    @app.route("/health")
    def health():
        logger.info("Health endpoint accessed")

        return {
            "status": "healthy"
        }