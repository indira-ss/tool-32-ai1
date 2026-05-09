from flask import Blueprint, jsonify
from datetime import datetime
from services.groq_client import get_average_response_time
import time

health_bp = Blueprint("health", __name__)

START_TIME = time.time()


@health_bp.route("/health", methods=["GET"])
def health():

    uptime_seconds = round(time.time() - START_TIME, 2)

    return jsonify({
        "service": "ai-service",
        "status": "running",
        "model": "llama-3.1-8b-instant",
        "avg_response_time": f"{get_average_response_time()} sec",
        "uptime_seconds": uptime_seconds,
        "timestamp": datetime.now().isoformat()
    })