class Player(object):
    ''' simple player object '''

    def __init__(self):
        self.name = input("Name? ")
        self.__occ = input("Occupation? ")
        self.__race = input("Race? ")
        self.__health = randint(1,10)
        self.__defense = randint(1,3)
        self.__attack = randint(1,3)
        self.__armor = ["",0]
        self.__weapon = ["",0]

        #modifiers
        if self.__race == "Dwarf":
            self.__defense += 2

        if self.__occ == "Fighter":
            self.__attack += 2

    def report(self):
        ''' report condition to outside world '''
        print("My name is:", self.name)
        print("I'm a",self.__race,self.__occ)
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
        #print("You pick up a " + name + ", it can do " + str(damage) + " damage.")
        self.__weapon = [name, damage] 

    def get_armor(self, name, defense):
        #print("You pick up " + name + " armor, which adds " + str(defense) + " defense.")
        self.__armor = [name, defense]
        
