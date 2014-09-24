"""
    Program: Weapon.py
    Author: Michael Rouse
    Data: 12/17/13
    Description: Create a class called weapon.
"""
from random import randint

class Weapon(object):
    """ Object Class Weapon """
    def __init__(self, name="sword", weaponType="sword", numDice=1, diceSides=3, modifier=0):
        """ Initializer """
        self.__name = name
        self.__weaponType = weaponType
        self.__numDice = numDice
        self.__diceSides = diceSides
        self.__modifier = modifier

    def set_name(self, new_name):
        """ Change the name """
        self.__name = new_name
        
    def get_name(self):
        """ Return the name """
        return self.__name
    
    def set_weaponType(self, new_type):
        """ Change the type """
        self.__weaponType = new_type

    def get_weaponType(self):
        """ Return the type """
        return self.__weaponType
    
    def set_numDice(self, new_dice):
        """ Change the amount of dice """
        self.__numDice = new_dice

    def get_numDice(self):
        """ Return the amount of dice """
        return self.__numDice
    
    def set_diceSides(self, new_sides):
        """ Change the amount of sides on the dice """
        self.__diceSides = new_sides

    def get_diceSides(self):
        """ Return the amount of sides on the dice """
        return self.__diceSides
    
    def set_modifier(self, modifier):
        """ Change the dice modifier """
        self.__modifier = modifier

    def get_modifier(self):
        """ Return the modifier """
        return self.__modifier
    
    @property
    def damage(self):
        """ Roll for damage and return the amount """
        damage_rolled = self.__roll_dmg()

        return damage_rolled
    
    def __roll_dmg(self):
        """ Roll the dice for damage """
        # Initialize the roll_total with the modifer
        roll_total = self.__modifier

        # Loop to roll each dice
        for roll in range(1, (self.__numDice + 1)):
            # Generate random number between 1 and the amount of sides on the dice
            rolled = randint(1, self.__diceSides)

            roll_total += rolled # Add the roll value to the total

        return roll_total
    
