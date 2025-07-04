# PROPERTY DECORATORS
    # Use a property decorators in the Car class to make the model attribute read-only.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod
    def general_description():
        return "Cars are directly proportional to love"

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("BMW", "M3")
# my_car.model = "M5"
Car("BMW", "M4")

print(my_car.model)