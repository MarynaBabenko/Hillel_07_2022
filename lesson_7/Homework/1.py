class Car:

    def __init__(self, name, year, manufacturer, engine, colour, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.colour = colour                       # Я так розумію, що це - метод для введення данних
        self.price = price


    def show_details(self):
        print(f'Car name: {self.name}\nYear: {self.year}\n'
              f'Manufacturer: {self.manufacturer}\n'
              f'Engine: {self.engine}\nColour: {self.colour}\n'
              f'Price: {self.price}\n')                   # Це функція(метод) виведення даних


    def data_sale_print(self):
        print(f'Data for sale:\nCar name: {self.name}\nYear: {self.year}\nPrice: {self.price}\n')  #доступ до окремих полів через методи класу

    def data_sale(self):
        return(self.name,self.year,self.price)                  #доступ до окремих полів через методи класу треба "print"


Volkswagen = Car(name="Volkswagen T-Roc",year = "2015",price="25000",
          manufacturer="Volkswagen", engine="1,5", colour="Red")


Car.show_details(Volkswagen)

Car.data_sale_print(Volkswagen)

print(f'Data for sale:\n{Volkswagen.data_sale()}')
