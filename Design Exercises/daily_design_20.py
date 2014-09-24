"""
    Program: daily_design_20.py
    Author: Michael Rouse
    Date: 11/8/13
    Description: Daily Design. Create a function called customer_info() which gets information about the user, and puts it into a list
                 called customer, then returns the list.
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

customer = customer_info()

print("\n\n")

for element in customer:
    print(element)
