from turtle import Turtle

ALIGNMENT= "center"
FONT=("arial", 22,"normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)


    def inc_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score} ", align="center", font=("Arial",22, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
