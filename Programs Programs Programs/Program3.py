"""
    Program: Program3.py
    Author: Michael Rouse
    Date: 11/14/13
    Description: Loads three grades and names from a pickled file
"""
import pickle

# Write to the grades.dat file
file = open("grades.dat", "wb")
grades = ["Michael", 100, "Johnny", 85, "Kenny", 93]
pickle.dump(grades, file)
file.close()



grades_file = open("grades.dat", "rb")

grades = pickle.load(grades_file)

# Display the grades
print(grades[0]+" = "+str(grades[1])+"%")
print(grades[2]+" = "+str(grades[3])+"%")
print(grades[4]+" = "+str(grades[5])+"%")
