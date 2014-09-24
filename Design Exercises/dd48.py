"""
    Program......: dd48.py
    Author.......: Michael Rouse
    Date.........: 2/19/14
    Description..: Create a class called combatant give it attributes and what not...
"""
from random import randint

# Combatant class
class combatant():
    # Combatant initializer
    def __init__(self,name):
        self.__name = name
        self.__status = "alive"
        self.__health = randint(3, 12)

    # Print the status of the combatant
    def __str__(self):
        statusInfo = "\n  Name: " + self.__name.title() + "\nStatus: " + self.__status.title() + \
        "\n    HP: " + str(self.__health)
        
        return statusInfo

    # Attack an enemy
    def attack(self,enemy):
        # Random amount of damage points (1-6)
        damage = randint(1, 6)
        
        enemy.get_hurt(damage) # Do damage to the enemy
        
        # Print information on the attack
        print("\n" + self.__name.title() + " does " + str(damage) + " damage")

    # Inflict damage to combatant
    def get_hurt(self,damage):
        self.__health -= damage

        if self.__health < 1:
            self.__health = 0
            self.__status = "dead"
        
# Main
def main():
    # Create a hero and monster
    hero = combatant("Hero")
    monster = combatant("Monster")

    # Print starting stats for both
    print(hero)
    print(monster)

    # Attack each other
    hero.attack(monster)
    monster.attack(hero)

    # Print ending stats
    print(hero)
    print(monster)


main()
input("Press the Enter key to exit...")
