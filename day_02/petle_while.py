# while - pętle sterowane

# Pętla nieskończona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat II II")
    if licznik > 10:
        break
print(licznik)

licznik = 0
while licznik < 10:
    licznik += 1
    print("KOMUN III III")

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło, podaj ponownie")

# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
#
# print(lista)
# print(lista_int)


my_list = [2, 3, 4, 5, 21, 35, 5, 5, 23, 2]
element_to_remove = 5

licznik = 0
while element_to_remove in my_list:
    my_list.remove(element_to_remove)
# Lista bez utraty kolejności - idealne wykorzystanie while!!
print(my_list)

my_list = [2, 3, 4, 5, 21, 35, 5, 5, 23, 2]
# Element listy staje się kluczem w słowniku
print(dict.fromkeys(my_list))

# Drugi sposób na otrzymanie listy bez duplikatów
unique_numbers = list(dict.fromkeys(my_list))
print(unique_numbers)


