################################################## LECTURE ##################################################

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
student_1 = Student("Lola", 99)
#print(student_1.name)



################################################## LECTURE ##################################################

# Part A Classes and objects

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def is_long(self):
        return True if self.pages > 300 else False

first_book = Book("Stranger in a strange land", "Robert A. Heinlein", 486)
second_book = Book("The caves of Steel", "Isaac Asimov", 244)
third_book = Book("Gateway", "Fredrik Pohl", 386)
fourth_book = Book("Red Rising", "Pierce Brown", 444)
fifth_book = Book("Golden Son", "Pierce Brown", 386)

#print("Sample print of first book, the title:",first_book.title, "Author:", first_book.author, "Total pages:", first_book.pages)
#print("Sample print of first book, the title:",fifth_book.title, "Author:", fifth_book.author, "Total pages:", fifth_book.pages)


class Laptop:
    def __init__(self, brand, model, ram_gb = 64, price = 30000):
            self.brand = brand
            self.model = model
            self.ram_gb = ram_gb
            self.price = price

asus = Laptop("Asus", "Vivobook", 32, 10000)
asus_2 = Laptop("Asus", "Zenbook", 32, 12000)
msi = Laptop("MSI", "Stealth", 32, 15000)
#print("Current asus price=",asus.price)

asus.price = 20000
#print("Now it is",asus.price)


msi_2 = Laptop("MSI", "Stealth", 32, 15000) # same as msi
#print("Are they the same object?", msi is msi_2)


lenovo = Laptop("Lenovo", "Ideapad")
#print("Values for lenovo with default parameters: ", lenovo.brand, lenovo.model, lenovo.ram_gb, lenovo.price)

acer = Laptop(brand="acer", model="predator", ram_gb=24, price=17999)
#print("Acer values:", acer.brand, acer.model, acer.ram_gb, acer.price)


# Part B Methods and state

#print("Is the first book long?", first_book.is_long(), "Correct, since it's page count is", first_book.pages)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, sum_to_remove):
        if self.balance >= sum_to_remove:
            self.balance -= sum_to_remove
            print(f"{self.balance} if left on your bank account")
        else:
            raise ValueError(f"Not enough money in the account to withdraw {sum_to_remove}")

my_bank_account = BankAccount("Max", 100)
my_bank_account.deposit(100)
#print("Current sum:", my_bank_account.balance)

my_bank_account.withdraw(150)
#print("Updated sum:", my_bank_account.balance)

#my_bank_account.withdraw(150)
#print("Should be value error if I were to remove comment on line above..")


class Task:
    def __init__(self, title, completed = False):
        self.title = title
        self.completed = completed  

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

first_task = Task("Push Ups")
#print("State of the object first task is: ", first_task.title, first_task.completed)


second_task = Task("Pull Ups")
second_task.complete()
#print("Push Ups should not be false? ", first_task.completed, "Whilst pull ups are complete, right?", second_task.completed)

second_task.reopen()
#print("On second thought, let me double check something..and, are pull ups actually done?", second_task.completed, 
#      "Thereby demonstrating that changing state of the second task has absolutely no effect on the first_task")