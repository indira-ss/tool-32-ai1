from flask import Flask
import time

from routes.health import health_bp
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.generate_report import report_bp


app = Flask(__name__)

START_TIME = time.time()

app.register_blueprint(health_bp)
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)


if __name__ == "__main__":
    app.run(debug=True, port=5000)