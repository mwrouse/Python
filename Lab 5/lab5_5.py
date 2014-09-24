"""
    Program: lab5_5.py
    Author: Michael Rouse
    Date: 9/13/13
    Description: generates two random positive integers and displays them in a number sentence as strings and asks for the answer. Asks
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
        numSent1 = str(number1) + " + " + str(number2) + " = "
        numSent2 = str(number2) + " + " + str(number1) + " = "
    else:
        numSent1 = str(number2) + " + " + str(number1) + " = "
        numSent2 = str(number1) + " + " + str(number2) + " = "

    userAnswer1 = input("What is the answer to " + numSent1)
    userAnswer2 = input("What is the answer to " + numSent2)

    userInput = input("Do you want to display more numbers (yes/no)? ")
    


