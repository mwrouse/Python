"""
    Program: lab4_11.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Gets two numbers from user and tells how many of them are positive.
"""
print("Tell me two numbers and I will tell you how many are positive!\n\n\n")

first = int(input("First number: "))
second = int(input("Second number: "))

positive = 0

if first >= 0:
    positive += 1

if second >= 0:
    positive += 1

if positive == 2:
    print("\nBoth are positive.")

elif positive == 1:
    print("\nOne positive.")

else:
    print("\nNo positives.")


print("\n\n\nDone...")
