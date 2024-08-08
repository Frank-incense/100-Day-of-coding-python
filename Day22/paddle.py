from turtle import Turtle
LEFT = 90
RIGHT = 270
STEP = 40


class Paddle(Turtle):
    def __init__(self, coordinate: tuple) -> None:
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.goto(coordinate)
        self.shapesize(5,1)
        

    def right(self):
        newy = self.ycor() - STEP
        self.goto(x=self.xcor(), y=newy)

    def left(self):
        newy = self.ycor() + STEP
        self.goto(x=self.xcor(), y=newy)        

    def bounce(self):
        self.ycor *= -1
    