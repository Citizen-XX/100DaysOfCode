from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.snake = []
        self.initial_snake()
        self.head = self.snake[0]

    def initial_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(x=new_x, y=new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new_part = Turtle('square')
        new_part.color('white')
        new_part.penup()
        new_part.goto(position)
        self.snake.append(new_part)

    def extend(self):
        self.add_segment(self.snake[-1].position())

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
