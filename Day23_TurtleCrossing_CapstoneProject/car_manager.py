from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_maker(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape='square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(x=300,y=random_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
