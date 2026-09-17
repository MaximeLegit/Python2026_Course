################################################## LECTURE ##################################################
"""
numbers = [1, 2, 3, 4, 5, 6]

doubled_numbers = [ number + 2 for number in numbers]

squares = [number ** 2 for number in numbers]

names = ["Lola", "Max", "Bonny"]
upper_names = [name.upper() for name in names]

result = [number ** 2 for number in numbers if number % 2 == 0]

# Dictionary comprehensions

new_nums = [1, 2, 3, 4, 5]
squares = {}
for n in new_nums:
    squares[n] = n **2

squares = {n : n**2 for n in new_nums}
#print(squares)

data = {"apple": 10, "chewy": 25, "banana" : 170}
double_prices = {product : price * 2 for product, price in data.items()}
#print(double_prices)

# Sets comprehensions

words = ["Python", "Java", "C#", "C++"]
lengths = {len(word) for word in words}

# Tuple comprehensions

xyz = ( x * 2 for x in range(1,5))
#print(xyz)
# Meaning, it does not work, it creates generator expressions, no a readble format really.

#for index, language in enumerate(words):
#    print(index,language)

#for word, num in zip(words, new_nums):
#    print("\n",word, num)

pairs = list(zip(words, new_nums))

first, *rest = new_nums

person = ("Ada", 36, "London")
name, _, city = person
#print("\n",name, city)

first_list = [1, 2, 3]
scnd_list = [4, 5, 6]
combined = [*first_list, *scnd_list]

dict_1 = {"theme" : "dark", "language" :  "english"}
dict_2 = {"discount" : "NO", "language" :  "swe"}
combined_dict = {**dict_1, **dict_2}
#print("\n", combined_dict)

# LAMBDA Functions

def double(num):
    return num * 2
# method above == method below
double = lambda num: num * 2
#print(double(25))

sorted_langs = sorted(words, key = lambda name : len(name))
#print("\nSorted language list", sorted_langs)

data_set_2 = [{"score": 10, "Name" :"Lola" } , {"score": 25, "Name" :"Hora"}, {"score" : 170, "Name" :"Nova"}, {"score" : 5, "Name" :"Sora"}]

sorted_data_set_2 = sorted(data_set_2, key = lambda dt2: dt2["score"])
#print("\nSorted Data Set 2", sorted_data_set_2)

even_nums = list(filter(lambda number: number % 2 == 0, combined))
#print("\n", even_nums)
"""
################################################## LECTURE ##################################################

# Part A

# A.1
numbers = range(1,20)
squares = {}
for number in numbers:
    squares[number] = number ** 2
#print("Loop Style: ", squares)

squares = [number ** 2 for number in numbers]
#print("List comprehension Style: ", squares)

# A.2
result = [number for number in range(1, 100) if number % 2 == 0]
#print(result)


# A.3
student_names = ["Lola", "max", "bonny"]
#print([name.strip().title() for name in names])


# A.4
scores = [33, 44, 55, 66, 77, 88]
#print("Passing scores: ", [score for score in scores if score > 50])

#A.5

#print("Labels: ", [{score : "PASS"} if score > 50 else {score : "FAIL"} for score in scores])

# A.6
# E.1 rewritten

#print([(number-1) for number in (range(1,11)[::-1])])

# F.1 rewritten

x = [number for number in range(1, 100) if number % 7 == 0 and number % 9 == 0]
#print(x)
#print(x[0]) though this is odd but since I know it has only 1 element, it will remove the list brackets.

# F.2 rewritten

list_of_strings = ["banana", "apple", "", "kiwi", "", "icecream", "fudge", "orange"]
#print([{"You can eat" : string} if string != "" else "Not edible" for string in list_of_strings])


# Part B

# B.1
#print([(number, number ** 2) for number in range(1,10)])

# B.2
#print([(word, len(word)) for word in list_of_strings ])

# B.3
list_of_capital_words = ["MARS", "MOON", "SUN", "VENUS", "MARS"]
normalised_words = set((word.lower() for word in list_of_capital_words))
#print(normalised_words)

# B.4
products = {"apple": 10, "chewing gum": 25, "banana" : 170}
cheap_products = {product : price for product, price in products.items() if price < 50}
#print(cheap_products)

# B.5
#print({student : ("PASS" if student == "Lola" or student == "max" else "FAIL") for student in student_names} )


# Part C enumerate

# C.1
songs = ["I want it that way", "Moonlight", "Dark Sonatra", "Adajio"]
#for index, value in enumerate(songs, 1):
    #print(index, value)


# C.2
list_of_tasks = ["clean", "study", "work", "cook", "relax"]
indexed_list = []
for index, value in enumerate(list_of_tasks):
    indexed_list.append(["Task" + str(index) + ":" + value])
    #print("Task" + str(index) + ":",value)
#print(*list_of_tasks) # not certain but perhaps you guys wanted this option, or just a plain old new line print per task in the given list.
#print(*indexed_list)


# C.3
#print([{"Index:" : index, "Value:" : value} for index, value in enumerate(scores) if value > 50])


# C.4
#for index, value in enumerate(scores):
    #print(f"Index: {index}, Value: {value}")
    #print("")
    # This version is cleaner simply because we do not need to call extra two funcitonal calls when the values we need are
    # included as part of the index key value; All we do is just call them.


# Part D Zip and Unpacking

# D.1
#print(list(zip(list_of_tasks, scores)))

# D.2
#print(dict(zip(list_of_tasks, scores)))
#first, *rest = new_nums

# D.3
first_digits = [1, 2, 3]
scnd_digits = [4, 5, 6]
third_digits = [7, 8, 9]
combined = [*first_digits, *scnd_digits, *third_digits]
#print(combined)

# D.4 
merged_data = list(zip(songs, first_digits))
#print(merged_data)
# I tried this out during lecture, but simply put, the element that is outstanding is omitted

# D.5
#print("Tuple unpacking: ",[(index, song) for index, song in merged_data])

# D.6
a = 99
b = 19
#print("original values. a=", a, "b=",b)
a, b = b, a
#print("Did it work? a=", a, "b=",b, "Yes, beautiful.")


# Part E sorted lambda

# E.1
print("Sorting variable list_of_tasks by length:", sorted(list_of_tasks, key = lambda name : len(name)))

# E.2

data_set = [{"score": 10, "Name" :"Lola" } , 
              {"score": 25, "Name" :"Hora"}, 
              {"score" : 170, "Name" :"Nova"}, 
              {"score" : 5, "Name" :"Sora"}]

# where key is getDataSetValue where key is what i look for and sort based on what I return, value of ...
sorted_data_set = sorted(data_set, key = lambda data_set_value: data_set_value["score"])
print("Sorted ascending:", sorted_data_set)

sorted_data_set = sorted(data_set, key = lambda data_set_value: data_set_value["score"], reverse=True)
print("Sorted descending:", sorted_data_set)
print("\n\n")

# E.3
updated_products = {"apple": 10, "chewing gum": 25, "banana" : 170, "potato" : 8, "gurka" : 19}
print("Sort products by price using lambda: ", sorted(updated_products, key = lambda product : updated_products[product]))

# E.4
unsorted_list = [{"first_name": "Arnold", "last_name": "Muscles"}, 
                 {"first_name": "Ronnie", "last_name": "Calman"},
                 {"first_name": "Sophie", "last_name": "Turner"}]


# F.2
#Use .strip().title() to normalize the names and categories. That's all.