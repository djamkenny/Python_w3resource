#Write a Python program that calculates the area of a circle based on the radius entered by the user.

#Area of a circle is pi r sqrd

#given r by the user and pi is constant 3.14159

from math import pi

#prompt the user for the value of r since we are detailing with decimal it is ideal to use float

radius = float(input('what is the value of r: '))

#function area should compute for the area of the circle

def area(r):
    Area = pi * r**2
    print(Area)

area(radius)
