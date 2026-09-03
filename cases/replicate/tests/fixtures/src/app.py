import requests

REPLICATE_API_TOKEN = "r8_qyhP-xNjJ4oAe34rRVwJ__g5AQk1B7RVdJvnF"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {REPLICATE_API_TOKEN}"})
