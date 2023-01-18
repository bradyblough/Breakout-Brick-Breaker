from turtle import Turtle


class Block_Manager():
    def __init__(self):
        self.all_blocks = []

    def create_blocks(self):
        block_x_coordinate = -440
        block_y_coordinate = 320
        for block in range(1, 11):
            blocks = Turtle()  # row 1
            blocks.penup()
            blocks.shape("square")
            blocks.shapesize(stretch_len=3.77, stretch_wid=3)
            block_x_coordinate += 79
            blocks.fillcolor("lightgreen")
            blocks.pencolor("black")
            blocks.goto(block_x_coordinate, block_y_coordinate)
            if block % 10 == 0:
                block_x_coordinate = -440
                block_y_coordinate -= 62
            self.all_blocks.append(blocks)
        for block in range(1, 11):  # row 2
            blocks = Turtle()
            blocks.penup()
            blocks.shape("square")
            blocks.shapesize(stretch_len=3.77, stretch_wid=3)
            block_x_coordinate += 79
            blocks.fillcolor("coral1")
            blocks.pencolor("black")
            blocks.goto(block_x_coordinate, block_y_coordinate)
            if block % 10 == 0:
                block_x_coordinate = -440
                block_y_coordinate -= 62
            self.all_blocks.append(blocks)
        for block in range(1, 11):  # row 3
            blocks = Turtle()
            blocks.penup()
            blocks.shape("square")
            blocks.shapesize(stretch_len=3.77, stretch_wid=3)
            block_x_coordinate += 79
            blocks.fillcolor("mediumpurple")
            blocks.pencolor("black")
            blocks.goto(block_x_coordinate, block_y_coordinate)
            self.all_blocks.append(blocks)
