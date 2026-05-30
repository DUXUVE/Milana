<<<<<<< HEAD
class Passport:
    def __init__(self, name, bd, country, series, number):
        self.name = name
        self.bd = bd
        self.country = country
        self.series = series
        self.number = number


class ForeignPassport(Passport):
    def __init__(self, name, bd, country, series, number, visas, number_fp):
        super().__init__(self, name, bd, country, series, number)
        self.visas = visas
        self.number_fp = number_fp
=======
class Passport:
    def __init__(self, name, bd, country, series, number):
        self.name = name
        self.bd = bd
        self.country = country
        self.series = series
        self.number = number


class ForeignPassport(Passport):
    def __init__(self, name, bd, country, series, number, visas, number_fp):
        super().__init__(self, name, bd, country, series, number)
        self.visas = visas
        self.number_fp = number_fp
>>>>>>> 584b0d35490c6577054f9f07dca7c8cb65214a5c
