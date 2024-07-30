class User:
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self):
        self.books = ['harry potter', 'the hobbit', 'game of thrones', 'lord of the rings']
        self.users = []

    def register_user(self, name, email, phone, password):
        for user in self.users:
            if user.email == email:
                print("Email already registered.")
                return
        new_user = User(name, email, phone, password)
        self.users.append(new_user)
        print('Registration successful.')

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                print('Login successful.')
                return user
        print('Invalid email or password.')
        return None

    def display_books(self):
        print('Available books:')
        for book in self.books:
            print(book)

    def borrow_book(self, user, book):
        if book in self.books:
            self.books.remove(book)
            user.borrow_book(book)
            print(f'You have borrowed "{book}".')
        else:
            print('Book not available.')

    def return_book(self, user, book):
        if user.return_book(book):
            self.books.append(book)
            print(f'You have returned "{book}".')
        else:
            print('You did not borrow this book.')

    def display_borrowing_history(self, user):
        if user.borrowed_books:
            print('Your borrowing history:')
            for book in user.borrowed_books:
                print(book)
        else:
            print('You have not borrowed any books.')

# Main program
library = Library()

while True:
    print('\n1. Register\n2. Login')
    ch = int(input('Enter your choice: '))

    if ch == 1:
        name = input('Enter user name: ')
        email = input('Enter your email: ')
        phone = int(input('Enter your phone number: '))
        password = input('Enter your password: ')
        library.register_user(name, email, phone, password)

    elif ch == 2:
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        user = library.login(email, password)

        if user:
            while True:
                print('\n1. Borrow book\n2. Return book\n3. Check available books\n4. View borrowing history\n5. Logout')
                c = int(input('Enter your choice: '))

                if c == 1:
                    book = input('Enter the book you want to borrow: ')
                    library.borrow_book(user, book)

                elif c == 2:
                    book = input('Enter the book to return: ')
                    library.return_book(user, book)

                elif c == 3:
                    library.display_books()

                elif c == 4:
                    library.display_borrowing_history(user)

                elif c == 5:
                    print('Logged out.')
                    break

                else:
                    print('Invalid choice. Please try again.')

