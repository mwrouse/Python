"""
    Program......: monster.py
    Author.......: Michael Rouse
    Date.........: 3/19/14
    Description..: Module for the Monster classes in dd61
"""
from random import randint
from livewires import games, color
from damageLabel import *

# CLASS ====================================
# Name.........: Monster
# Description..: Class for monsters
# Syntax.......: Monster(name[, minimum HP[, maximum HP]])
# ==========================================
class Monster(games.Sprite):
    # Monster initializer
    def __init__(self, name, minHP=20, maxHP=53, image="", x=450, y=250, dx=0, dy=1):
        self.name = name.title()
        self.status = "Alive"
        self.health = randint(minHP, maxHP)

        self.alive = True
        self.moving = False
        self.attacking = False
        self.attackDelay = 0
                
        super(Monster, self).__init__(image=games.load_image(image, transparent=True), x=x, y=y, dx=dx, dy=dy)

        # Health label
        self.lblHP = games.Text(value="HP: " + str(self.health), size=30, x=self.x, y=self.top - 20, color=color.white)
        games.screen.add(self.lblHP)

    # Print the status of the Monster
    def __str__(self):
        statusInfo = "\n  Name: " + self.name + "\nStatus: " + self.status + \
        "\n    HP: " + str(self.health)
        
        return statusInfo

    # Display Health for Monster
    def update_label(self):
        self.lblHP.value = "HP: " + str(self.health)

        if not self.alive:
            self.lblHP.value = "DEAD"
            self.lblHP.color = color.red
        
    # Attack an enemy
    def attack(self, enemy, minDamage=1, maxDamage=6):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.dx = -1
            self.moving = True
            
            # R&&om amount of damage points (1-6)
            damage = randint(minDamage, maxDamage)
            
            # Print information on the attack
            print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + ".")

            enemy.get_hurt(damage)
            self.attacking = True

    # Inflict damage to Monster
    def get_hurt(self, damage):
        DamageLabel(damage, self.x, self.top - 30, self.top - 50)
        
        self.health -= damage

        if self.health < 1:
            self.health = 0
            self.status = "dead"
            self.alive = False
            
            print("\n" + self.name + " has died!")

    # Update Method
    def update(self):
        if self.moving:
            if self.x <= 400:
                self.dx = 1
                
            elif self.x >= 451:
                self.dx = 0
                self.x = 450
                
                self.moving = False
                
        self.lblHP.x = self.x
                
    # Do this every time the frame is refreshed
    def tick(self):
        if self.attacking:
            if self.attackDelay < 30:
                self.attackDelay += 1
            else:
                self.attackDelay = 0
                self.attacking = 0
                
        self.update_label()

# CLASS ====================================
# Name.........: Red_Dragon
# Description..: Class for a Red Dragon
# Syntax.......: Red_Dragon()
# ==========================================
class Red_Dragon(Monster):
    image = "sprites\dragon.png"

    def __init__(self):
        super(Red_Dragon, self).__init__(name="Red Dragon", image=Red_Dragon.image)
        
    # Fire Breath
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True

            # R&&om damage (6-12 points)
            damage = randint(6, 12)
        
            print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using fire breath.")
            enemy.get_hurt(damage)

    # Update method to move the dragon
    def update(self):
        if self.y > 270:
            self.dy = -1
        elif self.y < 230:
            self.dy = 1

        super(Red_Dragon, self).update()

# CLASS ====================================
# Name.........: White_Dragon
# Description..: Class for a white dragon
# Syntax.......: White_Dragon()
# ==========================================
class White_Dragon(Monster):
    image = "sprites\white_dragon.png"

    def __init__(self):
        super(White_Dragon, self).__init__(name="White Dragon", image=White_Dragon.image)
        
    # Ice Breath Attack
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            # R&&om damage (2-8 points)
            self.attacking = True
            
            damage = randint(2, 8)
            
            print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using ice breath.")

            enemy.get_hurt(damage)

    # Update method to move the dragon
    def update(self):
        if self.y > 270:
            self.dy = -1
        elif self.y < 230:
            self.dy = 1

        super(White_Dragon, self).update()

# CLASS ====================================
# Name.........: Gonlin
# Description..: Class for a Goblin
# Syntax.......: Goblin()
# ==========================================
class Goblin(Monster):
    image = "sprites\goblin.png"
    
    # Initialize
    def __init__(self):
        super(Goblin, self).__init__(name="Goblin", image=Goblin.image, x=450, y=350, dy=0)
        
    # Scream Attack
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True
            self.dx = -1
            self.moving = True

            damage = randint(6, 10)
        
            print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using its special.")

            enemy.get_hurt(damage)


# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (&& did not 'import' it).")
    input("\n\nPress the enter key to exit.")
