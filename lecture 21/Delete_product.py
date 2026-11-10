import requests

BASE_URL = "https://crudcrud.com/api/456c8173d8414299958ec574f1439f45/products"
product_id = "5"  

try:
    response = requests.delete(f"{BASE_URL}/{product_id}", timeout=5)
    response.raise_for_status()
    print(f"Status code: {response.status_code}")
    print("Product was successfully deleted from the server.")
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.HTTPError as e:
    print(f"Server returned a bad status code: {e}")
except requests.exceptions.ConnectionError:
    print("Connection problem, check your internet or the URL")
except requests.exceptions.RequestException as e:
    print(f"Unexpected error: {e}")