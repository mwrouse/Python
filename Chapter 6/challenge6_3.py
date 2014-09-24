"""
    Program: challenge6_3.py
    Author: Michael Rouse
    Date: 10/14/13
    Description: Modify the new version of the Guess My Number you created in the last challenge so that
                 the program's code is in a function called main().
"""            

import random

def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
            response = int(input(question))

    return response


def main():
    print("""
                  Can You Guess My Number?
            
        I am thinking of a number between 1 and 100.
   Try to guess the number in as few attempts as possible

     """)
    
    # Set the intital valuse for the game
    low = 1
    high = 100
    step = 1
    
    # the_number is the number the user needs to guess
    the_number = random.randint(low, high)

    # guess is the user's guess
    guess = 0

    # Number of tries
    tries = 1

    question = "Take a guess: "
    
    # Loop for guessing
    while guess != the_number:

        # Get user's guess
        guess = ask_number(question, low, high, step)

        # Tell the user if the guess is too high
        if guess > the_number:
            print("Lower...\n")
            
        # Tell the user if the guess is too low
        elif guess < the_number:
            print("Higher...\n")

        tries += 1

    # User guess was correct
    print("\nYou guess it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")



main()

input("\nPress the Enter key to exit...")


