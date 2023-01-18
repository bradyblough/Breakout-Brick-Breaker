from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        x_coordinate = 0
        y_coordinate = -300
        self.penup()
        self.shape("circle")
        self.shapesize(0.75)
        self.fillcolor("white")
        self.pencolor("black")
        self.goto(x_coordinate, y_coordinate)
        self.x_move = 1
        self.y_move = -1

    def move(self): # moves ball
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self): # bounces vertically
        self.y_move *= -1

    def bounce_x(self): # bounces horizontally
        self.x_move *= -1
