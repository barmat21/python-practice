import requests

response = requests.get("https://api.github.com")
print("Статус:", response.status_code)

data = response.json()
print("Ссылка:", data["current_user_url"])