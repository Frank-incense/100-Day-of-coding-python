import csv
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal",)

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.count = 0
        self.goto(0, 270)
        self.color('white')
        self.speed('fastest')
        self.highScore = self.readHighscore()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.highScore}", move=False, align=ALIGNMENT, font=FONT)

    def writeHighscore(self):
        newscore  = self.count
        with open(file='./100-Day-of-coding-python/Day20/highscore.txt', mode='w') as scores:
            scores.write(str(newscore))

    def readHighscore(self):
        with open(file='./100-Day-of-coding-python/Day20/highscore.txt', mode='r') as scores:
            highScore = scores.read()
            return highScore

    def add(self):
        self.count = self.count + 1
        self.update_score()

    def reset(self):
        if self.count > int(self.highScore):
            self.writeHighscore()
            self.highScore = self.readHighscore()
        self.count = 0
        self.update_score()
