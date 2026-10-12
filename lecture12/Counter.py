def make_counter()->callable[[], int]:
    start_value = 5 
    
    def counter() -> int:
        nonlocal start_value
        start_value +=1
        return start_value
    return counter

start_value: callable[[], int]=make_counter()

print(start_value())
print(start_value())
print(start_value())
print(start_value())
print(start_value())