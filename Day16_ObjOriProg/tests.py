import turtle
from prettytable import PrettyTable

# timmy = turtle.Turtle(shape="turtle")
# timmy.color("DarkOrchid1")
# # timmy.fillcolor = "DarkOrchid1"
# my_screen = turtle.Screen()
# timmy.forward(100)
# # print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"], align="l")
table.add_column("Type",["Electric","Water","Fire"], align="l")
print(table)