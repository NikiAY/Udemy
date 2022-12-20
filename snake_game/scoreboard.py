from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_score()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.update_board()
        

    def update_board(self):
        self.clear()
        self.write(f"Current Score = {self.score}, High Score: {self.highscore}", 
        align= ALIGNMENT, font= FONT)

    def add_score(self):
        self.score += 1
        self.update_board()

    def reset_board(self):
        if self.highscore < self.score:
            self.highscore = self.score
        self.score = 0
        self.update_board()
        with open("high_score.txt", mode="a") as file:
                if self.highscore not in self.high_scores_lst: 
                    file.write(f"\n{self.highscore}")

    def read_score(self):
        with open("high_score.txt", mode="r") as file:
            current_scores = file.read()
            current_scores = current_scores.split("\n")
            self.high_scores_lst = []
            for score in current_scores:
                self.high_scores_lst.append(int(score))
            self.highscore = max(self.high_scores_lst)
        print(current_scores)
        return self.highscore


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align= "center", font= ('Courier', 25, 'bold'))

    
