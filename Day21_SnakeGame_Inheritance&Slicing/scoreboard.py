from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')
GAME_OVER_FONT = ('Arial', 36, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.setposition(x=0,y=270)
        self.score = 0
        self.pen(fillcolor='white',pencolor='white',pensize=16)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score}',move=False, align=ALIGNMENT,font=FONT)
        self.score += 1

    def game_over(self):
        # self.clear()
        self.home()
        self.write(arg=f'GAME OVER',move=False, align=ALIGNMENT,font=FONT)

if __name__ == '__main__':
    scoreboard = Scoreboard()
    screen = Screen()
    screen.bgcolor('black')
    screen.exitonclick()