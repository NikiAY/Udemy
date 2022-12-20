from turtle import Turtle
import random 

class SnakeFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5,.5)
        self.color("blue")
        self.speed("fastest")
        self.random_cor()

    def random_cor(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.setpos(x, y)
        

    # def random_food(self):
    #     snake_ins = Snake
    #     if snake_ins.head.pos() == self.food.pos():
    #         self.random_cor()



