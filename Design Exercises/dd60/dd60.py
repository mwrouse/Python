"""
    Program......: dd60.py
    Author.......: Michael Rouse
    Date.........: 3/17/14
    Description..: Create an additional frame for dd59.py, this one being a main menu
"""
import dd60_menu # Import the main menu module





def main():
    # Show the main_menu and get what type of class the player wants to be
    classType = int(dd60_menu.main_menu())

    # Import the game module and start playing
    import dd60_game
    dd60_game.play(classType)
    
classType = 0
main()


