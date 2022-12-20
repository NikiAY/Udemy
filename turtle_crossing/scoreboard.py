from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.ht()
        self.goto(-200, 250)
        self.update_board()

    def add_level(self):
        self.level += 1
        self.clear()
        self.update_board()

    
    def update_board(self):
        self.write(f"Level = {self.level} ", align= "center", font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align= "center", font= ('Courier', 25, 'bold'))