# pętle
import random
from itertools import zip_longest

for x in range(0, 3):
    print("LECIMY Z pętlą ", x)

for i in range(10):
    pass  # nic nie rób

# uzywanie takiego czegos oznacza ze jest mało znacząca
for _ in range(10):  # niema zmienna
    print("Test podloga")
    print(_)

for i in range(5):
    print(i * 2)
    print(i + 2)

for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x * y))

print("LOTTTO ")
for _ in range(6):
    print(random.randint(1, 50))

print("LOTTTO 2")
lista_kule = list(range(1, 50))
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wynik.append(wyn)

print("Wynik losowania:", lista_wynik)

for i in range(10):
    if i % 2 == 0:
        print(i, "Parzysta")

l3 = []
for j in range(10):
    if j % 2 == 0:
        l3.append(j)
print(l3)

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

# foreach!!!!
for c in lista3:
    if c > 4:
        print("Wieksze od 4")
    else:
        print("mniejsze, równe 4")

# Co drugi element
for i in range(0, 10, 2):
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):
    print(i)

for c in lista3:
    if c == 2:
        c += 1
        print("printuje c: ", c)

imiona = ["Tomasz", "Krzysiu", "Ernest", "Zenek"]

for i in imiona:
    print(imiona.index(i), i)

print("Sposób dwa")
for i in range(len(imiona)):
    print(i, imiona[i])

print("sposób trzy")
for i, name in enumerate(imiona, start=1):
    print(i, name)

imiona = ["Tomasz", "Krzysiu", "Ernest", "Zenek"]
wiek = [44, 22, 1, 33]  # lista

print("sposób 4")
for p in imiona:
    print(p, wiek[imiona.index(p)])

print("sposób 5")
for i, w in zip(imiona, wiek):
    print(i, w)

print("sposób 6")
for i, (p, w) in enumerate(zip(imiona, wiek)):  # trzeba wskazac co jest do której krotki
    print(i, p, w)

# iterator
zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)

print(5 * "-")
for i in zipped:
    print(i)
print(5 * "-")

# itertools!!!
zipped = zip_longest(imiona, wiek, fillvalue=None)
zip_list = list(zipped)
for i in zip_list:
    print(i)