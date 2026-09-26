correct_pin = "1234"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    pin = input("enter PIN-cod: ")
    
    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect PIN. Remaining attempts: {remaining}")
        else:
            print("Card blocked!")
        