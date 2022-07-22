class Stadium:

    def __init__(self, name, open_date, country, city, placing):
        self.name = name
        self.open_date = open_date
        self.country = country
        self.city = city
        self.placing = placing

    def show_details(self):
        print(f'Stadium data:\nStadium name: {self.name}\n'
              f'Open date: {self.open_date}\nCountry: {self.country}\n'
              f'City: {self.city}\nPlacing: {self.placing}')


    def user_case(self):
        return(self.name,self.country,self.city)

Stadium_1 = Stadium(name="Donbass Arena",open_date="29.08.2009",country="Ukraine",
          city="Donetsk", placing="center of the city")

Stadium_2 = Stadium(name="Wembley Stadium",open_date="19.05.2007",country="England",
          city="London", placing="	Wembley")
Stadium.show_details(Stadium_1)
Stadium.user_case(Stadium_1)
print(f'User case: {Stadium_1.user_case()}\n')


Stadium.show_details(Stadium_2)
Stadium.user_case(Stadium_2)
print(f'User case: {Stadium_2.user_case()}\n')