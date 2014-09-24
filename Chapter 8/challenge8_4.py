"""
    Program: challenge8_4.py
    Author: Michael Rouse
    Date: 12/12/13
    Description: Turn the Critter Caretaker program into a Critter Farm
"""

from challenge8_4class import *
from random import randint

def main():
    # Create the Critter Farm with predecided names
    farm = []

    for name in ("Bobby", "Joe", "Susan", "Patty", "Alfred"):
        hunger = randint(0, 10)  # Generate a random hunger level for each critter
        boredom = randint(0, 10) # Generate a random boredom level for each critter

        # Add Critter to the farm list
        farm += [Critter(name, hunger, boredom)]

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Farm Caretaker
    
        0 - Quit
        1 - Listen to your critters
        2 - Feed your critters
        3 - Play with your critters
        """)
    
        choice = input("Choice: ")
        print()

        # Exit
        if choice == "0":
            print("Good-bye.")

        # Listen to your critter
        elif choice == "1":
            # Talk to each critter
            for critter in farm:
                critter.talk()
        
        # Feed your critter
        elif choice == "2":
            # Feed each critter
            for critter in farm:
                critter.eat()
         
        # Play with your critter
        elif choice == "3":
            # Play with each critter
            for critter in farm:
                critter.play()

        # Some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
