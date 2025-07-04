# CLASS INHERITANCE AND isInstance() FUNCTION
    # Demonstrate the use of isInstance() to check if my_ev is an instance of Car and ElectricCar.

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
    

my_ev = ElectricCar("Tata", "Punch", "65kWh")

print(isinstance(my_ev, Car))
print(isinstance(my_ev, ElectricCar))
