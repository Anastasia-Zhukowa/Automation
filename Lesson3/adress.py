class Adress:

    def __init__(self, index, city, street, building, flat ):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.flat = flat

    def get_address(self):
        return f'({self.index}), {self.city}, {self.street}, {self.building} - {self.flat}'


