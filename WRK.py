# #           #  marklist

# # # # Data storage
# # # students = {}
# # # current_student = None

# # # # Display the menu
# # # while True:
# # #     print("\nPlease select an option:")
# # #     print("1. Register")
# # #     print("2. Login")
# # #     print("3. Mark List")
# # #     print("4. Exit")

# # #     # Read user input
# # #     choice = int(input("Enter the number of your choice: "))

# # #     if choice == 1:  # Register
# # #         print("\n--- Student Registration ---")
# # #         student_id = input("Enter Student ID: ")
# # #         student_name = input("Enter Student Name: ")
# # #         student_age = input("Enter Student Age: ")
# # #         student_class = input("Enter Student Class: ")
# # #         student_password = input("Create Password: ")

# # #         # Collect marks
# # #         print("Enter marks for the subjects:")
# # #         math_marks = float(input("Math: "))
# # #         science_marks = float(input("Science: "))
# # #         english_marks = float(input("English: "))

# # #         # Store student details
# # #         students[student_id] = {
# # #             'name': student_name,
# # #             'age': student_age,
# # #             'class': student_class,
# # #             'password': student_password,
# # #             'marks': {
# # #                 'Math': math_marks,
# # #                 'Science': science_marks,
# # #                 'English': english_marks
# # #             }
# # #         }

# # #         print(f"\nStudent {student_name} registered successfully!")

# # #     elif choice == 2:  # Login
# # #         print("\n--- Student Login ---")
# # #         login_id = input("Enter Student ID: ")
# # #         login_password = input("Enter Password: ")

# # #         # Authenticate student
# # #         if login_id in students and students[login_id]['password'] == login_password:
# # #             current_student = login_id
# # #             print(f"\nWelcome, {students[login_id]['name']}!")
# # #         else:
# # #             print("\nInvalid Student ID or Password.")

# # #     elif choice == 3:  # Mark List
# # #         print("\n--- Mark List ---")
# # #         if current_student:
# # #             print(f"Mark list for {students[current_student]['name']}:")
# # #             marks = students[current_student]['marks']
# # #             for subject, mark in marks.items():
# # #                 print(f"{subject}: {mark}")
# # #         else:
# # #             print("\nPlease log in to view the mark list.")

# # #     elif choice == 4:  # Exit
# # #         print("Exiting the system.")
# # #         break

# # #     else:
# # #         print("Invalid selection. Please try again.")





# # L=[[000,'admin'],
# #    ['reg','name','eng','mal','maths','bio','phy','che'],
# #    [12345,'alal',50,40,55,34,73,47],
# #    [67890,'aro',43,65,45,51,33,63]]
# # # L=[[12345,'alal',[50,40,55,34,73,47]],
# # #     [67890,'aro',[43,65,45,51,33,63]]]
# # while True:
# #     # print("\n1.Login \n2.cancle")
# #     a=int(input("\n1.Login \n2.cancle \n3.Enter your choice : "))
    
    

# #     if a==1:
# #         reg=int(input("Enter regester number : "))
# #         name=str(input("Enter name : ")) 
# #         f=0
# #         for i in L:
# #             if reg==i[0] and name==i[1]: 
# #                 f=1
# #                 print("You have successfully logined .")
# #                 for row in L:
# #                     print()
# #                     print("Your results are : \n")
# #                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
# #                     print('_'*60)
# #                     # print("\t".join(map(str,row)))
# #                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7]))    
# #                     # print("Marks are : ",i[2],i[3],i[4],i[5],i[6],i[7])
# #                     # print("marks are : ",i[3])

# #                     break
# #             if f==0:
# #                 print("ID not found")
# #     elif a==2:
# #          print("You had exited .")
# #          break
# #     elif a==3:
# #         name=str(input("Enter name : ")) 
# #         reg=int(input("Enter password : "))
       
# #         f=0
# #         for i in L:
# #             if reg==i[0] and name==i[1]: 
# #                 f=1
# #                 b=int(input("\n1.Add student \n2.view student \n3.Exit \nEnter your choice : "))
# #                 if b==1:
# #                     reg=int(input("Enter regester number : "))
# #                     name=str(input("Enter student name : "))
# #                     eng=int(input("Enter mark in english : "))
# #                     mal=int(input("Enter mark in malayalam : "))
# #                     maths=int(input("Enter mark in maths : "))
# #                     bio=int(input("Enter mark in biology : "))
# #                     phy=int(input("Enter mark in physics : "))
# #                     che=int(input("Enter mark in chemistry : "))
                        
