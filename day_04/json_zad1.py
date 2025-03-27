'{"name":"John", "age":30, "car":null}'
import json

person_dict = {'name':'Patryk', 'age': 40, 'czy_pali': True}

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# Upiększanie!
with open('nasze_dane_beautify.json', "w") as f:
    json.dump(person_dict, f, indent=4) # indent - wcięcie


# Upiększanie!
with open('nasze_dane_sortowane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)


with open('nasze_dane.json', "r") as fh:
    data = json.load(fh)

print(data)
print(type(data))
print(data['name'])

json_text = json.dumps(data)
print(json_text)
print(type(json_text))

dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))

for k in dict_json:
    print("Klucz:",k)
