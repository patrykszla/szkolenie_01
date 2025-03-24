# Kolekcje
lista = []
print(lista)
print(type(lista))

pusta_lista = list()
print(pusta_lista)
print(type(pusta_lista))
lista.append('test')
lista.append('ernest')
lista.append('krzysztof')
lista.append('marian')
print(lista)

print(len(lista))

print(lista[len(lista) - 1])
print(lista[-1])
print(lista[-3])
print(lista[0:3])
print(lista[:3])
print(lista[2:])
print(lista[2:4])

print(lista[2:16])
print(lista[2:2])
print(lista[2:3])
print(lista[10:20])

print(lista[-2:0])
print(lista[0:-2])

lista_15 = list(range(15))
print(lista_15)
print(lista_15[0:15:2])
print(list(range(0, 15, 2)))
print(lista[::2])  # co drugi element!!!
print(lista[::-1])  # odwrócona lista!!

lista[3] = "ania"
print(lista)
lista.insert(1, 'Pawełek')
print(lista)

lista.insert(15, 'KRZYCHU')
print(lista)
print(lista.index("KRZYCHU"))

# USUNIĘCIE ELEMENTU
lista.remove("KRZYCHU")
lista.append(22)
print(lista)
# lista.pop(4)
print(lista.pop(4)) # zwraca element który usunął
print(lista.pop(-3))
print(lista.pop) # kasuje tylko ostatni element!!
print(lista)

a = 1
b = 3
a = b

print(f"{a=}, {b=}")
b = 9
print(f"{a=}, {b=}")

lista_2 = lista

print(lista_2)
print(lista)

lista_copy = lista.copy

lista.clear()
print(lista)
print(lista_2)

print(id(lista))
print(id(lista_2))
print(id(lista_copy)) #inny adres w pamięci!!

liczby = [54, 999, 34, 22, 11, 12.34, 567]
print(liczby)
print(type(liczby))
liczby.sort()
print(liczby)

liczby = [54, 999, 34, 22, 11, 12.34, 567, 'A']
print(type(liczby))

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby[-2])
print(liczby)

tekst = "Pytho on."
lista1 = list(tekst) # rozpakowanie sekwencji! z PHP explode
print(lista1)

lista2 = [tekst]
print(lista2)

krotka = tuple(liczby) #immutable!! ważne
print(krotka)
