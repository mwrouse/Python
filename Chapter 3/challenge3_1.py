"""
    Program: challenge3_1.py
    Author: Michael Rouse
    Date: 9/9/13
    Description: Simulates a fortune cookie, generates 1 of 5 fortunes each time it runs.
"""
import random

# Calculates a number between 1 and 5 and sets it the variable
number = random.randint(1, 5)

print("Welcome, your fortune is: \n")

if number == 1:
    print("\"Welcome\" is a powerful word.")
elif number == 2:
    print("A dubious friend may be an enemy in camouflage.")
elif number == 3:
    print("A golden egg of opportunity falls into your lap this month.")
elif number == 4:
    print("A light heart carries you through all the hard times.")
else:
    print("A truly rich life contains love and art in abundance.")

print("\n\nDone...")
