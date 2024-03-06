import colorgram
import turtle as t

frank = t.Turtle
screen = t.TurtleScreen

new_color = []
colors = colorgram.extract("C:/Users/fokwemba/Documents/code/100-Day-of-coding-python/Day18/hirst_painting/spots.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color.append((r,g,b))

print(new_color)


t.exitonclick()