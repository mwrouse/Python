"""
    Program: player.py
    Author:  Michael Rouse
    Date: 12/9/13
    Description: Practice with classes
"""

from player_class import *


# Main
char = Player("Michael", "Worker", "Dwarf")

char.report()
char.get_weapon("Axe", 6)
char.report()
char.get_armor("Chain", 3)
char.report()
