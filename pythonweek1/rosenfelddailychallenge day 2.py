from  datetime import date
count = 0
for i, char in enumerate(list(range(100))):
    count += 1
    while count == 51:
        print(i, char)
        break


my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for number in my_list:
    sum += number

print(sum)



birthday = input("Please enter your birthday with the following format DD/MM/YYYY: ")

day_of_bith = birthday[0:2]
month_of_birth = birthday[3:5]
year_of_birth = birthday[-4:]
birthday_final = date(year = int(year_of_birth), month = int(month_of_birth), day = int(day_of_bith))
today = date.today()
age = round((today-birthday_final).days/365.25)

number_of_candels = age % 10
candels = "i" * number_of_candels

print(f"Congratulations you are {age} years old")
print(f"      ___{candels}___")
print("     |:H:a:p:p:y:|")
print("   __|___________|__")
print("  |^^^^^^^^^^^^^^^^^|")
print("  |:B:i:r:t:h:d:a:y:|")
print("  |                 |")
print("  ~~~~~~~~~~~~~~~~~~~")

