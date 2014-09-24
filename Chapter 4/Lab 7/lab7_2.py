"""
    Program: lab7_2.py
    Author: Michael Rouse
    Date: 9/26/13
    Description: Orders a tuple by the alphabet
"""

# Directory of staff members
STAFF = ("Xavier", "Matt", "Joey", "Jordon", "Nick", "Cole", "Brad")

# Directory of staff members alphabetically
staffOrdered = ()

# This while-loop will execute as long as the STAFF tuple has elements in it
while STAFF:
    # Set first position to element 0
    firstPos = 0

    # This will execute the same amount of times as the length of the STAFF element
    for current in range(len(STAFF)):

        # Checks to see which element comes first in the alphabet
        if STAFF[firstPos] > STAFF[current]:
            # firstPos comes first
            firstPos = current         

    # After the for-loop above we know which element is next element in the alphabet
    # current = 0 => get element first in alphabet
    # current = 1 => get element second in alphabet
    # and so on and so forth

    # Add the element to the staffOrdered array
    staffOrdered += STAFF[firstPos: firstPos + 1]

    # Trim down the STAFF array so we don't pick the same name twice
    STAFF = STAFF[:firstPos] + STAFF[firstPos +1: len(STAFF)]


# Print the new, alphabetical staff directory
print("Here is a list of your employees and their ID:")
print("\nID\tName")
for i in range(len(staffOrdered)):
               print(i, "\t", staffOrdered[i])

input("\nPress the Enter key to exit...")
    
    
            
