from datetime import date, datetime
from random import randint
todays_date = date.today()


def get_age():
    my_date = input("Enter Birthday in YYYY/MM/DD format:")
    b_date = datetime.strptime(my_date, '%Y/%m/%d')
    age = (datetime.today() - b_date).days/365
    print(age)
    return age

def can_retire():
    gender = input("Please enter your gender M for male and F for female: ")
    if gender == "M":
        if get_age() >= 67:
                    print("The person is able to retire")
                    return True
        else:
            print("This person is not able to retire yet")
            return False
    elif gender == "F":
        if get_age() >= 62:
                print("The person is able to retire")
                return True
        else:
            print("This person is not able to retire yet")
            return False
    else:
        return False
can_retire()


2

def ex_8(x):
    x=int(x)
    value1 = x
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

random_number = randint(-10,40)



def get_random_temp(season):
    if season == 'winter':
        temperature = randint(-10, 16)
        print(f"The current temperature is {temperature}C and the season is {season}")
        return temperature
    elif season == 'spring':
        temperature = randint(16,25)
        print(f"The current temperature is {temperature}C and the season is {season}")
        return temperature
    elif season == 'summer':
        temperature = randint(25, 41)
        print(f"The current temperature is {temperature}C and the season is {season}")
        return temperature
    else:
        temperature = float(randint(12,30))
        print(f"The current temperature is {temperature}C and the season is {season}")
        return temperature




def main():
    season_choice = int(input("Please enter the current month by number: "))
    if season_choice == 1 or season_choice == 2 or season_choice == 12:
        season = "winter"
    elif season_choice == 3 or season_choice == 4 or season_choice == 5:
        season = "spring"
    elif season_choice == 6 or season_choice == 7 or season_choice == 8:
        season = "summer"
    else:
        season = "fall"
    temp = get_random_temp(season)
    if temp < 0:
            return print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 >= temp or temp <= 17:
            return print("Quite chilly! Don’t forget your coat")
    elif 17 >= temp or temp <= 24:
            return print("Its getting warmer up in here")
    elif 24 >= temp or temp <= 33:
            return print("Gotta wear some shorts today")
    elif 33 >= temp or temp <= 40:
            return print("Summer is here")
    else:
            return print("Too hot do not go out")


main()
