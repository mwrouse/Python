"""
   Program: lab7_1.py
   Author: Michael Rouse
   Date: 9/25/13
   Description: Program for Donald Trump, has a staff tuple and allows him to fire people.
"""

# Staff tuple
staff = ("Xavier", "Matt", "Joey", "Jordan", "Nick", "Cole", "Brad")

replay = "y"

print("""
                Donald Trump Firing Program
        Hello, Donald. Type an employees name to fire them

    """)

while replay.lower() != "n":
    
    print("\n\nStaff Directory:\n")
    print("\t ID: \t\t Name:")
    
    # print each memeber in the staff director and their ID (index)
    for i in range(0, len(staff)):
        print("\t",i, "\t\t", staff[i])
    print("\n")

    # Get user input on who to fire by their ID
    fire = int(input("Enter the ID of someone you would like to fire: "))

    # Loop if employee ID is not valid
    while fire >= len(staff) or fire < 0:
        print("\nNot a valid Employee ID...")
        fire = int(input("Enter the ID of someone you would like to fire: "))
        
    # Grab the employee name for display
    employeeName = staff[fire]
        
    # Remove the fired employee from the staff directory
    staff = staff[:fire] + staff[fire + 1: len(staff)]

    # Check to see if you have employees left in the staff directory
    if len(staff) < 1:
        replay = "n"
    else:
        print("\nYou have fired", employeeName)
        replay = input("\nDo you want to fire someone else (y/n)? ")

# If no more employees left
if len(staff) <1:   
    print("Good job! Now, fire yourself and go home!")


input("Press the Enter key to exit...")

      

            
    
    

        
    
    
