"""
    Program: lab5_2.py
    Author: Michael Rouse
    Date: 9/13/13
    Description: generates two random positive integers and displays them in order, then reverse order. Asks
                 user if they want to replay
"""
import random

userInput = "yes"

while userInput.lower() != "no" and userInput.lower() != "n":
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

    userInput = input("Do you want to display more numbers (yes/no)? ")
    


