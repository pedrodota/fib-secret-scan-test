import requests

GEMINI_API_KEY = "AIzaSyg67UTpNxxxxxxxxxxxxxxxxxxxxxxxxxx"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {GEMINI_API_KEY}"})
