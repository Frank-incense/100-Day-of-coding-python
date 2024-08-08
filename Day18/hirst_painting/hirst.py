import random as random
import turtle as turtle_module

frank = turtle_module.Turtle()
screen = turtle_module.Screen()
frank.speed()
screen.colormode(255)

color = [(249, 228, 18), (212, 13, 9), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48),  (244, 39, 149), (65, 203, 229), (223, 20, 110), (229, 164, 9), (15, 154, 23), (245, 57, 16), (98, 75, 9), (223, 139, 203), (67, 241, 160), (10, 97, 61)]

frank.penup()
frank.hideturtle()
frank.setheading(225)
frank.forward(250)
frank.setheading(0)


for i in range(10):
    for _ in range(10):
        frank.setheading(0)
        frank.dot(20, random.choice(color))
        frank.forward(50)
        
    frank.left(90)
    frank.forward(50)
    frank.left(90)
    frank.forward(500)
 

screen.exitonclick()