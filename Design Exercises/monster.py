"""
    Program......: monster.py
    Author.......: Michael Rouse
    Description..: monster class for dd52.py
"""
from random import randint


# Monster
class Monster(object):
    # Monster initializer
    def __init__(self,name,minHP=3,maxHP=13):
        self.__name = name
        self.__status = "Alive"
        self.__health = randint(minHP, maxHP)

    # Print the status of the Monster
    def __str__(self):
        statusInfo = "\n  Name: " + self.__name.title() + "\nStatus: " + self.__status.title() + \
        "\n    HP: " + str(self.__health)
        
        return statusInfo

    # Attack an enemy
    def attack(self,enemy,minDamage=1,maxDamage=6):
        # Random amount of damage points (1-6)
        damage = randint(minDamage, maxDamage)
        
        enemy.get_hurt(damage) # Do damage to the enemy
        
        # Print information on the attack
        print("\n" + self.__name.title() + " does " + str(damage) + " damage to " + enemy.name)

    # Get the Monsters name
    @property
    def name(self):
        return self.__name.title()
    
    # Get the Monsters health
    @property
    def health(self):
        return self.__health
    
    # Inflict damage to Monster
    def get_hurt(self,damage):
        self.__health -= damage

        if self.__health < 1:
            self.__health = 0
            self.__status = "dead"

# Red Dragon
class Red_Dragon(Monster):
    # Initializer
    def __init__(self, name):
        # Call the initializer of Monster
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

# Goblin
class Goblin(Monster):
    # Initialize
    def __init__(self, name, minHP=1,maxHP=8):
        super(Goblin, self).__init__(name,minHP,maxHP)

    # Goblin attack
    def attack(self, enemy):
        if randint(1, 2) == 1:
            # Use regular attack
            super(Goblin, self).attack(enemy, 1, 6)
        else:
            # Use scream attack
            self.scream_attack(enemy)
        
    # Scream Attack
    def scream_attack(self, enemy):
        print("\n" + self.name + " does 3 damage to " + enemy.name + " using scream attack")
        enemy.get_hurt(3)
