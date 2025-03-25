# wyjatki

try:
    print(5/0)
    print('TUAJ JESTES')
    print("TUTAJ JESTES 2 ")
    # print("A" * "23")
    # print(int("A"))
    # raise KeyError("Błąd klucza")
    wynik = 90 / 30
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print("Błąd: ", e)
else: #tylko gdy nie ma błędu
    print("Wynik: ", wynik)
finally: #wykonany zawsze!!!
    print("Koniec przetwarzania danych")

print("Program nadal działa")


