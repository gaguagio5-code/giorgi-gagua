def even_nambers():
    num = 0
    while True:
        yield num
        num += 2

count = 0
for n in even_nambers():
    print(n)
    count += 1
    if count >= 10:        
        break