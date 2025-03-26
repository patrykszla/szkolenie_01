class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = ""
    wzrost = ""
    plec = ""

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """

        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"NAzywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam lat {self.wiek}")

    def wypisz_plec(self):
        print(f"Jestem płci {self.plec}")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} wzrostu")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę XD")

    def __str__(self):  # dunder methods - metody magiczne
        return f"{self.imie}, {self.wiek}, {self.wzrost}, {self.plec} "


cz1 = Human("Krzysztof", 34, 177, 'm')

print(cz1.wzrost)
print(cz1.wiek)
print(cz1.plec)
print(cz1.imie)

cz1.wypisz_wzrost()

cz2 = Human('Agnieszka', 44, 212, "k")
cz2.ruszaj()

print(cz1)