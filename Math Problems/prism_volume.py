"""
    Program: prism_volume.py
    Author: Michael Rouse
    Date: 9/3/13
    Description: calculates volume of a prism
"""
print("Prism Volume Problem")

prismLength = int(input("What is the length? "))
prismHeight = int(input("What is the height? "))
prismWidth = int(input("What is the width? "))

# Calculates the base
prismBase = prismWidth * prismLength

# Calculates the volume V = B * H
prismVolume = prismBase * prismHeight

print("The volume of a prism with length", prismLength, ", width", prismWidth,\
      ", height", prismHeight, "is", prismVolume, ".")

print("\n\n\nDone...")
