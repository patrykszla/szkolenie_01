# Dowolna ilośc argumentów pozycyjnych!!
def liczby(name=None, *cyfry):
    start = 0
    if isinstance(name, str):
        name = name
    else:
        start = int(name)
        name = None
        pass

    print(cyfry)
    count = len(cyfry)
    suma = 0
    try:
        for i in cyfry:
            suma += i
        avg = suma / count
        print(f"Średnia wynosi {avg}")
    except Exception as e:
        print("błąd", e)
    else:
        print(f"średnia wynosi {avg}")
    finally:
        print(f"Koniec obliczeń dla ucznia {name}")
    # print(cyfry)


liczby(1, 2, 3, 4, 521, 1)
liczby('test', 1, 2, 3, 4, 521, 1)
# liczby()
# liczby(22)
