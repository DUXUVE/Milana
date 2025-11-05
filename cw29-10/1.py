class Person:
    def __init__(self, name, bd, phone_number, city, country, address):
        self.name = name
        self.bd = bd
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.address = address

    def Input_data(self):
        self.name = input()
        self.bd = input()
        self.phone_number = input()
        self.city = input()
        self.country = input()
        self.address = input()

    def __str__(self):
        return f"{self.name} {self.bd} {self.phone_number} {self.city} {self.country} {self.address}"


a = Person(name=None, bd=None, phone_number=None,
           city=None, country=None, address=None)

a.Input_data()
print(a)
