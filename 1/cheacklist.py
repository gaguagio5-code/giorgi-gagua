# 1. Names are stripped and capitalized
full_name = input("Enter your full name: giorgi gagua ")
cleaned_name = " ".join(full_name.split()).title()

# 2. replace(), find(), and slicing
workspace_msg = "Hello Alice, your workspace is Meta."
replaced_msg = workspace_msg.replace("Meta", cleaned_name)
index = workspace_msg.find("Alice")
sliced_part = workspace_msg[12:]

# 3. f-string matches the requested message
final_message = f"Hi {cleaned_name}! I found 'Alice' at index {index}, and here's the tail end: '{sliced_part}'"

# 4. Print everything so you can check terminal output
print("Cleaned name:", cleaned_name)
print("Replaced message:", replaced_msg)
print("Index of 'Alice':", index)
print("Sliced text:", sliced_part)
print("Final message:", final_message)