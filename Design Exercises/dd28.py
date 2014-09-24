"""
    Program: dd28.py
    Author: Michael Rouse
    Date: 12/5/13
    Description: Create a class called player, give it a methot called "report" and create a player called
                 bobobo-bo
"""

class Player(object):
    """ Class for a player """

    def __init__(player, name, age):
        player.name = name
        player.age = age

    def report(player):
        print("I'm okay... so far")

    def __str__(player):
        return player.name
    


# Main Program
Bo = Player("Bo", 29) # Generate a player called bobobo_bo


print(Bo.name)

print("\n\nPress the Enter key to exit...")
