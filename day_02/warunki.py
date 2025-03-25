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
if(n := len(a)) > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")

podatek = 0
zarobki = int(input("Podaj zarobki"))

if zarobki < 10000:
    podatek = 0
elif zarobki < 40000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.9


print(f"Podatek wynosi {podatek * zarobki}")


#podatek 0.2 dla zarobkow od 10000 do 39999

