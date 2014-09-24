"""
    Program......: dd60_game.py
    Author.......: Michael Rouse
    Date.........: 3/17/14
    Description..: Create an additional frame for dd59.py, this one being a main menu
"""
from livewires import games, color
from dd60_player import *
from dd60_monster import *

# Create the window and frame
games.init(screen_width=640, screen_height=480, fps=50)

def play(classType): 
    # Create and set the background image
    games.screen.background = games.load_image("dd60_background.jpg", transparent=False)

    # Create the correct class Type
    if classType == 1:
        player = Knight("knight", image="sprites\knight.png")
    elif classType == 2:
        player = Cleric("Cleric", image="sprites\cleric.png")
    elif classType == 3:
        player = Thief("Thief", image="sprites\thief.png")
    
    games.screen.add(player)
        
    # Create the Dragon  object
    dragon = Red_Dragon("Dragon", image="sprites\dragon.png") 
        
    games.screen.add(dragon)

    # Create Labels
    knightLabel = games.Text(value="Health: " + str(player.health), size=40, x=150, y=200, color=color.white)
    games.screen.add(knightLabel)
    
    dragonLabel = games.Text(value="Health: " + str(dragon.health), size=40, x=450, y=100, color=color.white)   
    games.screen.add(dragonLabel)

    games.screen.mainloop()


# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")

