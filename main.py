# import colorgram
#
# colors = colorgram.extract('image_hirst.jpg', 30)
# # first_color = colors[0]
# # rgb = first_color.rgb
# # red = rgb[0]
# # red = rgb.r
#
#
# colors_palet = []
# for color in colors:
#     rgb = color.rgb
#     new_color = (rgb.r, rgb.g, rgb.b)
#     colors_palet.append(new_color)
#
# print(colors_palet)

import turtle as t
from turtle import Screen
import random

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
t.colormode(255)
timmy = t.Turtle()
timmy.hideturtle()
timmy.shape('turtle')
timmy.home()
timmy.penup()

# Correct the turtle position for the beginning point
timmy.setheading(200)
timmy.forward(550)
timmy.setheading(0)
#print(current_position)

timmy.speed(7)
# Controls the amount of rows to create
for row in range(10):
    # Retrieve the current position of the turtle
    x_position = timmy.position()[0]
    y_position = timmy.position()[1]
    # Control the amount of columns to create
    for column in range(10):
        timmy.fd(50)
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.fd(50)
    # Return the beginning position of the turtle from the current row
    timmy.setposition(x_position, y_position)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)

screen = Screen()
screen.exitonclick()