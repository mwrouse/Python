"""
    Program......: challenge12_2.py
    Author.......: Michael Rouse
    Date.........: 3/25/14
    Description..: Create a version of Simon Says using random numbers and colors



#########################################################
    BEWARE OF THE CODE BELOW! 

    IT'S A FRIGGIN' MESS!
    I DON'T KNOW WHAT HAPPENED! 
    IT'S SO SLOPPY AND LAZY!
    JUST BE CAREFUL READING IT.
    
    THERE ARE AT LEAST THREE PLACES WHERE I COULD USE
    A METHOD INSTEAD I JUST COPIED AND PASTED THE CODE!
    OOPS!
#########################################################
"""
from livewires import games, color
import pygame.display
from random import randint

# Setup game window
games.init(screen_width=640, screen_height=480, fps=50)
pygame.display.set_caption("Simon Says")
games.screen.background = games.load_image("background.png", transparent=False)

# CLASS ====================================
# Name.........: Square
# Description..: Class for colored Square
# Syntax.......: Square()
# ==========================================
class Square(games.Sprite):
    def __init__(self, color, x, y):
        self.default = games.load_image("Sprites/" + color + ".png", transparent=False)
        
        super(Square, self).__init__(image=self.default, x=x, y=y)
        games.screen.add(self)

        self.flashImage = games.load_image("Sprites/" + color + "1.png", transparent=False)
        
        self.flashTimer = 0
        self.flashing = False

    def flash(self):
        """ Flash The Square """
        self._replace(self.flashImage)
        self.flashing = True

    def tick(self):
        """ Make Sure the Square doesn't stay lite up """
        if self.flashing:
            if self.flashTimer >= 25:
                # Restore the regular square
                self.flashing = False
                self.flashTimer = 0
                self._replace(self.default)

            else:
                self.flashTimer += 1
        
