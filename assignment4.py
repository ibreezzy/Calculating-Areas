#This program is designed to calculate the area of a square
print('This calculator helps you calculate the area of a square')
Length = float(input('What is the length?: '))
Area = Length ** 2
print('Area',(round(Area,2)))

#This program is designed to calculate the area of a trapezoid
print('This calculator helps you calculate the area of a trapezoid')
Base2a = float(input('Enter the value of a: '))
Base2b = float(input('Enter the value of b: '))
Height2 = float(input('Enter the value of h: '))
Area2 = (Base2a + Base2b) / (2) * (Height2)
print('Area =',(round(Area2,2)))

#This program is designed to calculate the area of a cylinder with closed surface
print('This calculator helps you calculate the area of a cylinder with closed surface')
from math import exp, pi
Radius = float(input('Enter the value of radius: '))
Height3 = float(input('Enter the value of Height: '))
Area3 = (2 * pi * Radius * Height3) + (2 * pi * Radius)
print('Area =',(round(Area3,2)))

#This program is designed to calcullate the area of a triangle
print('This calculator helps you calculate the area of a triangle')
Height4 = float(input('Enter the value of height: '))
Base4 = float(input('Enter the value of base: '))
Area4 = (Height4 * Base4) / (2)
print('Area =',(round(Area4,2)))
