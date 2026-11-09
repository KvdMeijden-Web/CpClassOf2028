
import requests
from getpass import getpass
import time

#Variables:
# API setup
API_KEY = getpass("Enter your Gemini API key: ")
url = "https://generativelanguage.googleapis.com/v1beta/interactions"

# Instructions for the AI
instructions = """
You are the Dungeon Master of a fantasy adventure game.

Rules:
- The player starts inside an abandoned castle.
- Describe the environment and what happens.
- Include monsters, treasure, puzzles and mysteries.
- Keep responses short (maximum 100 words).
- Always finish by asking what the player does next.
- Never decide what the player does.
- Remember previous decisions and events.
- Keep the story suitable for school students.

Start by describing the first room.
"""
# Stores the previous conversation ID
previous_id = None

#start
print("\n===== AI DUNGEON ADVENTURE =====")
print("Type 'exit' to quit.\n")

# First message starts the adventure
action = instructions

while True:

    # Prepare the API request form of a dictionary {model,input,generation_config}
    data = {
        "model": "gemini-3.5-flash-lite",
        "input": action,
        "generation_config": {
            "max_output_tokens": 500
        }
    }

    # Include previous conversation if available in the data Dictionary
    if previous_id is not None:
        data["previous_interaction_id"] = previous_id

    print("\nContacting Gemini...")
    start = time.time()

    # Send request
    try:
        response = requests.post(
            url,
            headers={"x-goog-api-key": API_KEY},
            json=data,
            timeout=60
        )

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)
        break

    print("Response time:", round(time.time() - start, 2), "seconds")

    # Check for API errors
    if response.status_code != 200:
        print("API error:", response.status_code)
        print(response.text)
        break

    # Convert JSON response
    result = response.json()

    # Get generated text from model_output steps
    answers = []

    for step in result.get("steps", []):
        if step.get("type") == "model_output":
            for content in step.get("content", []):
                if content.get("type") == "text":
                    answers.append(content["text"])

    if not answers:
        print("No text was returned.")
        print(result)
        break

    answer = "\n".join(answers)

    # Remember the conversation
    previous_id = result["id"]

    # Display the story
    print("\n===== DUNGEON MASTER =====")
    print(answer)

    # Ask for the player's next action
    action = input("\nWhat do you do? ").strip()

    if action.lower() == "exit":
        print("\nAdventure ended!")
        break

    if not action:
        action = "I look around the room."
