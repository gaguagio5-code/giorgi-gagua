class product:
    shop_name = "mega shop"
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock
    def sell(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            return False

laptop = product("Laptop", 1000, 10)

print(f"shop: {laptop.shop_name}")
print(f"stock before selling: {laptop.stock}")

laptop.sell(3)
print(f"stock after selling: {laptop.stock}")