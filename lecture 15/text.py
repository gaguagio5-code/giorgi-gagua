file = open("test.txt", "r")
data = str(file.read())
def add_quote():
    author = input("Enter your favorite writer: ").strip()
    quote = input("Enter a quote: ").strip()

    with open("test.txt", "a", encoding="utf-8") as file:
        file.write(f"{author}: {quote}\n")
print("Enter your favorite writer:")
print("Enter a quote:")
