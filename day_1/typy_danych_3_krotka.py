tupla_imiona = ("Radek", "Tomek", "Zenek", "Anna", "Marek")
print(tupla_imiona)
print(type(tupla_imiona))

tupla_liczby = 43, 55, 22, 33, 34, 11, 100
print(type(tupla_liczby))
print(tupla_liczby)
tupla = ("Radek")
print(type(tupla))
tupla = "Radek",
print(type(tupla))

del tupla_liczby  # usuniecie!!
# print(tupla_liczby)

print(tupla_imiona.index("Radek"))
print(tupla_imiona.count("Radek"))

tup = 1, 2
print(type(tup))
a, b = 1, 2

a, b = tup
print(f"{a=}, {b=}")

tup2 = 1, 2, 3

a, *b = tup2
print(f"{a=}, {b=}")

print(tupla_imiona)

a, b, *c = tupla_imiona

print(f"{a=}, {b=}, {c=}")

print(sorted(tupla_imiona))
print(tupla_imiona)
print(type(tupla_imiona))

lista_sorted = sorted(tupla_imiona)
print(type(lista_sorted))
print(lista_sorted)

lista = list(tupla_imiona)
print(lista)
print(type(lista))

array = [[3,4], [5,6]]
print(array)