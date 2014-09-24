"""
    Program: dd21.py
    Author: Michael Rouse
    Date: 11/13/13
    Description: Save a poem to a poem.txt file
"""

# Open poem.txt for writing (create the file if it doesn't exist)
the_file = open("poem.txt", "w")

# Write to the file
the_file.writelines("A Poem by Michael Rouse:\n")
the_file.writelines("\tRoses are red.\n")
the_file.writelines("\tViolets are blue.\n")
the_file.writelines("\tDon't you wish.\n")
the_file.writelines("\tThat you could code like me?\n")

# Close the file
the_file.close()

# Open poem.txt for reading
the_file = open("poem.txt", "r")

# Display the poem
for line in the_file:
    print(line)


# Close the file
the_file.close()

input("Press the Enter key to continue...")
