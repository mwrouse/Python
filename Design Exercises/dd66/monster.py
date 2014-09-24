"""
    Program......: monster.py
    Author.......: Michael Rouse
    Date.........: 4/4/14
    Description..: Module for the Monster classes in dd66
"""
from livewires import games, color
import dice
from damageLabel import *
from random import randint

# CLASS ====================================
# Name.........: Monster
# Description..: Class for monsters
# Syntax.......: Monster(name[, minimum HP[, maximum HP]])
# ==========================================
class Monster(games.Sprite):
    def __init__(self, name="", image="", attackSound="", specialSound="", xPos=450, yPos=250, dX=0, dY=1):
        # Initialize Sprite
        super(Monster, self).__init__(image=games.load_image(image), x=xPos, y=yPos, dx=dX, dy=dY)

        # General Variables
        self.name = name.title()
        self.health = randint(20, 53)
        self.money = dice.roll(20) # Roll d20 for amount of coins owned
        self.alive = True
        self.moving = False

        # Attack Variables
        self.attacking = False
        self.attackDelay = 0
        self.attackBonus = 0
        self.defenseBonus = 10

        # Sounds
        self.attackSound = games.load_sound(attackSound)
        self.specialSound = games.load_sound(specialSound)
        self.deathSound = games.load_sound("sounds/dragon_death.wav")

        # Sprite to show damage was inflicted
        self.damageSprite = games.Sprite(image=games.load_image("sprites/damage.png"), x=self.x, y=self.y)
        self.damageSpriteCounter = -1

        # Sprite to show health info above head
        self.healthLabel = games.Text(value="HP: " + str(self.health), size=30, x=self.x,
                                      y=self.top - 20, color=color.white)
        games.screen.add(self.healthLabel)

    # Update Health Label Above Head
    def update_label(self):
        self.healthLabel.value = "HP: " + str(self.health)

        # Turn label read if not alive
        if not self.alive:
            self.healthLabel.value = "DEAD"
            self.healthLabel.color = color.red

    # Attack an Enemy
    def attack(self, enemy, minDamage=1, maxDamage=6):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True
            
            self.attackSound.play() # play Sound
            
            # Move forwards
            self.moving = True
            self.dx = -1

            # Try and attack the enemy
            if (dice.roll(20) + self.attackBonus) > enemy.defenseBonus:
                # Roll dice to calculate damage
                damage = dice.roll(maxDamage)

                enemy.get_hurt(damage)

                print("\n" + self.name + " does " + str(damage) + " to " + enemy.name + ".")

            else:
                print("\n" + self.name + " attacks " + enemy.name + " but misses!")

    # Inflict Damage
    def get_hurt(self, damage):
        DamageLabel(damage, self.x, self.top - 20, 200) # Show damage points rising above head
        
        # Add Slash Sprite Over Monster
        games.screen.add(self.damageSprite)
        self.damageSpriteCounter = 0

        self.health -= damage

        # Check if Monster is Dead
        if self.health < 1:
            self.alive = False
            self.health = 0

            self.deathSound.play() # Play Death Sound

            print("\n" + self.name + " has been defeated!")

    # Update
    def update(self):
        # Move Monster left and back to original location
        if self.moving:
            if self.x <= 400:
                # Move Monster Backwards
                self.dx = 1

            elif self.x >= 451:
                # Stop Monster (In Original Location)
                self.moving = False
                self.dx = 0
                self.x = 450
        
        # Keep HP Label above Head
        self.healthLabel.x = self.x

    # Tick Method
    def tick(self):
        # Prevent repeated attacks from the keyboard buffer
        if self.attacking:
            if self.attackDelay < 30:
                self.attackDelay += 1

            else:
                self.attacking = False
                self.attackDelay = 0
        
        # Update Damage Sprite location and then remove from screen
        if self.damageSpriteCounter >= 0:
            self.damageSprite.x = self.x
            self.damageSprite.y = self.y

            if self.damageSpriteCounter < 30:
                self.damageSpriteCounter += 1

            else:
                self.damageSpriteCounter = -1
                games.screen.remove(self.damageSprite)

        # Update Health Label
        self.update_label()


