import hair 
import skin 
import nail 
import appoinment 
import customer 
import billing 

def main():
    # Initialize service modules
    hair_services = hair()
    skin_services = skin()
    nail_services = nail()
    
    # Initialize management modules
    appointments = appoinment()
    customers = customer()
    billing = billing()
    
    # Sample data
    customers.add_customer('Alice', '1234567890')
    customers.add_customer('Bob', '0987654321')

    appointments.book_appointment('Alice', 'Haircut', '10:00 AM')
    appointments.book_appointment('Bob', 'Facial', '11:00 AM')
    
    bill1 = billing.generate_bill('Alice', 'Haircut', hair_services.get_price('Haircut'))
    bill2 = billing.generate_bill('Bob', 'Facial', skin_services.get_price('Facial'))
    
    # Display sample data
    print("Customers:", customers.customers)
    print("Appointments:", appointments.list_appointments())
    print("Bills:", billing.list_bills())

if __name__== "_main_":
    main()