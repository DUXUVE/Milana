class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement
    

class Frigate(Ship):
    def mission(self):
        return "Противолодочные операции"

class Destroyer(Ship):
    def mission(self):
        return "Универсальный корабль"

class Cruiser(Ship):
    def mission(self):
        return "Флагманский корабль"