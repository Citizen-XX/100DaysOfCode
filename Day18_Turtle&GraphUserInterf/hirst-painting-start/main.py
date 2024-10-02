# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day18_Turtle&GraphUserInterf\hirst-painting-start\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle(shape='classic')
timmy.speed('fastest')
screen = Screen()
screen.setworldcoordinates(llx=-50,lly=-50,urx=300,ury=300)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), 
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), 
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

for row in range(10):
    for col in range(10):
        color = random.choice(color_list)
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(x=row*25,y=col*25)
        timmy.dot(40,color)

screen.exitonclick()