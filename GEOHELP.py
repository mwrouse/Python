""" 
    Program: GEOHELP.py
    Author: Michael Rouse
    Date: 10/21/13
    Description: Assists users with various geometry functions
"""

import my_math

"""
    my_math functions:
        circleArea(radius)
        circleDiameter(radius)
        circlePerimeter(radius)
        cylinderArea(radius, height)
        cylinderVolume(radius, height)
        prismArea(length, height, width)
        prsimVolume(length, height, width)
        rectangleArea(length, width)
        rectanglePerimeter(length, width)
        triangleArea(base, height)
"""

def get_float(prompt="Input a number> "):
    """ Gets a floating point number from the user """
    valid = False

    # Keeps asking for input until valid
    while not valid:
        userInput = input(prompt)

        # Check to see if user input is valid
        if check_input(userInput) == True:
            # Mark as valid
            valid = True

        else:
            # Mark as invalid
            valid = False

    # Return input as floating point number
    return float(userInput)
    
def get_radius():
    """ Get radius from user """
    # Get user input for radius
    radius = get_float("What is the radius? ")

    # Return the radius
    return radius   
    
def get_height():
    """ Get height from user """
    # Get user input for height
    height = get_float("What is the height? ")

    # Return the height
    return height   

def get_length():
    """ Get length from user """
    # Get user input for length
    length = get_float("What is the length? ")

    # Return the length
    return length   

def get_width():
    """ Get width from user """
    # Get user input for width
    width = get_float("What is the width? ")

    # Return the width
    return width    

def get_base():
    """ Get base from user """
    # Get user input for base
    base = get_float("what is the base? ")

    # Return the base
    return base

############
# DIAMETER #
############
def display_diameter():
    """ Find the diameter of a circle """
    print("\n\nCalculate the diameter of a circle\n")

    # Get measurements
    radius = get_radius()

    # Solve for diameter
    diameter = my_math.circleDiameter(radius)

    shape = "circle"

    # Display the diameter to the user
    print("\nThe diameter of the", shape, "is:", diameter)

############
#   AREA   #
############
def display_area(menuID):
    """ Solve for the area of a shape """
    if menuID == 1:
        # Area of a circle
        shape = "circle"
        print("\n\nCalculate the area of a", shape, "\n")

        # Get measurements
        radius = get_radius()
        
        # Solve for area
        area = my_math.circleArea(radius)

    elif menuID == 2:
        # Area of a cylinder
        shape = "cylinder"
        print("\n\nCalculate the area of a", shape, "\n")

        # Get measurements
        radius = get_radius()
        height = get_height()

        # Solve for area
        area = my_math.cylinderArea(radius, height)
        
    elif menuID == 3:
        # Area of a prism
        shape = "prism"
        print("\n\nCalculate the area of a", shape, "\n")

        # Get measurements
        length = get_length()
        width = get_width()
        height = get_height()

        # Solve for area
        area = my_math.prismArea(length, height, width)

    elif menuID == 4:
        # Area of a rectangle
        shape = "rectangle"
        print("\n\nCalculate the area of a", shape, "\n")

        # Get measurements
        length = get_length()
        width = get_width()

        # Solve for area
        area = my_math.rectangleArea(length, width)

    elif  menuID == 5:
        # Area of a triangle
        shape = "triangle"
        print("\n\nCalculate the area of a", shape, "\n")

        # Get measurements
        base = get_base()
        height = get_height()

        # Solve for area
        area = my_math.triangleArea(base, height)

    # Display the area to the user
    print("\nThe area of the", shape, "is:", area)

##########
# VOLUME #
##########
def display_volume(menuID):
    """ Solve for the volume of a shape """
    if menuID == 2:
        # Volume of a cylinder
        shape = "cylinder"
        print("\n\nCalculate the volume of a", shape, "\n")

        # Get measurements
        radius = get_radius()
        height = get_height()

        # Solve for volume
        volume = my_math.cylinderVolume(radius, height)
        
    elif menuID == 3:
        # Volume of a prism
        shape = "prism"
        print("\n\nCalculate the volume of a", shape, "\n")

        # Get measurements
        length = get_length()
        height = get_height()
        width = get_width()

        # Solve for volume
        volume = my_math.prismVolume(length, height, width)

    # Display the volume to the user
    print("\nThe volume of the", shape, "is:", volume)

#############
# PERIMETER #
#############
def display_perimeter(menuID):
    """ Solve for the perimeter of a shape """
    if menuID == 1:
        # Perimeter of a circle
        shape = "circle"
        print("\n\nCalculate the perimeter of a", shape, "\n")

        # Get measurements
        radius = get_radius()

        # Solve for perimeter
        perimeter = my_math.circlePerimeter(radius)

    elif menuID == 4:
        # Perimeter of a rectangle
        shape = "rectangle"
        print("\n\nCalculate the perimeter of a", shape, "\n")

        # Get measurements
        length = get_length()
        width = get_width()

        # Solve for perimeter
        perimeter = my_math.rectanglePerimeter(length, width)

    # Display the perimeter to user
    print("\nThe perimeter of the", shape, "is:", perimeter)
    
