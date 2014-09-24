"""
    Program: lab5_8.py
    Author: Michael Rouse
    Date: 9/13/13
    Description: generates two random positive integers and displays them in a number sentence as strings and asks for the answer then checks to make sure the answer is correct. Asks
                 user if they want to replay. Displays numSent1 every other time. Tells user how many they got corect and incorrect
"""
import random

counter = 1 #counter variable to determine which number sentence to display

correct = 0 #number of correct answers
incorrect = 0 #number of incorrect answers

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

    if counter % 2 == 0: #if counter is divisible by two (displays every other time)
        userAnswer = int(input("\nWhat is the answer to " + numSent1))
    else:
        userAnswer = int(input("\nWhat is the answer to " + numSent2))

    #check the users answer for answer2
    if userAnswer == answer:
        print("Correct! Good job!")
        correct += 1
    else:
        print("Sorry, the answer is actually " + str(answer))
        incorrect += 1

    counter += 1 #add 1 to counter to display the other number if continued
    
    
    userInput = input("\n\nDo you want to display more numbers (yes/no)? ")


print("\n\nYou got", str(correct), "problems correct")
print("You got", str(incorrect), "problems incorrect")
    


