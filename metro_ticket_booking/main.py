# # main.py
# import user
# from ticket import TicketBooking

# def main():
#     ticket_booking = TicketBooking()
#     while True:
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             username = input("Enter username: ")
#             password = input("Enter password: ")
#             if user.register_user(username, password):
#                 print("Registration successful!")
#             else:
#                 print("Username already exists!")
#         elif choice == '2':
#             username = input("Enter username: ")
#             password = input("Enter password: ")
#             if user.login_user(username, password):
#                 print("Login successful!")
#                 while True:
#                     print("1. Book Ticket")
#                     print("2. View Tickets")
#                     print("3. Logout")
#                     user_choice = input("Enter your choice: ")
#                     if user_choice == '1':
#                         source = input("Enter source: ")
#                         destination = input("Enter destination: ")
#                         ticket = ticket_booking.book_ticket(username, source, destination)
#                         print(f"Ticket booked successfully! Ticket ID: {ticket['ticket_id']}")
#                     elif user_choice == '2':
#                         tickets = ticket_booking.view_tickets(username)
#                         if tickets:
#                             print("Your tickets:")
#                             for ticket in tickets:
#                                 print(f"Ticket ID: {ticket['ticket_id']}, Source: {ticket['source']}, Destination: {ticket['destination']}")
#                         else:
#                             print("No tickets found.")
#                     elif user_choice == '3':
#                         print("Logged out.")
#                         break
#                     else:
#                         print("Invalid choice!")
#             else:
#                 print("Invalid username or password!")
#         elif choice == '3':
#             print("Exiting the system.")
#             break
#         else:
#             print("Invalid choice!")

# if __name__ == "__main__":
#     main()



# main.py

import user
from ticket import TicketBooking

def user_page(username, ticket_booking):
    while True:
        print("\n1. Book Ticket")
        print("2. View Tickets")
        print("3. Logout")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            ticket = ticket_booking.book_ticket(username, source, destination)
            print(f"Ticket booked successfully! Ticket ID: {ticket['ticket_id']}")

        elif user_choice == '2':
            tickets = ticket_booking.view_tickets(username)
            if tickets:
                print("Your tickets:")
                for ticket in tickets:
                    print(f"Ticket ID: {ticket['ticket_id']}, Source: {ticket['source']}, Destination: {ticket['destination']}")
            else:
                print("No tickets found.")

        elif user_choice == '3':
            print("Logged out.")
            break

        else:
            print("Invalid choice!")

def admin_page(ticket_booking):
    while True:
        print("\n1. View All Tickets")
        print("2. Logout as Admin")
        admin_choice = input("Enter your choice: ")

        if admin_choice == '1':
            tickets = ticket_booking.get_all_tickets()
            if tickets:
                print("All tickets:")
                for ticket in tickets:
                    print(f"Ticket ID: {ticket['ticket_id']}, User: {ticket['username']}, Source: {ticket['source']}, Destination: {ticket['destination']}")
            else:
                print("No tickets found.")

        elif admin_choice == '2':
            print("Logged out as Admin.")
            break

        else:
            print("Invalid choice!")

def main():
    ticket_booking = TicketBooking()

    while True:
        print("\nWelcome to Metro Ticket Booking System")
        print("1. Register as User")
        print("2. Register as Admin")
        print("3. User Login")
        print("4. Admin Login")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user.register_user(username, password):
                print("User registration successful!")
            else:
                print("Username already exists!")

        elif choice == '2':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if user.register_admin(username, password):
                print("Admin registration successful!")
            else:
                print("Admin username already exists!")

        elif choice == '3':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user.login_user(username, password):
                print("User login successful!")
                user_page(username, ticket_booking)
            else:
                print("Invalid username or password!")

        elif choice == '4':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if user.login_admin(username, password):
                print("Admin login successful!")
                admin_page(ticket_booking)
            else:
                print("Invalid admin username or password!")

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
