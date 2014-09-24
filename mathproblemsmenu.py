"""
    Program:
    Author: Michael Rouse
    Date: 10/18/13
    Description: Menu for math problems
"""

def menu(id=0):
    """Display a menu. 0=Main, 1=Circle, 2=Cylinder, 3=Prism, 4=Rectangle, 5=Triangle"""
    if id == 0:
        # Show main menu
        print("""
                   GEOMETRY HELPER

        Choose a shape you want to work with

        1. Circle
        2. Cylinder
        3. Prism
        4. Rectangle
        5. Triangle
        0. Exit

            """)

        userChoice = input("Option> ")
        
        if userChoice == "0":
            print()
            
        elif userChoice == "1":
            menu(1)
        elif userChoice == "2":
            menu(2)
        elif userChoice == "3":
            menu(3)
        elif userChoice == "4":
            
        
        
    if id == 1:
        # Show circle menu
        print("""
                   CIRCLE HELP

           What do you need to solve for?

        1. Area
        2. Diameter
        3. Perimeter
        0. Exit

            """)
        
        
    if id == 2:
        # Show cylinder menu
        print("""
                   CYLINDER HELP

           What do you need to solve for?

        1. Area
        2. Volume
        0. Exit
        
        """)

    if id == 3:
        # Show prism menu
        print("""
                   PRISM HELP

           What do you need to solve for?

        1. Area
        2. Volume
        0. Exit
        
        """)

    if id == 4:
        # Show rectangle menu
        print("""
                  RECTANGLE HELP

           What do you need to solve for?

        1. Area
        2. Perimeter
        0. Exit
        
        """)

    if id == 5:
        # Show triangle menu
        print("""
                  TRIANGLE HELP

           What do you need to solve for?

        1. Area
        0. Exit
        
        """)

        
menu(0)
