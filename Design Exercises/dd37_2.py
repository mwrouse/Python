"""
    Program: dd37.py
    Author: Michael Rouse
    Date: 1/16/14
    Description: Include Record.py (dd36) and create a program that will pickle a file called
                 customers.dat. It will create a customer record once created it will save it
                 to the pickled file. Then create dd37b.py that will read from the pickled
                 file
"""

from Record import *
import pickle


def save_record(record):
    """ Save a record to customers.dat """
    file = "customers.dat"
    records = [] # List of all the records to be saved in the file
    
    try:
        # Check if the file exist
        customer_file = open(file, "rb")

    except:
        # File does not exist so create it
        customer_file = open(file, "wb")
        customer_file.close()

    else:
        # File does exist, read from it
        try:
            # Check for content in the file
            records = pickle.load(customer_file)
            
        except:
            # Nothing to read from the file
            pass

        # Close the file
        customer_file.close()
    
    # Determine if the index already exists
    if record[0] <= len(records):
        # It exists, inform user of the error
        #print("Record number", record[0], "already exists. The last record number used was", str(records[len(records) -1][0]) + ".")
        
    else:
        # Add the record to the list
        records.append(record)

        # Open the file for writing
        customer_file = open(file, "wb")

        # Dump the list into the file
        pickle.dump(records, customer_file)

        # Close the file
        customer_file.close()

    return True

def read_records():
    """ read from the pickled file """
    customer_file = open("customers.dat", "rb")
    
    records = pickle.load(customer_file)

    customer_file.close()

    return records


#test = Record()

save_record([3, "Bob", "Rouse"])
a = read_records()
print(a)
#print(test)
