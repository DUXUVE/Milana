from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав"

class Cat(Animal):
    def make_sound(self):
        return "Мяу"

def let_animal_speak(animal: Animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

print("Собака говорит:", end=" ")
let_animal_speak(dog)
print("Кошка говорит:", end=" ")
let_animal_speak(cat)