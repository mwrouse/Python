"""
    Program: challenge6_2.py
    Author:  Michael Rouse
    Date: 10/14/13
    Description: Modifies the guess my number game by using the ask_number function
"""

import random

def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
            response = int(input(question))

    return response


print("""
                  Can You Guess My Number?
            
        I am thinking of a number between 1 and 100.
   Try to guess the number in as few attempts as possible

     """)

# Set initial values for the game
low = 1
high = 100

# the_number is the number the user has to guess
the_number = random.randint(1, 100) 

guess = 0
tries = 1

question = "Take a guess: "

# Main guessing loop
while guess != the_number:

    guess = ask_number(question, low, high)
    
    # Tell the user the guess is too lower
    if guess > the_number:
        print("Lower...\n")
        
    # Tell the user the guess it too high
    elif guess < the_number:
        print("Higher...\n")

    tries += 1

print("\nYou guess it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\nPress the Enter key to exit...")


