"""
    Program: read_dd18_v2.py
    Author: Michael Rouse
    Date: 11/6/13
    Description: Daily Design Exercise, have to readlines into a list from the "dd18.txt" file.
"""
import pickle

"""
    Read from .txt file
"""
# Open the file
the_file = open("dd18.txt", "r")

# Turn the file into a list
poem = the_file.readlines()

# Print each line of the poem
print("Original:\n")
for line in poem:
    print("\t"+line)

# Close the file
the_file.close()

"""
    Create .dat file and write to it
"""
# Append a new line to the poem list
poem.append("-Thorin Schmidt")

# Open the new file for the new poem with the appended line
the_file = open("dd19.dat", "wb+")

# Write the poem list to the_file
pickle.dump(poem, the_file)

# Close the file again
the_file.close()

"""
    Read from .dat file
"""
# Open the .dat file for display
the_file = open("dd19.dat", "rb")

# Load the contents of the .dat file to the poem
poemNew = pickle.load(the_file)

# Print the new poem
print("\nPoem from .dat file:\n")

for line in poemNew:
    print("\t"+line)

# Close the file
the_file.close()

input("\n\nPress the Enter key to exit...")    

