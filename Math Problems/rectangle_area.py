"""
    Program: rectangle_area.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: Calculates area of rectangle
"""

print("Rectangle Area Problem")

rectangleLength = int(input("What is the length of the rectangle? "))
rectangleWidth = int(input("What is the width of the rectangle? "))

# Calculates the area
rectangleArea = rectangleLength * rectangleWidth

print("The area of the rectangle with a length of", rectangleLength, \
      "and a width of", rectangleWidth, "is:", rectangleArea)

print("\n\n\nDone...")
