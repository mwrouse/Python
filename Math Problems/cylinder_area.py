"""
    Program: cylinder_area.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: Calculates the area of a cylinder
"""
print("Cylinder Area Problem")

radius = int(input("What is the radius? "))
height = int(input("What is the height? "))

# Calculates the area A = 2 * Pi * r^2 + 2 * Pi * r * h
area = (2 * 3.14 * (radius * radius)) + (2 * 3.14 * radius * height)

print("The area of a cylinder with the radius", radius, \
      "and the height", height, "is", area)

print("\n\n\nDone...")
