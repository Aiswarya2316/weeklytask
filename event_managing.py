# Initialize dictionaries for storing user and event details
users = {}
events = {}

# Registration and Login process
while True:
    print("Welcome to Event Management System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter username: ")
        if username in users:
            print("Username already exists. Try a different one.")
        else:
            password = input("Enter password: ")
            users[username] = password
            print("Registration successful!")

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            # Event Management process
            while True:
                print("\nEvent Management")
                print("1. Add Event")
                print("2. View Events")
                print("3. Delete Event")
                print("4. Logout")
                event_choice = input("Enter your choice: ")

                if event_choice == '1':
                    event_name = input("Enter event name: ")
                    event_date = input("Enter event date: ")
                    if username not in events:
                        events[username] = {}
                    events[username][event_name] = event_date
                    print("Event added successfully!")

                elif event_choice == '2':
                    if username in events and events[username]:
                        print("Your Events:")
                        for event, date in events[username].items():
                            print(f"{event}: {date}")
                    else:
                        print("No events found.")

                elif event_choice == '3':
                    event_name = input("Enter event name to delete: ")
                    if username in events and event_name in events[username]:
                        del events[username][event_name]
                        print("Event deleted successfully!")
                    else:
                        print("Event not found.")

                elif event_choice == '4':
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid username or password.")

    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")