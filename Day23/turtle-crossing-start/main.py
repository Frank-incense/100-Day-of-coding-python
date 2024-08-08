import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tutu = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(fun=tutu.moveUp, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.createCar()
    car.moveCar()
    
    for vehicle in car.cars:
        if vehicle.distance(tutu) < 20:
            score.gameOver()
            game_is_on = False
    
    if tutu.levelUp():
        car.speedUp()
        score.updateScore()


screen.exitonclick()