class Stadium:

    def __init__(self, name, open_date, country, city, placing):
        self.name = name
        self.open_date = open_date
        self.country = country
        self.city = city
        self.placing = placing

    def show_details(self):
        print(f'\nStadium data:\nStadium name: {self.name}\n'
              f'Open date: {self.open_date}\nCountry: {self.country}\n'
              f'City: {self.city}\nPlacing: {self.placing}\n')

    def name(self):
        print(f'Name:{self.name}')
        return (self.name)

    def date(self):
        print(f'Date:{self.date}')
        return (self.date)

    def country(self):
        print(f'Country:{self.country}')
        return (self.country)

    def city(self):
        print(f'City:{self.city}')
        return (self.city)

    def placing(self):
        print(f'City:{self.placing}')
        return (self.placing)

Stadium_1 = Stadium(name="Donbass Arena",open_date="29.08.2009",country="Ukraine",
          city="Donetsk", placing="center of the city")

Stadium_2 = Stadium(name="Wembley Stadium",open_date="19.05.2007",country="England",
          city="London", placing="	Wembley")
Stadium.show_details(Stadium_1)
Stadium.show_details(Stadium_2)

Stadium.name(Stadium_2)

# etc
