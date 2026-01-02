class Vehicle:
    def __init__(self, model, rate):
        self.model = model
        self.rate = rate

    def rent(self, days):
        print("Rental not defined")


class Car(Vehicle):
    def rent(self, days):
        print(self.model, "Rent:", self.rate * days)


class Bike(Vehicle):
    def rent(self, days):
        print(self.model, "Rent:", self.rate * days)


class Truck(Vehicle):
    def rent(self, days):
        print(self.model, "Rent:", (self.rate * days) + 500)


# Example
c = Car("Honda", 1000)
b = Bike("Yamaha", 300)
t = Truck("Tata", 2000)

c.rent(2)
b.rent(2)
t.rent(2)