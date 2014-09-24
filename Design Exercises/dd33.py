# Name: dd32.py
# Date: 12/13/2013
# Author: Thorin Schmidt

from Weapon import *

print("Welcome to the Weapon Module Tester!")
print("First, I'm going to make a weapon,")
print("with parameter values 'slash', 2, 8, 0, 'axe'.")
print("Let's see what happens!")

input("\nPress a key to see the fun!")

weapon1 = Weapon(weaponType = 'Slash', numDice = 2, diceSides = 8, 
                 modifier = 0, name = 'Axe')

print("\nFirst, the stats:")
print("\tThe", weapon1.get_name(),"is a",weapon1.get_weaponType(), 
      "weapon, and does", weapon1.get_numDice(), "d", 
      weapon1.get_diceSides(), "+", weapon1.get_modifier(), "damage.")

input("\nPress a key to continue")

print("\nNow to try out the damage property:")
print("\t", weapon1.damage)

input("\nPress a key to continue")

print("\nNow, let's test those set methods....")
print("I will attempt to change the weapon's attributes:")
weapon1.set_name("War Club")
weapon1.set_weaponType("Blunt")
weapon1.set_numDice(3)
weapon1.set_diceSides(6)
weapon1.set_modifier(2)
print("The weapon should now be a War Club which is a blunt type,")
print(" and does 3 d 6 + 2 damage")

input("Press enter to see how we did")

print("\tThe", weapon1.get_name(),"is a",weapon1.get_weaponType(), 
      "weapon, and does", weapon1.get_numDice(), "d", weapon1.get_diceSides(),
      "+", weapon1.get_modifier(), "damage.")

print("\nCongratulations!")
input("\nPress enter to exit...")


