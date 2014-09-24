"""
    Program......: dd53.py
    Author.......: Michael Rouse
    Date.........: 2/26/14
    Description..: 
"""
from random import randint
from dd53_monster import *
from dd53_player import *

# FUNCTION ====================================
# Name.........: fight
# Description..: Class for two characters fighting
# Syntax.......: fight(opponent1, opponent2)
# =============================================
def fight(opponent1, opponent2):
    # Fight loop
    choice = None
    while choice != 0:
        # Display stats
        print(opponent1)
        print(opponent2)

        choice = None
        while choice not in (0, 1, 2):
            print("""
What would you like to do?
    1. Fight
    2. Use Special
    0. Run""")
            
            try:
                choice = int(input("Choice>"))
            except:
                choice = None

        # Do something based on player's choice
        if choice == 0:
            # Stop the loop
            choice = 0
            print("\nYou ran.\nBetter luck next time...")
            
        elif choice == 1:
            # Fight
            opponent1.attack(opponent2)
            opponent2.attack(opponent1)
            
        elif choice == 2:
            # Use player special
            if opponent1.type == "Knight":
                opponent1.special(opponent2)
            else:
                opponent1.special()

        # Check if anyone is dead
        if opponent1.health <= 0:
            # Opponent one has been defeated
            choice = 0
            print("\n\nYou have been defeated by " + opponent2.name + ".")

        elif opponent2.health <= 0:
            # Opponent2 has been defeated
            choice = 0
            print("\n\nYou have defeated " + opponent2.name + ".")
            
    
# FUNCTION ====================================
# Name.........: main
# Description..: Main function for the program
# Syntax.......: main()
# =============================================
def main():
    player = None
    # Display the menu
    print("""
Choose a Character Class:
    1. Celric
    2. Knight
    3. Thief
    0. Exit""")

    # Loop until the user gives a valid choice
    choice = None
    while choice not in (0, 1, 2, 3):
        try:
            choice = int(input("choice> "))
        except:
            choice = None
            
    # Create the desired type of player
    if choice == 0:
        quit
    elif choice == 1:
        # Create a Celric player
        player = Celric("Player",classType="Celric")

    elif choice == 2:
        # Create a Knight player
        player = Knight("Player",classType="Knight")

    elif choice == 3:
        # Create a Thief player
        player = Thief("Player",classType="Thief")

    # Continue if not exit
    if player and choice != 0:   
        # Choose a monster at random
        enemy = randint(1, 3)
        if enemy == 1:
            # Spawn a Red Dragon
            enemy = Red_Dragon("Red Dragon")
           
        elif enemy == 2:
            # Spawn a White Dragon
            enemy = White_Dragon("White Dragon")

        elif enemy == 3:
            # Spawn a Goblin
            enemy = Goblin("Goblin")
            
        # Go to fight loop
        fight(player, enemy)
       
    

# Main
main()
