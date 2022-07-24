class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")

    def get_price(self):
        self.price *= self.discount
        return(float(self.price))


class Phone(Product):
    def __init__(self, name, color, price, amount,discount, lte=False):
        # Product.__init__(self, name, color, price, amount)
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = ", LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional

        return message

    # def show_description(self):
    #     # if self.lte is True:
    #     #     additional = "LTE"
    #     # else:
    #     #     additional = ""
    #     additional = "LTE" if self.lte else ""
    #     print(f"Description: {self.name}/{self.color}: {self.price} | {self.amount}, {additional}")


class Laptop(Product):
    def __init__(self,name, color, price, amount, discount, motherboard_type, material):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.material = material

    def show_details(self):
        print(f'Details: { self.name},{self.color},{self.price},{self.amount},'
              f'{self.discount},{self.motherboard_type},{self.material}')


iphone7 = Phone(name="iPhone 7", color="red", price=700.0, discount=0.8, amount=1)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, discount=0.95, lte=True)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1,discount=0.95,
                motherboard_type="NLX",material="plastik")

iphone13.show_description()
iphone7.show_description()
lenovo.show_details()
print(iphone7.get_price())
print(iphone13.get_price())
print(lenovo.get_price())
