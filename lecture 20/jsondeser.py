import json
class product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

json_string = '{"name": "Laptop", "price": 2500, "in_stock": true}'
data = json.loads(json_string)

p = product(**data)

print(type(p))
print(p.name)
print(p.price)
print(p.in_stock)