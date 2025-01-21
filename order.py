
# This file defines classes and functions for managing menu items and taking customer orders.
# Abstract base class 'MenuItem' provides a template for menu items.
# 'FoodItem' is a concrete implementation of 'MenuItem', representing food items with a name and price.
# 'take_order' function handles user input for placing orders based on the displayed menu.
from menu import display_menu

from abc import ABC, abstractmethod

class MenuItem(ABC):
    @abstractmethod
    def get_price(self):
        pass

class FoodItem(MenuItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

def take_order(menu):
    order = []
    while True:
        display_menu(menu)
        choice = input("Enter the number of the item you'd like to order (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(menu):
                order.append(menu[index])
                print(f"Added {menu[index]['name']} to your order.")
            else:
                print("Invalid choice. Please select a valid menu item.")
        except ValueError:
            print("Please enter a valid number.")
    return order
