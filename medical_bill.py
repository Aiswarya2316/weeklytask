# Step 1: Gather patient information
patient_name = input("Enter the patient's name: ")
patient_id = input("Enter the patient's ID: ")
age = int(input("Enter the patient's age: "))
gender = input("Enter the patient's gender: ")

# Step 2: Gather charges information
consultation_fee = float(input("Enter the consultation fee: "))
medication_cost = float(input("Enter the medication cost: "))
lab_tests_cost = float(input("Enter the cost of lab tests: "))
hospital_stay_cost = float(input("Enter the cost of hospital stay: "))

# Step 3: Calculate the total bill
total_bill = consultation_fee + medication_cost + lab_tests_cost + hospital_stay_cost

# Step 4: Display the bill
print("\n--- Medical Bill ---")
print("Patient Name: ", patient_name)
print("Patient ID: ", patient_id)
print("Age: ", age)
print("Gender: ", gender)
print("Consultation Fee: $", format(consultation_fee, '.2f'))
print("Medication Cost: $", format(medication_cost, '.2f'))
print("Lab Tests Cost: $", format(lab_tests_cost, '.2f'))
print("Hospital Stay Cost: $", format(hospital_stay_cost, '.2f'))
print("Total Bill: $", format(total_bill, '.2f'))


# Predefined user credentials and bill
stored_username = "user123"
stored_password = "pass123"
medical_bill = total_bill

# Simulate login
print("Please log in to check your medical bill.")

# Prompt user for username
username = input("Enter your username: ")

# Check username
if username == stored_username:
    # Prompt user for password
    password = input("Enter your password: ")
    
    # Check password
    if password == stored_password:
        # Successful login
        print("Login successful!")
        print(f"Your medical bill is ${medical_bill}")
    else:
        # Incorrect password
        print("Incorrect password. Access denied.")
else:
    # Incorrect username
    print("Username not found. Access denied.")