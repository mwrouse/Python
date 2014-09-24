"""
    Program: dd27.py
    Author: Michael Rouse
    Date: 12/2/13
    Description: Simulates rolling 4 6-sided dice and puts the results in a list, sorts them and modifies them.
"""
from random import randint

def roll_it():
    """ roll 4 6-sided dice, drop lowest and add the rest """
    theDice = []

    # Perform rolls
    for roll in range(4):
        # Generate a random number from 1-6 and append it to theDice[]
        theDice.append(randint(1, 6))

    theDice.sort() # Sort the list from least to greatest
    
    del theDice[0] # Remove item at index 0 (the lowest number)

    # Find the total by adding the remaining items in the list
    total = 0
    for i in range(0, len(theDice)):
        total += theDice[i]

    # Return the total to the main program
    return total


def main():
    """ Main Program """

    print("Rolling a set of four 6-sided dice a total of 6 times\n")
    
    # Empty list of the results of all the rolls
    results = []

    # Roll 6 times
    for roll in range(6):
        results.append(roll_it())

    print("Your results are: ", end="")
    # Display all the results
    for i in range(len(results)):
        print(results[i], end=", ")
        
        
    





# Main
main()
