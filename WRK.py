# # Data storage
# students = {}
# current_student = None

# # Display the menu
# while True:
#     print("\nPlease select an option:")
#     print("1. Register")
#     print("2. Login")
#     print("3. Mark List")
#     print("4. Exit")

#     # Read user input
#     choice = int(input("Enter the number of your choice: "))

#     if choice == 1:  # Register
#         print("\n--- Student Registration ---")
#         student_id = input("Enter Student ID: ")
#         student_name = input("Enter Student Name: ")
#         student_age = input("Enter Student Age: ")
#         student_class = input("Enter Student Class: ")
#         student_password = input("Create Password: ")

#         # Collect marks
#         print("Enter marks for the subjects:")
#         math_marks = float(input("Math: "))
#         science_marks = float(input("Science: "))
#         english_marks = float(input("English: "))

#         # Store student details
#         students[student_id] = {
#             'name': student_name,
#             'age': student_age,
#             'class': student_class,
#             'password': student_password,
#             'marks': {
#                 'Math': math_marks,
#                 'Science': science_marks,
#                 'English': english_marks
#             }
#         }

#         print(f"\nStudent {student_name} registered successfully!")

#     elif choice == 2:  # Login
#         print("\n--- Student Login ---")
#         login_id = input("Enter Student ID: ")
#         login_password = input("Enter Password: ")

#         # Authenticate student
#         if login_id in students and students[login_id]['password'] == login_password:
#             current_student = login_id
#             print(f"\nWelcome, {students[login_id]['name']}!")
#         else:
#             print("\nInvalid Student ID or Password.")

#     elif choice == 3:  # Mark List
#         print("\n--- Mark List ---")
#         if current_student:
#             print(f"Mark list for {students[current_student]['name']}:")
#             marks = students[current_student]['marks']
#             for subject, mark in marks.items():
#                 print(f"{subject}: {mark}")
#         else:
#             print("\nPlease log in to view the mark list.")

#     elif choice == 4:  # Exit
#         print("Exiting the system.")
#         break

#     else:
#         print("Invalid selection. Please try again.")





L=[[000,'admin'],
   ['reg','name','eng','mal','maths','bio','phy','che'],
   [12345,'alal',50,40,55,34,73,47],
   [67890,'aro',43,65,45,51,33,63]]
# L=[[12345,'alal',[50,40,55,34,73,47]],
#     [67890,'aro',[43,65,45,51,33,63]]]
while True:
    # print("\n1.Login \n2.cancle")
    a=int(input("\n1.Login \n2.cancle \n3.Enter your choice : "))
    
    

    if a==1:
        reg=int(input("Enter regester number : "))
        name=str(input("Enter name : ")) 
        f=0
        for i in L:
            if reg==i[0] and name==i[1]: 
                f=1
                print("You have successfully logined .")
                for row in L:
                    print()
                    print("Your results are : \n")
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
                    print('_'*60)
                    # print("\t".join(map(str,row)))
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7]))    
                    # print("Marks are : ",i[2],i[3],i[4],i[5],i[6],i[7])
                    # print("marks are : ",i[3])

                    break
            if f==0:
                print("ID not found")
    elif a==2:
         print("You had exited .")
         break
    elif a==3:
        name=str(input("Enter name : ")) 
        reg=int(input("Enter password : "))
       
        f=0
        for i in L:
            if reg==i[0] and name==i[1]: 
                f=1
                b=int(input("\n1.Add student \n2.view student \n3.Exit \nEnter your choice : "))
                if b==1:
                    reg=int(input("Enter regester number : "))
                    name=str(input("Enter student name : "))
                    eng=int(input("Enter mark in english : "))
                    mal=int(input("Enter mark in malayalam : "))
                    maths=int(input("Enter mark in maths : "))
                    bio=int(input("Enter mark in biology : "))
                    phy=int(input("Enter mark in physics : "))
                    che=int(input("Enter mark in chemistry : "))
                        
                    L.append([ reg,name,eng,mal,maths,bio,phy,che])
                    
                elif b==2:
                    for i in L:
                        print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
                        print('_'*60)
                        print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7])) 
                        break
        if f==0:   
            print("ID not found")            
        elif b==3:
            break
    else:
                    
                print("INVALID INPUT !")