import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv(override=True)

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

TOTAL_RESPONSE_TIME = 0
TOTAL_REQUESTS = 0


def call_groq(prompt):

    global TOTAL_RESPONSE_TIME
    global TOTAL_REQUESTS

    try:

        start_time = time.time()

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        end_time = time.time()

        response_time = end_time - start_time

        TOTAL_RESPONSE_TIME += response_time
        TOTAL_REQUESTS += 1

        return response.choices[0].message.content

    except Exception as e:
        return f"AI service error: {str(e)}"


def get_average_response_time():

    if TOTAL_REQUESTS == 0:
        return 0

    return round(TOTAL_RESPONSE_TIME / TOTAL_REQUESTS, 2)