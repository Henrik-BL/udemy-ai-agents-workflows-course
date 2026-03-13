import os
import requests

url = "https://api.openai.com/v1/responses"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['OPEN_AI_KEY']}"
}

payload = {
    "model": "gpt-5-nano",
    "input": "write a haiku about ai",
    "store": True
}

response = requests.post(url, headers=headers, json=payload)


data = response.json()

response_text = ""

for item in data["output"]:
    if item["type"] == "message":
        response_text = item["content"][0]["text"]

print(response_text)
