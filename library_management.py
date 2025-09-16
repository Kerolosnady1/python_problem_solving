# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initialize as available

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"You checked out '{book.title}'.")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        print(f"No book with title '{title}' found.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"You returned '{book.title}'.")
                else:
                    print(f"'{book.title}' was not checked out.")
                return
        print(f"No book with title '{title}' found.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")

