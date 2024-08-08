COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [-180, -120, -60, 0, 60, 120, 180]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def createCar(self):
        if random.randint(1,6) == 6:
            newCar = Turtle()
            newCar.shape('square')
            newCar.shapesize(1,2)
            newCar.color(random.choice(COLORS))
            newCar.penup()
            newCar.seth(180)
            newCar.setx(300)
            newCar.sety(random.choice(LANES))
            self.cars.append(newCar)

    def moveCar(self):
        for car in self.cars:
            car.forward(self.speed)

    def speedUp(self):
        self.speed += MOVE_INCREMENT
