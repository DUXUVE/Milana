class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def Input_data(self):
        self.title = input()
        self.year = input()
        self.publisher = input()
        self.genre = input()
        self.author = input()
        self.price = input()

    def __str__(self):
        return f"{self.title} {self.year} {self.publisher} {self.genre} {self.author} {self.price}"


book = Book(title=None, year=None, publisher=None, genre=None, author=None, price=None)
book.Input_data()
print(book)