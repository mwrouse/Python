"""
    Program: cylinder_volume.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: caclulates the volume of a cylinder
"""
print("Cylinder Volume Problem")

radius = int(input("What is the radius? "))
height = int(input("What is the height? "))

# Calculates volume V = Pi * r^2 * h
volume = 3.14 * (radius * radius) * height

print("The volume of a cylinder with the radius", radius, \
      "and the height", height, "is", volume)

print("\n\n\nDone...")
