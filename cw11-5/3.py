class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Builder(Human):
    def __init__(self, name, age, number_of_buildings):
        super().__init__(name, age)
        self.number_of_buildings = number_of_buildings

    def build(self):
        print("")


class Sailor(Human):
    def __init__(self, name, age, number_of_swimings):
        super().__init__(name, age)
        self.number_swimings = number_of_swimings

    def sail(self):
        print("")


class Pilot(Human):
    def __init__(self, name, age, number_of_flights):
        super().__init__(name, age)
        self.number_flights = number_of_flights

    def fly(self):
        print("")
