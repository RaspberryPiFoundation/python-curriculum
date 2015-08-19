from turtle import *

#a function for drawing a star
#'def' means 'define'
def drawStar():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()

#this will draw a light grey star on a dark blue background
color("WhiteSmoke")
bgcolor("MidnightBlue")

#use the function to draw stars!
drawStar()
forward(100)
drawStar()
left(120)
forward(150)
drawStar()

hideturtle()
done()
