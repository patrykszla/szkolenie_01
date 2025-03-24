user = "Paryk"
wiek = 22
wersja = 3.90001
liczba = 43213122121

print(type(wersja))

print("Witaj %s, masz teraz %d lat." %(user, wiek))
print("Witaj %(user)s, jesteś %(user)s" % {"user": user})
print(f"Witaj {user}, masz teraz {wiek}")

print("Używamy wersji pythona %i" % 3)
print("Używamy wersji pythona %f" % 3)
print("Używamy wersji pythona %.0f" % 3.9)
print("Używamy wersji pythona %.1f" % 3.9)
print("Używamy wersji pythona %.2f" % 3.9)

x = 3.78922
print(x)
x = (round(x, 2))
print(x)

print(f"Używamy wersji pythona {wersja}")
print(f"Używamy wersji pythona {wersja:.2f}")
print(f"Używamy wersji pythona {wersja:.1f}")
print(f"Używamy wersji pythona {wersja:.0f}")

print(f"{user:<10}")
print(f"{user:>10}")

print(liczba)
print(f"Nasza duza liczba {liczba:,}")
print(f"Nasza duza liczba {liczba:_}")
print(f"Nasza duza liczba {liczba:_}".replace("_", " "))
print(f"Nasza duza liczba {liczba:_}".replace("_", "."))

liczba = 1500000000000000000000
liczba = 1_500_000_000
print(liczba)