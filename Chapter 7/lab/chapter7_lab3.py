"""
    Program: chapter7_lab3.py
    Author: Michael Rouse
    Date: 11/8/13
    Description: Lab, modify the customer_info to loop if the info is not valid or correct. Save and load customer data into a .dat file
"""

import pickle

file = "customers.dat"

customer_list = []

try:
    customer_file = open(file, "rb")

except:
    # File does not exist, cannot read from it
    pass

else:
    # File exist, read from it
    try:
        customer_list += pickle.load(customer_file)

    except:
        pass
    

# Display customer info
print("Customer List:")
print("\tID:\t\tCustomer Info:")

for customer_id in range(0, len(customer_list)):

    
    display_info = "\t" + str(customer_id) + "\t\t" + customer_list[customer_id][0] + " " + customer_list[customer_id][1] + " " + customer_list[customer_id][2] + \
                 "\n\t\t\t"+ customer_list[customer_id][4] + \
                 "\n\t\t\t" + customer_list[customer_id][5] + ", " + customer_list[customer_id][6] + " " + customer_list[customer_id][7] + \
                 "\n\t\t\tSSN: " + customer_list[customer_id][3] + "\n"
            
    print(display_info)
    

input("\n\nPress the Enter key to exit...")
