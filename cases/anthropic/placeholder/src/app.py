import requests

ANTHROPIC_API_KEY = "sk-ant-api03-rLYW2hwn2anVV-TQhHQKdp8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {ANTHROPIC_API_KEY}"})
