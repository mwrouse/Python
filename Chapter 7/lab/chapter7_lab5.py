"""
    Program: chapter7_lab5.py
    Author: Michael Rouse
    Date: 11/12/13
    Description: Modify chapter 7 lab 4 to be able to enter in multiple customers then save it in a dictionary in a shelf file
"""

import pickle, shelve

def customer_info():
    """ Gets information about customer """
   
    # List to have in the dictionary
    customer_list = []

    # Get customer's full name
    customer_list.append(input("What is the customer's first name? "))
    customer_list.append(input("What is the customer's middle name? "))
    customer_list.append(input("What is the customer's last name? "))

    # Get customer's SSN
    customer_list.append(input("What is the customer's SSN? "))

    # Get customer's address
    customer_list.append(input("What is the customer's street address? "))
    customer_list.append(input("What is the customer's city? "))
    customer_list.append(input("What is the customer's state? "))
    customer_list.append(input("What is the customer's zip code? "))

    return customer_list


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

def store_it(customer):
    """ Converts the list into a dictionary and saves it in the shelf file """

    # Open the customer shelf
    customers = shelve.open("customer_shelf")

    # Grab the customer's social security number and remove it from the customer list
    ssn = customer[3]
    del customer[3]

    # Add a dictionary entry for the new customer in the shelf file
    customers[ssn] = customer

    # Sync the shelf
    customers.sync()

    # Close the shelf
    customers.close()

def get_it():
    """ Opens the shelf file and displays all customers in the shelf """
    
    # Open the shelf
    customers = shelve.open("customer_shelf")

    # Display the customers
    print("Customer List:")
    print("\t     SSN:\t  Customer Info:")

    # For each SSN in customers
    for ssn in customers:

        # Create a string that contains all info about the customer
        display_info = "\t " + str(ssn) + "\t" + customers[ssn][0] + " " + customers[ssn][1] + " " + customers[ssn][2] + \
                       "\n\t\t\t" + customers[ssn][3] + \
                       "\n\t\t\t" + customers[ssn][4] + ", " + customers[ssn][5] + " " + customers[ssn][6] + "\n"

        print(display_info)

    # Close the shelf
    customers.close()

    return True

def main():
    """ Main program """
    valid = False

    while not valid:

        # Will be the list returned by customer_info()
        customer = customer_info()

        print(customer)

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
        print("\n\n")

    # At this point all user input is correct and valid, save the customer to the list
    store_it(customer)

    # Display all customers
    get_it()
    

""" MAIN """
add_more = True

while add_more == True:
    main()

    # Ask customer if they want to add another customer
    add_more = get_yes_no("Add another customer (Y/N)? ")

    
input("\n\nPress the Enter key to exit...")
