class Vehicle:
    def __init__(self, mileage: int, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(20, 120)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
