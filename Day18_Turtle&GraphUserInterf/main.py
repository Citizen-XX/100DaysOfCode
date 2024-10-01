from turtle import Turtle, Screen

timmy = Turtle(shape='turtle')
timmy.color('purple')
timmy.speed(speed=5)

# x_dist = [100, 100, 0, 0]
# y_dist = [0, -100, -100, 0]

# for x, y in zip(x_dist, y_dist):
#     timmy.goto(x=x, y=y)

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
