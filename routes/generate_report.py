from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()
    text = data.get("text")

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": f"Generate AI report for: {text}"}
        ]
    )

    return jsonify({
        "input": text,
        "result": response.choices[0].message.content
    })