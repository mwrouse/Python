"""
    Program......: monster.py
    Author.......: Michael Rouse
    Date.........: 3/19/14
    Description..: Module for the Monster classes in dd61
"""
from livewires import *

# CLASS ====================================
# Name.........: Damage Label
# Description..: Shows a damage label
# Syntax.......: DamageLabel(damage, xPos, yPos, endY)
# ==========================================
class DamageLabel(games.Sprite):
    def __init__(self, damage, xPos, yPos, endY):
        super(DamageLabel, self).__init__(image=games.load_image("sprites\game.png"), x=0, y=0)

        self.endY = endY
        self.label = games.Text(value="-" + str(damage), size=30, x=xPos, y=yPos, dy=-.5, color=color.red)
        games.screen.add(self.label)
        games.screen.add(self)

    def update(self):
        if self.label.y <= self.endY:
            self.label.destroy()
            self.destroy()
