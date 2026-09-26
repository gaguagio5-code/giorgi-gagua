n = int(input("enter an integer n: "))

total = 0
for num in range(2, n + 1, 2):
    total += num

print(f"The sum of even numbers from 1 to {n} is: {total}")