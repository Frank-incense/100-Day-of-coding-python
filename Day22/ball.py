from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.xmove = 10
        self.ymove = 10
    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(x=newx, y=newy)

    def bouncey(self):
        self.ymove *= -1

    def bouncex(self):
        self.xmove *= -1

    def reset_game(self):
        self.goto(0,0)
        self.bouncex()