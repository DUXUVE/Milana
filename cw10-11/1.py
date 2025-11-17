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
