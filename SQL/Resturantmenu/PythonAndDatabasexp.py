import mysql.connector
import psycopg2
connection = mysql.connector.connect(
    host="localhost",
    user="jared",
    passwd="1234",
    database = 'RestaurantMenuManager'
)

cursor = connection.cursor()
# mycursor.execute("CREATE DATABASE RestaurantMenuManager")
# mydb.commit()


# mycursor.execute("CREATE TABLE MenuItem (id SERIAL, name VARCHAR(250),price int, PRIMARY KEY(id));")
# mydb.commit()
# class MenuItem:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         MenuItem.list_of_all = []
#     def save(self):
#         mycursor = mydb.cursor()
#         insertion = "INSERT INTO MenuItem(name,price)VALUES (%s,%s)"
#         mycursor.execute(insertion,(self.name,self.price))
#         mydb.commit()
#         print(mycursor.rowcount, "record inserted.")
#     def delete(self):
#         mycursor = mydb.cursor()
#         delete_sql = (f"DELETE FROM MenuItem WHERE name LIKE '%{self.name}%'")
#         mycursor.execute(delete_sql)
#         mydb.commit()
#     def update(self,item,price):
#         mycursor = mydb.cursor()
#         update_query = (f"UPDATE MenuItem SET price = {price} WHERE name LIKE '%{item}%'")
#         mycursor.execute(update_query)
#         mydb.commit()
#         count = mycursor.rowcount
#         print(count, "Record Updated successfully ")
#     def all():
#         mycursor = mydb.cursor()
#         query = ("SELECT * from MenuItem")
#         mycursor.execute(query)
#         results = mycursor.fetchall()
#         mydb.commit()
#         mydb.close()
#         for items in results:
#             MenuItem.list_of_all.append(items)
#         print(MenuItem.list_of_all)
#         return MenuItem.list_of_all
#     def get_by_name(item_name):
#         print(MenuItem.list_of_all)
#         for items in MenuItem.list_of_all:
#             if items[1] == item_name:
#                 print(items)
#                 return items
#             else:
#                 print("No items by that name here")
#                 return None
#
# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# # item2 = MenuItem.get_by_name('Beef Stew')
# items = MenuItem.all()

class MenuItem:
    def __init__(self):
        pass

    def save(self, name1, price1):
        query = f"INSERT INTO MenuItem (name,price) values ('{name1}',{price1});"
        cursor.execute(query)
        connection.commit()
        print("item added succesfully ")

    def delete(self, name):
        query = f"delete from MenuItem where name='{name}';"
        cursor.execute(query)
        connection.commit()
        print("item deleted succesfully ")

    def update(self, name, price):
        query = f"update MenuItem set price={price} where name='{name}';"
        cursor.execute(query)
        connection.commit()
        print("item updated succesfully ")

    def all(self):
        print("full data is: ")
        query = f"select*from MenuItem"
        cursor.execute(query)
        result= cursor.fetchall()
        for i in result:
            print(i)

    def get_by_name(self, name):
        query = f"select*from menuitem where name='{name}';"
        cursor.execute(query)
        connection.commit()
        result = self.run_query(query)
        for i in result:
            print(i)