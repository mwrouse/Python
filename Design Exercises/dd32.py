# Name: dd32.py
# Date: 12/13/2013
# Author: Thorin Schmidt

from Rectangle import *

print("Welcome to the Rectangle Module Tester!")
print("First, I'm going to make two rectangles,")
print("one with no parameters, and the second")
print("with values 6 and 9. Let's see what happens!")

input("\nPress a key to see the fun!")

rectangle1 = Rectangle()
rectangle2 = Rectangle(6,9)

print("\nFirst, the length and width:")
print("\tRectangle 1 length: ", rectangle1.get_length(), "width: ", rectangle1.get_width())
print("\tRectangle 2 length: ", rectangle2.get_length(), "width: ", rectangle2.get_width())

input("\nPress a key to continue")

print("\nNow the perimeters:")
print("\tRectangle 1 Perimeter:", rectangle1.perimeter)
print("\tRectangle 2 Perimeter:", rectangle2.perimeter)

input("\nPress a key to continue")

print("\nNow the areas:")
print("\tRectangle 1 Area:", rectangle1.area)
print("\tRectangle 2 Area:", rectangle2.area)

input("\nPress a key to continue")

print("\nNow, let's test those set methods....")
print("I will attempt to change rectangle 1's")
print("length and width to 3 and 7..")

input("Press a key to continue")
rectangle1.set_length("3")
rectangle1.set_width(7)

print("\tRectangle 1 length: ", rectangle1.get_length(), "width: ", rectangle1.get_width())
print("\tRectangle 1 Perimeter:", rectangle1.perimeter)
print("\tRectangle 1 Area:", rectangle1.area)

print("\nCongratulations!")
input("\nPress a key to exit...")


