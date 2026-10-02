import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()

usd = data["Valute"]["USD"]["Value"]
eur = data["Valute"]["EUR"]["Value"]

print(f"Курс доллара: {usd} руб.")
print(f"Курс евро: {eur} руб.")

with open("курс.txt", "w", encoding="utf-8") as f:
    f.write(f"Курс доллара: {usd} руб.\n")
    f.write(f"Курс евро: {eur} руб.\n")