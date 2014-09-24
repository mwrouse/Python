"""
    Program: lab4_03.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Gets input from a user and counts down to 0
"""
print ("Tell me a number and I will count down to 0.\n\n\n")

userNumber = int(input("Enter a number: "))

if userNumber <= 0:
    print("Error!")
else:
    while userNumber >= 0:
        print(userNumber)
        userNumber -= 1

print("\n\nDone...")

