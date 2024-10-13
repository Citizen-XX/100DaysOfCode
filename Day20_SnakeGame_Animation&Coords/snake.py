from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = self.initial_snake()
        self.head = self.snake[0]

    def initial_snake(self):
        snake = []
        for i in range(3):
            turtle = Turtle(shape='square')
            turtle.color('white')
            turtle.penup()
            turtle.setpos(x=-(i*20), y=0)
            snake.append(turtle)
        return snake

    def move(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(x=new_x, y=new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def head_north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def head_south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def head_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def head_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
