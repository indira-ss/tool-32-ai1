from flask import Flask, jsonify

from routes.describe import describe_bp
from routes.generate_report import report_bp

app = Flask(__name__)

app.register_blueprint(describe_bp)
app.register_blueprint(report_bp)


@app.route("/", methods=["GET"])
def home():
    return "AI Service is running"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "running"
    })


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)