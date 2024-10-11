# Base class
class Book:
    def __init__(self, title, author):
        """Initialize book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

# Derived class for EBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class for PrintBooks
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class demonstrating composition
class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all the books in the library."""
        for book in self.books:
            print(book)
