"""
    Program: lab4_07.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Has the user input three numbers and the program will print which number is larger.
"""
print("Tell me three numbers and I can tell you which is larger!\n\n")

firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))
thirdNumber = int(input("Third number: "))

#variable for comparison and printing the largest number
largerNumber = 0

if firstNumber > secondNumber:
    largerNumber = firstNumber
else:
    largerNumber = secondNumber

if thirdNumber > largerNumber:
    largerNumber = thirdNumber

print("The largest of those three numbers is", largerNumber)

print("\n\nDone...")
