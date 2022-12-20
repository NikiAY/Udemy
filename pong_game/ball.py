# from turtle import Turtle 
# import random

# MAX_X = 360
# MAX_Y = 250
# MIN_X = - 360
# MIN_Y = - 250

# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.color("white")
#         self.speed(2)
#         self.goto(x= 0, y= 0)
#         self.move_x = 10
#         self.move_y = 10
#         self.move_speed = 0.1
  
#     def move(self):
#         #distance = random.randint(1, 20)
#         new_x = self.xcor() + self.move_x
#         new_y = self.ycor() + self.move_y 
#         self.goto(new_x, new_y) 
          
    
#     def bounce_y(self):
#         self.move_y *= -1

#     def bounce_x(self):
#         speed_choice = random.randint(2, 8)
#         self.move_x *= -1
#         self.speed(speed_choice)  
#         print(speed_choice)
#         #self.move_speed *= 0.9 

#     def speed_change(self):
#         distance = random.choice([1.5, 2, 2.5, 3])
#         self.move_x *= distance

#     def reset_ball(self):
#         self.ht()
#         self.goto(0,0)
#         self.bounce_x()
#         self.speed(2)
#         self.move_speed = 0.1
#         self.st()

lst = list(range(10, 100, 10))
print(lst)
