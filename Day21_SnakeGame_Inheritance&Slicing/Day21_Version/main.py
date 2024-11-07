from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.head_north, key='Up')
screen.onkey(fun=snake.head_south, key='Down')
screen.onkey(fun=snake.head_west, key='Left')
screen.onkey(fun=snake.head_east, key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        food.refresh()
        snake.extend()

    if not (-280 <= snake.head.xcor() <= 280 and -280 <= snake.head.ycor() <= 280):
        game_is_on = False
        scoreboard.game_over()

    for piece in snake.snake[1:]:
        if snake.head.distance(piece) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
