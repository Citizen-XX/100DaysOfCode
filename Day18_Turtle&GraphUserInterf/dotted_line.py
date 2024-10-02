from turtle import Turtle, Screen

timmy = Turtle(shape='turtle')
timmy.color('purple')
timmy.speed(speed=5)

for _ in range(25):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)

screen = Screen()
screen.exitonclick()