# CLASS ====================================
# Name.........: Simon
# Description..: Class for Simon Says Game
# Syntax.......: Simon()
# ==========================================
class Simon(games.Sprite):
    def __init__(self):
        super(Simon, self).__init__(image=games.load_image("Sprites/blank.png"), x=0, y=0)
        
        self.playing = False # True when player needs to enter input
        self.started = False # True when game has started
        
        self.startTimer = 0

        self.flashWait = 0
        self.flashing = False
        self.correct = False
        self.correctCount = 0
        self.wrong = False
        self.wrongCount = 0
        
        self.sequence = [0, 0, 0, 0] # The Sequence that the user needs to duplicateds
        self.sequenceLength = len(self.sequence) # Length of the sequence (will increase)
        self.index = -1
        self.checkIndex = 0

        self.keyDelay = 0

        self.sequenceTimer = 0 # How long it took the computer to perform the sequence
        self.playerTimer = 0 # How long it takes the player to perform the sequence

        # Display the title on the screen
        games.screen.add(games.Text(value="SIMON SAYS", size=80, x=320, y=50, color=color.red))

        # Countdown to start the game
        self.countdown = 3
        self.lblCountdown = games.Text(value=self.countdown, size=85, x=325, y=270, color=color.blue)
        games.screen.add(self.lblCountdown)

        self.lblGo = games.Text(value="GO!", size=55, x=325, y=250, color=color.black)

        
        # Fail Label
        self.lblFail = games.Text(value="FAIL!", size=55, x=325, y=250, color=color.black)
        self.lblCorrect = games.Text(value="CORRECT!", size=55, x=325, y=250, color=color.black)
        # Generate Colored Squares
        self.green = Square(color="green", x=150, y=170)
        self.blue = Square(color="blue", x=500, y=170)
        self.red = Square(color="red", x=150, y=350)
        self.yellow = Square(color="yellow", x=500, y=350)

        # List of the squares (for easy access)
        self.squares = [4, self.green, self.blue, self.red, self.yellow]
        
        # Colors
        self.colors = [3, "green", "blue", "red", "yellow"]

    def create_sequence(self):
        print("\nGenerating A New Sequence!\n")

        # Generate a new sequence
        for i in range(0, len(self.sequence)):
            # Generate a new number (color) for that spot in the sequence
            self.sequence[i] = randint(1, 4)

        print("The Sequence Is:")
        print(self.sequence)
              
        self.flashing = True
        self.show_sequence()

    def show_sequence(self):
        self.index += 1

        if self.index > len(self.sequence) -1:
            self.index = -1
            self.flashing = False
            self.playing = True

            games.screen.add(self.lblGo)
            print("\nWaiting For User Input\n")
            
        else:
            self.squares[self.sequence[self.index]].flash()

    def check_sequence(self):
        """ Check if the user sequence is correct so far """
        if self.keyDelay >= 25:
            if games.keyboard.is_pressed(games.K_1) or games.keyboard.is_pressed(games.K_2) or games.keyboard.is_pressed(games.K_3) or games.keyboard.is_pressed(games.K_4):
                if games.keyboard.is_pressed(games.K_1) and self.sequence[self.checkIndex] == 1:
                    self.squares[1].flash()
                    self.checkIndex += 1

                elif games.keyboard.is_pressed(games.K_2) and self.sequence[self.checkIndex] == 2:
                    self.squares[2].flash()
                    self.checkIndex += 1

                elif games.keyboard.is_pressed(games.K_3) and self.sequence[self.checkIndex] == 3:
                    self.squares[3].flash()
                    self.checkIndex += 1

                elif games.keyboard.is_pressed(games.K_4) and self.sequence[self.checkIndex] == 4:
                    self.squares[4].flash()
                    self.checkIndex += 1

                else:
                    games.screen.remove(self.lblGo)
                    games.screen.add(self.lblFail)
                    self.wrong = True
                    self.playing = False
                    self.flashing = False

                    print("\nIncorrect Sequence!\n")

                self.keyDelay = 0

            if self.checkIndex >= len(self.sequence):
                self.playing = False
                self.flashing = False
                self.started = False
                self.correct = True
                self.checkIndex = 0

                games.screen.remove(self.lblGo)
                games.screen.add(self.lblCorrect)

                print("\nCorrect Sequence!\n")
                
        else:
            self.keyDelay += 1
    
    def update(self):
        # Check if game has started
        if self.started:
            # Check if the computer has shown a sequence or not
            if self.wrong:
                if self.wrongCount >= 150:
                    games.screen.remove(self.lblFail)
                    self.startTimer = 0
                    self.started = False
                    self.wrong = False

                    self.countdown = 3
                    self.lblCountdown.value = self.countdown
                    games.screen.add(self.lblCountdown)

                else:
                    self.wrongCount += 1
            
            elif self.correct:
                 if self.correctCount >= 150:
                     games.screen.remove(self.lblCorrect)
                     self.startTimer = 0
                     self.started = False
                     self.correct = False
                     self.sequence.append(0)

                     self.countdown = 3
                     self.lblCountdown.value = self.countdown
                     games.screen.add(self.lblCountdown)


                 else:
                    self.correctCount += 1

            elif not self.playing and not self.flashing:
                # Generate and show a sequence
                self.create_sequence()
                
            elif not self.flashing:
                # Wait for user input
                self.check_sequence()
            
    
    def tick(self):
        if self.startTimer >= 100 and not self.started:
            # Change the Graphical Countdown on the screen
            if self.countdown - 1 >= 1:
                self.countdown -= 1
                self.startTimer = 0

                self.lblCountdown.value = self.countdown
                
            else:
                self.started = True
                self.startTimer = 0
                games.screen.remove(self.lblCountdown)

        elif not self.started:
            self.startTimer += 1

        if self.flashing:
            if self.flashWait >= 80:
                self.show_sequence()
                self.flashWait = 0
                

            else:
                self.flashWait += 1
            
            

    




# FUNCTION =================================
# Name.........: Main
# Description..: Main Function To Start Game
# Syntax.......: main()
# ==========================================
def main():
    simon = Simon()
    games.screen.add(simon)
    games.screen.mainloop()


main()
                                    
