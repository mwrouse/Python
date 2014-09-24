#
#   Program: challenge4_4.py
#   Author: Michael Rouse
#   Date: 9/24/13
#   Description: Computer picks a random word, player has to guess the word. Computer will tell the user how many letters are in the word. Player
#                gets 5 chances to ask if a letter is in a word, then they have to guess the word.
#

import random

print("""
                           Word Guess 5000!
                           
        I will think of a word and you have 5 chances to ask me
        if a letter is in the word. After 5 guesses you have to
        guess the word!
     """)

playAgain = "y"

# sequence of words the computer can guess from
words = ("apple", "banana", "phython", "car", "computer", "hardware", "train")

# start the game
while playAgain == "y":
    word = random.choice(words)

    print("\nThe word has:", len(word), "characters")

    print("\nNow it's time for you to ask me 5 letters, and I will tell you if it's in the word.")

    # this for-loop will execute 4 times, each time the user gets to ask the computer a letter for a totall of 5 times
    for i in range(1, 6): 
        letterGuess = input("Ask me a letter: ")
        if letterGuess in word:
            print("yes")
        else:
            print("no")
        

    print("\nYour 5 questions are up, now it's time to guess the word.")
    guess = input("What's your guess? ")

    while guess != word:
            print("\nIncorrect! Try again!")
            guess = input("What's your guess? ")
    

    if guess == word:
          print("\nCorrect! The word was ", word)
          playAgain = input("Do you want to play again (y/n)? ")
    
    
    

    
    
    

