"""
    Program: die_roller.py
    Author: Michael Rouse
    Date: 11/4/13
    Description: Dice rolling function
"""
import random

def die_roller (sides, modifier=0):
    """ Function to similater dice rolling """
    # Generate random number between 1 and the sides of the dice
    roll = random.randint(1, sides)

    # Add the modifier to the roll
    roll += modifier

    return roll



    
