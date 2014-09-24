"""
    Program: dd37.py
    Author: Michael Rouse
    Date: 1/16/14
    Descrption: Save Record.py return to a pickled file
"""
from Record import *
import pickle


test = Record()

customer_file = open("customers.dat", "wb")
pickle.dump(test, customer_file)
customer_file.close()
