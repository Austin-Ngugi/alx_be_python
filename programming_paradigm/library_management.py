# library_management.py

# Define a class to represent individual books
class Book:
    def __init__(self, title, author):
        # Initialize the book with its title and author
        self.title = title
        self.author = author
        # Private variable to track if the book is checked out or not (False means available)
        self._is_checked_out = False

    def check_out(self):
        """Mark book as checked out"""
        # Change status to True to indicate the book is checked out
        self._is_checked_out = True

    def return_book(self):
        """Mark book as returned"""
        # Change status to False to indicate the book is available again
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available"""
        # Return True if not checked out, False otherwise
        return not self._is_checked_out


# Define a class to represent the library that manages books
class Library:
    def __init__(self):
        # Initialize the library with an empty list to store books
        self._books = []

    def add_book(self, book):
        """Add a book to the library"""
        # Add the given Book object to the library’s collection
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and mark it as checked out"""
        # Loop through all books in the library
        for book in self._books:
            # Check if the book title matches and the book is available
            if book.title == title and book.is_available():
                # Mark it as checked out
                book.check_out()
                # Inform the user that the checkout was successful
                print(f"Checked out '{title}'.")
                return  # Exit the method once the book is found and checked out
        # If no matching available book is found
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        """Return a book to the library"""
        # Loop through all books to find the one being returned
        for book in self._books:
            # Check if the title matches and the book is currently checked out
            if book.title == title and not book.is_available():
                # Mark it as returned
                book.return_book()
                # Inform the user
                print(f"Returned '{title}'.")
                return  # Exit the method after returning the book
        # If no matching checked-out book is found
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """List all available books"""
        # Create a list of books that are available
        available_books = [book for book in self._books if book.is_available()]
        # If there are available books, print their titles and authors
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            # If no books are available, print this message
            print("No available books.")
