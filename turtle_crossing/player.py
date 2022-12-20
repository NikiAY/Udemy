from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_speed = MOVE_DISTANCE
        

    def move_y(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.fd(self.move_speed)

    def increase_speed(self):
        self.move_speed += 3

    def reset_position(self):
        self.ht()
        self.goto(STARTING_POSITION)
        self.st()