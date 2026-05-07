from flask import Flask
from routes.describe import describe_bp
from routes.recommend import recommend_bp

app = Flask(__name__)

app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)


@app.route("/health")
def health():
    return {
        "service": "tool-32-ai-service",
        "status": "running"
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)