"""
    Program: lab7_4.py
    Author: Michael Rouse
    Date: 9/27/13
    Description: Picks a random car for each staff member and displays that car they drove to work
"""

import random

# Staff directory tuple
STAFF = ('Xavier', 'Matt', 'Joey', 'Jordon', 'Nick', 'Cole', 'Brad')

# Possible cars for each staff member tuple
CARS = ('Ferrari', 'Corvette', 'DeLorean', 'Mercedes', 'Chevrolet')

for i in range(len(STAFF)):
    car = random.choice(CARS)
    print(STAFF[i], "drove to work today, and he drove a", car,"\n")

input("Press the Enter key to exit...")
