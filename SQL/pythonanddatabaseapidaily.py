import mysql.connector
import requests
import json
import psycopg2
# connection = mysql.connector.connect(
#     host="localhost",
#     user="jared",
#     passwd="1234",)

connection = mysql.connector.connect(
    host="localhost",
    user="jared",
    passwd="1234",
    database = 'countries'
)


mycursor = connection.cursor()
# mycursor.execute("CREATE DATABASE countries")
# connection.commit()

def create_table():
    mycursor.execute("CREATE TABLE Sep_countries(id SERIAL, name VARCHAR(50), capital VARCHAR(50), subregion VARCHAR(50), population int, PRIMARY KEY (id));")
    connection.commit()
    print("done")

response = requests.get("https://restcountries.com/v2/all")
# print(response.text)
data_country = response.json()
text1 = response.text
# for items in data_country:
#     print(items)

def insert_into_table():
    for k in data_country:
        insert1 = ("INSERT INTO Sep_countries(name,capital,subregion,population)VALUES(%s,%s,%s,%s)")
        name = k['name']
        try:
            capital = k['capital']
        except:
            capital = 'Null'
        subregion = k['subregion']
        population = k['population']
        mycursor.execute(insert1,(name,capital,subregion,population))
    connection.commit()
def see_table():
    query = "select*from Sep_countries"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
        print(i)

#
# insert_into_table()
see_table()

# def delete():
#     delete = "TRUNCATE TABLE Sep_countries"
#     mycursor.execute(delete)
#     print('Done')
#     connection.close()
# delete()

# mycursor.execute("ALTER TABLE Sep_countries MODIFY COLUMN name VARCHAR(500)")
# connection.commit()
# print("altered")