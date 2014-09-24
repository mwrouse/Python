"""
    Program: challenge3_2.py
    Author: Michael Rouse
    Date: 9/9/13
    Description: Simulates a coin flip 100 times and tells the user how many times it landed on heads and tails
"""
import random

heads = 0
tails = 0
flips = 1

while flips <= 100:
    flip = random.randint(1, 2) #flips the coin; 1 = heads and 2 = tails

    if flip == 1:
        heads += 1
    else:
        tails += 1

    flips += 1

print("The results of 100 coin flips:\n")
print("Heads:", heads)
print("Tails:", tails)
