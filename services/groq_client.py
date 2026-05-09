import os
import requests
from dotenv import load_dotenv

# FORCE reload env every time
load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("ACTIVE GROQ KEY =", GROQ_API_KEY)


URL = "https://api.groq.com/openai/v1/chat/completions"


def call_groq(prompt):

    try:

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.5
        }

        response = requests.post(
            URL,
            json=payload,
            headers=headers,
            timeout=30
        )

        data = response.json()

        if "error" in data:
            return f"Groq API Error: {data['error']['message']}"

        if "choices" not in data:
            return "AI response unavailable"

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "AI request timeout"

    except requests.exceptions.ConnectionError:
        return "AI connection failed"

    except Exception as e:
        return f"AI service error: {str(e)}"