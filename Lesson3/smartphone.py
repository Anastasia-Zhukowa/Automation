class Smartphone:

    def __init__(self, brand, model, number ):
        self.brand = brand
        self.model = model
        self.number = number
    
    def print_brand(self):
        print(f"Марка телефона: {self.brand}")

    def print_model(self):
        print(f"Модель телефона: {self.model}")

    def print_number(self):
        print(f"Абонентский номер: {self.number}")
        
#smartphone = Smartphone("Iphone", "15", "+123456789")
#smartphone.print_brand()
#smartphone.print_model()
#smartphone.print_number()