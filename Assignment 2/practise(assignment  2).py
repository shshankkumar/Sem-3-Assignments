def book_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("LIBRARY BOOK REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


class Book:
    library_name = "City Central Library"

    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    @classmethod
    def change_library(cls, new_name):
        cls.library_name = new_name

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

    @book_header
    def display_book(self):
        print(f"Library: {Book.library_name}")
        print(self)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued")


if __name__ == "__main__":
    book1 = Book("Python Programming", "Prem Ji", True)
    book1.display_book()

    print()

    Book.change_library("National Digital Library")

    book2 = Book("Data Structures", "Shshank Kumar", False)
    book2.display_book()

'''output
========================================
LIBRARY BOOK REPORT
========================================
Library: City Central Library
Title: Python Programming
Author: Prem Ji
Status: Available
========================================

========================================
LIBRARY BOOK REPORT
========================================
Library: National Digital Library
Title: Data Structures
Author: Shshank Kumar
Status: Issued
========================================'''
