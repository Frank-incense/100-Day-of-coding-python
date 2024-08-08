FONT = ("Courier", 24, "normal")
POSITION = (-250, 250)
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(POSITION)
        self.color('black')
        self.score = 0
        self.write(arg=f"Level: {self.score}",font=FONT, align='left')
        
    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}",font=FONT, align='left')

    def gameOver(self):
        self.home()
        self.write(arg="Game Over", align="center", font=("Courier", 16, "normal"))