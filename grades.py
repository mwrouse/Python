"""
    Program: grades.py
    Author: Michael Rouse
    Date: 11/13/12
    Description: Gets a letter grade from the user and shows the numerical value
"""

print("Welcome to Grade Scale\n\n")

grade = None

while grade not in range(0, 101):
    grade = input("What is the percent grade (0-100)? ")

    try:
        grade = int(grade)

    except:
        print("Invalid")

    if grade > 100 or grade < 0:
        print("Invalid")

    
        


if grade > 89:
    print("A")

elif grade > 79:
    print("B")

elif grade > 69:
    print("C")

elif grade >59:
    print("D")

else:
    print("F")

