names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

products = list(zip(names, prices, ratings))
print("Products:", products)
by_price = sorted(products, key=lambda product: product[1], reverse=True)
print("Products sorted by price (descending):", by_price)
by_rating = sorted(products, key=lambda product: product[2])
print("Products sorted by rating (ascending):", by_rating)