"""
    Program: lab4_08.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Has the user input three numbers and the program will print which number is the middle number.
"""
print("Tell me three numbers and I can tell you which is the mide number!\n\n")

firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))
thirdNumber = int(input("Third number: "))

#variable for comparison and printing the middle number
middleNumber = 0

if firstNumber > secondNumber > thirdNumber:
    middleNumber = secondNumber
    
elif thirdNumber > secondNumber > firstNumber:
    middleNumber = secondNumber
    
elif secondNumber > firstNumber > thirdNumber:
    middleNumber = firstNumber

elif thirdNumber > firstNumber > secondNumber:
    middleNumber = firstNumber

elif firstNumber > thirdNumber > secondNumber:
    niddleNumber = thirdNumber
    
elif secondNumber > thirdNumber > firstNumber:
    middleNumber = thirdNumber
    

print("\nThe middle number is", middleNumber)


print("\n\nDone...")
