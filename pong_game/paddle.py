from turtle import Turtle 

DISTANCE = 20

class UserPaddle(Turtle):
    def __init__(self, init_x, init_y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid= 5,stretch_len= 1)
        self.init_x = init_x
        self.init_y = init_y
        self.goto(init_x, init_y) 
        #self.x = self.xcor()
        # self.y = self.ycor()
        #goto(x= -370, y= 0)
        
        
    def user_up(self):
        if self.ycor() <= 230:
            new_y = self.ycor() + 40
            self.goto(x= self.init_x, y= new_y)

    def user_down(self):
        if self.ycor() >= - 230:
            new_y = self.ycor() - 40
            self.goto(x= self.init_x, y= new_y)

class AutoPaddle:
    def __init__(self):
        self.auto_paddle = Turtle(shape= "square")
        self.auto_paddle.ht()
        self.auto_paddle.penup()
        self.auto_paddle.color("white")
        self.auto_paddle.shapesize(stretch_wid= 5,stretch_len= 1)
        self.auto_paddle.goto(x= 370, y= 0)
        self.auto_paddle.st()
        self.auto_paddle.speed(1)


    def auto_move(self):
        x = self.auto_paddle.xcor()
        for i in range(-230, 230, 20):
                self.auto_paddle.goto(x, i)



    

            
        
            


