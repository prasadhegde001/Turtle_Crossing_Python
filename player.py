from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def goup(self):
        self.forward(MOVE_DISTANCE)

