"""
    Program: triangle_area.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: Calculates area of triangle
"""
print("Triangle Area Problem")

triangleBase = int(input("what is the base length of the triangle? "))
triangleHeight = int(input("What is the height of the triangle? "))

# Calculates area A = (b * h)/2
triangleArea = (triangleBase * triangleHeight) / 2

print("The area of a triangle with a base of", triangleBase, \
      "and a height of", triangleHeight, "is", triangleArea)

print("\n\n\nDone...")
