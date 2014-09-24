"""
Program......: challenge9_2.py
Author.......: Michael Rouse
Date.........: 2/21/14
Description..: Create a single card version of the game War
"""
import random

class Player(object):
    """ A player for a game. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, name):
        self.name = name
        self.card = None
        self.suit = None

    def __str__(self):
        rep = self.name + ": " + str(self.card) + str(self.suit)
        return rep

    # Give the player a random card
    def give_card(self):
        # Pick a random card
        self.card = self.RANKS[random.randrange(12)]
        self.suit = self.SUITS[random.randrange(3)]

    # Return the player's card rank
    @property
    def card_rank(self):
        rank = 0
        for i in range(12):
            if self.RANKS[i] == self.card:
                rank += i + 1

        for i in range(3):
            if self.SUITS[i] == self.suit:
                rank += i + 1

        return rank
        
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    notValid = True
    while notValid:
        number = input(question)

        try:
            number = int(number)
            if number in range(low, high):
                notValid = False
        except:
            notValid = True

    return number

def main():
    print("\t\tWelcome to War!\n")

    players = [] # List of players
    
    numOfPlayers = ask_number("How many players? (2-7): ", 2, 7)

    for player in range(numOfPlayers):
        name = input("Player Name: ")
        player = Player(name)
        players.append(player) # Add to list of players

    again = None
    while again != "n":
        # Deal out a card to each player
        for player in players:
            player.give_card()
            
            print(player) # Display the player's name, card, and rank

        # Determine the winner
        winner = players[0]

        for player in players:
            if player.card_rank > winner.card_rank:
                winner = player

        # Display the winner        
        print("\nThe winner is: " + winner.name)

        # Ask if the user wants to play again
        again = ask_yes_no("Play again (y/n)? ")

    
        



main()
input("\n\nPress the Enter key to exit.")
