import mysql.connector

def create_connection():
   connection = mysql.connector.connect(
            host="localhost",
            user="aiswaryaa",
            password="aisu123",
            database="mydatabase"
    )
   def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employe (
            emp_id INT PRIMARY KEY,
            employee_name VARCHAR(100),
            start_date INT,
           department VARCHAR(100),
            leave_type VARCHAR(100),
           end_date INT,
           status INT,
            remarks VARCHAR(100)               
        )
    ''')

def add_leave(employee_id, employee_name, department, leave_type, start_date, end_date, status, remarks):
    conn = create_connection()
    cursor = conn.cursor()
    query = "INSERT INTO leaves (employee_id, employee_name, department, leave_type, start_date, end_date, status, remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (employee_id, employee_name, department, leave_type, start_date, end_date, status, remarks))
    conn.commit()
    cursor.close()
    conn.close()

# Similarly, define functions for update_leave and delete_leave

# Example usage
add_leave('E123', 'John Doe', 'IT', 'Sick Leave', '2024-08-10', '2024-08-15', 'Pending', 'Recovering from surgery')
def update_leave(leave_id, status=None, remarks=None, start_date=None, end_date=None):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Build the query dynamically based on provided fields
    query = "UPDATE leaves SET "
    params = []
    
    if status is not None:
        query += "status = %s, "
        params.append(status)
    
    if remarks is not None:
        query += "remarks = %s, "
        params.append(remarks)
    
    if start_date is not None:
        query += "start_date = %s, "
        params.append(start_date)
    
    if end_date is not None:
        query += "end_date = %s, "
        params.append(end_date)
    
    # Remove the last comma and space, and add WHERE clause
    query = query.rstrip(', ') + " WHERE id = %s"
    params.append(leave_id)
    
    cursor.execute(query, tuple(params))
    conn.commit()
    cursor.close()
    conn.close()
def delete_leave(leave_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM leaves WHERE id = %s"
    cursor.execute(query, (leave_id,))
    conn.commit()
    cursor.close()
    conn.close()
def main():
    while True:
        print("\nMedical Leave Management System")
        print("1. Add Leave Details")
        print("2. Update Leave Details")
        print("3. Delete Leave Details")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_leave()
        elif choice == 2:
            update_leave()
        elif choice == 3:
            delete_leave()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()