# CLASS ====================================
# Name.........: Red_Dragon
# Description..: Class for a Red Dragon
# Syntax.......: Red_Dragon()
# ==========================================
class Red_Dragon(Monster):
    image = "sprites/dragon.png"
    attackSound = "sounds/dragon/attack.wav"
    specialSound = "sounds/dragon/special.wav"

    def __init__(self):
        super(Red_Dragon, self).__init__(name="Red Dragon", image=Red_Dragon.image, attackSound=Red_Dragon.attackSound,
                                         specialSound=Red_Dragon.specialSound)

    # Red Dragon's Special: Fire Breath
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True

            self.specialSound.play() # Play Sound

            # Show attack Movement
            self.moving = True
            self.dx = -1

            # Try and attack enemy
            if (dice.roll(20) + self.attackBonus) > enemy.defenseBonus:
                # Roll d212 to calculate damage
                damage = dice.roll(12)

                enemy.get_hurt(damage)

                print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using fire breath.")

            else:
                print("\n" + self.name + " attacks " + enemy.name + " but misses!")

    # Update
    def update(self):
        if self.y > 270:
            # Move dragon back up
            self.dy = -1

        elif self.y < 230:
            # Move dragon down
            self.dy = 1

        super(Red_Dragon, self).update()

# CLASS ====================================
# Name.........: White_Dragon
# Description..: Class for a white dragon
# Syntax.......: White_Dragon()
# ==========================================
class White_Dragon(Monster):
    image = "sprites/white_dragon.png"
    attackSound = "sounds/dragon/attack.wav"
    specialSound = "sounds/dragon/special.wav"

    def __init__(self):
        super(White_Dragon, self).__init__(name="White Dragon", image=White_Dragon.image, attackSound=White_Dragon.attackSound,
                                         specialSound=White_Dragon.specialSound)

    # White Dragon's Special: Ice Breath
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True

            self.specialSound.play() # Play Sound

            # Show attack Movement
            self.moving = True
            self.dx = -1

            # Try and attack enemy
            if (dice.roll(20) + self.attackBonus) > enemy.defenseBonus:
                # Roll d212 to calculate damage
                damage = dice.roll(12)

                enemy.get_hurt(damage)

                print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using ice breath.")

            else:
                print("\n" + self.name + " attacks " + enemy.name + " but misses!")

    # Update
    def update(self):
        if self.y > 270:
            # Move dragon back up
            self.dy = -1

        elif self.y < 230:
            # Move dragon down
            self.dy = 1

        super(White_Dragon, self).update()

# CLASS ====================================
# Name.........: Goblin
# Description..: Class for a Goblin
# Syntax.......: Goblin()
# ==========================================
class Goblin(Monster):
    image = "sprites/goblin.png"
    attackSound = "sounds/goblin/attack.wav"
    specialSound = "sounds/goblin/special.wav"

    def __init__(self):
        super(Goblin, self).__init__(name="Goblin", image=Goblin.image, attackSound=Goblin.attackSound,
                                     specialSound=Goblin.specialSound, xPos=450, yPos=350, dY=0)

    # Goblin's Special: Scream
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True

            self.specialSound.play() # Play Sound

            # Attack Movement
            self.moving = True
            self.dx = -1

            # Try and Attack Enemy
            if (dice.roll(20) + self.attackBonus) > enemy.defenseBonus:
                # Roll d10 for damage
                damage = dice.roll(10)

                enemy.get_hurt(damage)

                print("\n" + self.name + " does " + str(damage) + " to " + enemy.name + " using Scream!")

            else:
                print("\n" + self.name + " attacks " + enemy.name + " but misses!")



# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (did not 'import' it).")
    input("\n\nPress the enter key to exit.") 
