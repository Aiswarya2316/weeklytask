# admin.py

products = [
    {"id": 1, "name": "Apple", "price": 0.5},
    {"id": 2, "name": "Banana", "price": 0.3},
    {"id": 3, "name": "Orange", "price": 0.8},
]

def add_product(product_id, name, price):
    products.append({"id": product_id, "name": name, "price": price})
    print(f"Added product: ID={product_id}, Name={name}, Price={price}")

def remove_product(product_id):
    global products
    products = [product for product in products if product['id'] != product_id]
    print(f"Removed product with ID={product_id}")

def view_inventory():
    print("Inventory:")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")
