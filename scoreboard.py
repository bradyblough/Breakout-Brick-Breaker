from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor('white')
        self.goto(-300, 360)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align='Center', font=('Courier', 30, 'normal'))
        self.update_score()

    def update_score(self):  # updates score after brick break
        self.penup()
        self.pencolor('white')
        self.goto(-300, 360)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align='Center', font=('Courier', 30, 'normal'))
        self.score += 1
