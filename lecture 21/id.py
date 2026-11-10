import requests

BASE_URL = "https://crudcrud.com/api/456c8173d8414299958ec574f1439f45/products"
product_id = "4" 

try:
    response = requests.get(f"{BASE_URL}/{product_id}", timeout=5)
    response.raise_for_status()
    product = response.json()

    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"In stock: {product['in_stock']}")
    print(f"ID: {product['_id']}")
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.HTTPError as e:
    print(f"Server returned a bad status code: {e}")
except requests.exceptions.ConnectionError:
    print("Connection problem, check your internet or the URL")
except requests.exceptions.RequestException as e:
    print(f"Unexpected error: {e}")