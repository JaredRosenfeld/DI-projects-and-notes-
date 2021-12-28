import PythonAndDatabasexp
from PythonAndDatabasexp import MenuItem
# def load_manager():
#

# def show_user_menu():
#     print("       Menu\n"
#           "(a) Add an item\n"
#           "(b) Delete an item\n"
#           "(v) View the item\n"
#           "(x) Exit")
#     while True:
#         user_input = input("Please enter your choice:")
#         if user_input == 'a':
#             add_item_to_menu()
#         elif user_input == 'b':
#             delete_item_from_menu()
#         elif user_input == 'v':
#             show_resturant_menu()
# def add_item_to_menu():
#     food_input = input("Please enter the name of the food that you would like to add: ")
#     price_input = int(input("Please enter the price of the food you would like to add: "))
#     item = pyd.MenuItem(food_input,price_input)
#     item.save()
#     print("Item was saved sucessfully")
#
# def delete_item_from_menu():
#     delete_input = input("Please enter the name of the food you would like to delete from the menu: ")
#     item = pyd.MenuItem
#     item.delete(delete_input)
# def show_resturant_menu():
#     item = pyd.MenuItem
#     item.all()
#
#
# show_user_menu()


def show_user_menu():
    print("      Menu\n"
          "(a) Add an item\n"
          "(d) Delete an item\n"
          "(v) View the item\n"
          "(x) Exit")
    while True:
        user_input = input("Please enter your choice:")
        if user_input == "a":
            add_item_to_menu()
        elif user_input == "d":
            remove_item_from_menu()
        elif user_input == "v":
            show_all()
        elif user_input == "x":
            exit()
        else:
            print("wrong input")
            return show_user_menu()


def add_item_to_menu():
    item_name = input("Enter name of item to input: ")
    item_price = int(input("Enter name of item to input: "))
    item.save(item_name, item_price)
    show_user_menu()


def remove_item_from_menu():
    item_name = input("Enter name of item to delete: ")
    item.delete(item_name)
    show_user_menu()

def show_all():
    item.all()
    show_user_menu()

item = MenuItem()
show_user_menu()