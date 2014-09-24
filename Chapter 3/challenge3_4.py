"""
    Program: challenge3_4.py
    Author: Michael Rouse
    Date: 9/9/13
    Description: Gets the user to think of a number between 1 and 100 and the computer has to guess
"""
import random

print("\tWelcome to the Random Number Guessing game!")
print("Pick a number between 1 and 100 and I will try to guess it within 10 tries!\n")

# gets user to input number between 1 and 100
theNumber = int(input("What is your random number between 1 and 100? "))

# makes sure the the user number is between 1 and 100
while theNumber > 100 or theNumber < 1:
    print("\nInvalid number! Please make sure it is between 1 and 100!")
    theNumber = int(input("What is your random number between 1 and 100? "))

guess = random.randint(1, 100)
attempts = 1

highest = 100
lowest = 1

# tries to guess within 10 tries
while guess != theNumber and attempts <= 10:
    if guess < theNumber:
        lowest = guess #sets the lowest number to the guess
        print("\nGuess of", guess, "is too low...")
        guess = random.randint(lowest, highest)
    else:
        highest = guess
        print("\nGuess of", guess, "is too high...")
        guess = random.randint(lowest, highest)

    attempts += 1


print("\nGuess correct! Your number is:", guess)

print("\n\nPress the enter key to exit...")

    
