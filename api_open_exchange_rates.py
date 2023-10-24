import requests

response = requests.get('https://openexchangerates.org/api/latest.json?app_id=2a79f1183f864ff19561b6a9e9d09860')
print(response.status_code)
print(response.json())