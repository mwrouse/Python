"""
    Program: dd38a.py
    Author: Michael Rouse
    Date: 1/17/14
    Description: Get three customer records and save them to a pickled file
"""
from Record import *
import pickle

def save_records(database, pickle_file="customers.dat"):
    """ Save the list (database) to a pickle_file """
    print("\nSaving the records to \"" + pickle_file + "\"...")
    
    # Open file for writting in binary mode
    customer_file = open(pickle_file, "wb")

    # Dump the list into the pickled file
    pickle.dump(database, customer_file)

    # Close the file
    customer_file.close()

    print("\nRecords saved.")
    
def main():
    """ Main program function """
    # Blank list for customer recorde
    database = []

    # Get 3 records using this for-loop
    for i in range(0, 3):
        # Create a new Record Object and get information
        new_record = Record()

        # Add to the database
        database.append(new_record.get_record())

        # Delete the record
        del new_record

        print("\n")

    # Save the records to customers.dat
    save_records(database)



main()
