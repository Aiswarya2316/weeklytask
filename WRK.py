#           #  marklist

# # # Data storage
# # students = {}
# # current_student = None

# # # Display the menu
# # while True:
# #     print("\nPlease select an option:")
# #     print("1. Register")
# #     print("2. Login")
# #     print("3. Mark List")
# #     print("4. Exit")

# #     # Read user input
# #     choice = int(input("Enter the number of your choice: "))

# #     if choice == 1:  # Register
# #         print("\n--- Student Registration ---")
# #         student_id = input("Enter Student ID: ")
# #         student_name = input("Enter Student Name: ")
# #         student_age = input("Enter Student Age: ")
# #         student_class = input("Enter Student Class: ")
# #         student_password = input("Create Password: ")

# #         # Collect marks
# #         print("Enter marks for the subjects:")
# #         math_marks = float(input("Math: "))
# #         science_marks = float(input("Science: "))
# #         english_marks = float(input("English: "))

# #         # Store student details
# #         students[student_id] = {
# #             'name': student_name,
# #             'age': student_age,
# #             'class': student_class,
# #             'password': student_password,
# #             'marks': {
# #                 'Math': math_marks,
# #                 'Science': science_marks,
# #                 'English': english_marks
# #             }
# #         }

# #         print(f"\nStudent {student_name} registered successfully!")

# #     elif choice == 2:  # Login
# #         print("\n--- Student Login ---")
# #         login_id = input("Enter Student ID: ")
# #         login_password = input("Enter Password: ")

# #         # Authenticate student
# #         if login_id in students and students[login_id]['password'] == login_password:
# #             current_student = login_id
# #             print(f"\nWelcome, {students[login_id]['name']}!")
# #         else:
# #             print("\nInvalid Student ID or Password.")

# #     elif choice == 3:  # Mark List
# #         print("\n--- Mark List ---")
# #         if current_student:
# #             print(f"Mark list for {students[current_student]['name']}:")
# #             marks = students[current_student]['marks']
# #             for subject, mark in marks.items():
# #                 print(f"{subject}: {mark}")
# #         else:
# #             print("\nPlease log in to view the mark list.")

# #     elif choice == 4:  # Exit
# #         print("Exiting the system.")
# #         break

# #     else:
# #         print("Invalid selection. Please try again.")





# L=[[000,'admin'],
#    ['reg','name','eng','mal','maths','bio','phy','che'],
#    [12345,'alal',50,40,55,34,73,47],
#    [67890,'aro',43,65,45,51,33,63]]
# # L=[[12345,'alal',[50,40,55,34,73,47]],
# #     [67890,'aro',[43,65,45,51,33,63]]]
# while True:
#     # print("\n1.Login \n2.cancle")
#     a=int(input("\n1.Login \n2.cancle \n3.Enter your choice : "))
    
    

#     if a==1:
#         reg=int(input("Enter regester number : "))
#         name=str(input("Enter name : ")) 
#         f=0
#         for i in L:
#             if reg==i[0] and name==i[1]: 
#                 f=1
#                 print("You have successfully logined .")
#                 for row in L:
#                     print()
#                     print("Your results are : \n")
#                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
#                     print('_'*60)
#                     # print("\t".join(map(str,row)))
#                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7]))    
#                     # print("Marks are : ",i[2],i[3],i[4],i[5],i[6],i[7])
#                     # print("marks are : ",i[3])

#                     break
#             if f==0:
#                 print("ID not found")
#     elif a==2:
#          print("You had exited .")
#          break
#     elif a==3:
#         name=str(input("Enter name : ")) 
#         reg=int(input("Enter password : "))
       
#         f=0
#         for i in L:
#             if reg==i[0] and name==i[1]: 
#                 f=1
#                 b=int(input("\n1.Add student \n2.view student \n3.Exit \nEnter your choice : "))
#                 if b==1:
#                     reg=int(input("Enter regester number : "))
#                     name=str(input("Enter student name : "))
#                     eng=int(input("Enter mark in english : "))
#                     mal=int(input("Enter mark in malayalam : "))
#                     maths=int(input("Enter mark in maths : "))
#                     bio=int(input("Enter mark in biology : "))
#                     phy=int(input("Enter mark in physics : "))
#                     che=int(input("Enter mark in chemistry : "))
                        
#                     L.append([ reg,name,eng,mal,maths,bio,phy,che])
                    
#                 elif b==2:
#                     for i in L:
#                         print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
#                         print('_'*60)
#                         print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7])) 
#                         break
#         if f==0:   
#             print("ID not found")            
#         elif b==3:
#             break
#     else:
                    
#                 print("INVALID INPUT !")



#                 # or


L = [
    [0, 'admin'],
    ['reg', 'name', 'eng', 'mal', 'maths', 'bio', 'phy', 'che'],
    [12345, 'alal', 50, 40, 55, 34, 73, 47],
    [67890, 'aro', 43, 65, 45, 51, 33, 63]
]

