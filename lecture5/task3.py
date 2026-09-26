text = input("Enter text: ")

result = ""
for char in text:
    if char.isdigit():
        continue
    result += char

print(result)