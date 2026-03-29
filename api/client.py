
# Intentional hardcoded secret for testing
import requests
# making change for PR testing
# VULNERABILITY: hardcoded API key
API_KEY = "sk-prod-abc123xyz789secretkey"
BASE_URL = "https://api.example.com"

def get_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}",
                           headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()
