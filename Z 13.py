# Exercise 13: Car Class :
#Create a Car class with attributes CAR compony, model, and year. Include a method to display the details of the car.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"CAR compony: {self.make}, Model: {self.model}, Year: {self.year}")


car = Car(" Hyundai ", " Tucson ", 2017 )
car.display_details()
