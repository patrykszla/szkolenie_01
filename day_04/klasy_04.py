from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """
    
    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa kura dziedzicy po klasie Ptak
    """

    def __init__(self, gatunek):
        # super - klasa wyższa
        super().__init__(gatunek, 0)  # obowiązkowo musimy wywołać konstruktor klasy wyższej

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print('Ko ko ko ko')

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")

class Orzel(Ptak):
    """
    Diedziczy po klasie ptak
    :param Ptak:
    :return:
    """

    def wydaj_odglos(self):
        print("Kir kier kir")

    def polowanie(self):
        print("Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Dziedziczy po klasie ptak
    """

    def wydaj_odglos(self):
        print("Ho ho ho ")



# pt1 = Ptak('Jastrząb', 200)
# pt1.latam()
# pt1.wydaj_odglos()
#
# pt2 = Ptak('Orzeł', 150)
# pt2.latam()
# pt2.wydaj_odglos()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()

kur2 = Kura("Kura")
kur2.latam()

orz2 = Orzel("Orzeł Bielik", 50)
orz2.wydaj_odglos()

kur2.wydaj_odglos()

sowa = Sowa("Sowa", 20)
sowa.wydaj_odglos()


print("----------------")
lista = [kur2, orz2]
for i in lista:
    i.wydaj_odglos()


