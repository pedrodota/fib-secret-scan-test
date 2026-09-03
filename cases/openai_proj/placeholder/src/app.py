import requests

OPENAI_API_KEY = "sk-proj-88cnkesOw2FBpfMU130lmkdAJUTompFCyYVIWQWiKvzzM_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {OPENAI_API_KEY}"})
