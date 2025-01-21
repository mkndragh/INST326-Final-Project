
# This file provides a function to generate a receipt for an order.
# 'generate_receipt' calculates the subtotal, tax, and tip, then saves the details to a file.
# Receipt includes itemized list of ordered items and the total cost.
def generate_receipt(order, file_name="receipt.txt"):
    subtotal = sum(item["price"] for item in order)
    tax = subtotal * 0.06
    tip = subtotal * 0.15 
    total = subtotal + tax + tip

    with open(file_name, 'w') as file:
        file.write("Receipt:\n")
        for item in order:
            file.write(f"{item['name']} - ${item['price']:.2f}\n")
        file.write(f"\nSubtotal: ${subtotal:.2f}\n")
        file.write(f"Tax (6%): ${tax:.2f}\n")
        file.write(f"Tip (15%): ${tip:.2f}\n")
        file.write(f"Total: ${total:.2f}\n")

    print(f"Receipt saved to {file_name}")
