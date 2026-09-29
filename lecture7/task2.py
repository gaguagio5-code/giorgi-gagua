try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise ValueError("You must be at least 18 years old to register!")
    print("Registration successful!")
except ValueError as e:
    print(e)
finally:
    print("The registration process has concluded.")