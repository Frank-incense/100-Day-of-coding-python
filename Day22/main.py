from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT = (480,0)
RIGHT = (-480,0)

screen  = Screen()
left_player = Paddle(LEFT)
right_player = Paddle(RIGHT)
ball = Ball()
score = Scoreboard()


screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('PINGPONG')


game_is_on = True
screen.onkey(right_player.right, "Right")
screen.onkey(right_player.left, "Left")
screen.onkey(left_player.right, "d")
screen.onkey(left_player.left, "a")
screen.listen()

step = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    
    # detect collision with right paddle 
    if ball.distance(left_player) < 50 and ball.xcor() > 450 or ball.distance(right_player) < 50 and ball.xcor() < -450:
        ball.bouncex()

    if ball.xcor() > 480:
        ball.reset_game()
        score.r_score += 1
    elif ball.xcor() < -480:
        ball.reset_game()
        score.l_score += 1

    score.update()
    


screen.exitonclick()