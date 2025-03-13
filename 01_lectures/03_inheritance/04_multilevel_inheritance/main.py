from project.car import Car
from project.sports_car import SportsCar
from project.vehicle import Vehicle

s = SportsCar()
c = Car()
v = Vehicle()

print(s.race())
print(s.move())
print(s.drive())
print(c.drive())
print(c.move())
print(v.move())
