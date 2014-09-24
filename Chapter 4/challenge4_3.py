"""
    Program: challenge4_3.py
    Author: Michael Rouse
    Date: 9/24/13
    Description: Improvement of the word jumble program. Adds hint, and a scoring system.
"""
# Word Jumble 2.0
#
# The computer picks a random word, jumbles it, user needs to guess the word.
# If user can guess the word without using a hint they get 2 points, if they use a hint they get 1 point

import random

#sequence of words the program can choose from:
words = ("phython", "jumble", "easy", "difficult", "answer", "xylophone")

#sequence of hints for the respective words in the sequence  above:
hints = ("The language this program was written in.", "This program does this to words.", "Not difficult.", 
         "Not easy.", "", "Musical instrument.")

playAgain = "y"

score = 0

#main game loop
while playAgain == "y":
    
    #reset the variable used to tell if a user used a hint
    userHint = 0
    
    #picks a number to find the hint and word:
    wordNumber = random.randint(0, 5)

    word = words[wordNumber]
    hint = hints[wordNumber]

    #used to tell if the user input was correct
    correct = word


    #create a jumbled version of the selected word
    jumble = ""
    while word: 
        position = random.randrange(len(word))
        jumble += word[position]    #adds the random letter to the jumbled word
        word = word[:position] + word[(position + 1):]  #used to remove the chosen letter

    # show game header only once; otherwise show the score.
    if score == 0: 
        print(
        """
                         Welcome to Word Jumble 2.0!
                
                   Unscramble the letters to make a word.
               (Press Enter with a blank guess to get a hint)
        """
        )
    else:
        print("Score:", score)
            
    print("The jumbled word is:", jumble)

    guess = input("\nYour Guess: ")

    while guess != correct:
        if guess == "":
            print("\nYour hint is:", hint)
            guess = input("New guess: ")
            userHint = 1
        else:
            print("Sorry, that's not it.")
            guess = input("Your guess: ")


    if guess == correct:
        print("That's it!  You guessed it!\n")

        # this if statement adds 1 point if the user used a hint, otherwise it adds 2 points
        if userHint == 1: #hint was used
            score += 1
        else: #no hint used
            score += 2

    #ask the user if they want to play anohter round
    playAgain = input("\nDo you wish to play again (y/n)? ")
    print("\n")
