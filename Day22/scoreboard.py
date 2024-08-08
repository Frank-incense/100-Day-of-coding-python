from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.goto(x=0, y=200)
        self.write(self.l_score, align='left', font=("Arial", 20, "normal"))
        self.write(self.r_score, align='right', font=("Arial", 20, "normal"))



    def update(self):
        self.clear()
        self.write(self.l_score, align='left', font=("Arial", 100, "normal"))
        self.write(self.r_score, align='right', font=("Arial", 100, "normal")) 