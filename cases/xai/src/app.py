import requests

XAI_API_KEY = "xai-njl2WiZdI0wsSP_trMb4AoEXnvvlLRdnUvq_wah1u8yoRAz57ksHVhaXvDFXRqupe3grq31O6GqI04TU"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {XAI_API_KEY}"})
