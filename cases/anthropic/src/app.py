import requests

ANTHROPIC_API_KEY = "sk-ant-api03-NY3NvWry74JFRq2aRdC5XAAYGNEdbK5vVxAZUTymBPt16OXaOvzqCsw4b-mJZdnjM2TH6yB200bg1sBlmk3E8yJ-OZ05aAA"


def call():
    return requests.post("https://api.example.com/v1", headers={"Authorization": f"Bearer {ANTHROPIC_API_KEY}"})
