from user import UserManager
from accessories import AccessoryManager
def main():
    user_manager = UserManager()
    accessory_manager = AccessoryManager()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.login_user(username, password):
                while True:
                    print("\n1. Add Accessory")
                    print("2. Remove Accessory")
                    print("3. View Accessories")
                    print("4. Logout")
                    choice = input("Choose an option: ")

                    if choice == '1':
                        accessory_id = input("Enter accessory ID: ")
                        name = input("Enter accessory name: ")
                        price = float(input("Enter accessory price: "))
                        accessory_manager.add_accessory(accessory_id, name, price)
                    elif choice == '2':
                        accessory_id = input("Enter accessory ID: ")
                        accessory_manager.remove_accessory(accessory_id)
                    elif choice == '3':
                        accessory_manager.view_accessories()
                    elif choice == '4':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
