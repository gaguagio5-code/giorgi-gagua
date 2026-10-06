def sum_of_digits(n) -> int:
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(1234))  # Output: 10    
print(sum_of_digits(56789))  # Output: 35