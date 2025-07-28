import requests
import json

try:
    response = requests.get("https://api.agify.io?name=test")
    response.raise_for_status() # Raise error for bad status
    data = response.json
    print("API Response:", data)
except requests.exceptions.RequestException as e:
    print(e)
except json.JSONDecodeError as e:
    print(e)
except Exception as e:
    print(e)