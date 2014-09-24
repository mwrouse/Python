"""
    Program......: dd51.py
    Author.......: Michael Rouse
    Date.........: 2/24/14
    Description..: Add a class called Goblin to dd50
"""
from random import randint

# Combatant
class Combatant(object):
    # Combatant initializer
    def __init__(self,name,minHP=3,maxHP=13):
        self.__name = name
        self.__status = "Alive"
        self.__health = randint(minHP, maxHP)

    # Print the status of the combatant
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

    # Get the combatants name
    @property
    def name(self):
        return self.__name.title()
    
    # Get the combatants health
    @property
    def health(self):
        return self.__health
    
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

# Goblin
class Goblin(Combatant):
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
        

# Ask yes or no question (Returns true if answered with yes and false if no)def ask(question):
def ask(question):
    notValid = True
    answer = None
    
    while notValid:
        userInput = input("\n" + question)
        if userInput.lower() == "yes" or userInput.lower() == "y":
            notValid = False
            answer = True
        elif userInput.lower() == "no" or userInput.lower() == "n":
            notValid = False
            answer = False
        
    return answer
        

# Have two objects fight
def fightToTheDeath(opponent1, opponent2):
    if opponent1.health > 0 and opponent2.health > 0:
        fighting = True
        last = randint(1, 2) # Who goes first

        while fighting:
            if last == 1:                
                opponent2.attack(opponent1)
                last = 2
            else:
                opponent1.attack(opponent2)
                last = 1

            if opponent1.health <= 0:
                print("\n" + opponent1.name + " fought a noble battle but suffered defeat.\n")
                fighting = False
            elif opponent2.health <= 0:
                print("\n" + opponent2.name + " fought a noble battle but suffered defeat.\n")
                fighting = False       

# Main
def main():
    # Create a hero and a goblin
    hero = Combatant("Hero",minHP=3,maxHP=12)
    goblin = Goblin("Goblin",minHP=1,maxHP=8)
    
    # Print starting stats
    print(hero)
    print(goblin)

    # Ask user to run or fight
    if ask("Would you like to fight? (y/n) "):
        # Hero and goblin fight to the death
        print()
        fightToTheDeath(hero, goblin)
    else:
        # Hero ran from the fight
        print("Better luck next time...")
    
    


main()
input("Press the Enter key to exit...")
