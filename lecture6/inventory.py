inventory = ["apple", "banana", "orange",
             "apple", "kiwi", "apple"]

new_items = ["mango", "grape"]

apple_count = inventory.count("apple")
print(f"'apple' count: {apple_count}")

orange_index = inventory.index("orange")
print(f"'orange' index: {orange_index}")

inventory.extend(new_items)
print(f"Updated inventory: {inventory}")

print(f"Reversed inventory: {inventory[::-1]}")