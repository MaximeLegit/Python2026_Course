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


################################################ Assignment ##################################################

# Part A. Polymorphism

class Notification:
    def send(self):
        return "General Message"

class EmailNotification(Notification):
    def send(self):
            return "Email Notification"

class SMSNotification(Notification):
    def send(self):
        return "SMS Notification"

notifications = [Notification(), EmailNotification(), SMSNotification()]

for notification in notifications:
    print(notification.send())
# Why this works. This works because notification is using whatever element, be that class object, and integer or a string to do what I say it to do, in this case,
# send the message. 


# Part B. Polymorphism with inheritance


class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "The document is " + self.title

class PDFDocument(Document):
    def describe(self):
        return "The PDF document is " + self.title

class TextDocument(Document):
    def describe(self):
        return "The Text document is " + self.title


documents = [PDFDocument("Aurora"), PDFDocument("Borealis"), TextDocument("Notepad"), TextDocument("++")]

for document in documents:
    print(document.describe())


# Part C. Duck typing



class Printer():
    def display_status(self):
        return "Printy Print"

class Screen():
    def display_status(self):
        return "Screeny Screen"

display_statuses = [Printer(), Printer(), Screen(), Screen()] # This is a bit odd, but it works. Would not get a +1 on a code review here though.

for ds in display_statuses:
    print(ds.display_status())
# This works simple since each class is its own entity with a function called display_status(). I simply create an object and then call that function
# that happens to have the same name, nothing more. Henec you see the printy print and screeny screen.


# Part D. isinstance()


class User:
    def who_am_i(self):
        return "User"

class AdminUser(User):
    def who_am_i(self):
        return "AdminUser"

auo = AdminUser()
print(f"Is auo an object is an AdminUser object? {isinstance(auo, AdminUser)}, a user object? {isinstance(auo, User)} and is it a string? {isinstance(auo, str)}")

# Admin user is considered an instance of user because of the IS-A relationship here, since AdminUser class inherits the User class, line 131.


