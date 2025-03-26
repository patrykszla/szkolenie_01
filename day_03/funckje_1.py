# PEP 8 - 2 linie odstępu między deklaracją a ciałem programu!!!
a = 8
b = 9


def dodaj():
    print(a + b)


dodaj()


def dodaj_1(a, b):
    print(a + b)


dodaj_1(22, 33)


def odejmij(a, b, c=0):
    return(a - b - c)


odejmij(10, 3, 2)

odejmij(b=20, a=13, c=2)
odejmij(b=20, a=13)

#argumenty mieszane
odejmij(a=2, b=2, c=1)

