class Book:

    def __init__(self, name, year, publishing_house, genre, author, price):
        self.author = author
        self.name = name
        self.year = year
        self.publishing_house = publishing_house
        self.genre = genre
        self.price = price


    def show_details(self):
        print(f'Author: {self.author}\nBook name: {self.name}\n'
              f'Year: {self.year}\n'
              f'Publishing house: {self.publishing_house}\n'
              f'Genre: {self.genre}\nPrice: {self.price}\n')

    def author(self):
        print(f'Author:{self.author}')
        return(self.author)

    def name(self):
        print(f'Name:{self.name}')
        return (self.name)

    def year(self):
        print(f'Name:{self.year}')
        return (self.year)

    def publishing_house(self):
        print(f'Publishing_house:{self.publishing_house}')
        return (self.publishing_house)

    def genre(self):
        print(f'Genre:{self.genre}')
        return (self.genre)

    def price(self):
        print(f'Genre:{self.price}')
        return (self.price)

Book_1 = Book(author="Jack_London", name="Martin Eden",year = "2002",publishing_house="New_Book",
          genre="novel", price="130")
Book_2 = Book(name="Murder at the Vicarage",year = "2017",publishing_house="Collins",
          genre="detective", author="Agatha Christie", price="300")

Book.show_details(Book_1)
Book.show_details(Book_2)

Book.author(Book_1)
Book.name(Book_2)
Book.publishing_house(Book_1)
Book.year(Book_2)
Book.genre(Book_1)
Book.price(Book_2)