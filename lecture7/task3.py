fruits = ["apple", "banana", "cherry", "orange"]

try:
    index = int(input("Enter the index number: "))
    print(f"Selected fruit: {fruits[index]}")
except ValueError:
    print("Invalid format! Please enter an integer..")
except IndexError:
    print(f"Index is out of range! Select from 0. {len(fruits) - 3}-until")
else:
    print("The item was successfully found!")