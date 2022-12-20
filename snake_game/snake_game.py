import turtle as t
from scoreboard import ScoreBoard


DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_growth = []
        self.create_snake()
        self.head = self.snake_body[0]

              
    def create_snake(self):
        for i in range(0,3):
            snake_part = t.Turtle(shape= "square")
            snake_part.penup()
            snake_part.color("white")
            snake_part.speed("fastest")
            self.snake_body.append(snake_part)
            #self.reset_pos()
    
    def grow(self):
            snake_part = t.Turtle(shape= "square")
            snake_part.penup()
            snake_part.ht()
            snake_part.color("white")
            snake_part.speed("fastest")
            snake_part.goto(self.snake_body[-1].pos())
            self.snake_body.append(snake_part)
            self.snake_growth.append(snake_part)
            snake_part.st()

    def reset_pos(self):
        for snake in self.snake_body:
            snake.goto(1000,1000)
        self.snake_body = []
        self.snake_growth = []
        self.create_snake()
        self.head = self.snake_body[0]

    
    def set_pos_y(self):
        for i in range(0,(len(self.snake_body)), -1):
            new_x = self.snake_body[i].xcor()
            new_y = self.snake_body[i].ycor()
            self.snake_body[i].setpos(x= new_x, y= new_y)
            new_y -=20

    def move_f(self):
        for i in range((len(self.snake_body) - 1), 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].setpos(x= new_x, y= new_y) 
        self.head.fd(DISTANCE)            
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            #self.move_f()
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            #self.move_f()
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            #self.move_f()

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            #self.move_f()


# snake_body = {}
# x = 0
# y = 0
# for i in range(1,4):
#     key = f"turtle_{i}"
#     snake_body[key] = t.Turtle(shape= "square")
#     snake_body[key].penup()
#     snake_body[key].color("white")
#     snake_body[key].setpos(x= x, y= y)
#     x -= 20

# game_on = True

# while game_on:
#     #time.sleep(0.1)
#     for key, value in snake_body.items():
#         value.penup()
#         x = value.position()
#         value.setpos(x)
#         screen.update() 
#         value.fd(30)
#         value.right(90)