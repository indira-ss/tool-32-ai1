from flask import Blueprint, jsonify
from datetime import datetime
import time

health_bp = Blueprint("health", __name__)

START_TIME = time.time()


@health_bp.route("/health", methods=["GET"])
def health():

    uptime_seconds = int(time.time() - START_TIME)

    return jsonify({
        "status": "running",
        "service": "tool-32-ai-service",
        "model": "llama-3.3-70b-versatile",
        "uptime_seconds": uptime_seconds,
        "timestamp": datetime.now().isoformat(),
        "avg_response_time": "<2 seconds"
    })