class Book:
    def __init__(self, title, author):
        """Initialize the common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook attributes along with inherited Book attributes."""
        super().__init__(title, author)  # Call the base class (Book) __init__ method
        self.file_size = file_size

    def __str__(self):
        """String representation for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook attributes along with inherited Bo
