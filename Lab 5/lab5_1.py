"""
    Program: lab5_1.py
    Author: Michael Rouse
    Date: 9/13/13
    Description: generates two random positive integers and displays them in order, then reverse order
"""
import random

#set number1 and number2 between 0 and 12
number1 = random.randint(0, 12)
number2 = random.randint(0, 12)

#make sure they're not the same
if number1 == number2:
    number2 = random.randint(0, 12)

#print them
if number1 > number2:
    print(number1, ",", number2)
    print(number2, ",", number1)
else:
    print(number2, ",", number1)
    print(number1, ",", number2)


