# POLYMORPHISM
    # Demonstrates polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

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

my_ev = ElectricCar("Tata", "Punch", "65kWh")
print(my_ev.fuel_type())

m3 = Car("BMW", "M3")
print(m3.fuel_type())