import requests

ANTHROPIC_API_KEY = "sk-ant-api03-pMehonmEjrcKYbyPoYfB3STDlKoDuZG7j9UDNY4lYarqsc_NNy0eq1L0S7HrlUC8ESosu7qEzDkCObGSq_YAB5GLLaWWSAA"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {ANTHROPIC_API_KEY}"})
