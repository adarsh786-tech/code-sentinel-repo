
# Intentional hardcoded secret for testing
import requests

# VULNERABILITY: hardcoded API key
" Vulnerability is there"
API_KEY = "sk-prod-abc123xyz789secretkey"
BASE_URL = "https://api.example.com"
PASSWORD = "testPassword@12345"
def get_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}",
                           headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()
