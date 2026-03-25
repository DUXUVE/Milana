class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def Input_data(self):
        self.model = input()
        self.year = input()
        self.manufacturer = input()
        self.engine_volume = input()
        self.color = input()
        self.price = input()

    def __str__(self):
        return f"{self.model} {self.year} {self.manufacturer} {self.engine_volume} {self.color} {self.price}"


car = Car(model=None, year=None, manufacturer=None, engine_volume=None, color=None, price=None)
car.Input_data()
print(car)