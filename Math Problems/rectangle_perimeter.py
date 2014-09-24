"""
    Program: rectangle_perimeter.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: Calculates the perimeter of a rectangle
"""
print("Rectangle Perimeter Problem\n")

rectangleLength = int(input("What is the length of the rectangle? "))
rectangleWidth = int(input("What is the width of the rectangle? "))

# Calculates perimeter
rectanglePerimeter = (2 * rectangleLength) + (2 * rectangleWidth)

print("The perimeter of a rectangle with a length of", rectangleLength, \
      "and a width of", rectangleWidth, "is:", rectanglePerimeter)

print("\n\n\nDone...")
