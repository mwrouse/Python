"""
    Program: dd35.py
    Author: Michael Rouse
    Date: 1/10/14
    Description: Program asks user if they want cookies, cake, or nothing. It will print an error
                 and loop if they enter anything but those three options
"""

# Display the main menu with all options
print("""
                    FOOD SELECTOR 2000
               Which would you like to have?

            A) Cookies
            B) Cake
            C) Nothing
        """)

# Get user input
user_input = input("Choice> ") 

while user_input.upper() not in "ABC":
    # Input was invalid, display an error and ask again
    print("Error: Unknown choice, try again.\n")
    user_input = input("Choice> ")

# User input was valid, thank them
print("Thank you! Have a good day.")

# Close the program
input("\n\nPress the Enter key to exit...")
