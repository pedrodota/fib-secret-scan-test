import requests

GROQ_API_KEY = "gsk_1T3H9iqXUSWre8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {GROQ_API_KEY}"})
