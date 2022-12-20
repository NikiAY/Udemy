import threading
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
Y_POSITIONS = list(range(-241, 240, 60))

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.init_speed = STARTING_MOVE_DISTANCE
        #self.create_cars()


    def create_cars(self):
            dice = random.randint(1,5)
            if dice == 4:            
                new_car = Turtle(shape= "square")
                new_car.ht()
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.shapesize(stretch_wid= 1, stretch_len= 2)
                new_car.goto(280, random.randint(-241, 240))
                new_car.st()
                self.all_cars.append(new_car)

    
    def move_cars(self):
        for i in range(len(self.all_cars)):
            self.all_cars[i].bk(self.init_speed)


    def speed_up(self):
        self.init_speed += MOVE_INCREMENT
        print(self.init_speed)







