
# This file handles loading the menu from a JSON file and displaying it to the user.
# 'load_menu' function reads the menu data from a given JSON file.
# 'display_menu' function prints the menu in a formatted manner for the user.
import json

def load_menu(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["menu"]

def display_menu(menu):
    print("Menu:")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item['name']} - ${item['price']:.2f}")
