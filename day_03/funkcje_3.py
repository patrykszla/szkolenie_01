a = 10
b = 1


def dodaj():
    a = 7
    b = 10
    print(a + b)


def dodaj_2():
    print(a + b)


def dodaj_3():
    global a
    a = 100
    b = 89
    print(a + b)


print(f"Wartość a z góry {a=} (globalna)")
dodaj()
print(f"Wartość a z góry {a=} (globalna)")

dodaj_2()
print(f"Wartość a z góry {a=} (globalna)")

dodaj_3()
print(f"Wartość a z góry {a=} (globalna)")