class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Bookcase:
    def __init__(self, books=None):
        self.books = books

    # the @ marks the classmethod as a decorator
    # A decorator is more or less a function that takes another function, 
    # does something with it and usually returns that function.
    @classmethod
    # Class methods don't take self or the instance as their first argument.
    # Instead, they take the class they are being called on.
    # cls is often used as abbreviation for class
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        # return a new instance of a class with the list of books
        return cls(books)