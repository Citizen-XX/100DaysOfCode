from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet',prompt='Which turtle will win the race? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']
height_distribution = [i for i in range(-160,160,int(380/6))]

for color,height in zip(colors,height_distribution):
    tim = Turtle(shape='turtle')
    tim.color(color)
    tim.penup()
    tim.speed(4)
    tim.goto(x=-230,y=height)

screen.exitonclick()