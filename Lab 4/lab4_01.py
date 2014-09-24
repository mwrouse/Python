"""
    Program: lab4_01.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Gets the user to input a number and tells the user if the number is odd or even
"""

print("Enter a  number and I can tell you if it's even or odd.\n\n")
playAgain = "y"

while playAgain == "y" or playAgain == "Y":
    userNumber = int(input("\nEnter the number: "))

    if userNumber % 2 == 0:
        print("\nYour number is even!")
    else:
        print("\nYour number is odd!")

    playAgain = input("Want to try another number (y/n)? ")

print ("\n\nDone...")
  
