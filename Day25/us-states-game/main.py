from turtle import Turtle, Screen
import pandas

states = Turtle()
screen = Screen()

screen.bgpic('./Day25/us-states-game/blank_states_img.gif')
screen.screensize(canvwidth=600,canvheight=500)
screen.title('US States')
states.penup()
states.ht()

data = pandas.read_csv('./Day25/us-states-game/50_states.csv')
gameIsOn = True

while gameIsOn:
    userResponse = screen.textinput('US States Game', 'Name a US State:').title()
    state = data[data["state"] == userResponse]
    answers = data['state']

    states.goto((int(state.x), int(state.y)))
    states.write(userResponse)

screen.exitonclick()