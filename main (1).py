
# Main file for the project to execute the program.
# Loads the menu, allows the user to take an order, and generates a receipt.
# Uses functions from 'menu.py', 'order.py', and 'receipt.py'.
from menu import load_menu
from order import take_order
from receipt import generate_receipt

if __name__ == "__main__":
    menu = load_menu("menu.json")
    order = take_order(menu)
    generate_receipt(order)
