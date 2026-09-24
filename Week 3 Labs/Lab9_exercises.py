################################################## LECTURE ##################################################
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "unknown"

class Dog(Animal):
    def make_sound(self):
        #return super().make_sound()
        return "Woof Woof"

class Cat(Animal):
    def make_sound(self):
        #return super().make_sound()
        return "Meow Meow"

animals = [Dog("Rex"), Cat("Shaula")]


for animal in animals:
    print(animal.name, animal.make_sound())

# work if class is empty, not with an init.
#dog = Dog("Buba")
#print(isinstance(dog, Dog("GG")))


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name} - Score: {self.score}"

student = Student("Lola", 99)


# has-a composition

class Engine:
    def __init__(self, hp):
        self.hp = hp
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine = Engine(200)
car = Car("Audi", engine)
print(car.brand, car.engine.hp)
################################################## LECTURE ##################################################