import requests

XAI_API_KEY = "xai-afOCH00TEwRl4cRyZS_IWyV_GoMbTjoDUphGKFwAbBUy_LUISbgtbV5V1OdVGMVLii8adF8j_XCSQcl9"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {XAI_API_KEY}"})
