age = int(input("Please enter your age: "))

if age < 0:
    print("Invalid age entered.")
elif age < 5:
    print("Your ticket price is $0. Enjoy the movie!")
elif age <= 12:
    print("Your ticket price is $8. Enjoy the movie!")
elif age <= 64:
    print("Your ticket price is $15. Enjoy the movie!")
else:
    print("Your ticket price is $10. Enjoy the movie!")
    