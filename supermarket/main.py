# main.py

import user
import admin

def user_interface():
    while True:
        print("\nUser Menu:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            user.view_products()
        elif choice == 2:
            product_id = int(input("Enter product ID to add to cart: "))
            quantity = int(input("Enter quantity: "))
            user.add_to_cart(product_id, quantity)
        elif choice == 3:
            user.view_cart()
        elif choice == 4:
            user.checkout()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def admin_interface():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            admin.add_product(product_id, name, price)
        elif choice == 2:
            product_id = int(input("Enter product ID to remove: "))
            admin.remove_product(product_id)
        elif choice == 3:
            admin.view_inventory()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. User")
        print("2. Admin")
        print("3. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            user_interface()
        elif choice == 2:
            admin_interface()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