# #                     L.append([ reg,name,eng,mal,maths,bio,phy,che])
                    
# #                 elif b==2:
# #                     for i in L:
# #                         print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
# #                         print('_'*60)
# #                         print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7])) 
# #                         break
# #         if f==0:   
# #             print("ID not found")            
# #         elif b==3:
# #             break
# #     else:
                    
# #                 print("INVALID INPUT !")



# #                 # or


# L = [
#     [0, 'admin'],
#     ['reg', 'name', 'eng', 'mal', 'maths', 'bio', 'phy', 'che'],
#     [12345, 'alal', 50, 40, 55, 34, 73, 47],
#     [67890, 'aro', 43, 65, 45, 51, 33, 63]
# ]

# while True:
#     # Display the main menu
#     print("\n1. Login")
#     print("2. Cancel")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         # User login
#         reg = int(input("Enter register number: "))
#         name = input("Enter name: ")
        
#         f = 0
#         for student in L:
#             if reg == student[0] and name == student[1]:
#                 f = 1
#                 print("You have successfully logged in.")
                
#                 if reg == 0 and name == 'admin':
#                     # Admin menu
#                     while True:
#                         print("\nAdmin Menu")
#                         print("1. Add Student")
#                         print("2. View All Students")
#                         print("3. Exit Admin Menu")
#                         admin_choice = int(input("Enter your choice: "))
                        
#                         if admin_choice == 1:
#                             # Add a new student
#                             new_reg = int(input("Enter register number: "))
#                             new_name = input("Enter student name: ")
#                             new_eng = int(input("Enter mark in English: "))
#                             new_mal = int(input("Enter mark in Malayalam: "))
#                             new_maths = int(input("Enter mark in Maths: "))
#                             new_bio = int(input("Enter mark in Biology: "))
#                             new_phy = int(input("Enter mark in Physics: "))
#                             new_che = int(input("Enter mark in Chemistry: "))
#                             L.append([new_reg, new_name, new_eng, new_mal, new_maths, new_bio, new_phy, new_che])
#                             print(f"Student {new_name} added successfully.")
                        
#                         elif admin_choice == 2:
#                             # View all students
#                             print("\nAll Students:")
#                             print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
#                                 "Reg No", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
#                             print('-' * 80)
#                             for student in L[2:]:  # Skip admin and headers
#                                 print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
#                                     student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
                        
#                         elif admin_choice == 3:
#                             break
                        
#                         else:
#                             print("Invalid choice. Please try again.")
                
#                 else:
#                     # Display the logged-in student's marks
#                     print("\nYour results are:")
#                     print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
#                         "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
#                     print('-' * 60)
#                     print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
#                         student[2], student[3], student[4], student[5], student[6], student[7]))
#                 break
        
#         if f == 0:
#             print("ID not found.")
    
#     elif choice == 2:
#         print("You have exited.")
#         break
    
#     else:
#         print("Invalid input! Please try again.")



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
# #                 # View all students
# #                 print("\nAll Students' Marks:")
# #                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
# #                 print('_' * 70)
# #                 for student in L[2:]:  # Skip the first two entries for the header and admin
# #                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
            
# #             elif admin_choice == 3:
# #                 print("Admin logged out.")
# #                 break
            
# #             else:
# #                 print("Invalid choice. Please try again.")               





# data=[{'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
#       {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
#       {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
#       {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
#       {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
#       {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},]

# while True:
#     # Display the menu
#     print("1.Regester \n2.Login \n3.Cancle")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         #regestration
#         op=int(input("Are you intrested in working as uber driver : \n1.Yes \n2.No"))
#         data.append({'op':op})
#         #cab regestration
#         if choice == 1:
#             uname=str(input("Enter the name : "))
#             pswd=int(input("Enter password : "))
#             email=str(input("Enter your place : "))
#             pno=int(input("Enter your phone number : "))
#             tno=str(input("Enter your taxi regestration number : "))
#             data.append({'name':uname,'pswd':pswd,'email':email,'pno':pno,'tno':tno})
#         #user regestration
#         elif choice == 2:
#             uname=str(input("Enter the name : "))
#             pswd=int(input("Enter password : "))
#             email=str(input("Enter your place : "))
#             pno=int(input("Enter your phone number : "))            
#             data.append({'name':uname,'age':pswd,'place':email,'pno':pno})
#         else:
#             print("Invalid input")
#     elif choice == 2:
#         uname = input("Enter your name : ")
#         pswd = int(input("Enter password : "))
       
        
#         found = False
#         for s in data:
#             if s['op'] == 2 and uname == s['uname'] and pswd == s['pswd']:
#                         found = True
#                         print("You have successfully logged in.")
                        
