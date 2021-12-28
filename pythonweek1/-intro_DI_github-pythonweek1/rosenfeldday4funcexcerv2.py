# from datetime import date, datetime
#
# todays_date = date.today()
#
#
# def get_age():
#     my_date = input("Enter Birthday in YYYY/MM/DD format:")
#     b_date = datetime.strptime(my_date, '%Y/%m/%d')
#     age = (datetime.today() - b_date).days/365
#     print(age)
#     return age
#
# def can_retire():
#     gender = input("Please enter your gender M for male and F for female: ")
#     if gender == "M":
#         if get_age() >= 67:
#                     print("The person is able to retire")
#                     return True
#         else:
#             print("This person is not able to retire yet")
#             return False
#     elif gender == "F":
#         if get_age() >= 62:
#                 print("The person is able to retire")
#                 return True
#         else:
#             print("This person is not able to retire yet")
#             return False
#     else:
#         return False
# can_retire()


2

def ex_8(x):
    x=int(x)
    value1 = x
    print(value1)
    value2 = f"{x}{x}"
    value3 = f"{x}{x}{x}"
    value4 = f"{x}{x}{x}{x}"
    value5 = f"{value1} + {value2} + {value3} + {value4}"
    value1 =int(value1)
    value2 = int(value2)
    value3 = int(value3)
    value4 = int(value4)
    print(value5)
    final_value = value1 + value2 + value3 +value4
    print(final_value)
    return final_value
ex_8(3)
