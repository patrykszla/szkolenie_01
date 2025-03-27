import requests


url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)

print(response.text)

print(type(response.text))

data = response.json()
print(type(data))

for k in data:
    print(k)

print(data['value'])


icon_url = data['icon_url']
response_img = requests.get(icon_url)

print(response_img)
print(type(response_img))

# Zapis bajtowo!!!!
with open('icona.jpg', 'wb') as f:
    f.write(response_img.content)

