import requests

REPLICATE_API_TOKEN = "r8_K4TdvCDus7xxxxxxxxxxxxxxxxxxxxxxxxxxx"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {REPLICATE_API_TOKEN}"})
