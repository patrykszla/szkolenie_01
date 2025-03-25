# instrukcje warunkowe
# instrukcje sterowania przepływem programu

odp = True
odp = False
if odp:
    print('Spelniony')
    print('Spelniony')
    print('Spelniony')
    print('Spelniony')
    print('Spelniony')

print("dalsza część programu")

odp = "Patryk"
print(bool(odp))
if odp:
    print("TEST")

odp = 0
if odp:
    print("DZIALA !!")
else:
    print("mamy else!!")

a = "Patryk"
if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, wiecej niz 3")

a = "Patryk"
n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")

# Operator mors, walrus operator :=
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
#
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 40000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9


# print(f"Podatek wynosi {podatek * zarobki}")


# podatek 0.2 dla zarobkow od 10000 do 39999


suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

# Zasymulujemy system logów
# Zmienna będzie pzechowywać informacje jaki system wysłał log
# email, console, inny
# gdy alert z systemu console -> "Stało się coś strasznego"
# gdy alert z systemu email -> "System email"
# gdy alert mail -> druga zmienna przechowująca error, medium inny
# Nalezy opis bledu dodac do listy bledow
# eror -> krytyczny

log = ''
error = "error"
errors = list()
alert = input("jaki log")
if alert == 'console':
    log = "Stało się coś strasznego"
elif alert == 'email':
    if error == "error":
        errors.append("Krytyczny")
    elif error == "medium":
        errors.append("Ostrzeżenie")
    else:
        errors.append("Inny")
    log = "system email"
else:
    log = "inny"

print(log)
print(errors)

odp = input("Podaj datę chrztu Polski (rok)")
punkty = 0
if odp.strip().casefold() == "966":
    print("Dobrze")
    punkty += 1
else:
    print("Musisz się dalej uczyć")

odp = input("Stolica Polski")
if odp.strip().casefold() == "Warszawa".casefold():
    print("Dobrze")
    punkty += 1
else:
    print("Musisz się dalej uczyć")

print(f"Twój wynik {punkty}")