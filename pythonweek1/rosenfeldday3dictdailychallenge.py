welcomemsg = input("Hello and welcome to the Ceaser cypher program, would you like encrypt or decrypt?: ")

if welcomemsg == "encrypt":
    msg_to_encode = input("Please enter the text that you would like to encrypt: ")
    cypher_text = []

    for letter2 in msg_to_encode:
        if letter2 == ' ':
            cypher_text.append(letter2)
        else:
            cypher_text += chr(ord(letter2) + 3)

    cypher_text_string = ''.join(cypher_text)
    print(f"The text has been encdoed as {cypher_text_string} and is ready to be sent")
elif welcomemsg == "decrypt":
    msg_to_decode = input("Please enter the text that you would like to decode: ")
    decoded_text = []
    for letter3 in msg_to_decode:
        if letter3 == ' ':
            decoded_text.append(letter3)
        else:
            decoded_text += chr(ord(letter3) - 3)

    decoded_text_string = ''.join(decoded_text)
    print(f"The text has been decoded and states: {decoded_text_string}")


else:
    print("Goodbye")



number1 = int(input("Please enter the number you would like to check: "))
sum1 = 0

for n in range(1,number1):
        if number1 % n == 0:
            sum1 += n
if sum1 == number1:
    print(f"This number, {number1} is a perfect number")
else:
    print(f"This number, {number1}, is not a perfect number")

string2 = "You have entered a wrong domain"
words = string2.split()
words = list(reversed(words))
new_string = " ".join(words)
print(string2)
print(new_string)



