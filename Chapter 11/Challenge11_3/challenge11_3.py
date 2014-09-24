"""
    Program......: challenge11_3.py
    Author.......: Michael Rouse
    Date.........: 3/17/14
    Description..: Create a one player pong game with the wall
"""
from livewires import games, color

# Create the window and frame
games.init(screen_width=1280, screen_height=816, fps=30)

# Create the score
score = games.Text(value=0, size=70, color=color.white, x=340, y=60, left=340)

class Paddle(games.Sprite):
    """ Paddle to hit the ball """
    image = games.load_image("challenge11_3_paddle.png")
    
    def __init__(self):
        super(Paddle, self).__init__(image=Paddle.image, x=600, y=games.mouse.y)
    
    # Move the paddle
    def update(self):
        self.y = games.mouse.y

        # Don't let paddle go above the top white line
        if self.y - 32 < 24:
            self.y = 24 + 32

        # Don't let the paddle go below the bottom white line
        if self.y + 32 > 460:
            self.y = 460 - 32

class Ball(games.Sprite):
    """ Ball to bounce and hit """
    image = games.load_image("challenge11_3_ball.png", transparent=True)

    def __init__(self):
        super(Ball, self).__init__(image=Ball.image, x=400, y=200, dx=2)

    def update(self):
        # Bounce off paddle
        if self.x + 8 in range(paddle.x - 18, paddle.x + 18) and self.y in range(paddle.y - 38, paddle.y + 38):
            score.value += 1

            if self.y > paddle.y - 38 and self.y < paddle.y + 2:
            # check where it hit on the paddle
                self.dy = -2
                
            elif self.y > paddle.y - 4 and self.y < paddle.y + 4:
                # Center of paddle
                self.dy = 0

            elif self.y > paddle.y and self.y < paddle.y + 38:
                # bottom of paddle  
                self.dy = 2
                
            self.dx = -self.dx - .5

        # Bounce off left border
        if self.x  <= 30:
            self.dx = -self.dx
            
        # Bounce off top border
        if self.y - 9 < 24:
            self.dy = 1
            self.dx -= 1

        # Bounce off bottom border
        if self.y + 9 > 460:
            self.dy = -1
            self.dx -= 1

        # Check if ball stopped
        if self.dx == 0:
            self.dx = 1

        # Check if ball is out of bounds (paddle missed)
        if self.x >= 600 + 20:
            game_over()
            self.destroy()

def game_over():
    # Player lost
    paddle.destroy()
    
    gameOver = games.Text(value="Game    Over", size=70, color=color.white, x=305, y=250)
    games.screen.add(gameOver)

    games.mouse.is_visible = True
    games.screen.event_grab = False

def main():
    # Set the background
    games.screen.background = games.load_image("challenge11_3_background.png", transparent=False)
    
    games.screen.add(score)

    # Create the paddle
    games.screen.add(paddle)

    # Create the ball
    ball = Ball()
    games.screen.add(ball)


    games.mouse.is_visible = False
    games.screen.event_grab = True
    
    games.screen.mainloop()
    

# Start
paddle = Paddle()
main()
