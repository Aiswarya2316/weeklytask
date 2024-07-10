users = []

def register():
    print("=== Registration ===")
    name = input("Enter your name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    user = {
        'name': name,
        'username': username,
        'password': password,
        'balance': 0
    }

    users.append(user)
    print("Registration successful.")

def login():
    print("=== Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful.")
            return user

    print("Invalid credentials. Please try again.")
    return None
