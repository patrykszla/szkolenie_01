import sys
from decimal import *
wiek = 47
rok = 2025
temp = 36.6

print(temp)
print(type(temp))

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)

print(rok // wiek)

print(rok % wiek)

print(wiek ** rok)

# sys.set_int_max_str_digits(6666)
# print(len(str(wiek ** rok ** 2)))

print(54 - 5 * 43 + 4 / 4 + 2 / 2)
print(54 - 5 * 43 + (4 / 4+ 2 )/ 2)

# Liczby float mają błąd zaokrąglenia!

print(0.2 + 0.8)
print(0.2 + 0.7)
print(0.2 + 0.1)
print(Decimal(0.3) + Decimal(0.2))

print(sys.float_info)

print(f"Sprawdzenie zmiennej {temp} {wiek}")
print(f"""
 {temp}
        {wiek}""")

czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))

print(int(czy_znasz_pythona))
print(int(False))

print(bool(1)) # - rzutowanie na typ logiczny
print(bool(0))

print(bool(100))
print(bool(-100))
print(bool(''))
print(bool(None))