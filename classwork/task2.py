try:
    password = input("enter password: ")
    if len(password) < 6:
        raise ValueError("The password is too short!")
    print("The password is acceptable!")
except ValueError as e:
    print(e)