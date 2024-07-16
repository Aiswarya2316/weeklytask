# # user.py
# import json
# import os

# USERS_FILE = 'users.json'

# def load_users():
#     if not os.path.exists(USERS_FILE):
#         return {}
#     with open(USERS_FILE, 'r') as file:
#         return json.load(file)

# def save_users(users):
#     with open(USERS_FILE, 'w') as file:
#         json.dump(users, file)

# def register_user(username, password):
#     users = load_users()
#     if username in users:
#         return False
#     users[username] = password
#     save_users(users)
#     return True

# def login_user(username, password):
#     users = load_users()
#     if username in users and users[username] == password:
#         return True
#     return False



# user.py

users = {}   # Dictionary to store user information
admins = {}  # Dictionary to store admin information

def register_user(username, password):
    if username in users:
        return False  # Username already exists
    users[username] = password
    return True  # Registration successful

def login_user(username, password):
    if username in users and users[username] == password:
        return True  # Login successful
    return False  # Invalid credentials

def register_admin(username, password):
    if username in admins:
        return False  # Username already exists
    admins[username] = password
    return True  # Registration successful

def login_admin(username, password):
    if username in admins and admins[username] == password:
        return True  # Login successful
    return False  # Invalid credentials
