### In-class-Assignment-9

#### Problem 1: Define a Class and Create Objects

**Question:**

Create a Python class named `Book` that represents a book in a library. The class should have the following attributes:
- `title`: a string
- `author`: a string
- `isbn`: a string (ISBN number)
- `publication_year`: an integer
- `available`: a boolean indicating if the book is available for checkout

The class should have the following methods:
1. `__init__`: Initialize the attributes.
2. `checkout`: Change the `available` attribute to `False`.
3. `return_book`: Change the `available` attribute to `True`.

Write code to create two `Book` objects and demonstrate checking out and returning a book.


#### Problem 2: Using Static Methods and Variables

**Question:**

Create a Python class named `Library` that keeps track of the total number of books in the library. The class should have the following:
- A class variable `total_books` that keeps track of the total number of books.
- A method `__init__` that increases the `total_books` count by 1 whenever a new book is added.
- A static method `get_total_books` that returns the value of `total_books`.

Write code to demonstrate adding books to the library and retrieving the total number of books.

