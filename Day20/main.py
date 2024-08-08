from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title('Snake Game')
game_is_on = True
    
snakes = Snake()
food = Food()
score = Score()


screen.onkey(fun=snakes.turn_down, key='Down')
screen.onkey(fun=snakes.turn_left, key='Left')
screen.onkey(fun=snakes.turn_right, key='Right')
screen.onkey(fun=snakes.turn_up, key='Up')
screen.listen()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    
    snakes.move()
    
    # Detect food
    if snakes.head.distance(food) < 15:
        food.refresh()
        snakes.extend()
        score.add()

    # Collision with wall
    if snakes.head.xcor() > 280 or snakes.head.xcor() < -280 or snakes.head.ycor() > 280 or snakes.head.ycor() < -280:
        game_is_on = False
        score.gameover()

    for segment in snakes.body[1:]:
        if snakes.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()


screen.exitonclick()