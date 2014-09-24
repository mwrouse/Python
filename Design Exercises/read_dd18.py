"""
    Program: read_dd18.py
    Author: Michael Rouse
    Date: 11/6/13
    Description: Daily Design Exercise, have to readlines into a list from the "dd18.txt" file.
"""
# Open the file
the_file = open("dd18.txt", "r")

# Turn the file into a list
poem = the_file.readlines()

# Print each line of the poem
for line in poem:
    print(line)

# Close the file
the_file.close()
