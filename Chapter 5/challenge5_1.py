"""
    Program: challenge5_1.py
    Author: Michael Rouse
    Date: 10/2/13
    Description: Program that prints a list of wrods in random order.
"""
import random

# List of words for the program to pick from
words = ["Apple", "Cow", "Mop", "Watch", "Dog", "Girl", "Horse", "Computer", "Shark",
         "Mammal", "Zebra", "Human"]

# Tell the user what this program does
print ("""
            Prints A List of Words in Random Order
        """)
print ("\n")

# Main program loop; will run until the list words is empty
while words:
    pickedWord = random.randrange(0, len(words))

    # Grab and remove word from list
    word = words.pop(pickedWord)
    
    print (word)
    
# Have the user hit the enter key to end the program
input("\nPress the Enter key to exit...")
