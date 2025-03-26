# klasy

# tworzenie obiektu uruchamia metode __init__ w klasie
# nazwy klas używa się PascalCase

class Human:
    """
    To jest dokumentacja
    """

    imie = ""
    wiek = ""
    plec = ""

    def __init__(self):
        print("JESTEM INIT!!")

    def powitanie(self):
        print(f"NAzywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam lat {self.wiek}")
    def wypisz_plec(self):
        print(f"Jestem płci {self.plec}")

# print(print.__doc__)
# print(Human.__doc__)

cz = Human()
cz.imie = "Patryk"
cz.wiek = 22
cz.plec = 'Nie wiadomo'
print(cz.imie)
print(cz.wiek)
print(cz.plec)

cz_sec = Human()
cz_sec.imie = "Adam"
cz_sec.wiek = 40
cz_sec.plec = "Helikopter"

print(cz_sec.imie)
print(cz_sec.plec)
print(cz_sec.wiek)

cz.powitanie()
cz_sec.powitanie()
cz_sec.wypisz_wiek()
cz_sec.wypisz_plec()
