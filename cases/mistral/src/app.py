import requests

MISTRAL_API_KEY = "YewebKJZruOROdCysKyASkxCfNnsoVyv"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"})
