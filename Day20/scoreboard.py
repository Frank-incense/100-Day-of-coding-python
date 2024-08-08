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
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.count}", move=False, align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def add(self):
        self.count = self.count + 1
        self.clear()
        self.update_score()