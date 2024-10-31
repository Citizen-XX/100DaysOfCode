from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(45)
        self.shape('circle')
        self.color('white')

    def move(self):
        self.forward(10)

    # def down_heading(self):
    #     if 360 > self.heading() > 270:
    #         self.setheading(45)
    #     elif 270 > self.heading() > 180:
    #         self.setheading(135)

    # def up_heading(self):
    #     if 90 > self.heading() > 0:
    #         self.setheading(315)
    #     elif 180 > self.heading() > 90:
    #         self.setheading(225)

    def check_heading(self):
        if 90 > self.heading() > 0:
            self.setheading(315)
        elif 180 > self.heading() > 90:
            self.setheading(225)
        elif 360 > self.heading() > 270:
            self.setheading(45)
        elif 270 > self.heading() > 180:
            self.setheading(135)