import user_module

def main():
    print("Welcome to the Supermarket Management System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            user_module.register()
        elif choice == '2':
            user = user_module.login()
            if user:
                supermarket_operations(user)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

def supermarket_operations(user):
    print(f"Welcome, {user['name']}!")

    while True:
        print("\nSelect an operation:")
        print("1. Check balance")
        print("2. Buy products")
        print("3. Logout")

        operation = input("Enter your choice: ")

        if operation == '1':
            print(f"Your balance is ${user['balance']}")
        elif operation == '2':
            # Placeholder for buying products
            pass
        elif operation == '3':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
