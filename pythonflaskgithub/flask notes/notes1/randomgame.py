import random
import sys
ran_num = random.randint(int(sys.argv[1]),int(sys.argv[2]))

while True:
    user_input = input("Please choose a number 1-10: ")
    if user_input == 'x':
        print("Good bye")
        break
    else:
        try:
            if 0 < int(user_input) < 11:
                if ran_num == int(user_input):
                    print('You win')
                    break
                else:
                    print("you lose")
        except ValueError:
            print("Please choose again")