"""
    Program: die_rollerv2.py
    Author: Michael Rouse
    Date: 11/4/13
    Description: Dice rolling function
"""
import random

def die_roller (number=1, sides=6, modifier=0):
    """ Function to similate dice rolling """
    rollTotal = 0
    
    # Loop to roll number of times
    for roll in range(1, (number + 1)):
        # Generate random number between 1 and the sides of the dice
        roll = random.randint(1, sides)

        # Add the modifier to the roll
        rollTotal += roll + modifier

    return rollTotal



print(die_roller(1, 6, 0))

