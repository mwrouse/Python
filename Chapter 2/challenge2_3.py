"""
    Program: challenge2_3.py
    Author: Michael Rouse
    Date: 8/29/13
    Description: Program that calulates a 15% and a 20% tip
"""

billTotal = float(input("What is the total bill amount? "))


tip15 = billTotal * .15
tip20 = billTotal * .20

print("\nA 15% tip would be: ", tip15)
print("\nA 20% tip would be: ", tip20)

print("\n\n\nDone...")
