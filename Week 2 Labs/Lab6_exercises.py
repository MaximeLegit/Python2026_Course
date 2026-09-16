################################################## LECTURE ##################################################

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
print(double(25))

sorted_langs = sorted(words, key = lambda name : len(name))
print("\nSorted language list", sorted_langs)

data_set_2 = [{"score": 10, "Name" :"Lola" } , {"score": 25, "Name" :"Hora"}, {"score" : 170, "Name" :"Nova"}, {"score" : 5, "Name" :"Sora"}]

sorted_data_set_2 = sorted(data_set_2, key = lambda dt2: dt2["score"])
print("\nSorted Data Set 2", sorted_data_set_2)

even_nums = list(filter(lambda number: number % 2 == 0, combined))
print("\n", even_nums)

################################################## LECTURE ##################################################