while True:
    # Display the main menu
    print("\n1. Login")
    print("2. Cancel")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # User login
        reg = int(input("Enter register number: "))
        name = input("Enter name: ")
        
        f = 0
        for student in L:
            if reg == student[0] and name == student[1]:
                f = 1
                print("You have successfully logged in.")
                
                if reg == 0 and name == 'admin':
                    # Admin menu
                    while True:
                        print("\nAdmin Menu")
                        print("1. Add Student")
                        print("2. View All Students")
                        print("3. Exit Admin Menu")
                        admin_choice = int(input("Enter your choice: "))
                        
                        if admin_choice == 1:
                            # Add a new student
                            new_reg = int(input("Enter register number: "))
                            new_name = input("Enter student name: ")
                            new_eng = int(input("Enter mark in English: "))
                            new_mal = int(input("Enter mark in Malayalam: "))
                            new_maths = int(input("Enter mark in Maths: "))
                            new_bio = int(input("Enter mark in Biology: "))
                            new_phy = int(input("Enter mark in Physics: "))
                            new_che = int(input("Enter mark in Chemistry: "))
                            L.append([new_reg, new_name, new_eng, new_mal, new_maths, new_bio, new_phy, new_che])
                            print(f"Student {new_name} added successfully.")
                        
                        elif admin_choice == 2:
                            # View all students
                            print("\nAll Students:")
                            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                                "Reg No", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
                            print('-' * 80)
                            for student in L[2:]:  # Skip admin and headers
                                print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                                    student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
                        
                        elif admin_choice == 3:
                            break
                        
                        else:
                            print("Invalid choice. Please try again.")
                
                else:
                    # Display the logged-in student's marks
                    print("\nYour results are:")
                    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                        "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
                    print('-' * 60)
                    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                        student[2], student[3], student[4], student[5], student[6], student[7]))
                break
        
        if f == 0:
            print("ID not found.")
    
    elif choice == 2:
        print("You have exited.")
        break
    
    else:
        print("Invalid input! Please try again.")



# List of students and their marks
# L = [
#     [000, 'admin'],
#     ['reg', 'name', 'eng', 'mal', 'maths', 'bio', 'phy', 'che'],
#     [12345, 'alal', 50, 40, 55, 34, 73, 47],
#     [67890, 'aro', 43, 65, 45, 51, 33, 63]
# ]

# while True:
#     # Display the menu
#     print("\n1. Login")
#     print("2. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         # User login
#         reg = int(input("Enter register number: "))
#         name = input("Enter name: ")
        
#         found = False
#         for student in L:
#             if reg == student[0] and name == student[1]:
#                 found = True
#                 print("You have successfully logged in.")
                
#                 # Display student marks
#                 print("\nYour results are:")
#                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
#                 print('_' * 70)
#                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
#                 break
        
#         if not found:
#             print("ID or name not found.")
    
#     elif choice == 2:
#         print("You have exited.")
#         break
    
#     else:
#         print("INVALID INPUT!")

#     # Admin menu
#     if reg == 000 and name == 'admin':
#         while True:
#             print("\nAdmin Menu:")
#             print("1. Add student")
#             print("2. View all students")
#             print("3. Logout")
#             admin_choice = int(input("Enter your choice: "))
            
#             if admin_choice == 1:
#                 # Add a new student
#                 reg = int(input("Enter register number: "))
#                 name = input("Enter student name: ")
#                 eng = int(input("Enter mark in English: "))
#                 mal = int(input("Enter mark in Malayalam: "))
#                 maths = int(input("Enter mark in Maths: "))
#                 bio = int(input("Enter mark in Biology: "))
#                 phy = int(input("Enter mark in Physics: "))
#                 che = int(input("Enter mark in Chemistry: "))
                
#                 L.append([reg, name, eng, mal, maths, bio, phy, che])
#                 print(f"Student {name} added successfully!")
            
#             elif admin_choice == 2:
#                 # View all students
#                 print("\nAll Students' Marks:")
#                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
#                 print('_' * 70)
#                 for student in L[2:]:  # Skip the first two entries for the header and admin
#                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
            
#             elif admin_choice == 3:
#                 print("Admin logged out.")
#                 break
            
#             else:
#                 print("Invalid choice. Please try again.")








# # # List of students and their marks
# # L = [
# #     [000, 'admin'],
# #     ['reg', 'name', 'eng', 'mal', 'maths', 'bio', 'phy', 'che'],
# #     [12345, 'alal', 50, 40, 55, 34, 73, 47],
# #     [67890, 'aro', 43, 65, 45, 51, 33, 63]
# # ]

# # while True:
# #     # Display the menu
#     print("\n1. Login")
#     print("2. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         # User login
#         reg = int(input("Enter register number: "))
#         name = input("Enter name: ")
        
#         found = False
#         for student in L:
#             if reg == student[0] and name == student[1]:
#                 found = True
#                 print("You have successfully logged in.")
                
#                 # Display student marks
#                 print("\nYour results are:")
#                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
#                 print('_' * 70)
#                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
#                 break
        
#         if not found:
#             print("ID or name not found.")
    
#     elif choice == 2:
#         print("You have exited.")
#         break
    
#     else:
#         print("INVALID INPUT!")

#     # Admin menu
#     if reg == 000 and name == 'admin':
#         while True:
#             print("\nAdmin Menu:")
#             print("1. Add student")
#             print("2. View all students")
#             print("3. Logout")
#             admin_choice = int(input("Enter your choice: "))
            
#             if admin_choice == 1:
#                 # Add a new student
#                 reg = int(input("Enter register number: "))
#                 name = input("Enter student name: ")
#                 eng = int(input("Enter mark in English: "))
#                 mal = int(input("Enter mark in Malayalam: "))
#                 maths = int(input("Enter mark in Maths: "))
#                 bio = int(input("Enter mark in Biology: "))
#                 phy = int(input("Enter mark in Physics: "))
#                 che = int(input("Enter mark in Chemistry: "))
                
#                 L.append([reg, name, eng, mal, maths, bio, phy, che])
#                 print(f"Student {name} added successfully!")
            
#             elif admin_choice == 2:
#                 # View all students
#                 print("\nAll Students' Marks:")
#                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
#                 print('_' * 70)
#                 for student in L[2:]:  # Skip the first two entries for the header and admin
#                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
            
#             elif admin_choice == 3:
#                 print("Admin logged out.")
#                 break
            
#             else:
#                 print("Invalid choice. Please try again.")               
