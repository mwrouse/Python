"""
    Program......: dice.py
    Author.......: Michael Rouse
    Date.........: 4/4/14
    Description..: Contains the dice function to simulate a dice roll
"""
from random import randint

def roll(sides=6):
    value = 0

    # Roll until a valid value
    while value not in range(1, sides):
        value = randint(1, sides)

    return value
    
