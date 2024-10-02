from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)
timmy = Turtle(shape='turtle')
timmy.color('purple')
timmy.speed(speed=5)

sides = 3
degrees = 360

while sides is not 11:
    angle = degrees/sides
    rgb_codes = [randint(0,255),randint(0,255),randint(0,255)]
    rgb_tuple = tuple(rgb_codes)
    timmy.pencolor(rgb_tuple)
    for _ in range(sides):
        timmy.right(angle)
        timmy.forward(50)
    sides += 1

screen = Screen()
screen.exitonclick()
