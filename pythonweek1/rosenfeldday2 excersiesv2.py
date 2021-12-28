list1 = ["duck", "rabbit", "hare", "bear"]
list2 = ["plane", "helicopter", "jet", "car",]
list1.append(list2)
print(list1)

2
number1 = int(input("Please enter in the first number: "))
number2 = int(input("Please enter in the second number: "))
number3 = int(input("Please enter in the third number: "))
if (number1 >= number2) and (number1 >=number3):
         print(f"The largest number is:{number1}")
elif (number2 >= number1) and (number2 >= number3):
         print(f"The largest number is:{number2}")
elif (number3 >= number1) and (number3 >= number2):
         print(f"The largest number is:{number3}")

3
import string
alphabet = list(string.ascii_lowercase)
for letter in alphabet:
    vowels = ["a", "e", "i", "o", "u"]
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_names = input("Please enter in a name: ")

if user_names in names:
    print(names.index(user_names))

5

user_words1= input("Please enter in seven words:")
words = user_words1.split(" ")
for word in user_words1:
     user_input1 = str(input("Please enter a leter to see if it is the words: "))
     if user_input1 in user_words1:
        print (user_words1.index(user_input1))
        break
     else:
            print(f"The letter that you chose {user_input1} is not in one of the words")
            break

6

numbers1 = list(range(0,1000001))
print(max(numbers1))
print(min(numbers1))
print(sum(numbers1))

7
number_list = []
num = int(input("Please the number of numbers in the list: "))
for n in range(0,num):
    t = int(input("Please enter 5 numbers: "))
    number_list.append(t)
    print(number_list)
    print(tuple(number_list))

8
import random
score_won = 0
score_lost = 0
while True:
    user_input11 = int(input("Please enter in a number from 1 to 9: "))
    random_number = random.randint(1, 9)
    if user_input11 == random_number:
        score_won += 1
        print(f"Congratulations your number {user_input11} is equal to the random number {random_number}, you win!!!")
    elif user_input11 == 00:
        print(f"Game over, your final score is {score_won} wins and {score_lost} losses")
        break
    else:
        score_lost += 1
        print(f"The number you chose {user_input11} is not equal to the random number {random_number} you lose.")



