# Name: dd28.py
# Date: 12/5/2013
# Author: Thorin Schmidt

#
#
# Michael Rouse dd28a
#
from random import randint
from player import *

# Main
player1 = Player()
damage = player1.hit()
print("Player 1 does", damage, "points")
player1.get_armor("Gold", 40)
player1.get_hit(randint(4,24))

player1.get_weapon("Axe", 25)





