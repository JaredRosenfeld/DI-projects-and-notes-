import random

random_number_list = []

while True:
    random_number = random.randint(-100,100)
    random_number_list.append(random_number)
    random_number_list.sort()
    if len(random_number_list) >= random.randrange(1 , 10):
        break
print(random_number_list)

login_info={
    'John': "Imagine123",
    'Paul': 'Letitbe023',
    'George': 'Whilemyguitar3432'

}

logged_in_list = []
while True:
    decision_one = input("Please enter login or exit: ")
    if decision_one == 'exit':
        break
    else:
            decision_two = input("Please enter a username: ")
            if decision_two not in login_info.keys():
                decision_four = input("There is no username with that name would you like to sign up? Please enter yes or no: ")
                if decision_four == "yes":
                    decision_six = input("Please enter the new password that would like to add: ")
                    login_info[decision_two] = decision_six
                    logged_in_list.append(decision_two)
                    break
                else:
                    break
            else:
                decision_three = input("Please enter your password: ")
                if decision_three in login_info[decision_two]:
                    print("Your are logged in")
                    logged_in_list.append(decision_two)
                    break
                else:
                    print("Password is incorrect")
                    break
print(logged_in_list)
print(login_info)

