from flask import Flask
from routes.health import health_bp

app = Flask(__name__)
from routes.describe import describe_bp

app.register_blueprint(describe_bp)
# register routes
app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)