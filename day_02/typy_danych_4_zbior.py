# zbiór (set) - nieprzechowują duplikatów
# nie zachowuje kolejności przy dodawaniu
# nie posiada indeksu
lista = [44, 55, 66, 777, 333, 222, 11, 33, 11]
zbior = set(lista)
print(zbior)
print(type(zbior))

# tworzenie zbioru tylko za pomoca set!!
zb2 = set()
print(zb2)
print(type(zb2))

# dodanie elementu do zbioru

zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(24)
zbior.add(33)
print(zbior)

# usuniecie elementu
zbior.remove(33)
print(zbior)

# pop() - usunięcie pierwszego elementu ze zbioru
print(zbior.pop())
print(zbior)
print(zbior.pop())

zmienna = zbior.pop()
print(f"usunelismy {zmienna}")

zbior_copy = zbior.copy()
print(zbior_copy)
print(zbior)
print(id(zbior))
print(id(zbior_copy))

# operacje na zbiorach
zbior_2 = {22, 211, 44, 55, 66, 18, 12.222}
print(type(zbior_2))
print(zbior_2)

# suma zbiorow - zwraca nowy zbior
print(zbior | zbior_2)
print(zbior.union(zbior_2))

# część wspólna
print(zbior & zbior_2)
print(zbior.intersection(zbior_2))

# roznica - kolejność ma znaczenie!!!!!!!!
print(zbior - zbior_2)
print(zbior.difference(zbior_2))
print(zbior_2.difference(zbior))

# łączy zbiory, zmienia bazowy
zbior.update(zbior_2)
print(zbior)

krotka = tuple(zbior)
print(krotka)
lista = list(zbior)
print(lista)

# Sprawdzenie elementu w kolekcji
print(66 in zbior)
print(333 in zbior)
print(33122 in zbior)

