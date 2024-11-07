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
        with open("Day21_SnakeGame_Inheritance&Slicing\Day24_Version\data.txt") as file:
            self.high_score = int(file.read())
        self.pen(fillcolor='white',pencolor='white',pensize=16)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score} High Score: {self.high_score}',move=False, align=ALIGNMENT,font=FONT)
        
    def increase_score(self):
        self.score += 1

    # def game_over(self):
    #     # self.clear()
    #     self.home()
    #     self.write(arg=f'GAME OVER',move=False, align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day21_SnakeGame_Inheritance&Slicing\Day24_Version\data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

if __name__ == '__main__':
    scoreboard = Scoreboard()
    screen = Screen()
    screen.bgcolor('black')
    screen.exitonclick()