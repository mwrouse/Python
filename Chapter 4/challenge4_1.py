"""
    Program: challenge4_1.py
    Author: Michael Rouse
    Date: 9/24/13
    Description: Lets user enter a starting numer and counts up by the amount a user defines.
"""

print("Let me count for you!\n\n")

startNum = int(input("What is the number you want to start at? "))

endNum = int(input("What is the number you want to end at? "))

countingNum = int(input("What do you want to count by? "))

print("\n\n")
print("Your numbers are:\n")

#Prints each number from startingNumber to the end number, increasing by the counting number
for i in range(startNum, endNum + countingNum, countingNum):
    print(i)



input("\nPress the Enter key to exit...")

    
