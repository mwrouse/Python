"""
    Program: circle_diameter.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: Finds the diameter of a circle
"""
print("Circle Diameter Problem")

circleRadius = int(input("What is the radius? "))

# Calculates the diameter D = r + r
circleDiameter = circleRadius + circleRadius

print("The diameter of a circle with radius", circleRadius, \
      "is", circleDiameter)

print("\n\n\nDone...")
