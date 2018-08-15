#This code program is created to calculate the area of the sector
print('This calculator helps you calculate the area of the sector')
Titha = float(input('Enter the angle of the circle: '))
radius = float(input('Enter the radius: '))
from math import exp, pi
Area = (Titha / 360) * (pi * radius ** 2)
print('Area =',(round(Area,2)))
