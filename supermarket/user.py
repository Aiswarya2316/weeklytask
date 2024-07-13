# user.py

products = [
    {"id": 1, "name": "Apple", "price": 0.5},
    {"id": 2, "name": "Banana", "price": 0.3},
    {"id": 3, "name": "Orange", "price": 0.8},
]

cart = []

def view_products():
    print("Available Products:")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")

def add_to_cart(product_id, quantity):
    for product in products:
        if product['id'] == product_id:
            cart.append({"name": product['name'], "price": product['price'], "quantity": quantity})
            print(f"Added {quantity} {product['name']}(s) to cart.")

def view_cart():
    print("Your Cart:")
    total = 0
    for item in cart:
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price per item: {item['price']}, Total: {item['price'] * item['quantity']}")
        total += item['price'] * item['quantity']
    print(f"Total Amount: {total}")

def checkout():
    print("Checking out...")
    view_cart()
    print("Thank you for your purchase!")
    cart.clear()
