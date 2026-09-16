def lesson():
    name = "Global ADA"

    def gr():
        global name
        name = "Local Grace"
        print(name)

    #list = [1,2,343,4]
    #new_list = list("Python")
    def show_nrs(*args):
        for arg in args:
            print(arg)
    show_nrs(10,20,40,55)


    def show_extra(n, *prices):
        print(n)
    show_extra(0.1, 100, 200, 300) # 100 - 300 go into prices
    # several positional values; all of the values not known;

    def add_three(a,b,c):
        return a + b + c

    numbers = [10,20,40]
    print(add_three(*numbers))


    def show_chars(**kwargs):
        print(kwargs)

    show_chars(name="Ada", age = 22, city = "Gbg")

# Part A

def part_a():
    course_name = "Python 2026"
    def show_course():
        course_name = "Machine Learning"
        print("Global variable overwritten:",course_name) # print locally overwritten variable. 
    show_course()
    #print("Global varible: ", course_name,) # scope ended, original name is printed.


    def counter():
        inside_counter = 0
        print(inside_counter)
    #print(inside_counter) # will give a complier error since we are calling a variable outside of its scope.

    def example():
        course_name = "Local Grace"
        print("\nBy printing the course_name variable: ",course_name,"you see that we are only printing local value, and doing nothing with the global")

    def example_2():
        global course_name
        course_name = "This value sticks"
        return course_name

    example()
    course_name = example_2()
    print("\nCalling example_2 method, you can see that whatever we do in the method, is there to say, ergo: ", course_name)


    def nested_func():
        name = "Global ADA"
        def reference_value_above():
            print(name)
        reference_value_above()
    nested_func()


    my_list = [1,2,3] # built in list command is avoided
    total_sum = sum(my_list)
    largest = max(my_list) # built in max is used
    text = str(my_list)
    print("\n\n", total_sum,",", largest, ",", text)

#part_a()

# Part B


def add_all(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(sum)
#add_all(1,2,3,4,5)


def average(*numbers):
    if(len(numbers) > 0):
        sum = 0
        for number in numbers:
            sum += number
        average = sum / (len(numbers))
        print("Average:", average)
    else:
        "No numbers supplied"
#average(1,2,3,4,5,6,7,8,9)


def longest_word(*words):
    longest = ""
    for word in words:
        if (len(word) > len(longest)):
            longest = word
    return longest
#print(longest_word("Abra", "AbraCadabra", "Alakazam", "OpenSesame"))

def build_sentence(separator, *words):
    sentence = ""
    for word in words:
        sentence += (separator+word)
    return sentence

#print(build_sentence("-","Abra", "AbraCadabra", "Alakazam", "OpenSesame"))


def describe_scores(student_name, *scores):
    avg = sum(scores) / len(scores)
    name = student_name
    number_of_scores = []
    for score in scores:
        number_of_scores.append(score)

    return {"Name":name, "Nr. of scores":number_of_scores, "Average":avg}
data = describe_scores("Lola", 1,5,9,77,66,55)

#print(data)


# Part C


def unpack_me(list):
    print(list[0] + list[1] + list[2])
unpack_me([10, 20, 30])


tuple_data = {"Max", "Olofsson", "Gbg"}
def call_me(*tuple):
    print(tuple)
#call_me(tuple_data)


# Not certain if this is what you wanted to be frank.
first, *middle, last = [1, (1,2,3,4,5), 6]
first, *middle, last = [1, (1,2,3,4,5,66,77,88,99), 6]
first, *middle, last = [1, (1111, 8888), 6]
#print("\nFirst:", first, "Last:", last, "Midddddle:", middle)

# Explanation:
# * in a functions definition means the argument that is pasted in is variable in length. It is positional.
# * in a function call, like take in a list that I have defined, then the call would be split my list into arguments.


# Part D

def show_profile(**kwargs):
    for x, y in kwargs.items():
        print("Name:", x, "Age:", y)


def create_user(username, **details):
    return {"Username" : username, "Details" : details}

my_user = create_user(username = "Lola",age = 22, city = "Gbg", occupation = "Coder" )
#print("\n\n",my_user)


def build_prodcut(name, price, **metadata):
    return {"Name:" : name, "Price:" : price, "Metadata:" : metadata}

build_prodcut = build_prodcut(name = "Cheap Asus", price = 9999, RAM = "16GB", harddisk = "1TB", graphic_card = "Radeon 880M")
#print("\n", build_prodcut)


def accept_settings(**settings):
    settings_list = []
    for setting, value in settings.items():
        if value != None:
            settings_list.append(setting)
    return settings_list

settings = accept_settings(privacy= "ON", spyware = "OFF", netflix= "UNNINSTALLED", quality=777, interest = None)
#print(settings)


data = {"name": "Lola", "age": 25, "height" : 1.70}
def matching_parameters(name, age, height):
    print("Name:", name, "Age:", age, "Height:", height)
#matching_parameters(**data)


# Part E

def log_event(event_type, *messages, **metadata):
    return {"event_type:" : event_type, "messages:" : messages, "metadata:" : metadata}
output = log_event("ERROR", "Disk full", "fix me", user="Lola", severity="catastrophical")
#print(output)


def calculate_order(customer, *prices, **options):
    shipping_fee = 150
    for key, value in options.items():
        if key == "discount" and value:
            shipping_fee *= 0.25
    #print("Customer:", customer, "Prices:", prices,"Shipping fee:", shipping_fee)

order = calculate_order("Max", 12, 35, 44, discount = True, shipping_method = "shipping_by_plane")


def clearer_parameters(name, surname):
    print("No need to overcomplicate things when we only need the name and surname:", name, surname)
#clearer_parameters("Max", "Awesome")


substantially_different = log_event("Malfunction", 
                                    "Electrical failure", "Unknown Reason", "Pay for Electricity",
                                    user = "Lola", severity = "catastrophical", countermeasure = "unkonwn")

substantially_different_2 = log_event("CPU Overclocking", 
                                    "Electrical drainage", "Cooling paste", "Extra venting", "Free cooling on balcony", "PC Hazard",
                                    user = "Edwin", surname = "Norton", reason = "Person bored", outcome = "who knows", cpu_type = "Ryzen 9 7850-3D")

substantially_different_3 = log_event("Groceries", 
                                    "Potato", "Tomato", "Buckwheat", "Lemon", "Blueberries", "Protein kurd", "Protein drink", "Barebells",
                                    user = "Arnold", surname = "Muscles", reason = "Lightweight", outcome = "Bulky Body", sideeffects = "N/A", benefits = "BigBoy")
#print(substantially_different_3)


# Part F

def create_report(title, *sections, **metadata):
    refined_sections = []
    if len(sections) > 1:
        for section in sections:
            for key, value in section.items():
                refined_sections.append(key + value)
    else:
        refined_sections.append(sections)

    refined_metadata = []
    for key, value in metadata.items():
        refined_metadata.append(key + value)
    return {"Title:" : title, "Sections:" : sections, "Metadata:" : metadata}


test_report = create_report("Horizon", 
                            {"Gengre" : "SciFi", "Year": 2002}, 
                            author = "David B.", department = "AstroPhysics", version = "1.0", confidential = "No")

print(test_report)


def summarize_report(report):
    for value in report.values():
        print(value)
#summarize_report(test_report)


big_dictionary = {"Gengre" : "SciFi", "Year": 2002, "Author" : "David B."}

def dictionary_unpacking(**reports):
    for report in reports:
        create_report(report)
        summarize_report(report)
#dictionary_unpacking(substantially_different, substantially_different_2)