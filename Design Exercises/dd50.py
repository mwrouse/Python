"""
    Program......: dd50.py
    Author.......: Michael Rouse
    Date.........: 2/20/14
    Description..: Add a class called white dragon and add it to dd49
"""
from random import randint

# Combatant
class Combatant(object):
    # Combatant initializer
    def __init__(self,name,minHP=3,maxHP=12):
        self.__name = name
        self.__status = "Alive"
        self.__health = randint(minHP, maxHP)

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

# Red Dragon
class Red_Dragon(Combatant):
    # Initializer
    def __init__(self, name):
        # Call the initializer of Combatant
        super(Red_Dragon, self).__init__(name)
        
    # Breathe fire
    def breath_attack(self, enemy):
        # Random damage (6-12 points)
        damage = randint(6, 12)
        enemy.get_hurt(damage)
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using fire breath")

# White Dragon
class White_Dragon(Red_Dragon):
    # Breathe ice
    def breath_attack(self, enemy):
        # Random damage (2-8 points)
        damage = randint(2, 8)
        enemy.get_hurt(damage)
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using ice breath")
    
# Main
def main():
    # Create a hero and dragon
    hero = Combatant("Hero")
    if randint(1, 2) == 1:
        # Generate a Red Dragon
        dragon = Red_Dragon("Red Dragon")
    else:
        # Generate a White Dragon
        dragon = White_Dragon("White Dragon")

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
