import random

print(random.randint(1, 100))
print(random.randrange(1, 100))
print(random.randrange(5))

print(random.random())
lista = [67, 45, 22, 11, 33, 44, 61]
print(lista)
print(random.choice(lista))

print(random.choice(lista))
i = random.choice(lista)
lista.remove(i)
print(lista)
print(i)

lista_kule = list(range(1, 50))
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(lista_kule)

print(random.choices(lista_kule, k=6))  # z powtórzeniami
print(random.sample(lista_kule, k=6))  # bez powtórzeń
