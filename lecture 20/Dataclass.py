from dataclasses import dataclass

@dataclass
class product:
    name: str
    price: float
    in_stock: int

product1 = product("Laptop", 999.99, 10)
product2 = product("Smartphone", 499.99, 25)
product3 = product("Headphones", 199.99, 50)

print(product1)
print(product2)
print(product3)
