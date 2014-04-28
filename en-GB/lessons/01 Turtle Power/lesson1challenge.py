from turtle import *

speed(0)
shape("turtle")

def shape(sides, length, angle):
    for count in range(sides):
        forward(length)
        right(angle)


shape(5, 100, 360/5)
