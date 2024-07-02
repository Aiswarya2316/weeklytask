    #   medicalbill

patients = {}
current_patient = None

while True:
    print("\nPlease select an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1: 
        print("\n--- Patient Registration ---")
        patient_id = input("Enter Patient ID: ")
        patient_name = input("Enter Patient Name: ")
        patient_age = input("Enter Patient Age: ")
        patient_address = input("Enter Patient Address: ")
        patient_password = input("Create Password: ")

        patients[patient_id] = {
            'name': patient_name,
            'age': patient_age,
            'address': patient_address,
            'password': patient_password
        }

        print(f"\nPatient {patient_name} registered successfully!")

    elif choice == 2:  
        print("\n--- Patient Login ---")
        login_id = input("Enter Patient ID: ")
        login_password = input("Enter Password: ")

        if login_id in patients and patients[login_id]['password'] == login_password:
            current_patient = login_id
            print(f"\nWelcome, {patients[login_id]['name']}!")
        else:
            print("\nInvalid Patient ID or Password.")

    print("\nPlease select an option:")
    print("1. Medical Bill")
    print("2. Exit")
    choice = int(input("Enter the number of your choice: "))
    if choice==1:
        print("\n--- Medical Bill ---")
        if current_patient:
            print(f"Medical bill for {patients[current_patient]['name']}:")
            print("Consultation Fee: $50")
            print("Medication: $30")
            print("Total: $80")
        else:
            print("\nPlease log in to view the medical bill.")

    elif choice == 2:  
        print("THANK YOU .............!")
        break

    else:
        print("Invalid selection. Please try again.")