#                         while True:
#                             u_choice=int(input("1.Book taxi \n2.View details \n3.Logut \nEnter your choice : "))
#                             if u_choice == 1:                                
#                                 livloc=str(input("Share your current location : "))
#                                 headloc=str(input("Where do you want to go : "))     
#                                 time=str(input("Enter the time you want taxi to arive"))   
#                                 data.append({'livloc':livloc,'headloc':headloc,'time':time})
#                             elif u_choice == 2:
#                                 print(details&price) #booking details

#                             elif u_choice == 3:
#                                 print("You had logouted")
#                                 break
#                             else:
#                                  print("Invalid input")

                            
                        
        
#             elif s['op'] == 1 and uname == s['uname'] and pswd == s['pswd']:
#                         found = True
#                         print("You have successfully logged in.")
#                         while True:
#                             cab_choice = int(input("1.View booking \n2.Add details \n3.Logout \nEnter your choice : "))  
#                             if cab_choice == 1:
#                                 print(details&price) #booking details

#                             elif cab_choice == 2:
#                                 livloc=str(input("Share your current location : "))
#                                 data.append({'livloc':livloc})
#                             elif cab_choice == 3:
#                                 print("You had logouted")
#                                 break
#                             else:
#                                  print("Invalid input")


#     elif choice == 3:
#         print("You had exited")
#         break







#     {'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
#     {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
#     {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
#     {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
#     {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
#     {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},
# ]

# while True:
#     # Display the menu
#     print("1.Register \n2.Login \n3.Cancel")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         # Registration
#         op = int(input("Are you interested in working as an Uber driver?\n1.Yes\n2.No\nEnter your choice: "))
        
#         if op == 1:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             tno = input("Enter your taxi registration number: ")
#             data.append({'op': 1, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'tno': tno})
#             print("Registration successful!")
        
#         elif op == 2:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             data.append({'op': 2, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno})
#             print("Registration successful!")
        
#         else:
#             print("Invalid input")
    
#     elif choice == 2:
#         uname = input("Enter your name: ")
#         pswd = int(input("Enter password: "))
        
#         found = False
#         for entry in data:
#             if entry['uname'] == uname and entry['pswd'] == pswd:
#                 found = True
#                 print("Login successful!")
                
#                 if entry['op'] == 1:  # Cab driver
#                     while True:
#                         cab_choice = int(input("1.View bookings\n2.Add details\n3.Logout\nEnter your choice: "))
                        
#                         if cab_choice == 1:
#                             # Implement view bookings functionality
#                             print("User name : ")
#                             print("destination : ")
#                             print("Time of departure :")
#                             print("Earning : ")



#                             #need notification , when the user booked cab
                        
#                         elif cab_choice == 2:
#                             livloc = input("Share your current location: ")
#                             # Add location to data
#                             entry['livloc'] = livloc
#                             print("Location added successfully.")
                        
#                         elif cab_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
                
#                 elif entry['op'] == 2:  # User
#                     while True:
#                         u_choice = int(input("1.Book taxi\n2.View details\n3.Logout\nEnter your choice: "))
                        
#                         if u_choice == 1:
#                             livloc = input("Share your current location: ")
#                             if entry['livloc'] == livloc:        #####live location of taxi




#                                 headloc = input("Where do you want to go: ")
#                                 time = input("Enter the time you want taxi to arrive: ")
#                                 data.append({'livloc': livloc, 'headloc': headloc, 'time': time})
#                                 print("Booking successful!")
#                             else :
#                                 ("Sorry,No taxi is avialable")





                        
#                         elif u_choice == 2:
#                             # Implement view details functionality
#                             print("Taxi driver name : ")
#                             print("Taxi driver number :")
#                             print("cab cost : ")
                        
