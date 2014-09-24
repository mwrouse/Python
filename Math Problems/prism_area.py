"""
    Program: prism_area.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: Calculates area of a prism
"""
print("Prism Area Problem")

length = int(input("What is the length? "))
height = int(input("What is the height? "))
width = int(input("What is the width? "))

# Calculates the surface area A = 2 & (wh + lw + lh)
area = 2 * ((width * height) + (length * width) + (length * height))

print("The area of a prism with length", length, ", width", width,\
      ", height", height, "is", area, ".")

print("\n\n\nDone...")
