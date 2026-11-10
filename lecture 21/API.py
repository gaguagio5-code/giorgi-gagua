import requests

BASE_URL = "https://crudcrud.com/api/456c8173d8414299958ec574f1439f45/products"

product_data = {"name": "Laptop", "price": 2500, "in_stock": True}

try:
    response = requests.post(BASE_URL, json=product_data, timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.Timeout:
    print("The request didn't make it in time.")
except requests.exceptions.HTTPError as e:
    print(f"The server returned a bad status code.: {e}")
except requests.exceptions.ConnectionError:
    print("There is a connection issue; check your internet or the URL.")
except requests.exceptions.RequestException as e:
    print(f"Another error: {e}")
    