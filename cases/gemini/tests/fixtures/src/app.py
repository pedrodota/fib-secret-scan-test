import requests

GEMINI_API_KEY = "AIzaSytPqcJpLRsQLMQv1_4zM55A7rr__RyaPQG"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {GEMINI_API_KEY}"})
