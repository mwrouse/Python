"""
    Program......: challenge11_2_superman.py
    Author.......: Michael Rouse
    Date.........: 3/18/14
    Description..: Superman class for challenge11_2.py
"""
from livewires import games, color
from kryptonite import *

# CLASS ====================================
# Name.........: Superman
# Description..: Class for superman character
# Syntax.......: Superman()
# ==========================================
class Superman(games.Sprite):
    """ Superman """
    def __init__(self):
        # Load Sprites
        self.LEFTSPRITE = games.load_image("sprites\superman\superman_left.png", transparent=True)
        self.RIGHTSPRITE = games.load_image("sprites\superman\superman_right.png", transparent=True)
        
        super(Superman, self).__init__(image=self.RIGHTSPRITE, x=games.mouse.x, y=410, dx=0, dy=0)

        self.timer = 0
        self.facing = 1
        self.time_til_drop = 0
        self.dead = False
        self.playing = False # Used to tell if the instructions have been displayed yet

        # Display game Instructions
        self.lbl_instructs = games.Text(value="Avoid The Kryptonite", size=80, x=320, y=250, color=color.white)
        games.screen.add(self.lbl_instructs)
        
    # METHOD ===================================
    # Name.........: Update
    # Description..: Change location of sprite/direction
    # Syntax.......: n/a
    # ==========================================
    def update(self):
        if games.mouse.x < self.x:
             self.facing = 0 # Left
             
        elif games.mouse.x > self.x: 
            self.facing = 1 # Right

        # Update the sprite
        self.update_sprite()

        if not self.dead:
            self.x = games.mouse.x
            
        self.check_impact()

        if self.dead:
            if self.bottom < 500:
                self.dy = 1
            else:
                self.dy = 0
                
        # Only spawn kryptonite after instructions have gone away
        if self.playing:
            self.spawn_kryptonite()


    # METHOD ===================================
    # Name.........: Update Sprite
    # Description..: Display the correct sprite based on location
    # Syntax.......: update_sprite()
    # ==========================================
    def update_sprite(self):
        # Check if Dead
        if self.facing == 0:
            # Left
            self._surface = self.LEFTSPRITE
                
        else:
            # Right
            self._surface = self.RIGHTSPRITE
            
    # METHOD ===================================
    # Name.........: Check For Impact
    # Description..: Check if Kryptonite has hit Superman
    # Syntax.......: check_impact()
    # ==========================================
    def check_impact(self):
        for item in self.overlapping_sprites:
            item.explode()
            self.game_over()

    # METHOD ===================================
    # Name.........: Spawn Kryptonite
    # Description..: Soawn new Kryptonite on the screen
    # Syntax.......: spawn_kryptonite()
    # ==========================================
    def spawn_kryptonite(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
            
        else:
            # Spawn new Kryptonite
            new_kryptonite = Kryptonite()
            games.screen.add(new_kryptonite)
            
            self.time_til_drop = int(62 * 1.3 / 1) + 1

    # METHOD ===================================
    # Name.........: Ticker
    # Description..: Ticks to 5 seconds and displays the instructions
    # Syntax.......: n/a
    # ==========================================
    def tick(self):
        if self.timer < 250:
            self.timer += 1
            
        elif self.timer == 250:
            # Destroy instructions and start playing
            self.lbl_instructs.destroy()
            self.playing = True

    # METHOD ===================================
    # Name.........: Game Over
    # Description..: Displays game over label and destroys Superman
    # Syntax.......: game_over()
    # ==========================================
    def game_over(self):
        self.dead = True
        self.destroy()

        # Show "Game Over" Label
        lbl_gameOver = games.Text(value="Game Over", size=80, x=320, y=250, color=color.white)
        games.screen.add(lbl_gameOver)

        # Release the mouse
        games.mouse.is_visible = True
        games.mouse.event_grab = False

# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
