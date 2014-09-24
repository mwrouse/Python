"""
    Program: Program1.py
    Author: Michael Rouse
    Date: 11/14/13
    Description: Get ten grades from the users, then print the average in an informative way
"""

# List of grades
grades = []

# Get ten grades from the user
for grade_number in range(0, 10):

    valid = False
    
    while not valid or grade not in range(0, 101):
        # Ask for a grade
        grade = input("What is the grade? ")

        try:
            grade = int(grade)
            if grade not in range(0, 101):
                print("Grade not valid, try again.")
            
            valid = True
            
        except:
            print("Grade not valid, try again")
            valid = False


    # Add grade to the grades list
    grades.append(grade)



# Program has 10 valid grades, find the average
total = 0

for i in range(0, 10):
    total += grades[i]


average = (total / 10)

print("The average is: "+str(average)+"%")


input("\n\nPress Enter to exit...")

    
