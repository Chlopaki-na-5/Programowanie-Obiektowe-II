# bilet.py

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Bilet(metaclass=SingletonMeta):
    ilosc = 0
    is_normalne = None
    cena = 0

    def reset(self):
        self.ilosc = 0
        self.is_normalne = None
        self.cena = 0

    def change_count(self, how_many):
        if self.ilosc + how_many >= 0:
            self.ilosc += how_many

    def price(self):
        if self.is_normalne:
            self.cena = round((self.ilosc * 4.0), 2)
            print(type(self.cena))
            print(self.cena)
            return str(round(self.cena, 2)) + "0 zł"
        else:
            self.cena = round((self.ilosc * 2.0), 2)
            return str(self.cena) + "0 zł"

    def pay(self):
        if self.cena > 0:
            return str(self.cena) + "0 zł"
        else:
            return str(0) + " zł"