"""
    Program: challenge5_3.py
    Author: Michael Rouse
    Date: 10/2/13
    Description: Has the user enter the name of a male and tells
                 the user who their daddy is... Also allows user
                 to add, replace, or remove son-father pairs
"""

# Dictionary for father-son pairs
# daddy = {name: their daddy}
daddy = {"michael": "George Romero",
         "james": "Wes Craven",
         "jake": "Stanely Kubrick",
         "john": "Alfred Hitchcock",
         "mark": "Peter Jackson",
         "kyle": "Neil Marshall",
         "jordan": "Tobe Hooper",
         "nick": "John Carpenter"}

choice = None
error = 0

# Main loop, loop until user picks to exit
while choice != "4":

    # Print the main menu
    print ("""
                    WHO'S YOUR DADDY?

            0 - Look up someone's daddy
            1 - Add a daddy
            2 - Change someone's daddy
            3 - Remove a daddy
            4 - Exit program
            
            """)

    # Display error messages
    if error != 0:

        # Input Error
        if error == 1:
            print("\nUnknown Input. Please try again.")
            error = 0

        # Unknown name error
        if error == 2:
            print("\nI'm sorry, I don't know who their daddy is, try adding their daddy.")
            error = 0

        # Daddy already in dictionary error
        if error == 3:
            print("\nI'm sorry, I already know their daddy, try changing their daddy.")
            error = 0

    # Get user input
    choice = input("Choice: ")
    print ("")

    # Look up someone's daddy
    if choice == "0":
        name = input("Enter a male name and I will look up their daddy: ")

        name = name.lower()
        # Check if name is in daddy dictionary
        if name in daddy:
            father = daddy[name]
            
            sentence = name.title() + "'s daddy is " + daddy[name] + "."
            print("\n\n\n\n", sentence)
            
        # Name not in dictionary
        else:
            error = 2

    # Add a daddy
    elif choice == "1":
        name = input("Enter the name of someone who's daddy you want to add: ")
        name = name.lower()

        if name not in daddy:
            father = input("Who is their daddy? ")
            father = father.title()

            # Add daddy to dictionary
            daddy[name] = father

            print ("\n\n", name.capitalize(), "has been added, his daddy is", father.capitalize())

        # Name is in dictionary   
        else:
            error = 3

    # Change a daddy
    elif choice == "2":
        name = input("\n\nEnter the name of someone who's daddy you want to change: ")
        name = name.lower()

        if name in daddy:
            sentence = name.title() + "'s current daddy is " + daddy[name] + "."
            print ("\n\n", sentence)

            father = input("Enter the name of their new daddy: ")
            father = father.title()

            daddy[name] = father

            sentence = name.title() + "'s new daddy is " + father + "."
            print ("\n\n", sentence)

        # Name not in dictionary   
        else:
            error = 2

    # Remove a daddy
    elif choice == "3":
        name = input("\n\nEnter the name of someone's daddy that you want to remove: ")
        name = name.lower()

        if name in daddy:           
            sentence = name.title() + " and his daddy, " + daddy[name ] + " have been removed."
            print ("\n\n", sentence)

            del daddy[name]

        # Name not in dictionary
        else:
            error = 2

    # Exit program
    elif choice == "4":
        print("\n\nGoodbye.")
        
    # Unknown input
    else:
        error = 1

    
