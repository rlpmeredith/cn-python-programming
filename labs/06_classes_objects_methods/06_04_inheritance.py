'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class LibraryItem:

    def __init__(self, item_type="Book"):
        self.item_type = item_type

    def __str__(self):
        return f"{self.item_type}"


class Book(LibraryItem):

    library_category = "book"

    def __init__(self, title: object, author: object, stock: object, item_type: object = "Book", book_type: object = "kindle") -> object:
        super().__init__(item_type)
        self.title = title
        self.author = author
        self.stock = stock
        self.book_type = book_type

    def __str__(self):
        return f"{self.title, self.author, self.stock, self.book_type, self.item_type}"

    def issue(self):
        self.stock -= 1


class IndBook(Book):

    def __init__(self, title, author, stock, id, status , item_type="Book", book_type="kindle"):
        super().__init__(title, author, stock, item_type, book_type)
        self.id = id
        self.status = status

    def issue(self):
        self.status = "Out"

    def book_return(self):
        self.status = "In"


indbook1 = IndBook("How to Code", "Rob M", 5, 1234, "In")
indbook1.issue()
