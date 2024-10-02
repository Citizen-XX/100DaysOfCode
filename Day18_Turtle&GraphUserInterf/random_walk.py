from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)
timmy = Turtle(shape='turtle')
timmy.color('purple')
timmy.speed(speed='fastest')

screen = Screen()

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color_code = (r,g,b)
    return color_code

for i in range(0,360,6):
    timmy.pencolor(random_color())
    timmy.setheading(i)
    timmy.circle(75)

screen.exitonclick()