#                         elif u_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
        
#         if not found:
#             print("Invalid inputs. Please try again.")
    
#     elif choice == 3:
#         print("Exiting...")
#         break
    
#     else:
#         print("Invalid choice. Please enter a valid option.")




#2





# data=[
#     {'ekm':20,'ktm':25,'vkm':23},
#     {'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
#     {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
#     {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
#     {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
#     {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
#     {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},
# ]



# while True:
#     # Display the menu
#     print("1.Register \n2.Login \n3.Cancel")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         # Registration
#         op = int(input("Are you interested in working as an Uber driver?\n1.Yes\n2.No\nEnter your choice: "))
        
#         if op == 1:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             tno = input("Enter your taxi registration number: ")
#             data.append({'op': 1, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'tno': tno, 'livloc': ''})
#             print("Registration successful!")
        
#         elif op == 2:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             data.append({'op': 2, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'livloc': '', 'headloc': '', 'time': ''})
#             print("Registration successful!")
        
#         else:
#             print("Invalid input")
    
#     elif choice == 2:
#         uname = input("Enter your name: ")
#         pswd = int(input("Enter password: "))
        
#         found = False
#         for entry in data:
#             if entry['uname'] == uname and entry['pswd'] == pswd:
#                 found = True
#                 print("Login successful!")
                
#                 if entry['op'] == 1:  # Cab driver
#                     while True:
#                         cab_choice = int(input("1.View bookings\n2.Add details\n3.Logout\nEnter your choice: "))
                        
#                         if cab_choice == 1:
#                             # Implement view bookings functionality
#                             print("Your bookings:")
#                             for booking in data:
#                                 if booking.get('livloc') == entry['livloc'] and booking.get('headloc'):
#                                     print(f"User name: {booking['uname']}")
#                                     print(f"Destination: {booking['headloc']}")
#                                     print(f"Time of departure: {booking['time']}")
#                                     print("Earning: ",livloc*headloc)  # Example earning calculation
#                                     print()
#                             # Notify when a user books a cab (suggested implementation)
#                             # Check if a new booking is made
#                             for booking in data:
#                                 if booking.get('livloc') and booking.get('headloc') and booking.get('time'):
#                                     print(f"New booking by {booking['uname']} at {booking['time']}: {booking['livloc']} to {booking['headloc']}")
                        
#                         elif cab_choice == 2:
#                             livloc = input("Share your current location: ")
#                             entry['livloc'] = livloc
#                             print("Location added successfully.")
                        
#                         elif cab_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
                
#                 elif entry['op'] == 2:  # User
#                     while True:
#                         u_choice = int(input("1.Book taxi\n2.View details\n3.Logout\nEnter your choice: "))
                        
#                         if u_choice == 1:
#                             livloc = input("Share your current location: ")
#                             if any(driver['livloc'] == livloc for driver in data if driver['op'] == 1):  # Check if taxi is available
#                                 headloc = input("Where do you want to go: ")
#                                 time = input("Enter the time you want taxi to arrive: ")
#                                 data.append({'op': 2, 'uname': uname, 'pno': pno, 'livloc': livloc, 'headloc': headloc, 'time': time})
#                                 print("Booking successful!")
#                             else:
#                                 print("Sorry, no taxi is available at your location.")
                        
#                         elif u_choice == 2:
#                             print("Taxi details:")
#                             for driver in data:
#                                 if driver['op'] == 1 and driver['livloc']:
#                                     print(f"Taxi driver name: {driver['uname']}")
#                                     print(f"Taxi driver number: {driver['pno']}")
#                                     # print(f"Cab cost: $10")  # Example cost calculation
#                                     print(f"Cab cost:" ,livloc * headloc)
                                    
#                                     cancle=("1.Exit \n2.Cancle cab") #notify cab driver if cancled
#                                     if cancle == 1:
#                                         break
#                                     elif cancle == 2 :
#                                         #  give option to cancle cab
#                                         #notify cab driver if cancled
#                                     else :
#                                         print("invalid input")
#                         elif u_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
        
#         if not found:
#             print("Invalid inputs. Please try again.")
    
#     elif choice == 3:
#         print("Exiting...")
#         break
    
#     else:
#         print("Invalid choice. Please enter a valid option.")


#3




