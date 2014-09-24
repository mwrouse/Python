"""
    Program......: dd59.py
    Author.......: Michael Rouse
    Date.........: 3/13/14
    Description..: Create a game frame with a hero and monster
"""
from livewires import games, color
from dd59_player import *
from dd59_monster import *

# Create the window and frame
games.init(screen_width=640, screen_height=480, fps=50)

class Dragon(games.Sprite, Red_Dragon):
    """ Dragon Class """
    image = games.load_image("dd59_dragon.gif")

    def __init__(self):
        # Initialize the sprite
        super(Dragon, self).__init__(image=Dragon.image, x=450, y=250, dx=0, dy=1)

        # Also create a red dragon object for this class
        Red_Dragon.__init__(self, "Red Dragon")

    # Update method to move the dragon
    def update(self):
        if self.y > 270:
            self.dy = -1
        elif self.y < 230:
            self.dy = 1

class Player(games.Sprite, Knight):
    """ Player Class """
    image = games.load_image("dd59_knight.png")

    def __init__(self):
        # Initialize the sprite
        super(Player, self).__init__(image=Player.image, x=150, y=350, dx=0, dy=0)

        # Also create the Knight object for this class
        Knight.__init__(self, "Knight")
        
def main(): 
    # Create and set the background image
    games.screen.background = games.load_image("dd59_background.jpg", transparent=False)

    # Create the Knight Object
    knight = Player()
    
    games.screen.add(knight)
        
    # Create the Dragon  object
    dragon = Dragon() 
        
    games.screen.add(dragon)

    # Create Labels
    knightLabel = games.Text(value="Health: " + str(knight.health), size=40, x=150, y=200, color=color.white)
    games.screen.add(knightLabel)
    
    dragonLabel = games.Text(value="Health: " + str(dragon.health), size=40, x=450, y=100, color=color.white)   
    games.screen.add(dragonLabel)

    games.screen.mainloop()



main()



