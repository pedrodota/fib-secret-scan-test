import requests

GROQ_API_KEY = "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"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {GROQ_API_KEY}"})
