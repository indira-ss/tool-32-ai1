import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "AI Service Running"})

@app.route("/health")
def health():
    return jsonify({"status": "running"})

@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()
    return jsonify({
        "input": data.get("text"),
        "result": "API working on Render"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)