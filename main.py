import os
import requests


OPEN_AI_KEY = os.environ.get("OPEN_AI_KEY")

def generate_x_post(topic: str) -> str:
    prompt = (f"You're an expert social media manager, and you excel at crafting viral and highly engaging posts for X(formerly Twitter)."
              f"Your task is to generate a post that is concise, impactful and tailored to the topic provided by the user."
              f"Avoid using hashtags and lots of emojis (a few emojis are fine, but don't overdo it)."
              f"Keep the post short and focused structure it in a clean readable way, using line breaks and empty lines to enhance readability."
              f"Here's the topic for the post: "
              f"---"
              f"{topic}"
              f"---")

    url = "https://api.openai.com/v1/responses"
    payload = {
        "model": "gpt-5-nano",
        "input": prompt,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_KEY}"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    data = response.json()
    response_text = ""
    for item in data["output"]:
        if item["type"] == "message":
            response_text = item["content"][0]["text"]

    return response_text


def main():
    # user input => AI (LLM) to generate X post => output post
    user_input = input("What should the post be about? ")
    x_post = generate_x_post(user_input)
    print("Generated X post:")
    print(x_post)


if __name__ == "__main__":
    main()
