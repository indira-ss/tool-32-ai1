from flask import Flask, request, jsonify

app = Flask(__name__)


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