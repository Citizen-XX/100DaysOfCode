import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
# snake = []
# for i in range(3):
#     turtle = Turtle(shape='square')
#     turtle.color('white')
#     turtle.penup()
#     turtle.setpos(x=-(i*20), y=0)
#     # turtle.goto(x=-(i*20), y=0)
#     snake.append(turtle)
# # screen.turtles()

snake = Snake()

screen.listen()
screen.onkey(fun=snake.head_north, key='Up')
screen.onkey(fun=snake.head_south, key='Down')
screen.onkey(fun=snake.head_west, key='Left')
screen.onkey(fun=snake.head_east, key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg_num in range(len(snake)-1, 0, -1):
    #     new_x = snake[seg_num-1].xcor()
    #     new_y = snake[seg_num-1].ycor()
    #     snake[seg_num].goto(x=new_x, y=new_y)
    # snake[0].forward(20)
    snake.move()

screen.exitonclick()
