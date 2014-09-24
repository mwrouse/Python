"""
    Program......: dd49.py
    Author.......: Michael Rouse
    Date.........: 2/20/14
    Description..: Add a class called dragon to dd48
"""
from random import randint

# Combatant class
class combatant(object):
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
        print("\n" + self.__name.title() + " does " + str(damage) + " damage to " + enemy.name)

    # Ge the combatants name
    @property
    def name(self):
        return self.__name.title()
    
    # Inflict damage to combatant
    def get_hurt(self,damage):
        self.__health -= damage

        if self.__health < 1:
            self.__health = 0
            self.__status = "dead"

# Dragon class that's derived from combatant
class Dragon(combatant):
    # Breath fire attack
    def breath_attack(self, enemy):
        # Random damage (6-12 points)
        damage = randint(6, 12)
        enemy.get_hurt(damage)
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using fire breath")
        
        
    
# Main
def main():
    # Create a hero and dragon
    hero = combatant("Hero")
    dragon = Dragon("Dragon")

    # Print starting stats
    print(hero)
    print(dragon)

    # Attack
    hero.attack(dragon)
    dragon.breath_attack(hero)

    # Print ending stats
    print(hero)
    print(dragon)
    


main()
input("Press the Enter key to exit...")
