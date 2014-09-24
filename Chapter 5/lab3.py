"""
    Program: lab3.py
    Author: Michael Rouse
    Date: 10/7/13
    Description: Randomly picks a first name, last name, race, class, and alignment for an RPG
                 character generator
"""
import random

# Tuple of first names
FIRST_NAMES = ("dark", "fire", "midnight", "shadow", "silent", "demon", "black", "death", "fury", "white",
               "sin", "dawn", "wonder", "annie", "raj", "marlow", "harry", "chip", "kid", "thunder", "steve",
               "vibe", "dune", "trap", "rubble", "doom", "sam", "sadira", "MC", "miranda", "poppy",
               "jennifer", "jeffer", "sticky", "mr.", "ophelia", "teresa", "raki", "helen", "billy", "rick",
               "chris", "sapur", "rudolf", "selene", "nemea", "keina", "balor", "marion", "odelia", "juris",
               "caesar", "yulie", "miu", "terrence", "oscar", "mike", "vivvenne", "neil")

# Tuple of last names
LAST_NAMES = ("blade", "thornz", "storm", "heart", "blood", "wrath", "soul", "pulse", "dream", "oemn",
              "thirst", "mist", "red", "arma", "pierre", "briggs", "fidel", "biffo", "devil", "beak",
              "trevor", "fryno", "bug", "shadow", "rouser", "stone", "nam", "henry", "clip", "cowan",
              "mitchell", "goodwin", "wofe", "stickler", "justice", "cranley", "miria", "jean", "rufus",
              "hope", "trager", "walker", "stride", "wernicke", "areus", "zofor", "swaya", "dagda",
              "quinn", "linca", "gruden", "grazel", "scardigne", "eldore", "greenbriar", "masan", "tekken",
              "DeSoto", "scootaloo")

# Tuple of races
RACES = ("dwarf", "elf", "gnome", "half elf", "half orc", "halfing", "human")

# Tuple of classes
CLASSES = ("barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue",
         "sorcerer", "wizard")

# Tuple of alignments
BASE_ALIGNMENTS = ("good", "neutral", "evil")
ALIGNMENTS = ("lawfaul", "neutral", "chaotic")

# Display main title
print("""
               RPG CHARACTER GENERATOR

        At the prompt type "q" and hit Enter to exit
        or press Enter to display another name.
      """)

# user input to quit or continue
option = ""

# main loop will loop until user inputs "q" at prompt
while option.lower() != "q":
    
    # String for finished character, will reset every loop
    # character = (First name, Last name, Race, Class, Alignment)
    character =  []
    
    # Generate character info
    firstName = random.choice(FIRST_NAMES)
    lastName = random.choice(LAST_NAMES)
    race = random.choice(RACES)
    charClass = random.choice(CLASSES)
    alignment = random.choice(BASE_ALIGNMENTS) + " " + random.choice(ALIGNMENTS)

    if alignment == "neutral nuetral":
        alignment = "neutral"

    # Add character info to character list
    character.append(firstName.title())
    character.append(lastName.title())
    character.append(race.title())
    character.append(charClass.title())
    character.append(alignment.title())  

    print("\nHere is your RPG character:\n")
    for i in range(0, len(character)):
        if i == 0:
            title = "\tFirst Name:"
        elif i == 1:
            title = "\t Last Name:"
        elif i == 2:
            title = "\t      Race:"
        elif i == 3:
            title = "\t     Class:"
        elif i == 4:
            title = "\t Alignment:"

        print (title, character[i])
    
    option = input("\nPrompt (q to quit)> ")


# User typed "q" to exit
print("\nGoodbye...")
    
