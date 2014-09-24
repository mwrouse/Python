from random import randint

class Player(object):
    """ simple player object """

    def __init__(self, name="", occ="", race=""):
        if name == "":
            self.name = input("Name? ")
        else:
            self.name = name
            
        if occ == "":
            self.__occ = input("Occupation? ")
        else:
            self.__occ = occ
            
        if race == "":
            self.__race = input("Race? ")
        else:
            self.__race = race
            
        self.__health = randint(1,10)
        self.__defense = randint(1,3)
        self.__attack = randint(1,3)
        self.__armor = ["",0]
        self.__weapon = ["",0]

        # Modifiers
        if self.__race == "Dwarf":
            self.__defense += 2

        if self.__occ == "Fighter":
            self.__attack += 2

        # Generate valid list of commands
        self.__validCommands = ("die", "attack")
        
    def report(self):
        """ report condition to outside world """
        print("My name is:", self.name)
        print("I'm a", self.__race, self.__occ)
        print("My health is:", self.__health)

    def hit(self):
        total = self.__attack + self.__weapon[1]
        return total

    def get_hit(self,damage):
        totalDef = self.__defense + self.__armor[1]
        if damage > totalDef:
            self.__health -= totalDef
        print("OW!")

    def get_weapon(self, name, damage):        
        self.__weapon = [name, damage] 

    def get_armor(self, name, defense):
        self.__armor = [name, defense]

    def do_command(self,commands):
        """ Parse Player Commands """
        # For each command in the commands tuple
        for command in commands:
            if command.lower() in self.__validCommands:
                # Command is valid, perform an action
                print("Command:", command.title())
            else:
                # Command is not valid, inform player
                print("Sorry, \"" + command.title() + "\" is not a valid command.")

    if __name__ == "__main__":
        print("Run another module")
