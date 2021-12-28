birthdays = {
    "Paul": "1994/02/13",
    "George": "1993/01/12",
    "Ringo": "1992/05/16",
    "John": "1994/06/18",
    "Brian": "1993/01/22"
}

print("Hi new person, you can look up the birthdays of the people in the list!")
birthday_names = birthdays.keys()
birthday_dates = birthdays.values()
print(birthday_names)

question_name = str(input("Please enter a name that you would like to look up: "))
question_birthday = str(input("Please enter the persons birthday in the following format YYYY/MM/DD: "))

birthdays[question_name] = question_birthday
print(birthdays)

for k,v in birthdays.items():
    if question_name in birthday_names:
        print(f"The birthday of {question_name} is {v}")
        break
    else:
        print(f"The birthday of {question_name} is not in the list")

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
print("The items that we have are as follows:")
for item , amount in items.items():
    print(f"{item} which costs ${amount}")

items2 = {
    "grapes": 5,
    "pepper": 2,
    "lemon": 1.5,
    "grapefruit": 4
}

sum_of_items = sum(items2.values())
print("$",sum_of_items)

cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
list_of_cars = list(cars.split(" "))
print(list_of_cars)
number_of_companies = len(list_of_cars)
print(number_of_companies)
list_of_cars.sort()
list_of_cars.sort(reverse=True)
print(list_of_cars)

new_car_list =[]
for company in list_of_cars:
    if "o" in company:
        new_car_list.append(company)
print(f"There are {len(new_car_list)} companies that have the letter o in them")

new_car_list1 = []
for comp in list_of_cars:
    if "i" not in comp:
        new_car_list1.append(comp)
print(f"There are {len(new_car_list1)} companies that do not have the letter i in them")


cars2 = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars3 = set(cars2)
cars4 = list(cars3)
print(cars4)
cars4.sort()
print(f"This is a list of companies that are now selling cars here: {cars4[0]},{cars4[1]},{cars4[2]},{cars4[3]}, and {cars4[4]}, bringing the total to {len(cars4)} differnt companies")
