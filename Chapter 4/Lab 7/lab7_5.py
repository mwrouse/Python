"""
    Program: lab7_5.py
    Author: Michael Rouse
    Date: 9/27/13
    Description: Picks a random car for each staff member and displays that car they drove to work,
                if they drove a special car then say they need a promotion.
"""

import random

# Staff directory tuple
STAFF = ('Xavier', 'Matt', 'Joey', 'Jordon', 'Nick', 'Cole', 'Brad')

# Possible cars for each staff member tuple
CARS = ('Ferrari', 'Corvette', 'DeLorean', 'Mercedes', 'Chevrolet')

for i in range(0, len(STAFF)):
    car = random.choice(CARS)
    print(STAFF[i], "drove to work today, and he drove a", car)
    if car == "Chevrolet" or car == "Mercedes":
        print(STAFF[i], "deserves a nice promotion!\n")
    elif car == "Ferrari":
        print(STAFF[i], "is making too much money and should be fired.\n")
    else:
        print("\n")
        

input("Press the Enter key to exit...")
