import turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from block_manager import Block_Manager
from endscreen import EndScreen

# screen setup
screen = turtle.Screen()
screen.title("Breakout")
screen.setup(height=800, width=800)
screen.bgcolor("black")
screen.tracer(0)

# creating each of the object instances
paddle = Paddle()
ball = Ball()
block_manager = Block_Manager()
block_manager.create_blocks()
scoreboard = Scoreboard()
end_screen = EndScreen()

# controls setup
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")
screen.listen()

game_on = True
while game_on:
    ball.move()  # sets ball in motion
    # detect ball collision with block
    for block in block_manager.all_blocks:
        if ball.distance(block) < 50:
            ball.bounce_y()
            block.goto(800, 800)
            scoreboard.clear()
            scoreboard.update_score()
    # detect ball collision with paddle
    if ball.distance(paddle) < 65 and ball.ycor() == -335:
        ball.bounce_y()

    # detect ball collision with wall
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()
    if ball.ycor() > 350 or ball.ycor() < -390:
        ball.bounce_y()

    # detect game over
    if ball.ycor() < -375:
        game_on = False
        end_screen.game_over()

    # detect winning
    if scoreboard.score > 30:
        game_on = False
        end_screen.win()
    screen.update()

screen.mainloop()
