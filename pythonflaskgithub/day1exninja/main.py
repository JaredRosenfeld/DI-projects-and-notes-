import random
import string
pwd = []
spec_characters1 ="!@#$%^&*()"

def user_check():
    user_input = input("Please enter the length that you want your password to be must be between 6-30 characters: ")
    if 6 <= int(user_input) <= 30:
        possible_pwd = ([random.choice(spec_characters1),random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.digits)]
                        + [random.choice(string.ascii_lowercase
                              + string.ascii_uppercase
                              + spec_characters1
                              + string.digits) for i in range(int(user_input))])
        random.shuffle(possible_pwd)
        pwd = ''.join(possible_pwd)
    else:
        print('not okay')

    print(pwd)

def password_gen():
    for i in range(6,30):
        possible_pwd = ([random.choice(spec_characters1), random.choice(string.ascii_lowercase),
                         random.choice(string.ascii_uppercase), random.choice(string.digits)]
                        + [random.choice(string.ascii_lowercase
                                         + string.ascii_uppercase
                                         + spec_characters1
                                         + string.digits) for i in range(i)])
        random.shuffle(possible_pwd)
        pwd = ''.join(possible_pwd)
    print(pwd)

count = 0
while count <= 100:
    password_gen()
    count += 1