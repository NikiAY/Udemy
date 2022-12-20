from turtle import Turtle 

ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")

class ScoreBoard(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.goto(x, y)
        self.write(f"{self.score}", align= ALIGNMENT, font= FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align= ALIGNMENT, font= FONT)

    def game_over(self, user_name):
        self.goto(0,0)
        self.write(f"Game Over! {user_name} wins!", align= ALIGNMENT, font= ("Courier", 25, "bold"))

