from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_x_coord:int):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.speed('fastest')
        self.goto(x=starting_x_coord,y=0)
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color('white')

    def move_up(self):
        if not self.ycor() > 230:
            self.forward(35)

    def move_down(self):
        if not self.ycor() < -230:
            self.back(35)

    