try:
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the quantity: "))
    total = price * quantity
except ValueError:
    print("Error: Price and quantity must be numbers.!")
else:
    print(f"Total payable: {total:.2f} Gel")