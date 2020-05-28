# implementacja obiektowa
# odwolanie do samego siebie, do wnetrza obiektu, pozwala nam do
# obiektu dopisac zmienna
# kazdy obiekt ma swoja metode self, czyli taki konstruktor
class Konto:
    def __init__(self, stan_poczatkowy, imie, nazwisko, numer):
        print("Jestem metoda __init__")
        # atrybut obiektu o nazwie stan i wartosci, ktora przypiszemy
        # przy tworzeniu instancji tej klasy
        self.stan = stan_poczatkowy
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def wplac(self, kwota):
        self.stan += kwota

    def wyplac(self, kwota, ):
        if self.stan >= kwota:
            self.stan -= kwota
            print("Wyplaciles: ", kwota)
        else:
            raise Exception("Nie masz wystarczajacych srodkow, aby wyplacic dana kwote")

    def pokaz_detale(self, ):
        string = f"{self.imie} {self.nazwisko} {self.stan}"
        print(string)

    def przelej(self, kwota, konto_odbiorcy):
        try:
            temp = self.wyplac(kwota)
            konto_odbiorcy.wplac(temp)
        except Exception:
            print("EKRAN STRONY INTERENTOWEJ: Brak środków do przelewu")


'''za kazdym razem jak tworzymy instancje danej klasy, twrzony 
jest nowy obiekt, czyli ponizej stworzyly nam sie 2 nowe obiekty'''
konto1 = Konto(1000, "Jan", "Kowalski", 123456789)
konto2 = Konto(1220, "Zbigniew", "Nowak", 123456789)
konto1.wplac(100)
konto1.wyplac(100)
konto1.przelej(5,konto2)
konto1.pokaz_detale()
konto2.pokaz_detale()