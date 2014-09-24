"""
    Program......: dd52.py
    Author.......: Michael Rouse
    Date.........: 2/24/14
    Description..: Add a class called Celric to dd51.py
"""
from random import randint
from monster import Monster
from monster import Red_Dragon
from monster import White_Dragon
from monster import Goblin

# Player
class Player(object):
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

    # Increase health
    def get_health(self,increase):
        self.__health += increase

# Celric Class
class Celric(Player):
    # Heal the Celric
    def heal(self):
        self.get_health(randint(1, 8))

        print(self)
        
        

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
        last = 2 # Who goes first

        while fighting:
            if last == 1:                
                opponent2.attack(opponent1)
                last = 2
            else:
                opponent1.attack(opponent2)
                last = 1

            # Check for deaths
            if opponent1.health <= 0:
                # Opponent 1 has died
                print("\n" + opponent1.name + " fought a noble battle but suffered defeat.\n")
                print("\nBetter luck next time...")
                fighting = False
                
            elif opponent2.health <= 0:
                # Opponent2 has died
                print("\n" + opponent2.name + " fought a noble battle but suffered defeat.\n")
                fighting = False

            else:
                # No players have died, ask questions before next round
                if last == 2:
                    # Print current stats for each opponent
                    print(opponent1)
                    print(opponent2)
                    
                    # Figure out if the player wants to heal and continue fighting
                    notValid = True
                    while notValid:
                        # Ask player to heal
                        userInp = input("\nWould you like to heal? (y/n) ")
                        if userInp.lower() in ("y", "yes", "n", "no"):

                            # Decide if the player wants to heal
                            if userInp.lower() == "y" or userInp.lower() == "yes":
                                opponent1.heal() # Heal the player

                            # Ask if the player wants to continue fighting
                            userInp = input("Would you like to continue fighting? (y/n) ")
        
                            if userInp.lower() in ("y", "yes", "n", "no"):
                                
                                # Stop fighting if the player picked no
                                if userInp.lower() in ("n", "no"):
                                    fighting = False
                                
                                notValid = False
                        else:
                            notValid = True
                        
            

# Main
def main():
    # Create a Celric and a hero
    player = Celric("Player")
    dragon = Red_Dragon("Red Dragon")
    
    # Print starting stats
    print(player)
    print(dragon)

    print("\n" + dragon.name + " wishes to fight with you!\n")
    
    # Ask user to run or fight
    if ask("Would you like to fight? (y/n) "):
        # Player wishes to fight
        fightToTheDeath(player, dragon)
        
    else:
        # Hero ran from the fight
        print("Better luck next time...")
    
    


main()
input("Press the Enter key to exit...")
