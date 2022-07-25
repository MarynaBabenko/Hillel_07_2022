<<<<<<< HEAD
class Car:

    def __init__(self, name, year, manufacturer, engine, colour, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.colour = colour
        self.price = price


    def show_details(self):
        print(f'\nCar name: {self.name}\nYear: {self.year}\n'
              f'Manufacturer: {self.manufacturer}\n'
              f'Engine: {self.engine}\nColour: {self.colour}\n'
              f'Price: {self.price}\n')

    def name(self):
        print(f'Car name:{self.name}')
        return (self.name)

    def year(self):
        print(f'Year:{self.year}')
        return (self.year)

    def manufacturer(self):
        print(f'Manufacturer:{self.manufacturer}')
        return (self.manufacturer)

    def engine(self):
        print(f'Engine:{self.engine}')
        return (self.engine)

    def colour(self):
        print(f'Colour:{self.colour}')
        return (self.colour)

    def price(self):
        print(f'Price:{self.price}')
        return (self.price)

Volkswagen = Car(name="Volkswagen T-Roc",year = "2015",price="25000",
          manufacturer="Volkswagen", engine="1,5", colour="Red")

Nissan= Car(name="Nissan Note",year = "2010",price="6500",
          manufacturer="Nissan", engine="1,6", colour="Black")

Car.show_details(Volkswagen)
Car.name(Volkswagen)
Car.year(Volkswagen)
Car.price(Volkswagen)
Car.manufacturer(Volkswagen)
Car.engine(Volkswagen)
Car.colour(Volkswagen)
=======
class Car:

    def __init__(self, name, year, manufacturer, engine, colour, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.colour = colour
        self.price = price


    def show_details(self):
        print(f'\nCar name: {self.name}\nYear: {self.year}\n'
              f'Manufacturer: {self.manufacturer}\n'
              f'Engine: {self.engine}\nColour: {self.colour}\n'
              f'Price: {self.price}\n')

    def name(self):
        print(f'Car name:{self.name}')
        return (self.name)

    def year(self):
        print(f'Year:{self.year}')
        return (self.year)

    def manufacturer(self):
        print(f'Manufacturer:{self.manufacturer}')
        return (self.manufacturer)

    def engine(self):
        print(f'Engine:{self.engine}')
        return (self.engine)

    def colour(self):
        print(f'Colour:{self.colour}')
        return (self.colour)

    def price(self):
        print(f'Price:{self.price}')
        return (self.price)

Volkswagen = Car(name="Volkswagen T-Roc",year = "2015",price="25000",
          manufacturer="Volkswagen", engine="1,5", colour="Red")

Nissan= Car(name="Nissan Note",year = "2010",price="6500",
          manufacturer="Nissan", engine="1,6", colour="Black")

Car.show_details(Volkswagen)
Car.name(Volkswagen)
Car.year(Volkswagen)
Car.price(Volkswagen)
Car.manufacturer(Volkswagen)
Car.engine(Volkswagen)
Car.colour(Volkswagen)
>>>>>>> 6644533 ( update_Homework_lesson_3)
Car.show_details(Nissan)