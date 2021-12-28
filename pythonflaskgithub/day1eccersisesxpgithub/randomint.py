import random

def random_number(ints):
    ran_num = random.randint(1,100)
    if 0 < int(ints) < 101:
        if ran_num == int(ints):
            print('You win')
        else:
            print("you lose")
    else:
        print("Not a valid entry")
