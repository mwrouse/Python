"""
    Program: dd38b.py
    Author: Michael Rouse
    Date: 1/17/14
    Description: Read from the pickled file created by dd38a.py
"""
import pickle

def get_records(pickle_file="customers.dat"):
    """ Read records from pickle_file """
    # Open file in reading binary mode
    file = open(pickle_file, "rb")

    # Load information from the pickled file
    database = pickle.load(file)

    # Close file
    file.close()

    return database

def display_records(database):
    """ Display records neatly """
    for element in database:
        print("\n")
        print(" Record: #" + str(element[0]))
        print("   Name: " + element[1].title() + " " + element[2].title())
        print("    SSN: " + element[3])
        print("Address: " + element[4])
        print("         " + element[5] + ", " + element[6] + " " + str(element[7]))
            
    return True

def main():
    """ Main program function """
    # Use get_records to load information from the pickled file
    database = get_records()
    print(database)
    # Use display_records to display what was in the file neatly
    display_records(database)


main()
