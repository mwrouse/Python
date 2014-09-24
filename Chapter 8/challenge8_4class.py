"""
    Program: challenge8_4class.py
    Author: Michael Rouse
    Date: 12/12/13
    Description: Class object for challenge8_4.py
"""
class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        return ""
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print(self.name + " is " + self.mood + ".")
        self.__pass_time()
    
    def eat(self, food=4):
        print("Brruppp! " + self.name + " has been feed.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Wheee! " + self.name + " had lots of fun.")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
