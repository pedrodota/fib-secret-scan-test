import requests

OPENAI_API_KEY = "sk-XrzbQ3hIJwO0Kqxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {OPENAI_API_KEY}"})
