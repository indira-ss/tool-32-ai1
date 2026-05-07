import os
import requests
from dotenv import load_dotenv
load_dotenv(override=True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("KEY =", GROQ_API_KEY)
URL = "https://api.groq.com/openai/v1/chat/completions"


def call_groq(prompt):
    try:
        # Debug key
        print("DEBUG KEY:", GROQ_API_KEY)
        print("FINAL KEY USED:", GROQ_API_KEY)
        print("GROQ KEY LOADED:", GROQ_API_KEY)
        if not GROQ_API_KEY:
            return "ERROR: GROQ_API_KEY not found in .env"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
           "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5
        }

        response = requests.post(URL, json=payload, headers=headers)

        data = response.json()

        # Debug full response
        print("GROQ RESPONSE =", data)

        # Safe check
        if "choices" not in data:
            return f"Groq API Error: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI service error: {str(e)}"