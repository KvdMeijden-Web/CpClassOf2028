import requests

url = "https://textbelt.com/status/956929"

response = requests.get(url, timeout=10)
data = response.json()

print("SMS status:", data["status"])