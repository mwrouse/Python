"""
    Program: challenge8_2.py
    Author: Michael Rouse
    Date: 12/12/13
    Description: Create a program that simulates a television, the user should be
                 able to increase and decrease the volume as well as change the channel.
"""

from challenge8_2class import *

print("""
     ============== TV Simulator ===============
    |            + = Volume Up                  |
    |            - = Volume Down                |
    |        0-100 = Valid channel numbers      |
    |            E = Exit program               |
    |    Enter one of the valid inputs above    |
    |          At the TV prompt (>>)            |
     ===========================================

    """)

TV = Television() # Create TV Object

print(TV)

# Action is used the variable for user input
action = None

while action != "E":
    action = input(">> ")
    action = action.upper()

    # If action is blacnk then set it to a space to avoid error
    if action == "":
        action = " "
        
    if action[0] == "+" or action[0] == "-":
        # Increase or decrease TV volume
        modifier = 0

        # For every "-" sign subtract 1 from modifier; for every "+" sign add one to it
        for i in range(0, len(action)):
            if action[i] == "-":
                modifier -= 1

            elif action[i] == "+":
                modifier += 1

        # Change the volume
        TV.change_volume(modifier)           

    else:
        # User does not want to change the volume; attempt to change the channel
        try:
            # Try to convert action to a number
            action = int(action)

        except:
            # Action is not a number; inform user
            print("Not a valid command, please try again.\n")

        else:
            # Action is a number, change to that channel number
            TV.change_channel(action)
        
    # Print TV information
    print(TV)

input("Press the Enter key to exit...")

    
