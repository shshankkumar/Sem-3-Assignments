class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print("Book Name:", self.title)


class Patron:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Patron Name:", self.name)


class Library:
    def add_book(self, book):
        print(book.title, "was added to the library.")

    def register_patron(self, patron):
        print(patron.name, "has been registered.")

    def borrow_book(self, patron, book):
        print(patron.name, "borrowed", book.title)

    def return_book(self, patron, book):
        print(patron.name, "returned", book.title)


# Creating Objects
book1 = Book("Python")
patron1 = Patron("Shshank")
library = Library()

# Calling Methods
library.add_book(book1)
library.register_patron(patron1)
library.borrow_book(patron1, book1)
library.return_book(patron1, book1) 


'''output 
Python was added to the library.
Shshank has been registered.
Shshank borrowed Python
Shshank returned Python '''