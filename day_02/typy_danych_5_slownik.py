# slownik
# "{"user": "Radek", 'wiek': 76}
# '{"name":"John", "age":30, "car":null}'
# odpowiednik json!!

# Pusty słownik
dictionary = dict()
print(dictionary)
print(type(dictionary))

dictionary_1 = {}
print(dictionary_1)
print(type(dictionary_1))

# Dodanie elementu do słownika
dictionary['imie'] = "Patryk"
print(dictionary)
print(dictionary['imie'])
dictionary['wiek'] = 18
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# nadpisanie elementu
dictionary['imie'] = "krzyś"
print(dictionary)

# wypisanie wartości dla elementu ze słownika
print(dictionary['imie'])

print(dictionary.get('imie'))
print(dictionary.get('Imie'))  # case sensitive
print(dictionary.get('Imie', 'defaultowa wartość'))

dictionary.update({'data': '12-12-2025'})
print(dictionary)

dict_small = {'x': 2}
print(dict_small)
dict_small.update([('y', 5), ('z', 48)])
print(dict_small)

# input - pozwala wprowadzic dane
# tekst = input("podaj imię")
# print(tekst)

# liczba_1 = input("liczba 1")
# liczba_2 = input("liczba 2")
# print(f"dodawanie {int(liczba_1) + int(liczba_2)}")


# Napisac aplikacje slownik polsko_ang
slow_pol_ang = {'czesc': 'hi', 'kot': 'cat'}
print("Dostępne słowa: ")
print(slow_pol_ang.keys())
# slowo = input("Podaj slowo")

# print("Przetłumaczone słowo: ", slow_pol_ang[slowo.lower().strip()])
# print(slow_pol_ang.get(slowo.strip().lower(), "nie ma "))


# ẞ  - ss
name1 = "GROSS"
name2 = 'groẞ'
print(name1.lower() == name2.lower())
print(name1.casefold() == name2.casefold())









