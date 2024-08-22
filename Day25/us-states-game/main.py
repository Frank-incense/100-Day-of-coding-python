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
stateCount = 0
answered = []

while gameIsOn:
    userResponse = screen.textinput(f'{stateCount}/50 States answered', 'Name a US States:').title()
    state = data[data["state"] == userResponse]
    answerList = data['state'].to_list()
    

    if userResponse == 'Exit':
        break
    
    if userResponse in answerList:
        if userResponse not in answered:
            states.goto(state.x.item(), state.y.item())
            states.write(userResponse)
            stateCount += 1
    
    answered.append(userResponse)

    if stateCount == 50:
        gameIsOn = False

# States to learn
toLearn = {
    'state': [n for n in answerList if n not in answered]
}
# for i in answerList:
#     if i in answered:
#         answerList.pop(answerList.index(i))
#     else:
#         extract = data[data["state"] == i]
#         toLearn["state"].append(extract.state.item())
        
newfile = pandas.DataFrame.from_dict(toLearn)
newfile.to_csv('./Day25/us-states-game/states_to_learn.csv')