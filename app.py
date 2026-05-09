from flask import Flask

from routes.describe import describe_bp
from routes.generate_report import report_bp
from routes.health import health_bp
from flask import render_template
app = Flask(__name__)

app.register_blueprint(describe_bp)
app.register_blueprint(report_bp)
app.register_blueprint(health_bp)
@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/")
def home():
    return "AI Service is running"


if __name__ == "__main__":
    print("Starting Flask AI Service...")
    app.run(debug=True, host="127.0.0.1", port=5000)
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=10000)