data=[
    {'ekm':20,'ktm':25,'vkm':23},
    {'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
    {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
    {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
    {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
    {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
    {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},
]

while True:
    # Display the menu
    print("1.Register \n2.Login \n3.Cancel")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Registration
        op = int(input("Are you interested in working as an Uber driver?\n1.Yes\n2.No\nEnter your choice: "))
        
        if op == 1:
            uname = input("Enter the name: ")
            pswd = int(input("Enter password: "))
            email = input("Enter your email: ")
            pno = input("Enter your phone number: ")
            tno = input("Enter your taxi registration number: ")
            data.append({'op': 1, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'tno': tno, 'livloc': ''})
            print("Registration successful!")
        
        elif op == 2:
            uname = input("Enter the name: ")
            pswd = int(input("Enter password: "))
            email = input("Enter your email: ")
            pno = input("Enter your phone number: ")
            data.append({'op': 2, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'livloc': '', 'headloc': '', 'time': ''})
            print("Registration successful!")
        
        else:
            print("Invalid input")
    
    elif choice == 2:
        uname = input("Enter your name: ")
        pswd = int(input("Enter password: "))
        
        found = False
        for entry in data:
            if entry['uname'] == uname and entry['pswd'] == pswd:
                found = True
                print("Login successful!")
                
                if entry['op'] == 1:  # Cab driver
                    while True:
                        cab_choice = int(input("1.View bookings\n2.Add details\n3.Logout\nEnter your choice: "))
                        
                        if cab_choice == 1:
                            # Implement view bookings functionality
                            print("Your bookings:")
                            for booking in data:
                                if booking.get('livloc') == entry['livloc'] and booking.get('headloc'):
                                    print(f"User name: {booking['uname']}")
                                    print(f"Destination: {booking['headloc']}")
                                    print(f"Time of departure: {booking['time']}")
                                    # Calculate fare based on distance
                                    fare = abs(data[0][entry['livloc']] - data[0][booking['headloc']]) * 10  # Example fare calculation
                                    print(f"Fare: ${fare}")
                                    print()
                            # Notify when a new booking is made
                            for booking in data:
                                if booking.get('livloc') and booking.get('headloc') and booking.get('time'):
                                    print(f"New booking by {booking['uname']} at {booking['time']}: {booking['livloc']} to {booking['headloc']}")
                        
                        elif cab_choice == 2:
                            livloc = input("Share your current location: ")
                            entry['livloc'] = livloc
                            print("Location added successfully.")
                        
                        elif cab_choice == 3:
                            print("Logout successful.")
                            break
                        
                        else:
                            print("Invalid input")
                
                elif entry['op'] == 2:  # User
                    while True:
                        u_choice = int(input("1.Book taxi\n2.View details\n3.Logout\nEnter your choice: "))
                        
                        if u_choice == 1:
                            livloc = input("Share your current location: ")
                            if any(driver['livloc'] == livloc for driver in data if driver['op'] == 1):  # Check if taxi is available
                                headloc = input("Where do you want to go: ")
                                time = input("Enter the time you want taxi to arrive: ")
                                data.append({'op': 2, 'uname': uname, 'pno': pno, 'livloc': livloc, 'headloc': headloc, 'time': time})
                                print("Booking successful!")
                            else:
                                print("Sorry, no taxi is available at your location.")
                        
                        elif u_choice == 2:
                            print("Taxi details:")
                            for driver in data:
                                if driver['op'] == 1 and driver['livloc']:
                                    print(f"Taxi driver name: {driver['uname']}")
                                    print(f"Taxi driver number: {driver['pno']}")
                                    # Calculate fare based on distance
                                    fare = abs(data[0][livloc] - data[0][headloc]) * 10  # Example fare calculation
                                    print(f"Cab cost: ${fare}")
                                    
                                    cancel = int(input("1.Exit \n2.Cancel cab\nEnter your choice: "))
                                    if cancel == 2:
                                        # Cancel the booking
                                        data.remove(driver)
                                        print("Booking canceled successfully.")
                                    elif cancel != 1:
                                        print("Invalid input.")
                                        
                        elif u_choice == 3:
                            print("Logout successful.")
                            break
                        
                        else:
                            print("Invalid input")
        
        if not found:
            print("Invalid inputs. Please try again.")
    
    elif choice == 3:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")