"""
    Program......: challenge11_2_kryptonite.py
    Author.......: Michael Rouse
    Date.........: 3/18/14
    Description..: Kryptonite class for challenge11_2.py
"""
from livewires import games, color
from random import randint

# CLASS ====================================
# Name.........: Kryptonite
# Description..: Class for Kryptonite
# Syntax.......: Kryptonite()
# ==========================================
class Kryptonite(games.Sprite):
    """ kryptonite """
    speed = 1
    
    def __init__(self):
        # Load the sprite
        self.SPRITE = games.load_image("sprites\kryptonite\kryptonite.png", transparent=True)
        
        super(Kryptonite, self).__init__(image=self.SPRITE, x=randint(20, 620), y=100, dx=0, dy=1)

    # METHOD ===================================
    # Name.........: Update
    # Description..: Change location of the Kryptonite
    # Syntax.......: n/a
    # ==========================================
    def update(self):
        # Explode if at bottom of the screen
        if self.bottom == 480:
            self.explode()
            
    # METHOD ===================================
    # Name.........: Explosion
    # Description..: Display explosion animation and destroy Kryptonite
    # Syntax.......: explode()
    # ==========================================
    def explode(self):
        self.dx = 0
        self.dy = 0
        self.destroy()

        # Display explosion
        explosion_files = ["sprites\kryptonite\explosion\kryptonite_explode1.png",
                           "sprites\kryptonite\explosion\kryptonite_explode2.png",
                           "sprites\kryptonite\explosion\kryptonite_explode3.png",
                           "sprites\kryptonite\explosion\kryptonite_explode4.png",
                           "sprites\kryptonite\explosion\kryptonite_explode5.png",
                           "sprites\kryptonite\explosion\kryptonite_explode6.png"]

        explosion = games.Animation(images=explosion_files, x=self.x, y=self.y, n_repeats=1, repeat_interval=4.5)
        games.screen.add(explosion)

# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
