"""
    Program: popquiz.py
    Author: Michael Rouse
    Date: 10/29/13
    Description: Pop Quiz
"""
print("Divison!\n")

try:
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me a second number: "))

    answer = num1 / num2

except ZeroDivisionError:
    print("You can't divide by zero")

else:
    string = "\n\n" + str(num1) + " / " + str(num2) + " = " + str(answer)
    print(string)

input("Press the Enter key to exit...")

