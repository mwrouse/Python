"""
    Program: circle_perimeter.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: Calculates the perimeter of a circle
"""
print("Circle Perimeter Problem")

circleRadius = int(input("What is the radius of the circle? "))

# Calculates the perimeter P = Pi * d
circlePerimeter = 3.14 * (circleRadius + circleRadius)

print("The perimeter of a circle with a radius of", circleRadius, \
      "is:", circlePerimeter)

print("\n\n\nDone...")
