"""
    Program: challenge8_1.py
    Author: Michael Rouse
    Date: 12/12/13
    Description: Modify the Critter caratker program to allow the user to control
                how much they feed the critter and how long the play with the critter.
"""

from challenge8_1class import *

# Main function
def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            food = input("How much food do you want to feed your critter (0-100)? ")
            try:
                # Check to see if they input a number
                food = int(food)

            except:
                food = 4 # Not a number, choose default

            else:
                # Check to make sure food is within 0-100
                if food not in range(0, 101):
                    food = 4   # Not within 0-100, choose default

            crit.eat(food)
         
        # play with your critter
        elif choice == "3":
            fun = input("How much do you want to play with your critter (0-100)? ")

            try:
                # Check to see if they input a number
                fun = int(fun)

            except:
                fun = 4 # Not a number, choose default

            else:
                # Check to see if fun is within 0-100
                if fun not in range(0, 101):
                    fun = 4 # Not within 0-100, choose default

            crit.play(fun)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
