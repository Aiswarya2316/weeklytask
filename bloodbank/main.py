from menu import display_menu
from donor import add_donor, view_donors, update_donor, delete_donor
from auth import login
from storage import initialize_storage

def main():
    initialize_storage()
    if not login():
        print("Login failed. Exiting the system.")
        return
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_donor()
        elif choice == '2':
            view_donors()
        elif choice == '3':
