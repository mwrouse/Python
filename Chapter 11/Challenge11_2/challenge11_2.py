"""
    Program......: challenge11_2.py
    Author.......: Michael Rouse
    Date.........: 3/17/14
    Description..: Create a game where the player has to avoid falling objects
"""
from livewires import games, color
import pygame.display

# Initialize the window and frame
games.init(screen_width=640, screen_height=480, fps=50)
games.screen.background = games.load_image("background.png", transparent=False)
pygame.display.set_caption("Superman Defender") # Change the window title

# Import classes for superman and kryptonite
from superman import *
from kryptonite import *


# FUNCTION =================================
# Name.........: Main
# Description..: Function for main game
# Syntax.......: main()
# ==========================================
def main():
    player = Superman()
    games.screen.add(player)

    games.mouse.is_visible = False
    games.mouse.event_grab = True
    
    games.screen.mainloop()


# Start!
main()
