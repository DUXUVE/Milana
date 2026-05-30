class City:
    def __init__(self, name, region_name, country_name, population, postal_code, phone_code):
        self.name = name
        self.region_name = region_name
        self.country_name = country_name
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        self.name = input()
        self.region_name = input()
        self.country_name = input()
        self.population = input()
        self.postal_code = input()
        self.phone_code = input()

    def __str__(self):
        return f"{self.name} {self.region_name} {self.country_name} {self.population} {self.postal_code} {self.phone_code}"


a = City(name=None, region_name=None, country_name=None,
         population=None, postal_code=None, phone_code=None)

a.input_data()
print(a)
