"""
    Program......: dd53_monster.py
    Author.......: Michael Rouse
    Date.........: 2/26/14
    Description..: Module for the Monster classes in dd53
"""
from random import randint
from livewires import games, color

# CLASS ====================================
# Name.........: Monster
# Description..: Class for monsters
# Syntax.......: Monster(name[, minimum HP[, maximum HP]])
# ==========================================
class Monster(games.Sprite, object):
    # Monster initializer
    def __init__(self,name,minHP=3,maxHP=13, image=""):
        self.name = name.title()
        self.status = "Alive"
        self.health = randint(minHP, maxHP)
        self.sprite = None
        super(Monster, self).__init__(image=games.load_image(image), x=450, y=250, dx=0, dy=1)

    # Print the status of the Monster
    def __str__(self):
        statusInfo = "\n  Name: " + self.name + "\nStatus: " + self.status + \
        "\n    HP: " + str(self.health)
        
        return statusInfo

    # Attack an enemy
    def attack(self,enemy,minDamage=1,maxDamage=6):
        # Random amount of damage points (1-6)
        damage = randint(minDamage, maxDamage)
        
        enemy.get_hurt(damage) # Do damage to the enemy
        
        # Print information on the attack
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name)

    # Inflict damage to Monster
    def get_hurt(self,damage):
        self.health -= damage

        if self.health < 1:
            self.health = 0
            self.status = "dead"

# CLASS ====================================
# Name.........: Red_Dragon
# Description..: Class for a Red Dragon
# Syntax.......: Red_Dragon(name)
# ==========================================
class Red_Dragon(Monster):
    # Breathe fire
    def attack(self, enemy):
        # Random damage (6-12 points)
        damage = randint(6, 12)
        enemy.get_hurt(damage)
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using fire breath")

    # Update method to move the dragon
    def update(self):
        if self.y > 270:
            self.dy = -1
        elif self.y < 230:
            self.dy = 1

# CLASS ====================================
# Name.........: White_Dragon
# Description..: Class for a white dragon
# Syntax.......: White_Dragon(name)
# ==========================================
class White_Dragon(Red_Dragon):
    # Breathe ice
    def attack(self, enemy):
        # Random damage (2-8 points)
        damage = randint(2, 8)
        enemy.get_hurt(damage)
        print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using ice breath")

# CLASS ====================================
# Name.........: Gonlin
# Description..: Class for a Goblin
# Syntax.......: Goblin(name[, minimum HP[, maximum HP]])
# ==========================================
class Goblin(Monster):
    # Initialize
    def __init__(self, name, minHP=1,maxHP=8):
        super(Goblin, self).__init__(name,minHP,maxHP)

    # Goblin attack
    def attack(self, enemy):
        if randint(1, 2) == 1:
            # Use regular attack
            super(Goblin, self).attack(enemy, 1, 6)
        else:
            # Use scream attack
            self.scream_attack(enemy)
        
    # Scream Attack
    def scream_attack(self, enemy):
        print("\n" + self.name + " does 3 damage to " + enemy.name + " using scream attack")
        enemy.get_hurt(3)


# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
