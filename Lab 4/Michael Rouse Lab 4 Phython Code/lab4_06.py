"""
    Program: lab4_06.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Has the user input two numbers and the program will print which number is larger.
"""
print("Tell me two numbers and I can tell you which is larger!\n\n")

firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))

if firstNumber > secondNumber:
    print("\nThe larger number is", firstNumber)
elif secondNumber > firstNumber:
    print("\nThe larger number is", secondNumber)
else:
    print("\nThe numbers are the same.")

print("\n\nDone...")
