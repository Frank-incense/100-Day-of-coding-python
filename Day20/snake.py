from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    def __init__(self) -> None:
        self.body = [] 
        self.color = 'white'
        self.shape = 'square'
        self.makeBody()
        self.head = self.body[0]
        
    
    def addSegment(self, position):
        new_body = Turtle(self.shape)
        new_body.color(self.color)
        new_body.penup()
        new_body.goto(position)
        self.body.append(new_body)
        
    
    def extend(self):
        self.addSegment(self.body[-1].position())

    def makeBody(self):
        '''Creates the segments of the snake.'''
        for position in STARTING_POSITIONS:
            self.addSegment(position)
            

    def move(self):
        for seg in range(len(self.body)-1, 0, -1):
            newx = self.body[seg-1].xcor()
            newy = self.body[seg-1].ycor()
            self.body[seg].goto(x=newx, y=newy)

        self.body[0].forward(MOVE_DISTANCE)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.body[0].seth(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.body[0].seth(LEFT)

    def turn_up(self):
        if self.body[0].heading() == RIGHT or self.body[0].heading() == LEFT:
            self.body[0].seth(UP)

    def turn_down(self):
        if self.body[0].heading() == RIGHT or self.body[0].heading() == LEFT:
            self.body[0].seth(DOWN)

    def border(self):
        x = self.body[0].xcor()
        y = self.body[0].ycor()
        if x >= 280 or x <= -280:
            return True
        elif y >= 280 or y <= -280:
            return True
        
    def reset(self):
        for seg in self.body:
            seg.goto((1000,1000))
        
        self.body.clear()
        self.makeBody()
        self.head = self.body[0]
        

    
