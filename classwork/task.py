try:
    birth_year = int(input("Enter your year of birth.: "))
    age = 2026 - birth_year
    print(f"It's your age.: {age}")
except ValueError:
    print("13.10")