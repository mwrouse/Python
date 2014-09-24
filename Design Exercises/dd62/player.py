"""
    Program......: player.py
    Author.......: Michael Rouse
    Date.........: 3/19/14
    Description..: Module for player class in dd61
"""
from livewires import games, color
from random import randint
from damageLabel import *

# CLASS ====================================
# Name.........: Player
# Description..: Class for any player
# Syntax.......: Player(name[, minimum HP[, maximum HP]])
# ==========================================
class Player(games.Sprite, object):
    # Player
    def __init__(self, name, classType="Player", image=""):
        super(Player, self).__init__(image=games.load_image(image), x=150, y=350, dx=0, dy=0)
        
        self.name = name.title()
        self.status = "Alive"
        self.health = randint(20, 45)
        self.money = 0
        self.type = classType

        self.alive = True
        self.moving = False
        self.attacking = False
        self.attackDelay = 0
        
        # label for health info
        self.lblHP = games.Text(value="HP: " + str(self.health), size=30, x=self.x, y=self.top - 20, color=color.white)
        games.screen.add(self.lblHP)
                
    # Print the status of the Player
    def __str__(self):
        statusInfo = "\n  Name: " + self.name + "\nStatus: " + self.status + \
        "\n    HP: " + str(self.health) + "\n  Gold: " + str(self.money)
        
        return statusInfo

    # Display Health above the character
    def update_label(self):
        self.lblHP.value = "HP: " + str(self.health)

        if not self.alive:
            self.lblHP.value = "DEAD"
            self.lblHP.color = color.red
        
    # Attack an enemy
    def attack(self, enemy, minDamage=1, maxDamage=6):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.dx = 1
            self.moving = True
            
            self.attacking = True
            
            # Random amount of damage points (1-6)
            damage = randint(minDamage, maxDamage)
            
            # Print information on the attack
            print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + ".")

            enemy.get_hurt(damage) # Do damage to the enemy
    
    # Inflict damage to Player
    def get_hurt(self, damage):
        DamageLabel(damage, self.x, self.top - 30, 200)
        
        self.health -= damage

        if self.health < 1:
            self.health = 0
            self.status = "dead"
            self.alive = False
            
            print("\n" + self.name + " has died!")


    # Update Method
    def update(self):
        """ Display Information When the "F1" key is hit """
        if self.moving:
            if self.x >= 200:
                self.dx = -1
                
            elif self.x <= 149:
                self.dx = 0
                self.moving = False
                self.x = 150

        self.lblHP.x = self.x

    # Perfom this everytime the frame is refreshed
    def tick(self):
        # Perform the attack delay
        if self.attacking:
            if self.attackDelay < 30:
                self.attackDelay += 1
            else:
                self.attackDelay = 0
                self.attacking = False
                
        self.update_label()
        
                
        
# CLASS ====================================
# Name.........: Cleric
# Description..: Class for any cleric (Player is the derived class)
# Syntax.......: Cleric(name[, minimum HP[, maximum HP]])
# ==========================================
class Cleric(Player):
    image = "sprites\cleric.png"
    def __init__(self):
        super(Cleric, self).__init__("Player", classType="Cleric", image=Cleric.image)
            
    # Heal the Cleric
    def special(self, enemy):
        if not self.attacking:
            self.moving = False
            self.attacking = True
            
            heal = (randint(1, 8))
            self.health += (randint(1, 8))

            print("\n" + self.name + " heals himself by " + str(heal) + " health points.")


# CLASS ====================================
# Name.........: Knight
# Description..: Class for a knight
# Syntax.......: Knight(name[, minimum HP[, maximum HP]])
# ==========================================
class Knight(Player):
    image = "sprites\knight.png"

    def __init__(self):
        super(Knight, self).__init__("Player", classType="Cleric", image=Knight.image)
        
    # Knight's Smite attack
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.dx = 1
            self.moving = True

            self.attacking = True
            damage = randint(12, 20)

            print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using Smite.")

            enemy.get_hurt(damage) # Do damage to the enemy


# CLASS ====================================
# Name.........: Thief
# Description..: Class for a thief
# Syntax.......: Thief(name[, minimum HP[, maximum HP]])
# ==========================================
class Thief(Player):
    image = "sprites\thief.png"

    def __init__(self):
        super(Thief, self).__init__("Player", classType="Thief", image=Thief.image)
        
    # Thief's Steal
    def special(self):
        if not self.attacking:
            self.attacking = True
            stolen = randint(1, 10)
            self.money += stolen

            print("\n" + self.name + " steals " + str(stolen) + " gold pieces.")
    

# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")

