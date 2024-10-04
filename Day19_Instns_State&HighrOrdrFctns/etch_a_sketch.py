from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_right():
    tim.right(5)

def rotate_left():
    tim.left(5)

def reset_sketch():
    tim.reset()

screen.listen()
screen.onkey(fun=move_forwards, key='Up')
screen.onkey(fun=move_backwards, key='Down')
screen.onkey(fun=rotate_left, key='Left')
screen.onkey(fun=rotate_right, key='Right')
screen.onkey(fun=reset_sketch,key='c')
screen.exitonclick()