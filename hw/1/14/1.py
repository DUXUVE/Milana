class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class CoffeeMachine(Device):
    def make_coffee(self):
        return "Кофе готовится"

class Blender(Device):
    def blend(self):
        return "Измельчение продуктов"

class MeatGrinder(Device):
    def grind_meat(self):
        return "Мясо измельчено"