"""
    Program: chapter7_lab4.py
    Author: Michael Rouse
    Date: 11/8/13
    Description: functions called store_it(list) to save to .dat file and program should get info from .dat file
"""

import pickle

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

def store_it(customer):
    """ Gets data from a binary file and saves to it """
    file = "customers.dat"
    
    # List of all customers and the one entered
    customer_list = []
    
    try:
        # Check if file exists
        customer_file = open(file, "rb")

    except:
        # File does not exist, create it
        customer_file = open(file, "wb")
        customer_file.close()

    else:
        # File does exist
        try:
            # Check for content in file, if it has items in it, add to customer_list
            customer_list += pickle.load(customer_file)
            
        except:
            # Do nothing
            pass
                          
        # Close the file
        customer_file.close()

    # At this point the file has been created if it doesn't exist, and data has been read from the file if it has any, add current customer info to the list
    customer_list.append(customer)

    # Open file for writing
    customer_file = open(file, "wb")

    # Dump customer_list (contains old customers and new customer) into the customer file  
    pickle.dump(customer_list, customer_file)

    customer_file.close()
    
def get_it():
    """ Reads from binary file and displays customer information """

    file = "customers.dat"

    customers = []

    try:
        # Check if file exists by trying to open it
        customer_file = open(file, "rb")

    except:
        # File does not exist, do nothing
        pass
    
    else:
        # File exists, read from it
        try:
            # Try to load from file
            customers += pickle.load(customer_file)

        except:
            # No data in file, do nothing
            pass

    # At this point the customers list will be filled with information from .dat file, or left blank if nothing inside of it
    # Display information in customers list
    print(customers)
    print("Customer List:")
    print("\tID:\t\t  Customer Info:")

    for i in range(0, len(customers)):

        # Create a string that contains all information about the customer
        display_info = "\t " + str(i) + "\t\t" + customers[i][0] + " " + customers[i][1] + " " + customers[i][2] + \
                 "\n\t\t\t"+ customers[i][4] + \
                 "\n\t\t\t" + customers[i][5] + ", " + customers[i][6] + " " + customers[i][7] + \
                 "\n\t\t\tSSN: " + customers[i][3] + "\n"

        print(display_info)


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
        print("\n\n")

    # At this point all user input is correct and valid, save the customer to the list
    store_it(customer)

    # Display all customers
    get_it()
    
           
    
main()
input("\n\nPress the Enter key to exit...")
