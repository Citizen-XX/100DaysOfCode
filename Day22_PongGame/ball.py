from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(45)
        self.shape('circle')
        self.color('white')
        self.mov_speed = 1
        self.up_down_determinant = 1

    def move(self):
        self.forward(15)

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

    def horiz_check_heading(self):
        if 90 > self.heading() > 0:
            self.setheading(315)
        elif 180 > self.heading() > 90:
            self.setheading(225)
        elif 360 > self.heading() > 270:
            self.setheading(45)
        elif 270 > self.heading() > 180:
            self.setheading(135)

    def vert_check_heading(self):
        if 90 > self.heading() > 0:
            self.setheading(135)
        elif 180 > self.heading() > 90:
            self.setheading(45)
        elif 360 > self.heading() > 270:
            self.setheading(225)
        elif 270 > self.heading() > 180:
            self.setheading(315)

    def ball_reset(self):
        if self.xcor() > 350:
            self.home()
            if self.up_down_determinant % 2 == 0:
                self.setheading(135)
            elif self.up_down_determinant % 2 == 1:
                self.setheading(-135)
            self.up_down_determinant += 1
        elif self.xcor() < -350:
            self.home()
            if self.up_down_determinant % 2 == 0:
                self.setheading(45)
            elif self.up_down_determinant % 2 == 1:
                self.setheading(-45)
            self.up_down_determinant += 1
        self.mov_speed *= 0.95