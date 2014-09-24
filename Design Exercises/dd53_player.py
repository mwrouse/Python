"""
    Program......: dd53_player.py
    Author.......: Michael Rouse
    Date.........: 2/26/14
    Description..: Module for player class in dd53
"""
from random import randint

# CLASS ====================================
# Name.........: Player
# Description..: Class for any player
# Syntax.......: Player(name[, minimum HP[, maximum HP]])
# ==========================================
class Player(object):
    # Combatant initializer
    def __init__(self,name,minHP=3,maxHP=13,classType="Player"):
        self.name = name.title()
        self.status = "Alive"
        self.health = randint(3, 13)
        self.money = 0
        self.type = classType

    # Print the status of the combatant
    def __str__(self):
        statusInfo = "\n  Name: " + self.name + "\nStatus: " + self.status + \
        "\n    HP: " + str(self.health) + "\n  Gold: " + str(self.money)
        
        return statusInfo

    # Attack an enemy
    def attack(self,enemy,minDamage=1,maxDamage=6):
        # Random amount of damage points (1-6)
        damage = randint(minDamage, maxDamage)
        
        enemy.get_hurt(damage) # Do damage to the enemy
        
        # Print information on the attack
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name)
    
    # Inflict damage to combatant
    def get_hurt(self,damage):
        self.health -= damage

        if self.health < 1:
            self.health = 0
            self.status = "dead"

# CLASS ====================================
# Name.........: Celric
# Description..: Class for any celric (Player is the derived class)
# Syntax.......: Celric(name[, minimum HP[, maximum HP]])
# ==========================================
class Celric(Player):
    
    # Heal the Celric
    def special(self):
        heal = (randint(1, 8))
        self.health += (randint(1, 8))
        print("\n" + self.name + " heals himself by " + str(heal) + " health points.")

        print(self)

# CLASS ====================================
# Name.........: Knight
# Description..: Class for a knight
# Syntax.......: Knight(name[, minimum HP[, maximum HP]])
# ==========================================
class Knight(Player):
    # Knight's Smite attack
    def special(self, enemy):
        damage = randint(12, 20)
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using Smite.")
        enemy.get_hurt(damage)

# CLASS ====================================
# Name.........: Thief
# Description..: Class for a thief
# Syntax.......: Thief(name[, minimum HP[, maximum HP]])
# ==========================================
class Thief(Player):
    # Thief's Steal
    def special(self):
        stolen = randint(1, 10)
        self.money += stolen
        print("\n" + self.name + " steals " + str(stolen) + " gold pieces.")


# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")

