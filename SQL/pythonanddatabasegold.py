import mysql.connector
import base64
mydb = mysql.connector.connect(
    host="localhost",
    user="jared",
    passwd="1234",
    database='AuthenticationDatabase'
)

mycursor = mydb.cursor()

def create_database():
    mycursor.execute("CREATE DATABASE AuthenticationDatabase")
    mydb.commit()
    mydb.close()


def create_table():
    mycursor.execute("CREATE TABLE Users(id SERIAL, name VARCHAR(250),password VARCHAR(100), PRIMARY KEY(id));")
    mydb.commit()

dict1 = {
    'Joe': '123',
    'Bob' : '456',
    'Tim' : 'abc'
}

def insert_into():
    for k , v in dict1.items():
        insert1 = ("INSERT INTO Users(name,password)VALUES(%s,%s)")
        insert2 = (k,v)
        mycursor.execute(insert1,insert2)
    mydb.commit()

def read_from():
    view = "SELECT * from Users"
    mycursor.execute(view)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

list_of_logged_in = []

def login():
    while True:
        user_input = input("Menu: \n"
                           "(l) login\n"
                           "(x) Exit: \n")
        if user_input == 'l':
            username_input = input("Please enter username: ")
            if username_input in dict1:
                    password_input = input("Please enter password: ")
                    if password_input == dict1[username_input]:
                        print(f"Username :{username_input} has logged in")
                        list_of_logged_in.append(username_input)
                        continue
                    else:
                        print("Password is incorrect please try again")
            else:
                input1 = input("That username is not in the system, would you like to sign up? (y/n): ")
                if input1 == 'n':
                    print("Good Bye")
                    break
                elif input1 == 'y':
                    while True:
                        input2 = input("Please enter the username that you would like to use: ")
                        if input2 in dict1:
                            print("Please enter in another username that one is taken")
                            continue
                        else:
                            input3 = input("Please enter in a password: ")
                            password_encoded = input3.encode("utf-8")
                            encoded = base64.b64encode(password_encoded)
                            dict1[input2] = encoded
                            print(f"Your username {input2} has been added to the database with password {encoded}\n"
                                  f"Good Bye")
                            list_of_logged_in.append(input2)
                            break

        elif user_input == 'x':
            print("Good Bye")
            break
        else:
            print("Not a correct value, please enter again")
            continue

login()
insert_into()
read_from()

def delete():
    delete = "TRUNCATE TABLE Users"
    mycursor.execute(delete)
    print('Done')
    mydb.close()

delete()