import random


string = input("Please enter a string that is exactly 10 characters long: ")

if len(string) > 10:
    print("The string is too long")
elif len(string) < 10:
    print("The string is not long enough")
else:
    print("The string is the correct length")
    print("The first character of the string is", string[:1])
    print("The last character of the string is", string[-1:10])

print(string[0:1])
print(string[0:2])
print(string[0:3])
print(string[0:4])
print(string[0:5])
print(string[0:6])
print(string[0:7])
print(string[0:8])
print(string[0:9])
print(string[0:10])

string1 = list(string)
random.shuffle(string1)
print (''.join(string1))