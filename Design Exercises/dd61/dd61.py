"""
    Program......: dd61.py
    Author.......: Michael Rouse
    Date.........: 3/19/14
    Description..: 
"""
import main_menu

def main():
    # Display the main menu and have player pick a class type
    classType = int(main_menu.display())
    
    # Start the game
    import game
    game.play(classType)



# Start!
main()
