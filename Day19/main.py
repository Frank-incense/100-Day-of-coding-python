import turtle as turtle_module
import random 

race = False
screen = turtle_module.Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
positions = [-150,-100,-50,0,50,100,150]
all_players = []

for t in range(7):
    new_turtle = turtle_module.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=-230, y=positions[t])
    all_players.append(new_turtle)

if user_bet:
    race = True

while race:
    for tut in range(7):
        if all_players[tut].xcor() > 230:
            race = False
            if colors[tut] == user_bet:
                print(f"You've WON! The {colors[tut]} turtle is the winner!")
            else:
                print(f"You've LOST! The {colors[tut]} turtle is the winner!")
            break

        all_players[tut].forward(random.randint(0, 10))

screen.exitonclick()