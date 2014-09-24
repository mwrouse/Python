"""
    Program: challenge3_4v2.py
    Author: Michael Rouse
    Date: 9/9/13
    Description: Gets the user to think of a number between 1 and 100 and the computer has to guess
"""
import random

print("Think of a number between 1 and 100 and I will try to guess the number!")
input("\nPress enter when you have thought of a number...")

highest = 100
lowest = 1

# takes a guess between lowest and highest(set above)
guess = random.randint(lowest, highest)

correct = False

while not correct:
    answer = input("\n\nIs the guess " + str(guess) + " correct? (y\\n) ")

    if answer == "n":
        #asks if guess is too low
        lowOrHigh = input("Is " + str(guess) + " too low? (y\\n) ")

        if lowOrHigh == "y":
            #guess is too low
            lowest = guess
            guess = random.randint(lowest, highest)
        elif lowOrHigh == "n":
            #guess is too high
            highest = guess
            guess = random.randint(lowest, highest)
        else:
            #user input not y or n
            guess = guess
    elif answer == "y":
        #guess is correct
        correct = True
    else:
        #user input not "y" or "n"
        guess = guess


print("\nThe number is", guess, "! Thank you for play!")

print("\n\nPress the enter key to exit...")
    

