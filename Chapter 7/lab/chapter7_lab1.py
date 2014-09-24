"""
    Program: chapter7_lab1.py
    Author: Michael Rouse
    Date: 11/8/13
    Description: Lab, modify the customer_info to loop if the info is not valid or correct.
"""

def customer_info():
    """ Gets information about customer """
    # List of customer information
    customer = []
    
    # Get customer's full name
    customer.append(input("What is your first name? "))
    customer.append(input("\nWhat is your middle name? "))
    customer.append(input("\nWhat is your last name? "))

    # Get customer's SSN
    customer.append(input("\nWhat is your SSN? "))

    # Get customer's address
    customer.append(input("\nWhat is your street address? "))
    customer.append(input("\nWhat is your city? "))
    customer.append(input("\nWhat is your state? "))
    customer.append(input("\nWhat is your zip code? "))
    
    return customer

def get_yes_no(question=""):
    """ Asks user yes or no question, will return False if no and True if yes """
    # Ask question
    user_input = input(question)
    user_input = user_input.upper()
    
    # Check user input
    if user_input == "NO" or user_input == "N":
        valid = False
    elif user_input == "YES" or user_input == "Y":
        valid = True
    else:
        valid = False

    # Return true or false
    return valid
    

def main():
    """ Main program """
    valid = False

    while not valid:
    
        customer = customer_info()

        # Display the customer info
        print("\n\n")
        print("Customer Info:")
        print("\t   Name: "+customer[0]+" "+customer[1]+" "+customer[2])
        print("\t    SSN: "+customer[3])
        print("\tAddress: "+customer[4])
        print("\t         "+customer[5]+", "+customer[6]+" "+customer[7])
        print("\n\n")

        # Ask user and check input
        valid = get_yes_no("Is this correct (Y/N)? ")
               


main()
input("\n\nPress the Enter key to exit...")    
