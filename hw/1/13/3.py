class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def Input_data(self):
        self.name = input()
        self.opening_date = input()
        self.country = input()
        self.city = input()
        self.capacity = input()

    def __str__(self):
        return f"{self.name} {self.opening_date} {self.country} {self.city} {self.capacity}"


stadium = Stadium(name=None, opening_date=None, country=None, city=None, capacity=None)
stadium.Input_data()
print(stadium)