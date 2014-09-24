"""
    Program: challenge5_2.py
    Author: Michael Rouse
    Date: 10/2/13
    Description: Program that creates a character for a role-playing game. Character has 30 points
                 to put into attributes: strength, health, wisdom, and dexterity.
                 Player will be able to add points to each attribute and remove points
                 as well
"""

# List for character's attribute points
# character[strength, health, wisdom, dexterity]
character = [0, 0, 0, 0]

# points (start with 30 points)
points = 30

# variable to exit program
exitProgram = 0

# Error strings
error = 0
noPoints = "\n\nYou have no points to add, try removing some.\n"


while exitProgram != 1:
    # Show menu
    print ("""
                Role-Playing Game Character Generator

        Points left: """ + str(points) + """

        Character:
             Strength: """ + str(character[0]) + """
               Health: """ + str(character[1]) + """
               Wisdom: """ + str(character[2]) + """
            Dexterity: """ + str(character[3]) + """

        Choose an option to modify your character:
            0 - Add points to Strength
            1 - Remove points from Strength
            2 - Add points to Health
            3 - Remove points from Health
            4 - Add points to Wisdom
            5 - Remove points from Wisdom
            6 - Add points to Dexterity
            7 - Remove points from Dexterity
            8 - Exit program
        """)
 
    # Show error message and reset error variable
    if error != 0:
        # Adding points error
        if error == 1:
            print("\n\nYou have no points to add, try removing some.\n")

        # Input error
        if error == 2:
            print("\n\nUnknown input. Please try again.\n")

        # Removing points error
        if error == 3:
            print("\n\nYou have no points to remove, try adding some. \n")
            
        error = 0

    
    # Get user input
    userOption = input("Option: ")

    # User selected to add points to Strength
    if userOption == "0":
        
        # Check if user has points to add
        if points <= 0:
            error = 1

        else:
            pointsToAdd = int(input("How many points do you wish to add? "))
            
            # Check if user input was more than the points they have
            if pointsToAdd <= points and pointsToAdd > 0:
                character[0] += pointsToAdd
                points -= pointsToAdd
                
            else:
                error = 1
                
    # User selected to remove points from Strength
    elif userOption == "1":
        
        # Check if user has any points to remove
        if character[0] <= 0:
            error = 3

        else:
            pointsToRemove = int(input("How many points do you wish to remove? "))

            # Check if user input was more than points they have
            if pointsToRemove <= character[0] and pointsToRemove > 0:
                character[0] -= pointsToRemove
                points += pointsToRemove
                
            else:
                error = 3
        
    # User selected to add points to Heatlh
    elif userOption == "2":
        
         # Check if user has points to add
        if points <= 0:
            error = 1

        else:
            pointsToAdd = int(input("How many points do you wish to add? "))
            
            # Check if user input was more than the points they have
            if pointsToAdd <= points and pointsToAdd > 0:
                character[1] += pointsToAdd
                points -= pointsToAdd
                
            else:
                error = 1
        
    # User selcted to remove points from Health
    elif userOption == "3":
        
        # Check if user has any points to remove
        if character[1] <= 0:
            error = 3

        else:
            pointsToRemove = int(input("How many points do you wish to remove? "))

            # Check if user input was more than points they have
            if pointsToRemove <= character[1] and pointsToRemove > 0:
                character[1] -= pointsToRemove
                points += pointsToRemove
                
            else:
                error = 3
        
    # User selected to add points to Wisdom
    elif userOption == "4":
        
         # Check if user has points to add
        if points <= 0:
            error = 1

        else:
            pointsToAdd = int(input("How many points do you wish to add? "))
            
            # Check if user input was more than the points they have
            if pointsToAdd <= points and pointsToAdd > 0:
                character[2] += pointsToAdd
                points -= pointsToAdd
                
            else:
                error = 1
                
    # User selected to remove points from Wisdom
    elif userOption == "5":
        
        # Check if user has any points to remove
        if character[2] <= 0:
            error = 3

        else:
            pointsToRemove = int(input("How many points do you wish to remove? "))

            # Check if user input was more than points they have
            if pointsToRemove <= character[2] and pointsToRemove > 0:
                character[2] -= pointsToRemove
                points += pointsToRemove
                
            else:
                error = 3
        
    # User selected to add points to Dexterity
    elif userOption == "6":
        
         # Check if user has points to add
        if points <= 0:
            error = 1

        else:
            pointsToAdd = int(input("How many points do you wish to add? "))
            
            # Check if user input was more than the points they have
            if pointsToAdd <= points and pointsToAdd > 0:
                character[3] += pointsToAdd
                points -= pointsToAdd
                
            else:
                error = 1
                
    # User selected to remove points from Dexterity
    elif userOption == "7":
        
        # Check if user has any points to remove
        if character[3] <= 0:
            error = 3

        else:
            pointsToRemove = int(input("How many points do you wish to remove? "))

            # Check if user input was more than points they have
            if pointsToRemove <= character[3] and pointsToRemove > 0:
                character[3] -= pointsToRemove
                points += pointsToRemove
                
            else:
                error = 3
        
    # User selected to exit program
    elif userOption == "8":
        exitProgram = 1
        
    # User selection is unknown
    else:
        error = 2
        
    
# User exited program
input("\nPress the Enter key to exit...")


