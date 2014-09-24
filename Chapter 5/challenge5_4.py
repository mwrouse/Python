"""
    Program: challenge5_4.py
    Author: Michael Rouse
    Date: 10/2/13
    Description: Has the user enter the name of a male and tells
                 the user who their daddy is... Also allows user
                 to add, replace, or remove son-father pairs.
                 Adds grandaddys as well
"""

# Dictionary for father-son pairs
daddy = {"michael romero": "George Romero",
         "james craven": "Wes Craven",
         "jake kubrick": "Stanely Kubrick",
         "john hitchcock": "Alfred Hitchcock",
         "mark jackson": "Peter Jackson",
         "kyle marshall": "Neil Marshall",
         "jordan hooper": "Tobe Hooper",
         "nick carpenter": "John Carpenter",
# Grandaddys
         "george romero": "Nick Romero",
         "wes craven": "Bob Craven",
         "stanely kubrick": "Stanely Kubrick",
         "alfred hitchcock": "Mark Hitchcock",
         "peter jackson": "John Jay Jackson Jr.",
         "neil marshall": "Michael Marshall",
         "tobe hooper": "Craig Hooper",
         "john carpenter": "The Carpenter"
         }

choice = None
error = 0

# Main loop, loop until user picks to exit
while choice != "8":

    # Print the main menu
    print ("""
                    WHO'S YOUR DADDY?

            0 - Look up someone's daddy
            1 - Look up someone's grandaddy
            2 - Add a daddy
            3 - Add a grandaddy
            4 - Change someone's daddy
            5 - Change someone's grandaddy
            6 - Remove a daddy
            7 - Remove a grandaddy
            8 - Exit program
            
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

        # Gradaddy already in dictionary error
        if error == 4:
            print("\nI'm sorry, I already know their grandaddy, try changing their grandaddy.")
            error = 0

        # Unknown grandaddy
        if error == 5:
            print("\nI'm sorry, I don't know their grandaddy, try adding their grandaddy.")
            error = 0

    # Get user input
    choice = input("Choice: ")
    print ("")

    # Look up someone's daddy
    if choice == "0":
        name = input("Enter someone's first and last name and I will look up their daddy: ")
        name = name.lower()
        
        # Check if name is in daddy dictionary
        if name in daddy:
            father = daddy[name]
            
            sentence = name.title() + "'s daddy is " + daddy[name] + "."
            print("\n\n\n\n", sentence)
            
        # Name not in dictionary
        else:
            error = 2

    # Look up someone's grandaddy
    elif choice == "1":
        name = input("Enter someone's first and last name and I will look up their grandaddy: ")
        name = name.lower()

        # Check if name is in dictionary
        if name in daddy:
            father = daddy[name]
            father = father.lower()

            if father in daddy:
            
                grandaddy = daddy[father.lower()]

                sentence = name.title() + "'s grandaddy is " + grandaddy + "."
                print("\n\n\n\n", sentence)

            else:
                error = 5

        # Name not in dictionary
        else:
            error = 2
        
    # Add a daddy
    elif choice == "2":
        name = input("Enter the first and last name of someone whose daddy you want to add: ")
        name = name.lower()

        if name not in daddy:
            father = input("What is their daddy's first and last name? ")
            father = father.title()

            # Add daddy to dictionary
            daddy[name] = father

            print ("\n\n", name.capitalize(), "has been added, his daddy is", father.capitalize())

        # Name is in dictionary   
        else:
            error = 3

    # Add a grandaddy
    elif choice == "3":
        name = input("Enter the first and last name of someone whose grandaddy you want to add: ")
        name = name.lower()

        # Check if we know their daddy
        if name in daddy:
            father = daddy[name]
            father = father.lower()
            
            #Check if we know their grandaddy
            if father not in daddy:
                grandaddy = input("Who is their grandaddy's first and last name? ")
                grandaddy = grandaddy.title()

                daddy[father] = grandaddy

                sentence = name + "'s grandaddy, " + grandaddy + " has been added."
                print("\n\n\n", sentence)

            else:
                error = 4
        else:
            error = 2  
        
    # Change a daddy
    elif choice == "4":
        name = input("\n\nEnter the first and last name of someone whose daddy you want to change: ")
        name = name.lower()

        if name in daddy:
            sentence = name.title() + "'s current daddy is " + daddy[name] + "."
            print ("\n\n", sentence)

            father = input("Enter the  first and last name of their new daddy: ")
            father = father.title()

            daddy[name] = father

            sentence = name.title() + "'s new daddy is " + father + "."
            print ("\n\n", sentence)

        # Name not in dictionary   
        else:
            error = 2

    # Change a grandaddy
    elif choice == "5":
        name = input("\n\nEnter the first and last name of someone whose grandaddy you want to change: ")
        name = name.lower()

        if name in daddy:
            father = daddy[name]
            father = father.lower()

            if father in daddy:
                sentence = name.title() + "'s current grandaddy is " + daddy[father] + "."
                print("\n\n", sentence)

                grandaddy = input("Enter the first and last name of their new grandaddy: ")
                grandaddy = grandaddy.title()

                daddy[father] = grandaddy

                sentence = name.title() + "'s new grandaddy is " + grandaddy + "."
                print("\n\n", sentence)
                    
            # Unknown grandaddy
            else:
                error = 4

        else:
            error = 2
        
    # Remove a daddy
    elif choice == "6":
        name = input("\n\nEnter the first and last name of someone's daddy that you want to remove: ")
        name = name.lower()

        if name in daddy:           
            sentence = name.title() + " and his daddy, " + daddy[name ] + " have been removed."
            print ("\n\n", sentence)

            del daddy[name]

        # Name not in dictionary
        else:
            error = 2

    # Remove a grandaddy
    elif choice == "7":
        name = input("\n\nEnter a first and last name of someone whose grandaddy you want to remove: ")
        name = name.lower()

        if name in daddy:
            father = daddy[name]
            father = father.lower()

            if father in daddy:
                sentence = name.title() + "'s grandaddy, " + daddy[father] + " has been removed."
                print("\n\n", sentence)

                del daddy[father]
            
            else:
                error = 5

        else:
            error = 2
            
    # Exit program
    elif choice == "5":
        print("\n\nGoodbye.")
        
    # Unknown input
    else:
        error = 1

    
