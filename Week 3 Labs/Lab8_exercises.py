# Part A Mutable default arguments

class BadTeam:
    def __init__(self, name, members = None):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

bad_team_one = BadTeam("bad_team_one")
bad_team_two = BadTeam("bad_team_two")
bad_team_two.add_member("Lola")
print("List One:", bad_team_one.members, "List Two:", bad_team_two.members)
bad_team_one.add_member("Zhora")
print("List One after ontrudction of None:", bad_team_one.members)

# This work in an odd way such that since the list is initilialised as empty, and how I see it it is part of the constructor,
# this list is reused. There may be cases where this is wanted but this is generally considered unsafe coding which can lead to many issues later on.
# AFTER the correct in point 3, when the list for each object call is set to None (empty), each bew call to the class whilst making an objects will have
# that particular list, not a shared one, that is bound to the object so to say, hence, we have Lola in bad team two but not one.


# Part B Dictionary or class?

movie = {"title" : "Memento", "director" : "Christopher Nolan", "rating" : 8.5}
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating
    def is_movie_highly_rated(self):
        return True if self.rating > 7 else False

movie_class_style = Movie("Memento", "Christopher Nolan", 8.5)
print("Is Movie highle rated?", movie_class_style.is_movie_highly_rated())

# It usually depends on the use case of course. classes are more versatile, you can add methods inside and do more operations, so it will be neat and tidy.
# Dictionary, singular use in this case, a one liner, is good if you want to conserve space in memory, for instance, if we need one variable, we would not
# need a class in this case. We can always access everyhting we need via "key" syntax, roughly. Personally, I would not define a class for a small data set.


# Part C Inheritance fundamentals

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

account_one = SavingsAccount("Lola", "5000", "0.03")
account_two = SavingsAccount("Ida", "25000", "0.09")

print(f"Account one owner: {account_one.owner}, account two balance: {account_two.balance}, account two interest rate: {account_two.interest_rate}")

# My understand is as follows. By invoking the SavingsAccount(Account) call, we are saying that hey python, my class, SA, is inheriting values defined in your 
# constructor which in this case are owner and balance. Hence, later on when we supply owner and balance, the line super().. says I am reusing what you have
# already instead of rewriting the same code twice. 


# Part D Inheritance fundamentals


class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return self.name

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)
    def set_age(self, age):
        self.age = age

class Person(Employee):
    def __init__(self, name):
        super().__init__(name)
    def set_gender(self, gender):
        self.gender = gender


developer_one = Developer("Max")
developer_two = Developer("Sam")
developer_one.set_age(35)
developer_two.set_age(36)

print(developer_one.get_information(), developer_two.get_information())

developer_one_gender = Person("Max")
developer_two_gender = Person("Sam")
developer_one_gender.set_gender("Male")
developer_two_gender.set_gender("Female")
print(developer_one_gender.get_information(), developer_one_gender.gender, "whilst", developer_two_gender.get_information(), developer_two_gender.gender)

employee_object = Employee("Bonita")
employee_object.get_information() # as we see here, its own method within its class is accessible
#employee_object.set_age(36) this will give us a compilation error, due to Employee class does NOT see members of Person or Developer class.


# Part E super() and shared initialization

class Device:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year if year > 0 else print("Year must not be a neagtive value")
        self.is_active = True

class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

class Owner(Device):
    def __init__(self, brand, year, owner):
        super().__init__(brand, year)
        self.owner = owner

laptop = Laptop("asus", 2000, 21)
owner = Owner("lenovo", 2010, "Max")
#print(owner.brand, owner.year, owner.owner)
#laptop_2 = Laptop("asus", -25, 21)
#print(laptop_2.brand, laptop_2.year, laptop_2.ram_gb) # this print out will give us none as the error msg id displayed and the negative variable is not assigned


# Part F Method Overriding

