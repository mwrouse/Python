"""
Program......: challenge9_4.py
Author.......: Michael Rouse
Date.........: 2/21/14
Description..: Create a simple adventure game using objects where a player can travel between various,
                connected locations
"""


class Player(object):
    """ Player in the game """
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.traveling = True

    def __str__(self):
        return "You are currently in " + self.location.city
    
    def travel(self, location):
        if location.city == self.location.city:
            # User is already in this city
            print("\nYou are currently in this city")
        else:
            # Change cities
            self.location.leave() # Leave the current city
            self.location = location # Change the city
            self.location.arrive() # Arrive at the new city
            
    # Menu of all the cities
    def mainMenu(self, cities):
        print("\n\nChoose another City to visit\n")
        print("\t1. New York City, United States")
        print("\t2. Paris, France")
        print("\t3. Oslo, Norway")
        print("\t4. End Trip")
        print("\t0. Stay in " + self.location.city)
        userOption = ask_number("Choice> ", 1, 5)
        
        if userOption == 1:
            # Travel to city 1
            self.travel(cities[0])
        elif userOption == 2:
            # Travel to city 2
            self.travel(cities[1])
        elif userOption == 3:
            # Travel to city 3
            self.travel(cities[2])
        elif userOption == 4:
            # End Trip
            print("\n\nYou take the next plane back home and you feel the home sickness rush out of you as you arrive.")
            self.traveling = False
        
class Location(Player):
    """ Class to hold a location """
    def __init__(self, city, country):
        self.city = city
        self.country = country
        
    def __str__(self):
        return str(self.city) + ", " + self.country
    
class New_York_City(Location):
    """ New York City Location """
    def __init__(self):
        super(New_York_City, self).__init__("New York City","United States")

    # New York City Menu
    def whatToDo(self):
        userOption = None
        
        while userOption != 0:
            print("\nYou are in New York City, what would you like to do?\n")
            print("\t1. Visit Central Park")
            print("\t2. Visit Time Square")
            print("\t3. Visit the Statue of Liberty")
            print("\t0. Change Cities")

            # Get user option
            userOption = ask_number("Choice> ", 0, 4)

            if userOption == 1:
                print("\n\nYou visit Central Park and it's absolutely beautiful.")
            elif userOption == 2:
                print("\n\nYou visit Time Square and you're amazed at all it has to offer.")
            elif userOption == 3:
                print("\n\nAs you visit the Statue of Liberty you begin to feel a sudden rush of patriotic thoughts.")
            elif userOption != 0:
                print("\n\nUnknown option, please try again.")

        # User hit 0, return to the main function        

    # Arrive in New York City
    def arrive(self):
        print("\nAs your plane lands in New York City you feel happy to be home after a long trip.")
        #self.whatToDo()
        
    # Leave New York City
    def leave(self):
        print("\nAs you fly out of New York City you smile at the city lights shining bright at night.")
                            
class Paris(Location):
    """ Paris Location """
    def __init__(self):
        super(Paris, self).__init__("Paris", "France")

    # Paris Menu
    def whatToDo(self):
        userOption = None

        while userOption != 0:
            print("\nYou are in Paris, what would you like to do?\n")
            print("\t1. Visit an Art Museum")
            print("\t2. Visit Monuments")
            print("\t3. Have a Nice Dinner")
            print("\t0. Change Cities")

            # Get user option
            userOption = ask_number("Choice>", 0, 4)

            if userOption == 1:
                # Visit art museum
                print("\n\nYou visit all the most famous art mesuems and you have a new found love for classic art.")
            elif userOption == 2:
                # Visit monuments
                print("\n\nYou go around the city visiting all the popular monuments such as the Eiffel Tower.")
            elif userOption == 3:
                # Nice dinner
                print("\n\nYou treat yourself to a nice dinner at a restraunt in the heart of Paris.")
            elif userOption != 0:
                # Unknown Option
                print("\n\nUnknown option, please try again.")
        # User hit 0, return to main function

    # Arrive in Paris
    def arrive(self):
        print("\nAs the plan lands you can hardly control your excitement about being in Paris.")

    # Leave Paris
    def leave(self):
        print("\nThe flight attendants have a hard drive getting you on the plane because you don't want to leave.")
    
class Oslo(Location):
    """ Oslo Location """
    def __init__(self):
        super(Oslo, self).__init__("Oslo", "Norway")

    # Oslo Menu
    def whatToDo(self):
        userOption = None

        while userOption != 0:
            print("\n\nYou are in Oslo, what would you like to do?\n")

            # Get user input
            userOption = ask_number("Choice> ", 0, 4)
            
        # user hit 0, return to main function for main menu

    # Arrive in Oslo
    def arrive(self):
        print("\nAs you arrive in Oslo you are amazed at the breath-taking landscape.")

    # Leave Oslo
    def leave(self):
        print("\nAs your flight leaves the beatiful city of Oslo a tear runs down your face.")

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def main():
    print("\tWelcome to Python Traveler!\n")

    # Create cities
    NEW_YORK_CITY = New_York_City()
    PARIS = Paris()
    OSLO = Oslo()
    
    # Create player
    player = Player(input("What is your name? "), NEW_YORK_CITY)
    
    # Loop until the user is done traveling
    while player.traveling:
        player.mainMenu([NEW_YORK_CITY, PARIS, OSLO])

        if player.traveling:
            player.location.whatToDo()
    
        


main()
input("\n\nPress the Enter key to exit.")
