class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year, predkosc):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # pole prywatne - hermetyzacja
        self.__predkosc = predkosc # pole prywatne!!!

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkośc wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __str__(self):
        return(f"{self.model} + {self.year} + {self.__predkosc}")

    def __zmien_bieg(self):
        print("zmiana biegu")


car = Car('Twingo', 2023, 10)


car.gaz()
car.gaz()
car.__predkosc = 0
car.licznik()
car.hamuj()
car.hamuj()
print(car)
