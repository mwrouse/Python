"""
    Program: Program2.py
    Author: Michael Rouse
    Date: 11/14/13
    Description: Get ten grades from a file called grades.txt and print the grades and the
                 average in an informative way.
"""

# Total grade percent
total = 0

# Try and open grades.txt
try:
    grades_file = open("grades.txt", "r")
    
except:
    print("'grades.txt' file does not exist.")

else:
    # Grade file does exist
    # Load the grades into the grades list
    for i in range(0, 9):
        grade = grades_file.readline()

        total += int(grade)

    # Find the average
    average = total / 10

    print("The average is: "+str(average)+"%")

    
    


input("\n\nPress Enter to exit...")

    
