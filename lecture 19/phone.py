class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

phone_book = {}
phone_book["John"] = "123-456-7890"
phone_book["Jane"] = "987-654-3210"
phone_book["Alice"] = "555-555-5555"

name = input("Enter a name to look up: ")
result = phone_book.get(name)
if result:
    print(f"{name}'s phone number is: {result}")
else:
    print(f"{name} is not in the phone book.")