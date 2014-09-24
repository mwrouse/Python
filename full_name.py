"""
    Program: full_name.py
    Author: Michael Rouse
    Date: 11/6/13
    Description: Review of lists
"""

# List of a full name
FULL_NAME = ["Michael", "Wayne", "Rouse"]

# Print last name, first name middle initial.
print(FULL_NAME[2]+", "+FULL_NAME[0]+" "+FULL_NAME[1][0]+".")

"""
    Modify the last name
"""
# Change the last name
FULL_NAME[2] = "Smith"

# Print last name, first name middle initial.
print(FULL_NAME[2]+", "+FULL_NAME[0]+" "+FULL_NAME[1][0]+".")

"""
    Add a second middle name
"""
# Add the last name to the list again
FULL_NAME.append(FULL_NAME[2])

# Add a second last name
FULL_NAME[2] = "John"

# Print out the full name
for name in FULL_NAME:
    print(name, end=" ")


input("\n\nPress Enter to exit...")

