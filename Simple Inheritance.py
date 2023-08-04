class Vehicle:
    def _init_(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self):
        self.capacity = 50
    def BusCapacity(self, name, max_speed, mileage, capacity):
        self._init_(name, max_speed, mileage)
        self.seating_capacity(capacity)

o = Bus()
o.BusCapacity( 'Volvo',100,10,50)
print("The seating capacity of a", o.name, "Bus is", o.capacity, "passengers")

o.BusCapacity( 'BharatBenz',100,10,70)
print("The seating capacity of a", o.name, "Bus is", o.capacity, "passengers")