"""
    Program: lab5_2.py
    Author: Michael Rouse
    Date: 10/4/13
    Description: Randomly picks a name from a tuple each time the user hits the enter key and quits
                when the q key is pressed
"""
import random

# Tuple of game character first names
FIRST_NAMES = ["dark", "fire", "midnight", "shadow", "silent", "demon", "black", "death", "fury", "white",
               "sin", "dawn", "wonder", "annie", "raj", "marlow", "harry", "chip", "kid", "thunder", "steve",
               "vibe", "dune", "trap", "rubble", "doom", "sam", "sadira", "MC", "miranda", "poppy",
               "jennifer", "jeffer", "sticky", "mr.", "ophelia", "teresa", "raki", "helen", "billy", "rick",
               "chris", "sapur", "rudolf", "selene", "nemea", "keina", "balor", "marion", "odelia", "juris",
               "caesar", "yulie", "miu", "terrence", "oscar", "mike", "vivvenne", "neil"]

# Tuple of game character last names
LAST_NAMES = ["blade", "thornz", "storm", "heart", "blood", "wrath", "soul", "pulse", "dream", "oemn",
              "thirst", "mist", "red", "arma", "pierre", "briggs", "fidel", "biffo", "devil", "beak",
              "trevor", "fryno", "bug", "shadow", "rouser", "stone", "nam", "henry", "clip", "cowan",
              "mitchell", "goodwin", "wofe", "stickler", "justice", "cranley", "miria", "jean", "rufus",
              "hope", "trager", "walker", "stride", "wernicke", "areus", "zofor", "swaya", "dagda",
              "quinn", "linca", "gruden", "grazel", "scardigne", "eldore", "greenbriar", "masan", "tekken",
              "DeSoto", "scootaloo"]

# Display main title
print("""
            Random Character Name Generator

        At the prompt type "q" and hit Enter to exit
        or press Enter to display another name.
      """)

# user input to quit or continue
option = ""

# Used to see if the name choosen is the same as last displayed
oldName = ""

# name genrator will loop until user inputs "q" at prompt
while option.lower() != "q":
    # Pick a random name from the NAMES tuple
    name = random.choice(FIRST_NAMES)
    name += " " + random.choice(LAST_NAMES)

    # Name was not repeated
    if oldName != name:
        oldName = name
        print("\nYour character name is:", name.title())
        option = input("Prompt (q to quit)> ")

    # Name was repeated, pick another one
    else:
        name = random.choice(NAMES)
        option = ""

# User typed "q" to exit
print("\nGoodbye...")
    
