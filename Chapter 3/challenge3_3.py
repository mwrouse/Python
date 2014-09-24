"""
    Program: challenge3_3.py
    Author: Michael Rouse
    Date: 9/9/13
    Description: Guess My Number game but the user only has a limited number of guesses
"""
import random

print("\tWelcome to the Guess My Number game!")
print("\nI am thinking of a number between 1 and 100.")
print("Try and guess the number within 10 guesses.\n")

# initialize values
theNumber = random.randint(1, 100)
guess = int(input("What's your guess? "))
attempts = 1

while guess != theNumber and attempts <= 10:
    if guess > theNumber:
        print("Guess is too high...")
    else:
        print("Guess is too low...")

    guess = int(input("What's your guess? "))
    attempts += 1

print("Congratulations! The number was", theNumber)
print("\nIt took you", attempts, "tries!")

input("\n\nPress the enter key to exit...")
    
