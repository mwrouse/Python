"""
    Program......: game.py
    Author.......: Michael Rouse
    Date.........: 3/19/14
    Description..: Game module for dd61
"""
from livewires import games, color
from player import *
from monster import *
from random import randint

# Create the window and frame
games.init(screen_width=640, screen_height=480, fps=50)

class Game(games.Sprite):
    """ class for the game """
    def __init__(self, classType):
        super(Game, self).__init__(image=games.load_image("sprites\game.png"), x=0, y=0)
        
        # Create the correct class Type
        if classType == 1:
            self.player = Knight()
        elif classType == 2:
            self.player = Cleric()
        elif classType == 3:
            self.player = Thief()

        # Create the enemy
        enemy = randint(1, 3)
        
        if enemy == 1:
            self.enemy = Red_Dragon()
        elif enemy == 2:
            self.enemy = White_Dragon()
        elif enemy == 3:
            self.enemy = Goblin()

        # Add the player and the enemy to the screen
        games.screen.add(self.enemy)
        games.screen.add(self.player)
        
        # Labels and Variables to show controls
        self.controlsOnScreen = False
        self.controlsCounter = 0
        
        self.lblControls_Attack = games.Text(value="a - Attack", size=40, x=100, y=30, color=color.white)
        self.lblControls_Special = games.Text(value="s - Special Ability", size=40, x=155, y=70, color=color.white)
        self.lblControls_Help = games.Text(value="F1 - Help", size=40, x=95, y=110, color=color.white)
        self.lblControls_Exit = games.Text(value="Esc - Exit", size=40, x=100, y=150, color=color.white)
        
    def update(self):
        # F1 - Display controls
        if games.keyboard.is_pressed(games.K_F1) and self.controlsOnScreen == False:
            # Display controls on the screen
            games.screen.add(self.lblControls_Attack)
            games.screen.add(self.lblControls_Special)
            games.screen.add(self.lblControls_Help)
            games.screen.add(self.lblControls_Exit)

            self.controlsOnScreen = True

        # A - Attack
        if games.keyboard.is_pressed(games.K_a):
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)

        # S - Player Special
        if games.keyboard.is_pressed(games.K_s):
            self.player.special(self.enemy)
            self.enemy.attack(self.player)
    
    def tick(self):
        if self.controlsOnScreen:
            self.controlsCounter += 1

            if self.controlsCounter >= 250:
                self.controlsCounter = 0
                self.controlsOnScreen = False
                
                # Remove the controls labels
                games.screen.remove(self.lblControls_Attack)
                games.screen.remove(self.lblControls_Special)
                games.screen.remove(self.lblControls_Help)
                games.screen.remove(self.lblControls_Exit)
        
def play(classType):
    
    # Create and set the background image
    games.screen.background = games.load_image("dd61_background.jpg", transparent=False)
    
    mainGame = Game(classType)
    games.screen.add(mainGame)
    #games.screen.add(mainGame.player)
    #games.screen.add(mainGame.enemy)
    
    games.screen.mainloop()


# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")

