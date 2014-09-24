"""
    Program: character_names.py
    Author: Michael Rouse
    Date: 11/12/13
    Description: Daily Design. Display names of four characters from a shelf, ask the user to choose
    one and then display info about the character.
"""
import pickle, shelve

# Load the shelf
char_shelf = shelve.open("pregen")

# Display the character names to choose from
print("Your characters available are:")

for character in char_shelf:
    # Print each character name
    print("\t"+character)

# Ask the user for a character
choice = input("\nPlease choose a character: ")

# Check if user choice is a valid character
while choice not in char_shelf:

    # Not a valid character, inform the user and ask again
    print("\nNot a valid character. Try again.")
    choice = input("Please choose a character: ")

print("\nYou picked "+choice+".")
print("\nInformation about "+choice+":")

# List containing character info
char_info = char_shelf[choice]

# Display character info
print("\t       Class:", char_info[0])
print("\t    Strenght:", char_info[1])
print("\t   Dexterity:", char_info[2])
print("\t         Con:", char_info[3])
print("\tIntelligence:", char_info[4])
print("\t      Wisdom:", char_info[5])
print("\t    Charisma:", char_info[6])
print("\t  Hit Points:", char_info[7])
print("\t       Armor:", char_info[8])
print("\t      Weapon:", char_info[9])

# Sync the shelf
char_shelf.sync()

# Close the data shelf
char_shelf.close()

input("\n\nPress the Enter key to exit...")
