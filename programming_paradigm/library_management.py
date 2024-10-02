class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"You have checked out '{book.title}' by {book.author}.")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"You have returned '{book.title}' by {book.author}.")
                else:
                    print(f"'{book.title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
