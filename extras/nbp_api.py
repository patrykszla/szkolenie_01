# https://api.nbp.pl/api/exchangerates/tables/{table}/
import requests

url = 'https://api.nbp.pl/api/exchangerates/tables/A/today/'

response = requests.get(url)
print(response)

print(response.text)

print(type(response.text))

data = response.json()
print(type(data))

print("------------------")
for item in data:
    # Możemy tu wydrukować szczegóły kursów walutowych
    print(f"Date: {item['effectiveDate']}")
    for rate in item['rates']:
        print(f"{rate['currency']}: {rate['mid']} PLN")


url = 'https://api.nbp.pl/api/exchangerates/rates/A/today/'
