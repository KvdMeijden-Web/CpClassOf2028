import requests
from getpass import getpass
import time

API_KEY = getpass("Enter API key: ")

url = "https://generativelanguage.googleapis.com/v1beta/interactions"

data = {
    "model": "gemini-3.5-flash-lite",
    "input": "Say hello in one short sentence.",
    "generation_config": {
        "thinking_level": "low",
        "max_output_tokens": 200
    }
}

print("Contacting Gemini...")
start = time.time()

try:
    response = requests.post(
        url,
        headers={"x-goog-api-key": API_KEY},
        json=data,
        timeout=60
    )

    print("Response time:", round(time.time() - start, 2), "seconds")
    print("HTTP status:", response.status_code)
    print(response.text[:3000])

except requests.exceptions.RequestException as error:
    print("Connection error:", error)