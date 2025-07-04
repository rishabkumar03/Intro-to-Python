# CLASS VARIABLE
    # Add a class variable to Car that track of the number of cars created.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    
Car("BMW", "M3")
Car("BMW", "M4")

print(Car.total_car)