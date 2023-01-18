from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        x_coordinate = 0
        y_coordinate = -350
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=6)
        self.color("cornsilk")
        self.goto(x_coordinate, y_coordinate)

    # functions to move paddles
    def left(self):
        self.fd(-60)

    def right(self):
        self.fd(60)


