from time import time

1
my_fav_numbers = {1,3,6,17}

my_fav_numbers.add(5)
my_fav_numbers.add(11)
my_fav_numbers.remove(17)

print(my_fav_numbers)

friend_fav_numbers = {4,10,20,55}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

2
print("no")
3
num = list(range(0,21))
for n in num:
    print(num)
    break

4

#The difference between an integer and a float is that an integer is a whole number while a float has decime place

list1 =  [1.5, 2, 2.5, 3, 3.5,4]
list_floats = []
for num in list1:
    list_floats.append((float(num)))
    print(list_floats)

5

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
num_of_apples = int(basket.count("Apples"))
print(num_of_apples)
print(basket)
basket.clear()
print(basket)

6


"""while True:
    name = input("Please enter your name: ")
    if name == "Jared":
        print(f"Yes that is my name, {name}")
        break
    else:
        print(f"No that is not my name, {name}, please try again")"""

7

list1 = [0,2,4,5,66,43,21,10101]

for number in list1:
    if number %2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

8.

range1 = range(1500,2500)

for number in range1:
    if number % 5 == 0 and number % 7 == 0:
        print(number)
        continue
    else:
        continue

9

fruits1 = input("Please enter your favorite fruits (please enter fruits with a single space): ")
fruit_list = list(fruits1.split(" "))

for fruit in fruit_list:
    choice = input("Please enter a favorite fruit to chose from: ")
    if choice in fruit_list:
        print("You chose one of your favorite fruits Enjoy!")
        break
    else:
        print("Your choice is not on the list, choose again")

10

pizza_toppings = []

while True:
    pizza = input("Please enter the topping that you want: ")
    if pizza == "quit":
        break
    else:
        pizza_toppings.append(pizza)
        print(f"We have added {pizza} to your pizza")

price = len(pizza_toppings)
final_price1 = price * 2.5 + 10
clean = ''
for z in pizza_toppings:
    clean += ' '+ z + ','
    continue
print(f"We have added the following pizza topping(s) to your pizza:{clean} with your final price being ${final_price1}")

11
ticket_prices = []
family_size = int(input("How many people are you: "))


while True:
    if len(ticket_prices) == family_size:
        break
    else:
        age = int(input("Please enter the movie-goers age: "))
        if age <= 3:
            ticket_prices.append(0)
        elif 4 <= age <=12:
            ticket_prices.append(10)
        else:
            if 16 <= age <=21:
                ticket_prices.append(0)
                print(f"You are not allowed to watch this moive because you are {age} years old")
            else:
                ticket_prices.append(15)

final_ticket_prices = sum(ticket_prices)
print(f"The final prices for the tickets is ${final_ticket_prices}")

12
list_of_names = ["Paul", "George", "John", "Ringo"]

for names in list_of_names[::]:
    ages_of_names = int(input(f"Please enter {names}\'s age: "))
    if ages_of_names <= 16:
        list_of_names.remove(names)
        continue
        print(list_of_names)
    else:
        continue
print(list_of_names)

13

sandwhich_orders = ["tuna", "cheese", "meat", "pastrami" , "pizza"]
finished_sandwhich = []

for sandwhich in sandwhich_orders:
     finished_sandwhich.append(sandwhich)
     print(f"I have finish making your {sandwhich}, please pick it up at the counter")

14


while True:
    for sandwhich in sandwhich_orders:
        if sandwhich == "pastrami":
            sandwhich_orders.remove(sandwhich)
        else:
            finished_sandwhich.append(sandwhich)
    break

print(f"I have finished the following sandwhiches for you {finished_sandwhich} please pick it up at the counter")



