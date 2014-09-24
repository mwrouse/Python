"""
    Program......: player.py
    Author.......: Michael Rouse
    Date.........: 4/4/14
    Description..: Module for player class in dd66
"""
from livewires import games, color
import dice
from damageLabel import *
from random import randint

# CLASS ====================================
# Name.........: Player
# Description..: Class for any player
# Syntax.......: Player(name[, minimum HP[, maximum HP]])
# ==========================================
class Player(games.Sprite):
    def __init__(self, name, image="", attackSound="", specialSound=""):
        # Initialize Sprite
        super(Player, self).__init__(image=games.load_image(image), x=150, y=350, dx=0, dy=0)

        # General Variables
        self.name = name.title()
        self.health = randint(20, 45) # Random amount of health
        self.money = dice.roll(2) # Roll d20 for amount of coins owned
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
        self.deathSound = games.load_sound("sounds/death.wav")

        # Sprite to show damage inflicted
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
            
            self.attackSound.play() # Play Sound

            # Move forwards
            self.moving = True
            self.dx = 1

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
        
        # Add Slash Sprite Over Character
        games.screen.add(self.damageSprite)
        self.damageSpriteCounter = 0

        self.health -= damage

        # Check if Player is Dead
        if self.health < 1:
            self.alive = False
            self.health = 0

            self.deathSound.play() # Play Death Sound

            print("\n" + self.name + " has been defeated!")

    # Update
    def update(self):
        # Move Character Forwards And Then Backwards
        if self.moving:
            if self.x >= 200:
                # Move Player Backwards
                self.dx = -1

            elif self.x <= 149:
                # Stop Character (In Original Location)
                self.moving = False
                self.dx = 0
                self.x = 150
        
        self.healthLabel.x = self.x # Keep HP Label above player's head

    # Tick Method
    def tick(self):
        # Prevent from repeated attacks from keyboard buffer
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
# Name.........: Cleric
# Description..: Class for any cleric (Player is the derived class)
# Syntax.......: Cleric(name[, minimum HP[, maximum HP]])
# ==========================================
class Cleric(Player):
    image = "sprites/cleric.png"
    attackSound = "sounds/cleric/attack.wav"
    specialSound = "sounds/cleric/special.wav"
    
    def __init__(self):
        super(Cleric, self).__init__("Player", image=Cleric.image, attackSound=Cleric.attackSound,
                                     specialSound=Cleric.specialSound)


    # Cleric's Special: Healting
    def special(self, enemy):
        if (not self.attacking) and (self.alive):
            self.moving = False
            self.attacking = True

            heal = dice.roll(8) # Roll d8 for health points

            self.health += heal

            print("\n" + self.name + " heals himself by " + str(heal) + " health points.")


# CLASS ====================================
# Name.........: Knight
# Description..: Class for a knight
# Syntax.......: Knight(name[, minimum HP[, maximum HP]])
# ==========================================
class Knight(Player):
    image = "sprites/knight.png"
    attackSound = "sounds/knight/attack.wav"
    specialSound = "sounds/knight/special.wav"

    def __init__(self):
        super(Knight, self).__init__("Player", image=Knight.image, attackSound=Knight.attackSound,
                                     specialSound=Knight.specialSound)

    # Knight's Special: Smite
    def special(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True
            
            self.specialSound.play() # Play Sound

            # Show attack movement
            self.moving = True
            self.dx = 1

            # Try and attack the enemy
            if (dice.roll(20) + self.attackBonus) > enemy.defenseBonus:
                # Roll dice to calculate damage
                damage = dice.roll(maxDamage)

                enemy.get_hurt(damage)

                print("\n" + self.name + " does " + str(damage) + " damage to " + enemy.name + " using Smite!")

            else:
                print("\n" + self.name + " attacks " + enemy.name + " but misses!")
                
# CLASS ====================================
# Name.........: Thief
# Description..: Class for a thief
# Syntax.......: Thief(name[, minimum HP[, maximum HP]])
# ==========================================
class Thief(Player):
    image = "sprites/thief.png"
    attackSound = "sounds/thief/attack.wav"
    specialSound = "sounds/thief/special.wav"

    def __init__(self):
        super(Thief, self).__init__("Player", image=Thief.image, attackSound=Thief.attackSound,
                                    specialSound=Thief.specialSound)

    # Thief's Specail: Steal
    def specia(self, enemy):
        if (not self.attacking) and (self.alive) and (enemy.alive):
            self.attacking = True

            stolen = dice.roll(enemy.money) # Try and steal from enemy

            self.money += stolen

            print("\n" + self.name + " steals " + str(stolen) + " gold coins from " + enemy.name + ".")

            
# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")






        
        
        
        
