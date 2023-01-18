from turtle import Turtle


class EndScreen(Turtle):
    def game_over(self):  # Game over screen setup
        self.penup()
        self.screen.bgcolor("black")
        self.pencolor("white")
        self.hideturtle()
        self.write("Game Over", move=False, align='Center', font=('Courier', 50, 'normal'))

    def win(self):  # win screen setup
        self.penup()
        self.screen.bgcolor("black")
        self.pencolor("white")
        self.hideturtle()
        self.write("You Win!", move=False, align='Center', font=('Courier', 50, 'normal'))
