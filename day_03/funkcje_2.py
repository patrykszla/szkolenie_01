# zwracanie wyników

def dodaj(a, b):
    return a + b


print(dodaj(2, 3))


def odejmij(a,b,c):
    return a-b-c

print(odejmij(10,2,2))

def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100

print(oblicz_vat(100))

print(oblicz_vat(vat=8, kwota=1000))

a = oblicz_vat(1000)
if a == 1230:
    print("OK")


print(dodaj(6,4) + dodaj(5,5))