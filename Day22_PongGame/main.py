from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

right_paddle = Paddle(starting_x_coord=350)
left_paddle = Paddle(starting_x_coord=-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=right_paddle.move_up,key='Up')
screen.onkey(fun=right_paddle.move_down,key='Down')
screen.onkey(fun=left_paddle.move_up,key='w')
screen.onkey(fun=left_paddle.move_down,key='s')

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.05*ball.mov_speed)
    ball_position = ball.pos()
    
    if ball_position[1] >= 280:
        ball.horiz_check_heading()
    elif ball_position[1] <= -280:
        ball.horiz_check_heading()
    
    if ball.distance(right_paddle) < 50 and ball_position[0] > 330:
        ball.vert_check_heading()
    elif ball.distance(left_paddle) < 50 and ball_position[0] < -330:
        ball.vert_check_heading()
    
    if ball_position[0] > 350:
        scoreboard.l_point()
        ball.ball_reset()
    elif ball_position[0] < -350:
        scoreboard.r_point()
        ball.ball_reset()

    scoreboard.update_scoreboard()

screen.exitonclick()