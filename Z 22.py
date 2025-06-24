# Exercise 22: Composition Over Inheritance
# Create a Book class with a Author class included within it, demonstrating composition over inheritance.

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Book Title:", self.title)
        print("Author:", self.author.name)
        print("Nationality:", self.author.nationality)

author = Author("George Orwell", "British")
book = Book("1984", author)
book.display_info()
