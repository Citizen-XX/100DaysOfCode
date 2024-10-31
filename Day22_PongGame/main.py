from turtle import Screen
from paddles import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

right_paddle = Paddle(starting_x_coord=350)
left_paddle = Paddle(starting_x_coord=-350)
ball = Ball()

screen.listen()

screen.onkey(fun=right_paddle.move_up,key='Up')
screen.onkey(fun=right_paddle.move_down,key='Down')
screen.onkey(fun=left_paddle.move_up,key='w')
screen.onkey(fun=left_paddle.move_down,key='s')

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.04)
    ball_position = ball.pos()
    if ball_position[1] >= 280:
        ball.check_heading()
    elif ball_position[1] <= -280:
        ball.check_heading()
    # if ball.distance(right_paddle) <= 10 or ball.distance(left_paddle) <= 10:
    #     ball.check_heading()
    

screen.exitonclick()