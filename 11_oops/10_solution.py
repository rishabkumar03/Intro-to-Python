# MULTIPLE INHERITANCE
    # Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

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
    
class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is engine"
    
class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_ev = ElectricCarTwo("Tesla", "Model S")
print(my_new_ev.battery_info())
print(my_new_ev.engine_info()) 