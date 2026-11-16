class Car:
    def __init__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def description (self):
        print(f"Car Description --: {self.make}, {self.model}, {self.year}")

# Q: Instantiate an object of the class Car and display its description.

my_car = Car("Toyota", "GT86", "2020")
my_car.description()