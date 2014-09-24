"""
    Program: dd37b.py
    Author: Michael Rouse
    Date: 1/16/14
    Description: read from customers.dat
"""
import pickle

customer_file = open("customers.dat", "rb")
customer = pickle.load(customer_file)
customer_file.close()

print(customer)
