"""
    Program: lab5_6.py
    Author: Michael Rouse
    Date: 9/13/13
    Description: generates two random positive integers and displays them in a number sentence as strings and asks for the answer then checks to make sure the answer is correct. Asks
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

    answer = number1 + number2
    userAnswer = int(input("\nWhat is the answer to " + numSent1))

    #check the users answer for answer1
    if userAnswer == answer:
        print("Correct! Good job!")
    else:
        print("Sorry, the answer is actually " + str(answer))
              
    userAnswer = int(input("\nWhat is the answer to " + numSent2))

    #check the users answer for answer2
    if userAnswer == answer:
        print("Correct! Good job!")
    else:
        print("Sorry, the answer is actually " + str(answer))
    
    
    
    userInput = input("\n\nDo you want to display more numbers (yes/no)? ")
    


