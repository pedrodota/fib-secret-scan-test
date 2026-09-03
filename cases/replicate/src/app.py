import requests

REPLICATE_API_TOKEN = "r8_DV3fgdBq5j3o-nX5atXe91KeER3Kg8H0YSEf1"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {REPLICATE_API_TOKEN}"})
