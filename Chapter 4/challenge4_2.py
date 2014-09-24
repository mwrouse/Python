"""
    Program: challenge4_2.py
    Author: Michael Rouse
    Date: 9/24/13
    Description: Gets the user to input a message and then prints it backwards.
"""

print("Tell me a message and I will print it backwards for you!")

userMsg = input("What is your message? ")

print("\n\n")

backwardsMsg = "" #user message shown backwards

#adds each letter of userMsg (starting from last letter) to the backwordsMsg string
for i in range(-1, -(len(userMsg) +1), -1):
    backwardsMsg += userMsg[i]

#show the user their backwards message
print("Your message backwards is:", backwardsMsg)

input("\n\nPress the Enter key to exit...")

