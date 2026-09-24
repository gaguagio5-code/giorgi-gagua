correct_pin = 1234          # integer
balance = 500.00            # float
requested_amount = 150.00   # float

entered_pin = int(input("Enter your PIN:1234 "))

if entered_pin == correct_pin:
    # Second check: only reached if the PIN is correct
    if requested_amount <= balance:
        balance -= requested_amount
        print(f"Withdrawal successful! Remaining balance: ${balance:.2f}")
    else:
        print("Amount of your balance isn't enough.")
else:
    print("Incorrect PIN. Access Denied.")