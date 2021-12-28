def display_message():
    print("I am learning a lot in this python course")

display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title} I love to read it all the time")

favorite_book("Alice in Wonderland")


def describe_city(city,country):
    print(f"The city of {city} is located in the county, {country}")

describe_city("Tel-Aviv", "Israel")

from random import randint

def random_number(number):
    rand_number = randint(1,100)
    if rand_number == number:
        print(f"Sucess! Both number {number} and {rand_number} are equal")
    else:
        print(f"Both {number} and {rand_number} are not equal to eachother")

random_number(56)

def make_shirt(size = "Large", **text):
    if size == "Large" or size == "Medium":
        print(f"You have chosen a shirt size {size} which has the following text '{text.values()}'")
    else:
        print(f"You have chose a shirt with size {size} unfortantely we do not have that size in stock right now")
make_shirt("Large", text = "I love pythons")

magician_name = ["Frank", "Bob", "Joe", "Hue"]

def show_magicians():
    for name in magician_name:
        print(f"The magicians names are {name}")
make_great_list = []
def make_great():
    for name in magician_name:
        new_name = name + " The Great"
        make_great_list.append(new_name)
        make_great_list + magician_name
        print(make_great_list)

show_magicians()
# make_great()

def make_great_two():
    for index, magic in enumerate(magician_name):
        magician_name[index] += ' The Great'
    print(magician_name)

make_great_two()
show_magicians()