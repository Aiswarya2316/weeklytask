# Data storage
students = {}
current_student = None

# Display the menu
while True:
    print("\nPlease select an option:")
    print("1. Register")
    print("2. Login")
    print("3. Mark List")
    print("4. Exit")

    # Read user input
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:  # Register
        print("\n--- Student Registration ---")
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        student_age = input("Enter Student Age: ")
        student_class = input("Enter Student Class: ")
        student_password = input("Create Password: ")

        # Collect marks
        print("Enter marks for the subjects:")
        math_marks = float(input("Math: "))
        science_marks = float(input("Science: "))
        english_marks = float(input("English: "))

        # Store student details
        students[student_id] = {
            'name': student_name,
            'age': student_age,
            'class': student_class,
            'password': student_password,
            'marks': {
                'Math': math_marks,
                'Science': science_marks,
                'English': english_marks
            }
        }

        print(f"\nStudent {student_name} registered successfully!")

    elif choice == 2:  # Login
        print("\n--- Student Login ---")
        login_id = input("Enter Student ID: ")
        login_password = input("Enter Password: ")

        # Authenticate student
        if login_id in students and students[login_id]['password'] == login_password:
            current_student = login_id
            print(f"\nWelcome, {students[login_id]['name']}!")
        else:
            print("\nInvalid Student ID or Password.")

    elif choice == 3:  # Mark List
        print("\n--- Mark List ---")
        if current_student:
            print(f"Mark list for {students[current_student]['name']}:")
            marks = students[current_student]['marks']
            for subject, mark in marks.items():
                print(f"{subject}: {mark}")
        else:
            print("\nPlease log in to view the mark list.")

    elif choice == 4:  # Exit
        print("Exiting the system.")
        break

    else:
        print("Invalid selection. Please try again.")
