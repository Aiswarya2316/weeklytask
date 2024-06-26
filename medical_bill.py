                # "Medical billing"

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
medical_bill = consultation_fee + medication_cost + lab_tests_cost 


# Simulate login
print("Please log in to check your medical bill.")
username = input("Enter your username: ")
if username == stored_username:
    password = input("Enter your password: ")
    if password == stored_password:
        print("Login successful!")
        print(f"Your medical bill is ${medical_bill}")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found. Access denied.")


    # Initialize an empty list to store patient data
patients = []

# Enter details for multiple patients
num_patients = int(input("Enter the number of patients: "))

for _ in range(num_patients):
    # Initialize a dictionary to store a single patient's data
    patient = {}

    # Collect patient information
    patient['Patient Name'] = input("Enter patient's name: ")
    patient['Age'] = int(input("Enter patient's age: "))
    patient['Gender'] = input("Enter patient's gender (M/F): ")
    patient['Contact Number'] = input("Enter patient's contact number: ")

    # Collect bill information
    patient['Bill Number'] = input("Enter bill number: ")
    patient['Date of Service'] = input("Enter date of service (YYYY-MM-DD): ")
    patient['Service Description'] = input("Enter service description: ")
    patient['Amount'] = float(input("Enter amount: "))

    # Add the patient's data to the patients list
    patients.append(patient)

# Display all collected patient data
print("\nCollected Medical Bill Information:")
for idx, patient in enumerate(patients, 1):
    print(f"\nPatient {idx}:")
    print(f"Name: {patient['Patient Name']}")
    print(f"Age: {patient['Age']}")
    print(f"Gender: {patient['Gender']}")
    print(f"Contact Number: {patient['Contact Number']}")
    print(f"Bill Number: {patient['Bill Number']}")
    print(f"Date of Service: {patient['Date of Service']}")
    print(f"Service Description: {patient['Service Description']}")
    print(f"Amount: {patient['Amount']}")
