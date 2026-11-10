import requests

BASE_URL = "https://crudcrud.com/api/456c8173d8414299958ec574f1439f45/products"

try:
    response = requests.get(BASE_URL, timeout=5)
    response.raise_for_status()
    products = response.json()

    if not products:
        print("No products found.")
    else:
        for product in products:
            print(f"Name: {product['name']} | Price: {product['price']} | ID: {product['_id']}")
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.HTTPError as e:
    print(f"Server returned a bad status code: {e}")
except requests.exceptions.ConnectionError:
    print("Connection problem, check your internet or the URL")
except requests.exceptions.RequestException as e:
    print(f"Unexpected error: {e}")