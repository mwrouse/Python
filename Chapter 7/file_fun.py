"""
    Program: file_fun.py
    Author: Michael Rouse
    Date: 10/29/13
    Description: Practice with files
"""

print("Practice writing to a file.\n")

# Variable for the file
my_file = open("my_file.txt", "w")

# Write four lines of text
my_file.write("Program by Michael Rouse!\n")
my_file.write("How are you?\n")
my_file.write("I'm doing great!\n")
my_file.write("Do you like my program?\n")

# Write three numbers
my_file.write("3\n")
my_file.write("504\n")
my_file.write("7777\n")

print("Four lines of text and three numbers have been written to my_file.txt")

# Close my_file
my_file.close()
