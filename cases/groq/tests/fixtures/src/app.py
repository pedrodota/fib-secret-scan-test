import requests

GROQ_API_KEY = "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"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {GROQ_API_KEY}"})
