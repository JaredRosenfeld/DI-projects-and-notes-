1


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = dict(zip(keys,values))
print(dict1)


2

family2 = {}

while True:
    user_age = int(input("Please enter users age: "))
    user_name = input("Please enter user name: ")
    family2[user_name] = user_age
    if user_age == 00 or user_name == "done":
        break
    else:
        family2[user_name] = user_age

print(family2)
ticket_prices = []
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for name, age in family2.items():
        if age <= 3:
            ticket_prices.append(0)
        elif 4 <= age <=12:
            ticket_prices.append(10)
        else:
            ticket_prices.append(15)
print(ticket_prices)

final_ticket_prices = sum(ticket_prices)
print(f"The final prices for the tickets is ${final_ticket_prices}")

brand ={
    "name": "Zara" ,
    "creation_date": 1975,
    "creator_name": ["Amancio", "Ortega" , "Gaona"],
    "type_of_clothes": ["men", "women", "children", "home" ""],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color":{
         "France":"blue",
        "Spain": "red",
        "US": ["pink", "green"]}
}

print(brand)

brand["number_stores"] = 2
print(brand["number_stores"])


print(f"Some of {brand['name']}'s biggest clients include {brand['type_of_clothes']}, it was founded in the year {brand['creation_date']}")

brand["Country_creation"] = "Spain"

if 'international_competitors' in brand.keys():
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]
print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

for k,v in brand.items():
    print(k)

brand2 = {
    "creation_date": 1975,
    'number_of_stores': 10000
}

brand.update(brand2)
print(brand)

print(brand["number_stores"])
# it printed the orginal number of stores that I had updated

4

"Part1"
users1 = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]


char_dict = dict(enumerate(users1))

new_char_dict = {}

for key, value in char_dict.items():
    new_char_dict[value] = key
print(new_char_dict)

"Part2"

print(char_dict)


"Part 3"
sortednames= sorted(new_char_dict.keys())
print(sortednames)

new_sorted_names = dict(enumerate(sortednames))
sorted_names2 = {}
for keys, values in new_sorted_names.items():
    sorted_names2[values] = keys
print(sorted_names2)

"Part4"
users2 = ["Mickey", "Minnie","Donald","Ariel","Pluto"]
sorted_list1 = {}
for s in users2:
    if 'i' not in s:
        users2.remove(s)
        char_dict2 = dict(enumerate(users2))
        sorted_list1 = {vv:kk for kk, vv in char_dict2.items()}

print(sorted_list1)


users3 = []
sorted_list2 = {}
for t in users2:
    if t.startswith("M") or t.startswith("P"):
        users3.append(t)
        char_dict3 = dict(enumerate(users3))
        sorted_list2 = {vvv: kkk for kkk, vvv in char_dict3.items()}
print(sorted_list2)

