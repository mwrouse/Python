"""
    Program: dd36.py
    Author: Michael Rouse
    Date: 1/15/14
    Description: Create a class called "Record" that will be used to create a simple
                 database program
"""

class Record(object):
    """ Record Class """
    def __init__(self):
        """ Initialize the class """
        # Ask for user to input all variables
        self.__firstName = self.__askForString("First Name: ")
        self.__lastName = self.__askForString("Last Name: ")
        self.__ssn = self.__askForString("SSN: ")
        self.__address = self.__askForString("Address: ")
        self.__city = self.__askForString("City: ")
        self.__state = self.__askForString("State: ")
        self.__zipCode = self.__askForNumber("Zip Code: ", "Invalid Zip Code")
        self.__index = self.__askForNumber("Index: ", "Invalid Index Number")
        
    def __str__(self):
        """ Display information about the record """
        output = "\n\nRecord Number " + str(self.__index) + ":" + "\n" +self.__firstName.title() + " " + self.__lastName.title() + "\n" +\
                 self.__address + "\n" + self.__city + ", " + self.__state + ", " + str(self.__zipCode)

        return output

    def __askForString(self, prompt="> ", error="Invalid Input"):
        """ Ask for input and perform error checking to ensure the string isn't blank """
        valid = False

        while not valid:
            user_input = input(prompt) # Ask for input

            if user_input == "" or user_input.isspace():
                # User input is empty or contains only spaces
                print("\n" + error)
                
            else:
                # User input is valid
                valid = True

        # Valid input
        return user_input

    def __askForNumber(self, prompt="> ", error="Invalid Input"):
        """ Ask for input and perform error checking to ensure input was a number """
        valid = False

        while not valid:
            try:
                user_input = int(input(prompt)) # Ask for input

            except:
                # Not a valid number
                print("\n" + error)

            else:
                # Valid number
                valid = True

        # Input was valid, return the number
        return user_input
                

def main():
    """ Main program """

    test_record = Record() # Sample record

    print(test_record)












main()

