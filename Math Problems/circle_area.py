"""
    Program: cirlce_area.py
    Author:  Michael Rouse
    Date: 9/3/13
    Description: Calculates the area of a circle
"""
print("Circle Area Program")

circleRadius = int(input("What is the circle's radius? "))

# Calculates the area of the circle A = Pi * r^2
circleArea = 3.14 * (circleRadius * circleRadius)

print("The area of a circle with a radius of:", circleRadius, "is:",\
      circleArea)

print("\n\n\nDone...")
