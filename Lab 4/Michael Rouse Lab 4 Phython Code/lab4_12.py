"""
    Program: lab4_12.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Gets two numbers from the user and tells how many are even
"""
print("Input two numbers and I will tell you how many are even!\n\n\n")

first = int(input("First number: "))
second = int(input("Second number: "))

even = 0

if first % 2 == 0:
    even += 1

if second % 2 == 0:
    even += 1

if even == 2:
    print("\nBoth are even.")
    
elif even == 1:
    print("\nOne is even.")
    
else:
    print("\nNone are even.")


print("\n\nDone...")
