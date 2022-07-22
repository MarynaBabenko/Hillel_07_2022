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


    def students_use(self):
        return(self.author,self.name,self.genre)

Book_1 = Book(author="Jack_London", name="Martin Eden",year = "2002",publishing_house="New_Book",
          genre="novel", price="130")
Book_2 = Book(name="Murder at the Vicarage",year = "2017",publishing_house="Collins",
          genre="detective", author="Agatha Christie", price="300")

Book.show_details(Book_1)
Book.show_details(Book_2)

print(f'Data for students: {Book_1.students_use()}')