def menu(id=0):
    """Display a menu. 0=Main, 1=Circle, 2=Cylinder, 3=Prism, 4=Rectangle, 5=Triangle"""
    if id == 0:
        # Show main menu
        print("""
                   Geometry Helper

        Choose a shape you want to work with

        1. Circle
        2. Cylinder
        3. Prism
        4. Rectangle
        5. Triangle
        0. Exit

            """)
                
    if id == 1:
        # Show circle menu
        print("""
                   Circle Help

           What do you need to solve for?

        1. Area
        2. Diameter
        3. Perimeter
        0. Back

            """)
        
    if id == 2:
        # Show cylinder menu
        print("""
                   Cylinder Help

           What do you need to solve for?

        1. Area
        2. Volume
        0. Back
        
        """)

    if id == 3:
        # Show prism menu
        print("""
                   Prism Help

           What do you need to solve for?

        1. Area
        2. Volume
        0. Back
        
        """)

    if id == 4:
        # Show rectangle menu
        print("""
                  Rectangle Help

           What do you need to solve for?

        1. Area
        2. Perimeter
        0. Back
        
        """)

    if id == 5:
        # Show triangle menu
        print("""
                  Triangle Help

           What do you need to solve for?

        1. Area
        0. Back
        
        """)

    # Get user input for the menu
    userInput = menu_input(id)
    
    return userInput

def check_input(userInput):
    """ Checks to make sure user input is valid """
    valid = False
    error = None
    
    try:
        # Check to see if input is a number
        userInput = float(userInput)

        # Input is a number, check if it's valid
        if userInput > 0:
            # Number is valid
            valid = True

        else:
            # Not larger than zero, display an error
            if userInput == 0:
                # Input can't be zero error
                error = "\nZero is not a valid measurement."

            else:
                # Negative number error
                error = "\nPositive numbers only, please."
    
            valid = False

    except:
        # User input is not a number error
        error = "\nNumbers only, please."
        
        valid = False

    # Detect if an error occured
    if valid != True:
        # Error was detected, display error
        print(error)
        
        return False

    else:
        # No error
        return True

def menu_input(menuID):
    """ Get user input for menu navigation """
    # Tuple for available options on each menu
    menuOptions = ((0, 1, 2, 3, 4, 5), (0, 1, 2, 3), (0, 1, 2), (0, 1, 2), (0, 1, 2), (0, 1))

    # Get available options for the menu the user is on
    options =  menuOptions[menuID]

    valid = False
    error = None

    # Will loop until user inputs a valid option
    while not valid:
        # Get user's option
        userInput = input("Choice> ")

        try:
            # Check to see if input is a number
            userInput = int(userInput)

            # Input is a number, check if it's available for the menu
            if userInput not in options:
                # Not an available option, set the error
                error = "\nOption not available."
                valid = False

            else:
                # Option is valid
                valid = True

        except:
            # Input not a number, set the error
            error = "\nOption not available."
            valid = False

        # Display error if it was detected
        if error:
            print(error)
            error = None

    # User input is valid
    return userInput
            
##########
#  MAIN  #
##########
def main():
    """ Main program of Geometry Helper """
    close = False
    menuID = 0

    # Will loop until user picks to exit the program
    while close != True:
        
        # Display the menu and get user input
        option = menu(menuID)

        """
                      OPTIONS FOR EACH MENU
        main menu (0):
            option 1: Circle Menu          option 2: Cylinder Menu
            option 3: Prism Menu           option 4: Rectangle Menu
            option 5: Triangle Menu        option 0: Exit program
            
        circle menu (1):              cylinder menu(2):
           option 1: Area                  option 1: Area
           option 2: Diameter              option 2: Volume
           option 3: Perimeter             option 0: Return
           option 0: Return
           
        prism menu (3)                rectangle menu(4):
           option 1: Area                  option 1: Area
           option 2: Volume                option 2: Perimeter
           option 0: Return                option 0: Return
        
        triangle menu (5)
           option 1: Area
           option 0: Return
        """
                
        # Put user's option into action
        
        # Main menu has only two outcomes
        if menuID == 0:
            if option == 0:
                # User wants to exit program
                close = True

            else:
                # Options 1 - 5
                # User wants to navigate to a submenu
                menuID = option

        # All submenus (1-5)
        else:
            # Option 0 is the same across all submenus
            if option == 0:
                # Return to main menu
                menuID = option

            # Option 1 is the same across all submenus as well
            elif option == 1:
                # Solve for area of the shape
                display_area(menuID)

            # Option 2 varies for each submenu
            elif option == 2:
                if menuID == 1:
                    # Solve for diameter of a circle
                    display_diameter()
            
                elif menuID == 2 or menuID == 3:
                    # Solve for volume of a cylinder/prism
                    display_volume(menuID)
                    
                elif menuID == 4:
                    # Solve for perimeter of a rectangle
                    display_perimeter(menuID)

            # Option 3 is only available for one submenu
            elif option == 3:
                if menuID == 1:
                    # Solve for perimeter of a circle
                    display_perimeter(menuID)


    # Inform the user the program is closing
    print("""
                        Thank you for using Geometry Helper!

                      Press the Enter key to exit the program...
            """)
    input("")

# Go to main function
main()

