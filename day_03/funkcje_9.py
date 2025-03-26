# funkcja lambda
# coś jak funkcja anonimowa
from functools import reduce


def odejmij(a, b):
    return a - b


print(odejmij(5, 3))

odejmij2 = lambda a, b: a - b

print(odejmij2(45, 34))

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100

print(oblicz_vat(100))

wiek = lambda x: "dziecko" if x < 10 else ("Nastolatek" if x < 18 else "dorosły")
print(wiek(9))

lista = [1, 2, 4, 5, 24, 22]
wynik = [x * 2 for x in lista]
print(wynik)


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))

print(l2)

# funkcje wyższego rzędu
print(f"zastosowanie map {list(map(zmien, lista))}")

# Zastosowanie lambdy jako funkcja anonimowa!!!
# definicja w miejscu wywołania
print(f"zastosowanie map {list(map(lambda x: x * 2, lista))}")
print(f"zastosowanie map {list(map(lambda x: x * 4, lista))}")
print(f"zastosowanie map {list(map(lambda x: x * 8, lista))}")

# filter()
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)

print(l3)

print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")

print(f"Drugi filter {list(filter(lambda x: x < 3 and x < 250, lista))}")

sum_all = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
print("wynik reduce:", sum_all)

sil = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print("wynik reduce:", sil)
